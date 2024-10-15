# SNMP MIB module (IEEE8021-FQTSS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IEEE8021-FQTSS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:08:24 2024
# On host MacBook-Pro.local platform Darwin version 24.0.0 by user lextm
# Using Python version 3.12.0 (main, Nov 14 2023, 23:52:11) [Clang 15.0.0 (clang-1500.0.40.1)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint,
 ConstraintsUnion) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint",
    "ConstraintsUnion")

# Import SMI symbols from the MIBs this MIB depends on

(BridgeId,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "BridgeId")

(ieee8021BridgeBaseComponentId,
 ieee8021BridgeBaseEntry,
 ieee8021BridgeBasePort,
 ieee8021BridgeBasePortEntry) = mibBuilder.importSymbols(
    "IEEE8021-BRIDGE-MIB",
    "ieee8021BridgeBaseComponentId",
    "ieee8021BridgeBaseEntry",
    "ieee8021BridgeBasePort",
    "ieee8021BridgeBasePortEntry")

(IEEE8021PriorityValue,
 ieee802dot1mibs) = mibBuilder.importSymbols(
    "IEEE8021-TC-MIB",
    "IEEE8021PriorityValue",
    "ieee802dot1mibs")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ieee8021FqtssMib = ModuleIdentity(
    (1, 3, 111, 2, 802, 1, 1, 16)
)
ieee8021FqtssMib.setRevisions(
        ("2018-10-04 00:00",
         "2018-06-28 00:00",
         "2015-12-02 00:00",
         "2014-12-15 00:00",
         "2011-02-27 00:00",
         "2009-10-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class IEEE8021FqtssTrafficClassValue(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )



class IEEE8021FqtssDeltaBandwidthValue(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000000),
    )



class IEEE8021FqtssTxSelectionAlgorithmIDValue(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"


# MIB Managed Objects in the order of their OIDs

_Ieee8021FqtssNotifications_ObjectIdentity = ObjectIdentity
ieee8021FqtssNotifications = _Ieee8021FqtssNotifications_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 16, 0)
)
_Ieee8021FqtssObjects_ObjectIdentity = ObjectIdentity
ieee8021FqtssObjects = _Ieee8021FqtssObjects_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 16, 1)
)
_Ieee8021FqtssBap_ObjectIdentity = ObjectIdentity
ieee8021FqtssBap = _Ieee8021FqtssBap_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 16, 1, 1)
)
_Ieee8021FqtssBapTable_Object = MibTable
ieee8021FqtssBapTable = _Ieee8021FqtssBapTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 16, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ieee8021FqtssBapTable.setStatus("current")
_Ieee8021FqtssBapEntry_Object = MibTableRow
ieee8021FqtssBapEntry = _Ieee8021FqtssBapEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 16, 1, 1, 1, 1)
)
ieee8021FqtssBapEntry.setIndexNames(
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBaseComponentId"),
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePort"),
    (0, "IEEE8021-FQTSS-MIB", "ieee8021FqtssBAPTrafficClass"),
)
if mibBuilder.loadTexts:
    ieee8021FqtssBapEntry.setStatus("current")
