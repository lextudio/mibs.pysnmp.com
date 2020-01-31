#
# PySNMP MIB module RBUC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RBUC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:53:52 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
satcomMibs, = mibBuilder.importSymbols("CODAN-SMI", "satcomMibs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, Bits, Counter64, MibIdentifier, TimeTicks, NotificationType, ObjectIdentity, Unsigned32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Gauge32, ModuleIdentity, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Bits", "Counter64", "MibIdentifier", "TimeTicks", "NotificationType", "ObjectIdentity", "Unsigned32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Gauge32", "ModuleIdentity", "IpAddress")
TextualConvention, TestAndIncr, DateAndTime, DisplayString, TruthValue, TimeInterval = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TestAndIncr", "DateAndTime", "DisplayString", "TruthValue", "TimeInterval")
rbucMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 23304, 2, 1))
rbucMIB.setRevisions(('2009-02-11 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rbucMIB.setRevisionsDescriptions(('1.0 Initial version of this MIB module.',))
if mibBuilder.loadTexts: rbucMIB.setLastUpdated('200902110000Z')
if mibBuilder.loadTexts: rbucMIB.setOrganization('Codan Limited.')
if mibBuilder.loadTexts: rbucMIB.setContactInfo(' Magda Raltcheva Postal: Codan Limited 81 Graves St. Newton 5074 Australia Tel: +61-8-83050311 Fax: +61-8-83050411 Web: www.codan.com.au')
if mibBuilder.loadTexts: rbucMIB.setDescription('The Structure of Management Information for the Codan enterprise. Copyright(c) 2009 All rights reserved')
class ComponentRevision(DisplayString):
    description = 'The hex value in the first octet - xx - represents the major revision no. and the hex value in the second octet - yy - represents the minor revision no.'
    status = 'current'
    displayHint = 'vxx.yy'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(2, 2)
    fixedLength = 2

class FaultStatus(TextualConvention, Bits):
    description = 'Describes all the possible faults in the system as a bit pattern.'
    status = 'current'
    namedValues = NamedValues(("pafault", 0), ("lofault", 1), ("internalfault", 2), ("rcfault", 3), ("lnbfault", 4))

class TxStatus(TextualConvention, Bits):
    description = 'Describes all the possible faults in the system as a bit pattern.'
    status = 'current'
    namedValues = NamedValues(("txrs232", 0), ("txrs485", 1), ("txfsk", 2), ("txfsk", 3), ("txsnmp", 4), ("txtelnet", 5))

configuration = MibIdentifier((1, 3, 6, 1, 4, 1, 23304, 2, 1, 1))
status = MibIdentifier((1, 3, 6, 1, 4, 1, 23304, 2, 1, 2))
info = MibIdentifier((1, 3, 6, 1, 4, 1, 23304, 2, 1, 3))
txSettings = MibIdentifier((1, 3, 6, 1, 4, 1, 23304, 2, 1, 1, 1))
pktProtocol = MibIdentifier((1, 3, 6, 1, 4, 1, 23304, 2, 1, 1, 2))
rcSetting = MibIdentifier((1, 3, 6, 1, 4, 1, 23304, 2, 1, 1, 3))
freqs = MibIdentifier((1, 3, 6, 1, 4, 1, 23304, 2, 1, 1, 4))
misc = MibIdentifier((1, 3, 6, 1, 4, 1, 23304, 2, 1, 1, 5))
txOn = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 1, 1, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: txOn.setStatus('current')
if mibBuilder.loadTexts: txOn.setDescription('Sets Tx on/off.')
txDefault = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 1, 1, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: txDefault.setStatus('current')
if mibBuilder.loadTexts: txDefault.setDescription('Sets Tx default 1-last 0-off.')
txAttenuator = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setUnits('dBm').setMaxAccess("readwrite")
if mibBuilder.loadTexts: txAttenuator.setStatus('current')
if mibBuilder.loadTexts: txAttenuator.setDescription('Sets/Gets Tx attenuation value in 1dBm steps.')
protocol = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 1, 1, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: protocol.setStatus('current')
if mibBuilder.loadTexts: protocol.setDescription('Sets/Gets packet protocol 0 - ASCII, 1 - CODAN, 2 - .')
address = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 1, 1, 2, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: address.setStatus('current')
if mibBuilder.loadTexts: address.setDescription('Sets/Gets packet address: 0-31 NDSatcom ...')
mode = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 1, 1, 3, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mode.setStatus('current')
if mibBuilder.loadTexts: mode.setDescription('Sets/Gets redundancy mode 0-none, 1-warm, 2-hot.')
onLine = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 1, 1, 3, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: onLine.setStatus('current')
if mibBuilder.loadTexts: onLine.setDescription('Sets/Gets redundancy mode on on/off line state.')
rfFreq = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 1, 1, 4, 1), Integer32()).setUnits('MHz').setMaxAccess("readwrite")
if mibBuilder.loadTexts: rfFreq.setStatus('current')
if mibBuilder.loadTexts: rfFreq.setDescription('Sets/Gets the RBUC RF frequency.')
ifFreq = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 1, 1, 4, 2), Integer32()).setUnits('MHz').setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifFreq.setStatus('current')
if mibBuilder.loadTexts: ifFreq.setDescription('Sets/Gets the RBUC IF frequency.')
loFreq = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 1, 1, 4, 3), Integer32()).setUnits('MHz').setMaxAccess("readwrite")
if mibBuilder.loadTexts: loFreq.setStatus('current')
if mibBuilder.loadTexts: loFreq.setDescription('Sets/Gets the RBUC LO frequency.')
serIf = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 1, 1, 5, 1), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: serIf.setStatus('current')
if mibBuilder.loadTexts: serIf.setDescription('Sets/Gets serial interface - rate, length, parity, stop, terminate RS422/485.')
serEcho = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 1, 1, 5, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: serEcho.setStatus('current')
if mibBuilder.loadTexts: serEcho.setDescription('Sets/Gets serial interface echo on/off.')
pwrAlarmThresh = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 1, 1, 5, 3), DisplayString()).setUnits('dB').setMaxAccess("readwrite")
if mibBuilder.loadTexts: pwrAlarmThresh.setStatus('current')
if mibBuilder.loadTexts: pwrAlarmThresh.setDescription('Sets/Gets power alarm threshold.')
burstPwrThresh = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 1, 1, 5, 4), DisplayString()).setUnits('dB').setMaxAccess("readwrite")
if mibBuilder.loadTexts: burstPwrThresh.setStatus('current')
if mibBuilder.loadTexts: burstPwrThresh.setDescription('Sets/Gets burst power threshold.')
refSource = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 1, 1, 5, 5), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: refSource.setStatus('current')
if mibBuilder.loadTexts: refSource.setDescription('Sets/Gets reference source 0-external, 1-internal.')
ledState = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 1, 1, 5, 6), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ledState.setStatus('current')
if mibBuilder.loadTexts: ledState.setDescription('SetS/Gets LEDs status on/off.')
paStatus = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 1, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("off", 0), ("on", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: paStatus.setStatus('current')
if mibBuilder.loadTexts: paStatus.setDescription('Gets to 1 when PA is on.')
txPower = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 1, 2, 2), DisplayString()).setUnits('dB').setMaxAccess("readonly")
if mibBuilder.loadTexts: txPower.setStatus('current')
if mibBuilder.loadTexts: txPower.setDescription('Gets Tx power format x.x dB.')
txBurstPower = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 1, 2, 3), DisplayString()).setUnits('dB').setMaxAccess("readonly")
if mibBuilder.loadTexts: txBurstPower.setStatus('current')
if mibBuilder.loadTexts: txBurstPower.setDescription('Gets Tx power. Format is x.x,y.y,z.z, where x.x is current burst power, y.y is min and z.z is max burts power.')
faults = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 1, 2, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: faults.setStatus('current')
if mibBuilder.loadTexts: faults.setDescription("Gets the current fault status. Format - Bit0 PA fault, Bit1 Fan fault, Bit2 Power fault, Bit3 Temp fault, Bit4 10MHz fault, Bit5 Internal fault Bit6 LNB fault, Bit7 Red'cy Cont fault.")
latchedFaults = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 1, 2, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: latchedFaults.setStatus('current')
if mibBuilder.loadTexts: latchedFaults.setDescription('Gets the current latched faults. Format is same as Faults.')
temperature = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 1, 2, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: temperature.setStatus('current')
if mibBuilder.loadTexts: temperature.setDescription('Gets the BUC temperature. Format is x.x.')
minMaxTemperature = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 1, 2, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: minMaxTemperature.setStatus('current')
if mibBuilder.loadTexts: minMaxTemperature.setDescription('Gets the BUC temperature. Format is x.x,y.y where x.x is max and y.y is min temperature.')
systemSetting = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 1, 2, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2047))).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemSetting.setStatus('current')
if mibBuilder.loadTexts: systemSetting.setDescription('Gets the current system status. Format is Bit0 - PA state, Bit1 - RS232 Tx, Bit2 - FSK Tx, Bit3 - RS485 Tx Bit4 - Redundancy mode, Bit5 - Online, Bit6..Bit7 - Redundancy cold or hot mode, Bit8 - HTTP Tx, Bit9 - TELNET Tx, Bit10 - SNMP Tx.')
systemPoll = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 1, 2, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3))).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemPoll.setStatus('current')
if mibBuilder.loadTexts: systemPoll.setDescription('Gets the system poll status. Format is Bit0 - Fault, Bit1 - System change.')
deviceType = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 1, 2, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceType.setStatus('current')
if mibBuilder.loadTexts: deviceType.setDescription('Gets the device type. Format is X,Y where X is the model and Y is software version.')
gateway = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 1, 2, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gateway.setStatus('current')
if mibBuilder.loadTexts: gateway.setDescription('Gets the BUC gateway address.')
ipAddr = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 1, 2, 12), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipAddr.setStatus('current')
if mibBuilder.loadTexts: ipAddr.setDescription('Gets the BUC IP address.')
macAddress = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 1, 2, 13), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: macAddress.setStatus('current')
if mibBuilder.loadTexts: macAddress.setDescription('Gets the BUC MAC address.')
netmask = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 1, 2, 14), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: netmask.setStatus('current')
if mibBuilder.loadTexts: netmask.setDescription('Gets the BUC netmask.')
refPower = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 1, 2, 15), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: refPower.setStatus('current')
if mibBuilder.loadTexts: refPower.setDescription('Gets the BUC reference power.')
bucConfiguration = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 1, 2, 16), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bucConfiguration.setStatus('current')
if mibBuilder.loadTexts: bucConfiguration.setDescription('Gets the BUC configuration.')
buildStandard = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 1, 2, 17), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: buildStandard.setStatus('current')
if mibBuilder.loadTexts: buildStandard.setDescription('Gets the BUC build standard.')
idInfo = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 1, 3, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: idInfo.setStatus('current')
if mibBuilder.loadTexts: idInfo.setDescription('Gets the module firmware revision, serial number and model. This string will have a zero length if the revision is unknown.')
limits = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 1, 3, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: limits.setStatus('current')
if mibBuilder.loadTexts: limits.setDescription('Gets the limit data for the BUC. Format is: Power meter MIN/MAX , IF,RF and LO frequencies. This string will have a zero length if the revision is unknown.')
pktProtocolsInfo = MibScalar((1, 3, 6, 1, 4, 1, 23304, 2, 1, 3, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pktProtocolsInfo.setStatus('current')
if mibBuilder.loadTexts: pktProtocolsInfo.setDescription('Gets supported packet protocols and the corresponding address ranges.')
mibBuilder.exportSymbols("RBUC-MIB", macAddress=macAddress, protocol=protocol, ledState=ledState, txBurstPower=txBurstPower, systemPoll=systemPoll, paStatus=paStatus, configuration=configuration, txSettings=txSettings, freqs=freqs, ifFreq=ifFreq, limits=limits, refSource=refSource, misc=misc, ComponentRevision=ComponentRevision, loFreq=loFreq, ipAddr=ipAddr, rfFreq=rfFreq, PYSNMP_MODULE_ID=rbucMIB, temperature=temperature, rbucMIB=rbucMIB, refPower=refPower, serIf=serIf, minMaxTemperature=minMaxTemperature, faults=faults, latchedFaults=latchedFaults, mode=mode, address=address, deviceType=deviceType, idInfo=idInfo, bucConfiguration=bucConfiguration, TxStatus=TxStatus, systemSetting=systemSetting, pktProtocolsInfo=pktProtocolsInfo, serEcho=serEcho, txAttenuator=txAttenuator, txOn=txOn, gateway=gateway, txPower=txPower, onLine=onLine, info=info, pwrAlarmThresh=pwrAlarmThresh, burstPwrThresh=burstPwrThresh, pktProtocol=pktProtocol, FaultStatus=FaultStatus, netmask=netmask, rcSetting=rcSetting, buildStandard=buildStandard, status=status, txDefault=txDefault)