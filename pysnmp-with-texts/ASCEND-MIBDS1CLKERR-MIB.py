#
# PySNMP MIB module ASCEND-MIBDS1CLKERR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-MIBDS1CLKERR-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:27:09 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
configuration, = mibBuilder.importSymbols("ASCEND-MIB", "configuration")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, iso, Integer32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Counter64, IpAddress, Gauge32, Bits, Unsigned32, MibIdentifier, NotificationType, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "iso", "Integer32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Counter64", "IpAddress", "Gauge32", "Bits", "Unsigned32", "MibIdentifier", "NotificationType", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class DisplayString(OctetString):
    pass

mibds1ClockErrorProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 164))
mibds1ClockErrorProfileTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 164, 1), )
if mibBuilder.loadTexts: mibds1ClockErrorProfileTable.setStatus('mandatory')
if mibBuilder.loadTexts: mibds1ClockErrorProfileTable.setDescription('A list of mibds1ClockErrorProfile profile entries.')
mibds1ClockErrorProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 164, 1, 1), ).setIndexNames((0, "ASCEND-MIBDS1CLKERR-MIB", "ds1ClockErrorProfile-Index-o"))
if mibBuilder.loadTexts: mibds1ClockErrorProfileEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mibds1ClockErrorProfileEntry.setDescription('A mibds1ClockErrorProfile entry containing objects that maps to the parameters of mibds1ClockErrorProfile profile.')
ds1ClockErrorProfile_Index_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 164, 1, 1, 1), Integer32()).setLabel("ds1ClockErrorProfile-Index-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: ds1ClockErrorProfile_Index_o.setStatus('mandatory')
if mibBuilder.loadTexts: ds1ClockErrorProfile_Index_o.setDescription('')
ds1ClockErrorProfile_Enabled = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 164, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("ds1ClockErrorProfile-Enabled").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds1ClockErrorProfile_Enabled.setStatus('mandatory')
if mibBuilder.loadTexts: ds1ClockErrorProfile_Enabled.setDescription("Enables or disables the feature of swapping the master clock source with the next priority source, if it is experiencing errors. The default value is 'no'.")
ds1ClockErrorProfile_CrcThreshold = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 164, 1, 1, 3), Integer32()).setLabel("ds1ClockErrorProfile-CrcThreshold").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds1ClockErrorProfile_CrcThreshold.setStatus('mandatory')
if mibBuilder.loadTexts: ds1ClockErrorProfile_CrcThreshold.setDescription('Threshold value of Cyclic Redundancy Check ( CRC ) Error per second. If set to 0, will not be considered in switching the Clock.')
ds1ClockErrorProfile_FrameSlipsThreshold = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 164, 1, 1, 4), Integer32()).setLabel("ds1ClockErrorProfile-FrameSlipsThreshold").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds1ClockErrorProfile_FrameSlipsThreshold.setStatus('mandatory')
if mibBuilder.loadTexts: ds1ClockErrorProfile_FrameSlipsThreshold.setDescription('Threshold value of Frame Slips Error per second. If set to 0, will not be considered in switching the Clock.')
ds1ClockErrorProfile_FerThreshold = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 164, 1, 1, 5), Integer32()).setLabel("ds1ClockErrorProfile-FerThreshold").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds1ClockErrorProfile_FerThreshold.setStatus('mandatory')
if mibBuilder.loadTexts: ds1ClockErrorProfile_FerThreshold.setDescription('Threshold value of Framing Error ( FER ) per second. If set to 0, will not be considered in switching the Clock.')
ds1ClockErrorProfile_OofThreshold = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 164, 1, 1, 6), Integer32()).setLabel("ds1ClockErrorProfile-OofThreshold").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds1ClockErrorProfile_OofThreshold.setStatus('mandatory')
if mibBuilder.loadTexts: ds1ClockErrorProfile_OofThreshold.setDescription('Threshold value of Out Of Frame (OOF) Error per second. If set to 0, will not be considered in switching the Clock.')
ds1ClockErrorProfile_FebeThreshold = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 164, 1, 1, 7), Integer32()).setLabel("ds1ClockErrorProfile-FebeThreshold").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds1ClockErrorProfile_FebeThreshold.setStatus('mandatory')
if mibBuilder.loadTexts: ds1ClockErrorProfile_FebeThreshold.setDescription('Threshold value of Far end block ( FEBE ) Error per second. If set to 0, will not be considered in switching the Clock.')
ds1ClockErrorProfile_LcvThreshold = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 164, 1, 1, 8), Integer32()).setLabel("ds1ClockErrorProfile-LcvThreshold").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds1ClockErrorProfile_LcvThreshold.setStatus('mandatory')
if mibBuilder.loadTexts: ds1ClockErrorProfile_LcvThreshold.setDescription('Threshold value of Line code violations ( LCV ) Error per second. If set to 0, will not be considered in switching the Clock.')
ds1ClockErrorProfile_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 164, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("ds1ClockErrorProfile-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds1ClockErrorProfile_Action_o.setStatus('mandatory')
if mibBuilder.loadTexts: ds1ClockErrorProfile_Action_o.setDescription('')
mibBuilder.exportSymbols("ASCEND-MIBDS1CLKERR-MIB", DisplayString=DisplayString, ds1ClockErrorProfile_Action_o=ds1ClockErrorProfile_Action_o, mibds1ClockErrorProfileTable=mibds1ClockErrorProfileTable, ds1ClockErrorProfile_OofThreshold=ds1ClockErrorProfile_OofThreshold, ds1ClockErrorProfile_FrameSlipsThreshold=ds1ClockErrorProfile_FrameSlipsThreshold, ds1ClockErrorProfile_FebeThreshold=ds1ClockErrorProfile_FebeThreshold, mibds1ClockErrorProfileEntry=mibds1ClockErrorProfileEntry, ds1ClockErrorProfile_Enabled=ds1ClockErrorProfile_Enabled, ds1ClockErrorProfile_Index_o=ds1ClockErrorProfile_Index_o, ds1ClockErrorProfile_FerThreshold=ds1ClockErrorProfile_FerThreshold, ds1ClockErrorProfile_CrcThreshold=ds1ClockErrorProfile_CrcThreshold, ds1ClockErrorProfile_LcvThreshold=ds1ClockErrorProfile_LcvThreshold, mibds1ClockErrorProfile=mibds1ClockErrorProfile)