_Ieee8021FqtssBAPTrafficClass_Type = IEEE8021FqtssTrafficClassValue
_Ieee8021FqtssBAPTrafficClass_Object = MibTableColumn
ieee8021FqtssBAPTrafficClass = _Ieee8021FqtssBAPTrafficClass_Object(
    (1, 3, 111, 2, 802, 1, 1, 16, 1, 1, 1, 1, 1),
    _Ieee8021FqtssBAPTrafficClass_Type()
)
ieee8021FqtssBAPTrafficClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021FqtssBAPTrafficClass.setStatus("current")
_Ieee8021FqtssDeltaBandwidth_Type = IEEE8021FqtssDeltaBandwidthValue
_Ieee8021FqtssDeltaBandwidth_Object = MibTableColumn
ieee8021FqtssDeltaBandwidth = _Ieee8021FqtssDeltaBandwidth_Object(
    (1, 3, 111, 2, 802, 1, 1, 16, 1, 1, 1, 1, 2),
    _Ieee8021FqtssDeltaBandwidth_Type()
)
ieee8021FqtssDeltaBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021FqtssDeltaBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021FqtssDeltaBandwidth.setUnits("percent")
_Ieee8021FqtssOperIdleSlopeMs_Type = Unsigned32
_Ieee8021FqtssOperIdleSlopeMs_Object = MibTableColumn
ieee8021FqtssOperIdleSlopeMs = _Ieee8021FqtssOperIdleSlopeMs_Object(
    (1, 3, 111, 2, 802, 1, 1, 16, 1, 1, 1, 1, 3),
    _Ieee8021FqtssOperIdleSlopeMs_Type()
)
ieee8021FqtssOperIdleSlopeMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021FqtssOperIdleSlopeMs.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021FqtssOperIdleSlopeMs.setUnits("bits per second")
_Ieee8021FqtssOperIdleSlopeLs_Type = Unsigned32
_Ieee8021FqtssOperIdleSlopeLs_Object = MibTableColumn
ieee8021FqtssOperIdleSlopeLs = _Ieee8021FqtssOperIdleSlopeLs_Object(
    (1, 3, 111, 2, 802, 1, 1, 16, 1, 1, 1, 1, 4),
    _Ieee8021FqtssOperIdleSlopeLs_Type()
)
ieee8021FqtssOperIdleSlopeLs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021FqtssOperIdleSlopeLs.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021FqtssOperIdleSlopeLs.setUnits("bits per second")


class _Ieee8021FqtssAdminIdleSlopeMs_Type(Unsigned32):
    """Custom type ieee8021FqtssAdminIdleSlopeMs based on Unsigned32"""
    defaultValue = 0


_Ieee8021FqtssAdminIdleSlopeMs_Object = MibTableColumn
ieee8021FqtssAdminIdleSlopeMs = _Ieee8021FqtssAdminIdleSlopeMs_Object(
    (1, 3, 111, 2, 802, 1, 1, 16, 1, 1, 1, 1, 5),
    _Ieee8021FqtssAdminIdleSlopeMs_Type()
)
ieee8021FqtssAdminIdleSlopeMs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021FqtssAdminIdleSlopeMs.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021FqtssAdminIdleSlopeMs.setUnits("bits per second")


class _Ieee8021FqtssAdminIdleSlopeLs_Type(Unsigned32):
    """Custom type ieee8021FqtssAdminIdleSlopeLs based on Unsigned32"""
    defaultValue = 0


_Ieee8021FqtssAdminIdleSlopeLs_Object = MibTableColumn
ieee8021FqtssAdminIdleSlopeLs = _Ieee8021FqtssAdminIdleSlopeLs_Object(
    (1, 3, 111, 2, 802, 1, 1, 16, 1, 1, 1, 1, 6),
    _Ieee8021FqtssAdminIdleSlopeLs_Type()
)
ieee8021FqtssAdminIdleSlopeLs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021FqtssAdminIdleSlopeLs.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021FqtssAdminIdleSlopeLs.setUnits("bits per second")
_Ieee8021FqtssBapRowStatus_Type = RowStatus
_Ieee8021FqtssBapRowStatus_Object = MibTableColumn
ieee8021FqtssBapRowStatus = _Ieee8021FqtssBapRowStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 16, 1, 1, 1, 1, 7),
    _Ieee8021FqtssBapRowStatus_Type()
)
ieee8021FqtssBapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021FqtssBapRowStatus.setStatus("current")
_Ieee8021FqtssMappings_ObjectIdentity = ObjectIdentity
ieee8021FqtssMappings = _Ieee8021FqtssMappings_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 16, 1, 2)
)
_Ieee8021FqtssTxSelectionAlgorithmTable_Object = MibTable
ieee8021FqtssTxSelectionAlgorithmTable = _Ieee8021FqtssTxSelectionAlgorithmTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 16, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ieee8021FqtssTxSelectionAlgorithmTable.setStatus("current")
_Ieee8021FqtssTxSelectionAlgorithmEntry_Object = MibTableRow
ieee8021FqtssTxSelectionAlgorithmEntry = _Ieee8021FqtssTxSelectionAlgorithmEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 16, 1, 2, 1, 1)
)
ieee8021FqtssTxSelectionAlgorithmEntry.setIndexNames(
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBaseComponentId"),
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePort"),
    (0, "IEEE8021-FQTSS-MIB", "ieee8021FqtssTrafficClass"),
)
if mibBuilder.loadTexts:
    ieee8021FqtssTxSelectionAlgorithmEntry.setStatus("current")
