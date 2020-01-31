#
# PySNMP MIB module CISCO-ITP-ACL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-ITP-ACL-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:03:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
CItpTcEncodingSchemeValue, CItpTcSubSystemNumber, CItpTcAclId, CItpTcTranslationType, CItpTcPointCodeMask, CItpTcServiceIndicator, CItpTcNumberingPlan, CItpTcPointCode, CItpTcSubSystemNumberMask, CItpTcGlobalTitleSelector, CItpTcNAI = mibBuilder.importSymbols("CISCO-ITP-TC-MIB", "CItpTcEncodingSchemeValue", "CItpTcSubSystemNumber", "CItpTcAclId", "CItpTcTranslationType", "CItpTcPointCodeMask", "CItpTcServiceIndicator", "CItpTcNumberingPlan", "CItpTcPointCode", "CItpTcSubSystemNumberMask", "CItpTcGlobalTitleSelector", "CItpTcNAI")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
iso, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Gauge32, Bits, ObjectIdentity, Counter64, IpAddress, Unsigned32, ModuleIdentity, Counter32, MibIdentifier, Integer32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Gauge32", "Bits", "ObjectIdentity", "Counter64", "IpAddress", "Unsigned32", "ModuleIdentity", "Counter32", "MibIdentifier", "Integer32", "NotificationType")
TimeStamp, TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "TextualConvention", "RowStatus", "DisplayString")
ciscoItpAclMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 227))
ciscoItpAclMIB.setRevisions(('2001-08-29 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoItpAclMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoItpAclMIB.setLastUpdated('200108290000Z')
if mibBuilder.loadTexts: ciscoItpAclMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoItpAclMIB.setContactInfo(' Cisco Systems, Inc Customer Service Postal: 170 W. Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-ss7@cisco.com')
if mibBuilder.loadTexts: ciscoItpAclMIB.setDescription('The MIB for managing access lists that control messages transported over Signalling System No. 7 (SS7) Network via Cisco IP Transfer Point. The Cisco IP Transfer Point (ITP) is a hardware and software solution that transports SS7 traffic using IP. Each ITP node provides function similar to SS7 signaling point. The relevant ITU documents describing this technology is the ITU Q series, including ITU Q.700: Introduction to CCITT Signalling System No. 7 and ITU Q.701 Functional description of the message transfer part (MTP) of Signalling System No. 7.')
cItpAclMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 227, 0))
cItpAclMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 227, 1))
cItpAclMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 227, 2))
cItpAclScalars = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 227, 1, 1))
cItpAclConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 227, 1, 2))
class CItpAclAction(TextualConvention, Integer32):
    description = "The list of possible actions to be performed on a packet when information in message matches an access control entry . 'accept' : The matching packet is accepted for further processing. 'discard' : The matching packet is to be discarded without any further processing on this packet."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("accept", 1), ("discard", 2))

