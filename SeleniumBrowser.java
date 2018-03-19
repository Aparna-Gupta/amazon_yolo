package automationFramework;

import java.io.File;
import java.io.FileReader;
import java.util.HashMap;
import java.util.Map;
import java.util.NoSuchElementException;
import java.util.Set;
import java.util.Map.Entry;
import java.util.concurrent.TimeUnit;

import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.phantomjs.PhantomJSDriverService;
import org.openqa.selenium.remote.DesiredCapabilities;
import org.openqa.selenium.support.ui.ExpectedCondition;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import com.google.gson.JsonElement;

public class SeleniumBrowser {
	
    static File file = new File("D:\\Spring 2018\\Computational Social Science\\geckodriver-v0.20.0-win64\\geckodriver.exe");
	
	static String[] phantomArgs = new  String[] {
	        "--webdriver-loglevel=NONE"
	};
	
	static DesiredCapabilities dCaps;

	@SuppressWarnings("unchecked")
	public static void main(String[] args) {
		/*String exePath = "D:\\Spring 2018\\Computational Social Science\\chromedriver_win32\\chromedriver.exe";
		System.setProperty("webdriver.chrome.driver", exePath);
		WebDriver driver = new ChromeDriver();
		driver.manage().window().maximize();*/
		
		JSONParser parser = new JSONParser();
        JSONObject jsonObject;
		System.setProperty("webdriver.gecko.driver", file.getAbsolutePath());
		
	    dCaps = new DesiredCapabilities();
	    dCaps.setJavascriptEnabled(true);
	    dCaps.setCapability("takesScreenshot", true);
	    dCaps.setCapability(PhantomJSDriverService.PHANTOMJS_CLI_ARGS, new String[] {"--ignore-ssl-errors=true", "--ssl-protocol=tlsv1", "--web-security=false", "--webdriver-loglevel=OFF", "--webdriver-loglevel=NONE" , "--proxy-type=none"});
	    dCaps.setCapability(PhantomJSDriverService.PHANTOMJS_EXECUTABLE_PATH_PROPERTY, file.getAbsolutePath());
	    dCaps.setCapability(PhantomJSDriverService.PHANTOMJS_CLI_ARGS, phantomArgs);
		try {
			
			WebDriver driver = new FirefoxDriver();
			driver.get("https://www.junglescout.com/estimator/");
			driver.manage().window().maximize();
			WebElement category = driver.findElement(By.xpath("/html/body/div[1]/div/article/div/div/div[3]/div/div/div/section/div[2]/div[35]/div/img"));
			category.click();
			// Fetch element for the textbox.
			WebElement textBox = driver.findElement(By.className("category-handler"))
					.findElement(By.xpath("/html/body/div[1]/div/article/div/div/div[3]/div/div/div/div[1]/div/div/input"));
			jsonObject = (JSONObject) parser.parse(new FileReader("D://Workspace//SeleniumWebAPI//HomeKitchenCleanDataDict.json"));
			// Map<String, Object> attributes = new HashMap<String, Object>();
			   Set<Entry<String, JsonElement>> entrySet = jsonObject.entrySet();
			   JSONObject results = new JSONObject();
			   for(Map.Entry<String,JsonElement> entry : entrySet){
				   String key = entry.getKey().replace("\"","");
				   System.out.println(key);
				   JSONObject value = (JSONObject) jsonObject.get(key);
				   JSONObject salesRank = (JSONObject) value.get("salesRank");
				   Long rank = (Long) salesRank.get("Home &amp; Kitchen");
				   System.out.println(rank);
				   
				    // Click on the Category
					// FF: /html/body/div[1]/div/article/div/div/div[3]/div/div/div/section/div[2]/div[35]/div/img
					// Chrome : //*[@id=\"x-section-2\"]/div/div/div/section/div[2]/div[34]
					textBox.clear();
					textBox.sendKeys(rank.toString());
					driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);
					//WebDriverWait wait = new WebDriverWait(driver, 30);
					//Alert myAlert = wait.until(ExpectedConditions.alertIsPresent());
					//myAlert.accept();
					WebElement submitButton = driver.findElement(By.className("category-handler")).findElement(By.xpath("//*[@id=\"magicBtn\"]"));
					//driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);
					WebDriverWait wait = new WebDriverWait(driver,20);
				    wait.until(ExpectedConditions.elementToBeClickable(By.id("magicBtn")));
					submitButton.click();
					driver.manage().timeouts().implicitlyWait(20, TimeUnit.SECONDS);
					Thread.sleep(10000);
					WebElement salesValue = driver.findElement(By.xpath("//*[@id=\"magicResult\"]"));
					WebDriverWait driverWait = new WebDriverWait(driver, 20);
					ExpectedCondition<Boolean> expectation;
					expectation = new ExpectedCondition<Boolean>() {
					    public Boolean apply(WebDriver driverjs) {
					        return (Boolean) ((JavascriptExecutor) driver).executeScript("return (window.jQuery != null) && (jQuery.active === 0);");
					    }
					};
					driverWait.until(expectation);
					String estimatedSalesValue = salesValue.getText();
					results.put(key, estimatedSalesValue);
					System.out.println(estimatedSalesValue);
			}
			   System.out.println(results.toString());
			   driver.close();
		} catch (Exception e) {
			e.printStackTrace();
		} /*finally{
			driver.close();*/
		}
	
	
	public static boolean checkIfElementExistsByXpath(String xpath, WebDriver driver){
		try{
			driver.findElement(By.xpath(xpath));
		}catch (NoSuchElementException e) {
	    	System.err.println("Element not found: ");
	        return false;
	    }
		System.out.println("Element Found: ");
	    return true;
	}
}