_Ieee8021FqtssTrafficClass_Type = IEEE8021FqtssTrafficClassValue
_Ieee8021FqtssTrafficClass_Object = MibTableColumn
ieee8021FqtssTrafficClass = _Ieee8021FqtssTrafficClass_Object(
    (1, 3, 111, 2, 802, 1, 1, 16, 1, 2, 1, 1, 1),
    _Ieee8021FqtssTrafficClass_Type()
)
ieee8021FqtssTrafficClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021FqtssTrafficClass.setStatus("current")
_Ieee8021FqtssTxSelectionAlgorithmID_Type = IEEE8021FqtssTxSelectionAlgorithmIDValue
_Ieee8021FqtssTxSelectionAlgorithmID_Object = MibTableColumn
ieee8021FqtssTxSelectionAlgorithmID = _Ieee8021FqtssTxSelectionAlgorithmID_Object(
    (1, 3, 111, 2, 802, 1, 1, 16, 1, 2, 1, 1, 2),
    _Ieee8021FqtssTxSelectionAlgorithmID_Type()
)
ieee8021FqtssTxSelectionAlgorithmID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021FqtssTxSelectionAlgorithmID.setStatus("current")
_Ieee8021FqtssSrpRegenOverrideTable_Object = MibTable
ieee8021FqtssSrpRegenOverrideTable = _Ieee8021FqtssSrpRegenOverrideTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 16, 1, 2, 2)
)
if mibBuilder.loadTexts:
    ieee8021FqtssSrpRegenOverrideTable.setStatus("current")
_Ieee8021FqtssSrpRegenOverrideEntry_Object = MibTableRow
ieee8021FqtssSrpRegenOverrideEntry = _Ieee8021FqtssSrpRegenOverrideEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 16, 1, 2, 2, 1)
)
ieee8021FqtssSrpRegenOverrideEntry.setIndexNames(
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBaseComponentId"),
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePort"),
    (0, "IEEE8021-FQTSS-MIB", "ieee8021FqtssSrClassPriority"),
)
if mibBuilder.loadTexts:
    ieee8021FqtssSrpRegenOverrideEntry.setStatus("current")
_Ieee8021FqtssSrClassPriority_Type = IEEE8021PriorityValue
_Ieee8021FqtssSrClassPriority_Object = MibTableColumn
ieee8021FqtssSrClassPriority = _Ieee8021FqtssSrClassPriority_Object(
    (1, 3, 111, 2, 802, 1, 1, 16, 1, 2, 2, 1, 1),
    _Ieee8021FqtssSrClassPriority_Type()
)
ieee8021FqtssSrClassPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021FqtssSrClassPriority.setStatus("current")
_Ieee8021FqtssPriorityRegenOverride_Type = IEEE8021PriorityValue
_Ieee8021FqtssPriorityRegenOverride_Object = MibTableColumn
ieee8021FqtssPriorityRegenOverride = _Ieee8021FqtssPriorityRegenOverride_Object(
    (1, 3, 111, 2, 802, 1, 1, 16, 1, 2, 2, 1, 2),
    _Ieee8021FqtssPriorityRegenOverride_Type()
)
ieee8021FqtssPriorityRegenOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021FqtssPriorityRegenOverride.setStatus("current")
_Ieee8021FqtssSrpBoundaryPort_Type = TruthValue
_Ieee8021FqtssSrpBoundaryPort_Object = MibTableColumn
ieee8021FqtssSrpBoundaryPort = _Ieee8021FqtssSrpBoundaryPort_Object(
    (1, 3, 111, 2, 802, 1, 1, 16, 1, 2, 2, 1, 3),
    _Ieee8021FqtssSrpBoundaryPort_Type()
)
ieee8021FqtssSrpBoundaryPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021FqtssSrpBoundaryPort.setStatus("current")
_Ieee8021FqtssSRClassToPriorityTable_Object = MibTable
ieee8021FqtssSRClassToPriorityTable = _Ieee8021FqtssSRClassToPriorityTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 16, 1, 2, 3)
)
if mibBuilder.loadTexts:
    ieee8021FqtssSRClassToPriorityTable.setStatus("current")