cItpAclConfigLastChanged = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 227, 1, 1, 1), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cItpAclConfigLastChanged.setStatus('current')
if mibBuilder.loadTexts: cItpAclConfigLastChanged.setDescription('The value of sysUpTime at the time of the last creation or deletion of an entry in the cItpAclTable. If the local network management subsystem is re-initialization, then this object contains the sysUpTime at the time when this occurred. This value can be used to prevent unnecessary walks of the cItpAclTable.')
cItpAclTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 227, 1, 2, 1), )
if mibBuilder.loadTexts: cItpAclTable.setStatus('current')
if mibBuilder.loadTexts: cItpAclTable.setDescription('A table of SP access controls. The access control definition controls which packets are accepted or rejected. The access control may be applied before sending the packet to the routing table or may be applied after the packet is processed by the routing table. Entries are added to this table via cItpAclRowStatus in accordance with the RowStatus convention.')
cItpAclTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 227, 1, 2, 1, 1), ).setIndexNames((0, "CISCO-ITP-ACL-MIB", "cItpAclId"), (0, "CISCO-ITP-ACL-MIB", "cItpAclEntryType"), (0, "CISCO-ITP-ACL-MIB", "cItpAclEntryNumber"))
if mibBuilder.loadTexts: cItpAclTableEntry.setStatus('current')
if mibBuilder.loadTexts: cItpAclTableEntry.setDescription('A list of Signalling Point access control attributes.')
cItpAclId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 227, 1, 2, 1, 1, 1), CItpTcAclId())
if mibBuilder.loadTexts: cItpAclId.setStatus('current')
if mibBuilder.loadTexts: cItpAclId.setDescription('The identifier used to select a list of access list entries. The administrator will select an valid identifier within the specified range defined for SS7 access lists.')
cItpAclEntryType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 227, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("comment", 1), ("entry", 2))))
if mibBuilder.loadTexts: cItpAclEntryType.setStatus('current')
if mibBuilder.loadTexts: cItpAclEntryType.setDescription("The list of possible entry types. 'comments' : A statement used to describe and document access list entries. 'entry' : A access list entry.")
cItpAclEntryNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 227, 1, 2, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: cItpAclEntryNumber.setStatus('current')
if mibBuilder.loadTexts: cItpAclEntryNumber.setDescription('An numeric value assigned to each access list entry. The entries of the same type must be unique. Entries will be tested in ascending order.')
cItpAclAction = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 227, 1, 2, 1, 1, 4), CItpAclAction().clone('accept')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cItpAclAction.setStatus('current')
if mibBuilder.loadTexts: cItpAclAction.setDescription('The action to be performed on the packet that matched this access control.')
cItpAclParameters = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 227, 1, 2, 1, 1, 5), Bits().clone(namedValues=NamedValues(("si", 0), ("dpc", 1), ("dpcMask", 2), ("opc", 3), ("opcMask", 4), ("pattern", 5), ("comment", 6), ("cgpa", 7), ("cgpaMask", 8), ("cdpa", 9), ("cdpaMask", 10), ("selector", 11), ("aft", 12), ("aftMask", 13), ("all", 14)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cItpAclParameters.setStatus('current')
if mibBuilder.loadTexts: cItpAclParameters.setDescription("The cItpAclType object indicates which types of tests will be processed on the each access list entry. Each may contain one or more filters. The filter will be processed ascending order(si,dpc...all). Each test is evaluated and if true the packet is processed according to cItpAclAction. 'si' : The cItpAclSi is the relevant column. The packet is compared to cItpAclSi to determine if the packet matches this filter. 'dpc' : The cItpAclDpc and cItpAclDpcMask are the relevant columns. The packet is compared to cItpAclDpc in conjunction with cItpAclDpcMask to determine if the packet matches this access control. The mask is first negated (~mask) and bitwise AND is perform with mask and dpc. 'dpcMask' : Indicates that a mask is to be applied when the dpc filter is specified. If the mask is not specified then the mask is assumed to be all zeros. 'opc' : cItpAclOpc and cItpAclOpcMask are the relevant columns. The packet is compared to cItpAclOpc in conjunction with cItpAclOpcMask to determine if the packet matches this access control. The mask is first negated (~mask) and bitwise AND is perform with mask and opc. 'opcMask' : Indicates that a mask is to be applied when the opc filter is specified. If the mask is not specified then the mask is assumed to be all zeros. 'pattern' : cItpAclPattern and cItpAclOffset are the relevant columns. The matching criteria is based on matching the pattern specified by cItpAclPattern at offset cItpAclOffset from the start of the packet. 'comment' : The cItpAclComment object provides an entry that can be used to describe filters. 'cgpa' : The cItpAclCgpa, cItpAclCgpaMask, cItpAclCgpaSsn and cItpAclCgpaSsnMask are the relevant columns. The Calling Party Point code is compare with cItpAclCgpaPC using the ItpAclCgpaMask. Also, the cItpAclCgpaSsn and cItpAclCgpaSsnMask are compared if specified. 'cgpaMask': Indicates that a mask is to be applied when the cgpa filter is specified. If the mask is not specified then the mask is assumed to be all zeros. 'cgpaSsn' : Indicates that a Subsystem Number(SSN) is to be checked when the cgpa filter is specified. 'cgpaSsnMask': Indicates that SSN mask is to be applied when checking the SSN number for the cgpa filter is specified. If the mask is not specified then the mask is assumed to be all zeros. 'cdpa' : The cItpAclCdpa, cItpAclCdpaMask, cItpAclCdpaSsn and cItpAclCdpaSsnMask are the relevant columns. The Called Party Point code is compared with cItpAclCcpa using the ItpAclCcpaMask. Also, the cItpAclCcpaSsn and cItpAclCcpaSsnMask are compared if specified. 'cdpaMask': Indicates that a mask is to be applied when the cdpa filter is specified. If the mask is not specified then the mask is assumed to be all zeros. 'cdpaSsn' : Indicates that a SSN is to be checked when the cdpa filter is specified. 'cdpaSsnMask': Indicates that SSN mask is to be applied when checking the SSN number for the cdpa filter is specified. If the mask is not specified then the mask is assumed to be all zeros. 'selector': The Global Title Selector is used to select which objects will be tested and in what order the tests will be applied as follows. x The types of translations are different based on the variant. In both, variants the translation type and other parameters are used to provide the following types of translations. - Intermediate GTT resulting in MSUs routed to a solitary point code - Intermediate GTT resulting in MSUs load balanced across two or more point codes - Final GTT routed to a solitary point code - Final GTT routed to a primary and backup point-code and SSN (dominant mode) - Final GTT load balanced across a group of point-codes and subsystems For ANSI the translation types are defined in TABLE B.1/T1.112.3 of TR-NWT-000246. The ANSI selector table may be a simple flat table/array of 256 Translation Types(0-255). In this method of translation tables can be directly accessed using the translation type from the Called Party Point Code. For ITU section 2.4.5 of ITU-T Q.714, defines the use of the Global Tile Indicator(GTI), along with Translation Type(TT), Network Plan(NP), and Nature of Address Indicator(NAI), as selectors for the table to perform the Global Title Translation(GTT). In this cae the selector table must be searched using a combination oF GTI, TT, NP and NAI. The objects cItpAclGtiSelector, cItpAclGtiTranslateType, cItpAclGtiNumberingPlan, cItpAclGtiNai, and cItpAclGtiEsv are the relevant columns. These object will be used in the following order based on variant and translation type. 1 => cItpAclGtiNai 2 => cItpAclGtiTranslateType 3 => cItpAclGtiTranslateType cItpAclGtiNumberingPlan cItpAclGtiEsv 4 => cItpAclGtiTranslateType cItpAclGtiNumberingPlan cItpAclGtiNai cItpAclGtiEsv 'aft' : The cItpAclAft, cItpAclAftMask, cItpAclAftSsn and cItpAclAftSsnMask are the relevant columns. The affected point code is compared with cItpAclAftPC using the ItpAclAftMask. Also, the cItpAclAftSsn and cItpAclAftSsnMask are compared if specified. 'aftMask': Indicates that a mask is to be applied when the aft filter is specified. If the mask is not specified then the mask is assumed to be all zeros. 'all' : Used in conjunction with cItpAclAction to specify defaults for packet that did not match any specified access list entry.")
cItpAclDpc = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 227, 1, 2, 1, 1, 6), CItpTcPointCode()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cItpAclDpc.setStatus('current')
if mibBuilder.loadTexts: cItpAclDpc.setDescription("The destination point code specified for this ACL. The 'dpc' bit in the cItpAclParameters object is used indicate whether this object has been specified.")
cItpAclDpcMask = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 227, 1, 2, 1, 1, 7), CItpTcPointCodeMask()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cItpAclDpcMask.setStatus('current')
if mibBuilder.loadTexts: cItpAclDpcMask.setDescription("The mask used to define which part of the point code in the packet is significant when comparing the destination point code with cItpAclDpc. The 'dpcMask' bit in the cItpAclParameters object is used indicate whether this object has been specified.")
cItpAclOpc = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 227, 1, 2, 1, 1, 8), CItpTcPointCode()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cItpAclOpc.setStatus('current')
if mibBuilder.loadTexts: cItpAclOpc.setDescription("The origin point code specified in this ACL. The 'opc' bit in the cItpAclParameters object is used indicate whether this object has been specified.")
cItpAclOpcMask = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 227, 1, 2, 1, 1, 9), CItpTcPointCodeMask()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cItpAclOpcMask.setStatus('current')
if mibBuilder.loadTexts: cItpAclOpcMask.setDescription("The mask used to define which part of the origin point code in the packet is significant when comparing the origin point code with cItpAclDpc. The 'opcMask' bit in the cItpAclParameters object is used indicate whether this object has been specified.")
cItpAclSi = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 227, 1, 2, 1, 1, 10), CItpTcServiceIndicator()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cItpAclSi.setStatus('current')
if mibBuilder.loadTexts: cItpAclSi.setDescription("The Service Indicator Octet. The 'si' bit in the cItpAclParameters object is used indicate whether this object has been specified.")
cItpAclPattern = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 227, 1, 2, 1, 1, 11), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 40))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cItpAclPattern.setStatus('current')
if mibBuilder.loadTexts: cItpAclPattern.setDescription("The pattern used to match a packet at offset cItpAclOffset. The 'pattern' bit in the cItpAclParameters object is used indicate whether this object has been specified.")
cItpAclOffset = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 227, 1, 2, 1, 1, 12), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cItpAclOffset.setStatus('current')
if mibBuilder.loadTexts: cItpAclOffset.setDescription("The offset into the packet were we begin matching the pattern specified by cItpAclPattern is to start. The 'pattern' bit in the cItpAclParameters object is used indicate whether this object has been specified.")
cItpAclComment = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 227, 1, 2, 1, 1, 13), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 100))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cItpAclComment.setStatus('current')
if mibBuilder.loadTexts: cItpAclComment.setDescription("A brief description used to document access list entries. The 'comment' bit in the cItpAclParameters object is used indicate whether this object has been specified.")
cItpAclCgpa = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 227, 1, 2, 1, 1, 14), CItpTcPointCode()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cItpAclCgpa.setStatus('current')
if mibBuilder.loadTexts: cItpAclCgpa.setDescription("The Calling Party Point Code. The 'cgpa' bit in the cItpAclParameters object is used indicate whether this object has been specified.")
cItpAclCgpaMask = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 227, 1, 2, 1, 1, 15), CItpTcPointCodeMask()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cItpAclCgpaMask.setStatus('current')
if mibBuilder.loadTexts: cItpAclCgpaMask.setDescription("The Calling Party Point Code mask. The 'cgpaMask' bit in the cItpAclParameters object is used indicate whether this object has been specified.")
cItpAclCgpaSsn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 227, 1, 2, 1, 1, 16), CItpTcSubSystemNumber()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cItpAclCgpaSsn.setStatus('current')
if mibBuilder.loadTexts: cItpAclCgpaSsn.setDescription("The Calling Party Point Code subsystem number. The 'cgpa' bit in the cItpAclParameters object is used indicate whether this object has been specified.")
cItpAclCgpaSsnMask = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 227, 1, 2, 1, 1, 17), CItpTcSubSystemNumberMask()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cItpAclCgpaSsnMask.setStatus('current')
if mibBuilder.loadTexts: cItpAclCgpaSsnMask.setDescription("The Calling Party Point Code subsystem number Mask. The 'cgpa' bit in the cItpAclParameters object is used indicate whether this object has been specified.")
cItpAclCdpa = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 227, 1, 2, 1, 1, 18), CItpTcPointCode()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cItpAclCdpa.setStatus('current')
if mibBuilder.loadTexts: cItpAclCdpa.setDescription("The Called Party Point Code. The 'cdpa' bit in the cItpAclParameters object is used indicate whether this object has been specified.")
cItpAclCdpaMask = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 227, 1, 2, 1, 1, 19), CItpTcPointCodeMask()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cItpAclCdpaMask.setStatus('current')
if mibBuilder.loadTexts: cItpAclCdpaMask.setDescription("The Called Party Point Code mask. The 'cdpaMask' bit in the cItpAclParameters object is used indicate whether this object has been specified.")
cItpAclCdpaSsn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 227, 1, 2, 1, 1, 20), CItpTcSubSystemNumber()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cItpAclCdpaSsn.setStatus('current')
if mibBuilder.loadTexts: cItpAclCdpaSsn.setDescription("The Called Party Point Code subsystem number. The 'cdpa' bit in the cItpAclParameters object is used indicate whether this object has been specified.")
cItpAclCdpaSsnMask = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 227, 1, 2, 1, 1, 21), CItpTcSubSystemNumberMask()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cItpAclCdpaSsnMask.setStatus('current')
if mibBuilder.loadTexts: cItpAclCdpaSsnMask.setDescription("The Called Party Point Code subsystem number Mask. The 'cdpa' bit in the cItpAclParameters object is used indicate whether this object has been specified.")
cItpAclGtiSelector = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 227, 1, 2, 1, 1, 22), CItpTcGlobalTitleSelector()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cItpAclGtiSelector.setStatus('current')
if mibBuilder.loadTexts: cItpAclGtiSelector.setDescription("The Global Title Selector. The 'selector' bit in the cItpAclParameters object is used indicate whether this object has been specified.")
cItpAclGtiTranslateType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 227, 1, 2, 1, 1, 23), CItpTcTranslationType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cItpAclGtiTranslateType.setStatus('current')
if mibBuilder.loadTexts: cItpAclGtiTranslateType.setDescription("The Global Title Translate Type. The 'selector' bit in the cItpAclParameters object is used indicate whether this object has been specified.")
cItpAclGtiNumberingPlan = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 227, 1, 2, 1, 1, 24), CItpTcNumberingPlan()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cItpAclGtiNumberingPlan.setStatus('current')
if mibBuilder.loadTexts: cItpAclGtiNumberingPlan.setDescription("The Global Title Numbering Plan. The 'selector' bit in the cItpAclParameters object is used indicate whether this object has been specified.")
cItpAclGtiNai = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 227, 1, 2, 1, 1, 25), CItpTcNAI()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cItpAclGtiNai.setStatus('current')
if mibBuilder.loadTexts: cItpAclGtiNai.setDescription("The Global Title nature of address indicator. The 'selector' bit in the cItpAclParameters object is used indicate whether this object has been specified.")
cItpAclGtiEsv = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 227, 1, 2, 1, 1, 26), CItpTcEncodingSchemeValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cItpAclGtiEsv.setStatus('current')
if mibBuilder.loadTexts: cItpAclGtiEsv.setDescription("The Global Title encoding scheme value. The 'selector' bit in the cItpAclParameters object is used indicate whether this object has been specified.")
cItpAclAft = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 227, 1, 2, 1, 1, 27), CItpTcPointCode()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cItpAclAft.setStatus('current')
if mibBuilder.loadTexts: cItpAclAft.setDescription("The Affected Point Code. The 'aft' bit in the cItpAclParameters object is used indicate whether this object has been specified.")
cItpAclAftMask = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 227, 1, 2, 1, 1, 28), CItpTcPointCodeMask()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cItpAclAftMask.setStatus('current')
if mibBuilder.loadTexts: cItpAclAftMask.setDescription("The Affected Point Code mask. The 'aftMask' bit in the cItpAclParameters object is used indicate whether this object has been specified.")
cItpAclAftSsn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 227, 1, 2, 1, 1, 29), CItpTcSubSystemNumber()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cItpAclAftSsn.setStatus('current')
if mibBuilder.loadTexts: cItpAclAftSsn.setDescription("The Affected Point Code subsystem number. The 'aft' bit in the cItpAclParameters object is used indicate whether this object has been specified.")
cItpAclAftSsnMask = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 227, 1, 2, 1, 1, 30), CItpTcSubSystemNumberMask()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cItpAclAftSsnMask.setStatus('current')
if mibBuilder.loadTexts: cItpAclAftSsnMask.setDescription("The Affected Point Code subsystem number Mask. The 'aft' bit in the cItpAclParameters object is used indicate whether this object has been specified.")
cItpAclRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 227, 1, 2, 1, 1, 31), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cItpAclRowStatus.setStatus('current')
if mibBuilder.loadTexts: cItpAclRowStatus.setDescription('The object is used by a management station to create or delete the row entry in cItpAcl following the RowStatus textual convention.')
cItpAclMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 227, 2, 1))
cItpAclMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 227, 2, 2))
cItpAclMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 227, 2, 1, 1)).setObjects(("CISCO-ITP-ACL-MIB", "cItpAclScalarGroup"), ("CISCO-ITP-ACL-MIB", "cItpAclAccessListGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cItpAclMIBCompliance = cItpAclMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: cItpAclMIBCompliance.setDescription('The compliance statement for entities which implement the Cisco SP MIB')
cItpAclScalarGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 227, 2, 2, 1)).setObjects(("CISCO-ITP-ACL-MIB", "cItpAclConfigLastChanged"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cItpAclScalarGroup = cItpAclScalarGroup.setStatus('current')
if mibBuilder.loadTexts: cItpAclScalarGroup.setDescription('SP main objects.')
cItpAclAccessListGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 227, 2, 2, 2)).setObjects(("CISCO-ITP-ACL-MIB", "cItpAclAction"), ("CISCO-ITP-ACL-MIB", "cItpAclParameters"), ("CISCO-ITP-ACL-MIB", "cItpAclDpc"), ("CISCO-ITP-ACL-MIB", "cItpAclDpcMask"), ("CISCO-ITP-ACL-MIB", "cItpAclOpc"), ("CISCO-ITP-ACL-MIB", "cItpAclOpcMask"), ("CISCO-ITP-ACL-MIB", "cItpAclSi"), ("CISCO-ITP-ACL-MIB", "cItpAclPattern"), ("CISCO-ITP-ACL-MIB", "cItpAclOffset"), ("CISCO-ITP-ACL-MIB", "cItpAclComment"), ("CISCO-ITP-ACL-MIB", "cItpAclCgpa"), ("CISCO-ITP-ACL-MIB", "cItpAclCgpaMask"), ("CISCO-ITP-ACL-MIB", "cItpAclCgpaSsn"), ("CISCO-ITP-ACL-MIB", "cItpAclCgpaSsnMask"), ("CISCO-ITP-ACL-MIB", "cItpAclCdpa"), ("CISCO-ITP-ACL-MIB", "cItpAclCdpaMask"), ("CISCO-ITP-ACL-MIB", "cItpAclCdpaSsn"), ("CISCO-ITP-ACL-MIB", "cItpAclCdpaSsnMask"), ("CISCO-ITP-ACL-MIB", "cItpAclGtiSelector"), ("CISCO-ITP-ACL-MIB", "cItpAclGtiTranslateType"), ("CISCO-ITP-ACL-MIB", "cItpAclGtiNumberingPlan"), ("CISCO-ITP-ACL-MIB", "cItpAclGtiNai"), ("CISCO-ITP-ACL-MIB", "cItpAclGtiEsv"), ("CISCO-ITP-ACL-MIB", "cItpAclAft"), ("CISCO-ITP-ACL-MIB", "cItpAclAftMask"), ("CISCO-ITP-ACL-MIB", "cItpAclAftSsn"), ("CISCO-ITP-ACL-MIB", "cItpAclAftSsnMask"), ("CISCO-ITP-ACL-MIB", "cItpAclRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cItpAclAccessListGroup = cItpAclAccessListGroup.setStatus('current')
if mibBuilder.loadTexts: cItpAclAccessListGroup.setDescription('Signaling Point access control list objects.')
mibBuilder.exportSymbols("CISCO-ITP-ACL-MIB", cItpAclAftSsn=cItpAclAftSsn, cItpAclScalarGroup=cItpAclScalarGroup, cItpAclMIBNotifs=cItpAclMIBNotifs, cItpAclDpcMask=cItpAclDpcMask, PYSNMP_MODULE_ID=ciscoItpAclMIB, cItpAclMIBObjects=cItpAclMIBObjects, cItpAclScalars=cItpAclScalars, cItpAclEntryType=cItpAclEntryType, cItpAclGtiNumberingPlan=cItpAclGtiNumberingPlan, cItpAclCdpa=cItpAclCdpa, cItpAclDpc=cItpAclDpc, cItpAclCgpaMask=cItpAclCgpaMask, cItpAclMIBGroups=cItpAclMIBGroups, cItpAclCgpaSsn=cItpAclCgpaSsn, cItpAclAftMask=cItpAclAftMask, cItpAclMIBCompliance=cItpAclMIBCompliance, cItpAclPattern=cItpAclPattern, cItpAclSi=cItpAclSi, cItpAclOffset=cItpAclOffset, cItpAclGtiSelector=cItpAclGtiSelector, cItpAclAft=cItpAclAft, cItpAclCdpaSsn=cItpAclCdpaSsn, cItpAclComment=cItpAclComment, cItpAclEntryNumber=cItpAclEntryNumber, cItpAclId=cItpAclId, cItpAclAftSsnMask=cItpAclAftSsnMask, cItpAclGtiTranslateType=cItpAclGtiTranslateType, ciscoItpAclMIB=ciscoItpAclMIB, cItpAclGtiNai=cItpAclGtiNai, cItpAclTable=cItpAclTable, cItpAclAction=cItpAclAction, cItpAclTableEntry=cItpAclTableEntry, cItpAclMIBConformance=cItpAclMIBConformance, cItpAclCgpa=cItpAclCgpa, cItpAclConfigLastChanged=cItpAclConfigLastChanged, cItpAclRowStatus=cItpAclRowStatus, cItpAclMIBCompliances=cItpAclMIBCompliances, cItpAclOpc=cItpAclOpc, cItpAclOpcMask=cItpAclOpcMask, cItpAclCdpaSsnMask=cItpAclCdpaSsnMask, cItpAclParameters=cItpAclParameters, CItpAclAction=CItpAclAction, cItpAclCgpaSsnMask=cItpAclCgpaSsnMask, cItpAclConfig=cItpAclConfig, cItpAclAccessListGroup=cItpAclAccessListGroup, cItpAclCdpaMask=cItpAclCdpaMask, cItpAclGtiEsv=cItpAclGtiEsv)