_Ieee8021FqtssSRClassToPriorityEntry_Object = MibTableRow
ieee8021FqtssSRClassToPriorityEntry = _Ieee8021FqtssSRClassToPriorityEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 16, 1, 2, 3, 1)
)
ieee8021FqtssSRClassToPriorityEntry.setIndexNames(
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBaseComponentId"),
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePort"),
    (0, "IEEE8021-FQTSS-MIB", "ieee8021FqtssSrClassPriority"),
)
if mibBuilder.loadTexts:
    ieee8021FqtssSRClassToPriorityEntry.setStatus("current")
_Ieee8021FqtssSRClassToPrioritySrClassID_Type = IEEE8021FqtssTrafficClassValue
_Ieee8021FqtssSRClassToPrioritySrClassID_Object = MibTableColumn
ieee8021FqtssSRClassToPrioritySrClassID = _Ieee8021FqtssSRClassToPrioritySrClassID_Object(
    (1, 3, 111, 2, 802, 1, 1, 16, 1, 2, 3, 1, 1),
    _Ieee8021FqtssSRClassToPrioritySrClassID_Type()
)
ieee8021FqtssSRClassToPrioritySrClassID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021FqtssSRClassToPrioritySrClassID.setStatus("current")
_Ieee8021FqtssSRClassToPriorityRowStatus_Type = RowStatus
_Ieee8021FqtssSRClassToPriorityRowStatus_Object = MibTableColumn
ieee8021FqtssSRClassToPriorityRowStatus = _Ieee8021FqtssSRClassToPriorityRowStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 16, 1, 2, 3, 1, 2),
    _Ieee8021FqtssSRClassToPriorityRowStatus_Type()
)
ieee8021FqtssSRClassToPriorityRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021FqtssSRClassToPriorityRowStatus.setStatus("current")
_Ieee8021FqtssBapX_ObjectIdentity = ObjectIdentity
ieee8021FqtssBapX = _Ieee8021FqtssBapX_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 16, 1, 3)
)
_Ieee8021FqtssBapXTable_Object = MibTable
ieee8021FqtssBapXTable = _Ieee8021FqtssBapXTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 16, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ieee8021FqtssBapXTable.setStatus("current")
_Ieee8021FqtssBapXEntry_Object = MibTableRow
ieee8021FqtssBapXEntry = _Ieee8021FqtssBapXEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 16, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ieee8021FqtssBapXEntry.setStatus("current")
_Ieee8021FqtssBAPClassMeasurementInterval_Type = Unsigned32
_Ieee8021FqtssBAPClassMeasurementInterval_Object = MibTableColumn
ieee8021FqtssBAPClassMeasurementInterval = _Ieee8021FqtssBAPClassMeasurementInterval_Object(
    (1, 3, 111, 2, 802, 1, 1, 16, 1, 3, 1, 1, 1),
    _Ieee8021FqtssBAPClassMeasurementInterval_Type()
)
ieee8021FqtssBAPClassMeasurementInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021FqtssBAPClassMeasurementInterval.setStatus("current")


class _Ieee8021FqtssBAPLockClassBandwidth_Type(TruthValue):
    """Custom type ieee8021FqtssBAPLockClassBandwidth based on TruthValue"""


_Ieee8021FqtssBAPLockClassBandwidth_Object = MibTableColumn
ieee8021FqtssBAPLockClassBandwidth = _Ieee8021FqtssBAPLockClassBandwidth_Object(
    (1, 3, 111, 2, 802, 1, 1, 16, 1, 3, 1, 1, 2),
    _Ieee8021FqtssBAPLockClassBandwidth_Type()
)
ieee8021FqtssBAPLockClassBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021FqtssBAPLockClassBandwidth.setStatus("current")
_Ieee8021FqtssConformance_ObjectIdentity = ObjectIdentity
ieee8021FqtssConformance = _Ieee8021FqtssConformance_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 16, 2)
)
_Ieee8021FqtssCompliances_ObjectIdentity = ObjectIdentity
ieee8021FqtssCompliances = _Ieee8021FqtssCompliances_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 16, 2, 1)
)
_Ieee8021FqtssGroups_ObjectIdentity = ObjectIdentity
ieee8021FqtssGroups = _Ieee8021FqtssGroups_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 16, 2, 2)
)
ieee8021FqtssBapEntry.registerAugmentions(
    ("IEEE8021-FQTSS-MIB",
     "ieee8021FqtssBapXEntry")
)
ieee8021FqtssBapXEntry.setIndexNames(*ieee8021FqtssBapEntry.getIndexNames())

# Managed Objects groups

ieee8021FqtssBapGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 16, 2, 2, 1)
)
ieee8021FqtssBapGroup.setObjects(
      *(("IEEE8021-FQTSS-MIB", "ieee8021FqtssDeltaBandwidth"),
        ("IEEE8021-FQTSS-MIB", "ieee8021FqtssOperIdleSlopeMs"),
        ("IEEE8021-FQTSS-MIB", "ieee8021FqtssOperIdleSlopeLs"),
        ("IEEE8021-FQTSS-MIB", "ieee8021FqtssAdminIdleSlopeMs"),
        ("IEEE8021-FQTSS-MIB", "ieee8021FqtssAdminIdleSlopeLs"),
        ("IEEE8021-FQTSS-MIB", "ieee8021FqtssBapRowStatus"))
)
if mibBuilder.loadTexts:
    ieee8021FqtssBapGroup.setStatus("current")

ieee8021FqtssTxSelectionAlgorithmGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 16, 2, 2, 2)
)
ieee8021FqtssTxSelectionAlgorithmGroup.setObjects(
    ("IEEE8021-FQTSS-MIB", "ieee8021FqtssTxSelectionAlgorithmID")
)
if mibBuilder.loadTexts:
    ieee8021FqtssTxSelectionAlgorithmGroup.setStatus("current")

ieee8021FqtssBoundaryPortGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 16, 2, 2, 3)
)
ieee8021FqtssBoundaryPortGroup.setObjects(
      *(("IEEE8021-FQTSS-MIB", "ieee8021FqtssPriorityRegenOverride"),
        ("IEEE8021-FQTSS-MIB", "ieee8021FqtssSrpBoundaryPort"))
)
if mibBuilder.loadTexts:
    ieee8021FqtssBoundaryPortGroup.setStatus("current")

ieee8021FqtssBapMeasurementGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 16, 2, 2, 4)
)
ieee8021FqtssBapMeasurementGroup.setObjects(
      *(("IEEE8021-FQTSS-MIB", "ieee8021FqtssBAPClassMeasurementInterval"),
        ("IEEE8021-FQTSS-MIB", "ieee8021FqtssBAPLockClassBandwidth"))
)
if mibBuilder.loadTexts:
    ieee8021FqtssBapMeasurementGroup.setStatus("current")

ieee8021FqtssSRClassPriorityGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 16, 2, 2, 5)
)
ieee8021FqtssSRClassPriorityGroup.setObjects(
      *(("IEEE8021-FQTSS-MIB", "ieee8021FqtssSRClassToPrioritySrClassID"),
        ("IEEE8021-FQTSS-MIB", "ieee8021FqtssSRClassToPriorityRowStatus"))
)
if mibBuilder.loadTexts:
    ieee8021FqtssSRClassPriorityGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ieee8021FqtssCompliance = ModuleCompliance(
    (1, 3, 111, 2, 802, 1, 1, 16, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ieee8021FqtssCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IEEE8021-FQTSS-MIB",
    **{"IEEE8021FqtssTrafficClassValue": IEEE8021FqtssTrafficClassValue,
       "IEEE8021FqtssDeltaBandwidthValue": IEEE8021FqtssDeltaBandwidthValue,
       "IEEE8021FqtssTxSelectionAlgorithmIDValue": IEEE8021FqtssTxSelectionAlgorithmIDValue,
       "ieee8021FqtssMib": ieee8021FqtssMib,
       "ieee8021FqtssNotifications": ieee8021FqtssNotifications,
       "ieee8021FqtssObjects": ieee8021FqtssObjects,
       "ieee8021FqtssBap": ieee8021FqtssBap,
       "ieee8021FqtssBapTable": ieee8021FqtssBapTable,
       "ieee8021FqtssBapEntry": ieee8021FqtssBapEntry,
       "ieee8021FqtssBAPTrafficClass": ieee8021FqtssBAPTrafficClass,
       "ieee8021FqtssDeltaBandwidth": ieee8021FqtssDeltaBandwidth,
       "ieee8021FqtssOperIdleSlopeMs": ieee8021FqtssOperIdleSlopeMs,
       "ieee8021FqtssOperIdleSlopeLs": ieee8021FqtssOperIdleSlopeLs,
       "ieee8021FqtssAdminIdleSlopeMs": ieee8021FqtssAdminIdleSlopeMs,
       "ieee8021FqtssAdminIdleSlopeLs": ieee8021FqtssAdminIdleSlopeLs,
       "ieee8021FqtssBapRowStatus": ieee8021FqtssBapRowStatus,
       "ieee8021FqtssMappings": ieee8021FqtssMappings,
       "ieee8021FqtssTxSelectionAlgorithmTable": ieee8021FqtssTxSelectionAlgorithmTable,
       "ieee8021FqtssTxSelectionAlgorithmEntry": ieee8021FqtssTxSelectionAlgorithmEntry,
       "ieee8021FqtssTrafficClass": ieee8021FqtssTrafficClass,
       "ieee8021FqtssTxSelectionAlgorithmID": ieee8021FqtssTxSelectionAlgorithmID,
       "ieee8021FqtssSrpRegenOverrideTable": ieee8021FqtssSrpRegenOverrideTable,
       "ieee8021FqtssSrpRegenOverrideEntry": ieee8021FqtssSrpRegenOverrideEntry,
       "ieee8021FqtssSrClassPriority": ieee8021FqtssSrClassPriority,
       "ieee8021FqtssPriorityRegenOverride": ieee8021FqtssPriorityRegenOverride,
       "ieee8021FqtssSrpBoundaryPort": ieee8021FqtssSrpBoundaryPort,
       "ieee8021FqtssSRClassToPriorityTable": ieee8021FqtssSRClassToPriorityTable,
       "ieee8021FqtssSRClassToPriorityEntry": ieee8021FqtssSRClassToPriorityEntry,
       "ieee8021FqtssSRClassToPrioritySrClassID": ieee8021FqtssSRClassToPrioritySrClassID,
       "ieee8021FqtssSRClassToPriorityRowStatus": ieee8021FqtssSRClassToPriorityRowStatus,
       "ieee8021FqtssBapX": ieee8021FqtssBapX,
       "ieee8021FqtssBapXTable": ieee8021FqtssBapXTable,
       "ieee8021FqtssBapXEntry": ieee8021FqtssBapXEntry,
       "ieee8021FqtssBAPClassMeasurementInterval": ieee8021FqtssBAPClassMeasurementInterval,
       "ieee8021FqtssBAPLockClassBandwidth": ieee8021FqtssBAPLockClassBandwidth,
       "ieee8021FqtssConformance": ieee8021FqtssConformance,
       "ieee8021FqtssCompliances": ieee8021FqtssCompliances,
       "ieee8021FqtssCompliance": ieee8021FqtssCompliance,
       "ieee8021FqtssGroups": ieee8021FqtssGroups,
       "ieee8021FqtssBapGroup": ieee8021FqtssBapGroup,
       "ieee8021FqtssTxSelectionAlgorithmGroup": ieee8021FqtssTxSelectionAlgorithmGroup,
       "ieee8021FqtssBoundaryPortGroup": ieee8021FqtssBoundaryPortGroup,
       "ieee8021FqtssBapMeasurementGroup": ieee8021FqtssBapMeasurementGroup,
       "ieee8021FqtssSRClassPriorityGroup": ieee8021FqtssSRClassPriorityGroup}
)
