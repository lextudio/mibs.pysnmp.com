# SNMP MIB module (TRAPEZE-NETWORKS-INFO-RF-DETECT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TRAPEZE-NETWORKS-INFO-RF-DETECT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:07:32 2024
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
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")

(TrpzApNum,
 TrpzApRadioIndex,
 TrpzChannelNum,
 TrpzRadioRateEx,
 TrpzRssi) = mibBuilder.importSymbols(
    "TRAPEZE-NETWORKS-AP-TC",
    "TrpzApNum",
    "TrpzApRadioIndex",
    "TrpzChannelNum",
    "TrpzRadioRateEx",
    "TrpzRssi")

(TrpzRFDetectClassification,
 TrpzRFDetectClassificationReason,
 TrpzRFDetectDot11ModulationStandard,
 TrpzRFDetectNetworkingMode) = mibBuilder.importSymbols(
    "TRAPEZE-NETWORKS-RF-DETECT-TC",
    "TrpzRFDetectClassification",
    "TrpzRFDetectClassificationReason",
    "TrpzRFDetectDot11ModulationStandard",
    "TrpzRFDetectNetworkingMode")

(trpzMibs,) = mibBuilder.importSymbols(
    "TRAPEZE-NETWORKS-ROOT-MIB",
    "trpzMibs")


# MODULE-IDENTITY

trpzInfoRFDetectMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 4, 9)
)
trpzInfoRFDetectMib.setRevisions(
        ("2011-07-27 00:22",
         "2009-08-18 00:21",
         "2007-06-27 00:11",
         "2007-04-18 00:10",
         "2006-10-11 00:03")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TrpzInfoRFDetectObjects_ObjectIdentity = ObjectIdentity
trpzInfoRFDetectObjects = _TrpzInfoRFDetectObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 4, 9, 1)
)
_TrpzInfoRFDetectDataObjects_ObjectIdentity = ObjectIdentity
trpzInfoRFDetectDataObjects = _TrpzInfoRFDetectDataObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 4, 9, 1, 1)
)
_TrpzInfoRFDetectXmtrTable_Object = MibTable
trpzInfoRFDetectXmtrTable = _TrpzInfoRFDetectXmtrTable_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 9, 1, 1, 1)
)
if mibBuilder.loadTexts:
    trpzInfoRFDetectXmtrTable.setStatus("current")
_TrpzInfoRFDetectXmtrEntry_Object = MibTableRow
trpzInfoRFDetectXmtrEntry = _TrpzInfoRFDetectXmtrEntry_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 9, 1, 1, 1, 1)
)
trpzInfoRFDetectXmtrEntry.setIndexNames(
    (0, "TRAPEZE-NETWORKS-INFO-RF-DETECT-MIB", "trpzInfoRFDetectXmtrTransmitterMacAddress"),
    (0, "TRAPEZE-NETWORKS-INFO-RF-DETECT-MIB", "trpzInfoRFDetectXmtrListenerMacAddress"),
    (0, "TRAPEZE-NETWORKS-INFO-RF-DETECT-MIB", "trpzInfoRFDetectXmtrChannelNum"),
)
if mibBuilder.loadTexts:
    trpzInfoRFDetectXmtrEntry.setStatus("current")
_TrpzInfoRFDetectXmtrTransmitterMacAddress_Type = MacAddress
_TrpzInfoRFDetectXmtrTransmitterMacAddress_Object = MibTableColumn
trpzInfoRFDetectXmtrTransmitterMacAddress = _TrpzInfoRFDetectXmtrTransmitterMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 9, 1, 1, 1, 1, 1),
    _TrpzInfoRFDetectXmtrTransmitterMacAddress_Type()
)
trpzInfoRFDetectXmtrTransmitterMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trpzInfoRFDetectXmtrTransmitterMacAddress.setStatus("current")
_TrpzInfoRFDetectXmtrListenerMacAddress_Type = MacAddress
_TrpzInfoRFDetectXmtrListenerMacAddress_Object = MibTableColumn
trpzInfoRFDetectXmtrListenerMacAddress = _TrpzInfoRFDetectXmtrListenerMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 9, 1, 1, 1, 1, 2),
    _TrpzInfoRFDetectXmtrListenerMacAddress_Type()
)
trpzInfoRFDetectXmtrListenerMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trpzInfoRFDetectXmtrListenerMacAddress.setStatus("current")
_TrpzInfoRFDetectXmtrChannelNum_Type = TrpzChannelNum
_TrpzInfoRFDetectXmtrChannelNum_Object = MibTableColumn
trpzInfoRFDetectXmtrChannelNum = _TrpzInfoRFDetectXmtrChannelNum_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 9, 1, 1, 1, 1, 3),
    _TrpzInfoRFDetectXmtrChannelNum_Type()
)
trpzInfoRFDetectXmtrChannelNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trpzInfoRFDetectXmtrChannelNum.setStatus("current")
_TrpzInfoRFDetectXmtrRssi_Type = TrpzRssi
_TrpzInfoRFDetectXmtrRssi_Object = MibTableColumn
trpzInfoRFDetectXmtrRssi = _TrpzInfoRFDetectXmtrRssi_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 9, 1, 1, 1, 1, 4),
    _TrpzInfoRFDetectXmtrRssi_Type()
)
trpzInfoRFDetectXmtrRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzInfoRFDetectXmtrRssi.setStatus("current")


class _TrpzInfoRFDetectXmtrSsid_Type(DisplayString):
    """Custom type trpzInfoRFDetectXmtrSsid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TrpzInfoRFDetectXmtrSsid_Type.__name__ = "DisplayString"
_TrpzInfoRFDetectXmtrSsid_Object = MibTableColumn
trpzInfoRFDetectXmtrSsid = _TrpzInfoRFDetectXmtrSsid_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 9, 1, 1, 1, 1, 5),
    _TrpzInfoRFDetectXmtrSsid_Type()
)
trpzInfoRFDetectXmtrSsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzInfoRFDetectXmtrSsid.setStatus("current")
_TrpzInfoRFDetectXmtrNetworkingMode_Type = TrpzRFDetectNetworkingMode
_TrpzInfoRFDetectXmtrNetworkingMode_Object = MibTableColumn
trpzInfoRFDetectXmtrNetworkingMode = _TrpzInfoRFDetectXmtrNetworkingMode_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 9, 1, 1, 1, 1, 6),
    _TrpzInfoRFDetectXmtrNetworkingMode_Type()
)
trpzInfoRFDetectXmtrNetworkingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzInfoRFDetectXmtrNetworkingMode.setStatus("current")
_TrpzInfoRFDetectXmtrClassification_Type = TrpzRFDetectClassification
_TrpzInfoRFDetectXmtrClassification_Object = MibTableColumn
trpzInfoRFDetectXmtrClassification = _TrpzInfoRFDetectXmtrClassification_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 9, 1, 1, 1, 1, 7),
    _TrpzInfoRFDetectXmtrClassification_Type()
)
trpzInfoRFDetectXmtrClassification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzInfoRFDetectXmtrClassification.setStatus("current")
_TrpzInfoRFDetectXmtrClassificationReason_Type = TrpzRFDetectClassificationReason
_TrpzInfoRFDetectXmtrClassificationReason_Object = MibTableColumn
trpzInfoRFDetectXmtrClassificationReason = _TrpzInfoRFDetectXmtrClassificationReason_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 9, 1, 1, 1, 1, 8),
    _TrpzInfoRFDetectXmtrClassificationReason_Type()
)
trpzInfoRFDetectXmtrClassificationReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzInfoRFDetectXmtrClassificationReason.setStatus("current")
_TrpzInfoRFDetectCurrentXmtrTableSize_Type = Gauge32
_TrpzInfoRFDetectCurrentXmtrTableSize_Object = MibScalar
trpzInfoRFDetectCurrentXmtrTableSize = _TrpzInfoRFDetectCurrentXmtrTableSize_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 9, 1, 1, 2),
    _TrpzInfoRFDetectCurrentXmtrTableSize_Type()
)
trpzInfoRFDetectCurrentXmtrTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzInfoRFDetectCurrentXmtrTableSize.setStatus("current")
_TrpzInfoRFDetectClientTable_Object = MibTable
trpzInfoRFDetectClientTable = _TrpzInfoRFDetectClientTable_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 9, 1, 1, 3)
)
if mibBuilder.loadTexts:
    trpzInfoRFDetectClientTable.setStatus("current")
_TrpzInfoRFDetectClientEntry_Object = MibTableRow
trpzInfoRFDetectClientEntry = _TrpzInfoRFDetectClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 9, 1, 1, 3, 1)
)
trpzInfoRFDetectClientEntry.setIndexNames(
    (0, "TRAPEZE-NETWORKS-INFO-RF-DETECT-MIB", "trpzInfoRFDetectClientMacAddress"),
    (0, "TRAPEZE-NETWORKS-INFO-RF-DETECT-MIB", "trpzInfoRFDetectClientListenerMacAddress"),
)
if mibBuilder.loadTexts:
    trpzInfoRFDetectClientEntry.setStatus("current")
_TrpzInfoRFDetectClientMacAddress_Type = MacAddress
_TrpzInfoRFDetectClientMacAddress_Object = MibTableColumn
trpzInfoRFDetectClientMacAddress = _TrpzInfoRFDetectClientMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 9, 1, 1, 3, 1, 1),
    _TrpzInfoRFDetectClientMacAddress_Type()
)
trpzInfoRFDetectClientMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trpzInfoRFDetectClientMacAddress.setStatus("current")
_TrpzInfoRFDetectClientListenerMacAddress_Type = MacAddress
_TrpzInfoRFDetectClientListenerMacAddress_Object = MibTableColumn
trpzInfoRFDetectClientListenerMacAddress = _TrpzInfoRFDetectClientListenerMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 9, 1, 1, 3, 1, 2),
    _TrpzInfoRFDetectClientListenerMacAddress_Type()
)
trpzInfoRFDetectClientListenerMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trpzInfoRFDetectClientListenerMacAddress.setStatus("current")
_TrpzInfoRFDetectClientConnectedBssid_Type = MacAddress
_TrpzInfoRFDetectClientConnectedBssid_Object = MibTableColumn
trpzInfoRFDetectClientConnectedBssid = _TrpzInfoRFDetectClientConnectedBssid_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 9, 1, 1, 3, 1, 3),
    _TrpzInfoRFDetectClientConnectedBssid_Type()
)
trpzInfoRFDetectClientConnectedBssid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzInfoRFDetectClientConnectedBssid.setStatus("current")
_TrpzInfoRFDetectClientApNum_Type = TrpzApNum
_TrpzInfoRFDetectClientApNum_Object = MibTableColumn
trpzInfoRFDetectClientApNum = _TrpzInfoRFDetectClientApNum_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 9, 1, 1, 3, 1, 4),
    _TrpzInfoRFDetectClientApNum_Type()
)
trpzInfoRFDetectClientApNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzInfoRFDetectClientApNum.setStatus("current")
_TrpzInfoRFDetectClientApRadioIndex_Type = TrpzApRadioIndex
_TrpzInfoRFDetectClientApRadioIndex_Object = MibTableColumn
trpzInfoRFDetectClientApRadioIndex = _TrpzInfoRFDetectClientApRadioIndex_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 9, 1, 1, 3, 1, 5),
    _TrpzInfoRFDetectClientApRadioIndex_Type()
)
trpzInfoRFDetectClientApRadioIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzInfoRFDetectClientApRadioIndex.setStatus("current")
_TrpzInfoRFDetectClientModulation_Type = TrpzRFDetectDot11ModulationStandard
_TrpzInfoRFDetectClientModulation_Object = MibTableColumn
trpzInfoRFDetectClientModulation = _TrpzInfoRFDetectClientModulation_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 9, 1, 1, 3, 1, 6),
    _TrpzInfoRFDetectClientModulation_Type()
)
trpzInfoRFDetectClientModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzInfoRFDetectClientModulation.setStatus("current")
_TrpzInfoRFDetectClientChannelNum_Type = TrpzChannelNum
_TrpzInfoRFDetectClientChannelNum_Object = MibTableColumn
trpzInfoRFDetectClientChannelNum = _TrpzInfoRFDetectClientChannelNum_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 9, 1, 1, 3, 1, 7),
    _TrpzInfoRFDetectClientChannelNum_Type()
)
trpzInfoRFDetectClientChannelNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzInfoRFDetectClientChannelNum.setStatus("current")
_TrpzInfoRFDetectClientRate_Type = TrpzRadioRateEx
_TrpzInfoRFDetectClientRate_Object = MibTableColumn
trpzInfoRFDetectClientRate = _TrpzInfoRFDetectClientRate_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 9, 1, 1, 3, 1, 8),
    _TrpzInfoRFDetectClientRate_Type()
)
trpzInfoRFDetectClientRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzInfoRFDetectClientRate.setStatus("current")
_TrpzInfoRFDetectClientRssi_Type = TrpzRssi
_TrpzInfoRFDetectClientRssi_Object = MibTableColumn
trpzInfoRFDetectClientRssi = _TrpzInfoRFDetectClientRssi_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 9, 1, 1, 3, 1, 9),
    _TrpzInfoRFDetectClientRssi_Type()
)
trpzInfoRFDetectClientRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzInfoRFDetectClientRssi.setStatus("current")
_TrpzInfoRFDetectClientClassification_Type = TrpzRFDetectClassification
_TrpzInfoRFDetectClientClassification_Object = MibTableColumn
trpzInfoRFDetectClientClassification = _TrpzInfoRFDetectClientClassification_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 9, 1, 1, 3, 1, 10),
    _TrpzInfoRFDetectClientClassification_Type()
)
trpzInfoRFDetectClientClassification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzInfoRFDetectClientClassification.setStatus("current")
_TrpzInfoRFDetectConformance_ObjectIdentity = ObjectIdentity
trpzInfoRFDetectConformance = _TrpzInfoRFDetectConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 4, 9, 1, 2)
)
_TrpzInfoRFDetectCompliances_ObjectIdentity = ObjectIdentity
trpzInfoRFDetectCompliances = _TrpzInfoRFDetectCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 4, 9, 1, 2, 1)
)
_TrpzInfoRFDetectGroups_ObjectIdentity = ObjectIdentity
trpzInfoRFDetectGroups = _TrpzInfoRFDetectGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 4, 9, 1, 2, 2)
)

# Managed Objects groups

trpzInfoRFDetectXmtrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14525, 4, 9, 1, 2, 2, 1)
)
trpzInfoRFDetectXmtrGroup.setObjects(
      *(("TRAPEZE-NETWORKS-INFO-RF-DETECT-MIB", "trpzInfoRFDetectXmtrRssi"),
        ("TRAPEZE-NETWORKS-INFO-RF-DETECT-MIB", "trpzInfoRFDetectXmtrSsid"))
)
if mibBuilder.loadTexts:
    trpzInfoRFDetectXmtrGroup.setStatus("current")

trpzInfoRFDetectXmtrClassificationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14525, 4, 9, 1, 2, 2, 2)
)
trpzInfoRFDetectXmtrClassificationGroup.setObjects(
      *(("TRAPEZE-NETWORKS-INFO-RF-DETECT-MIB", "trpzInfoRFDetectXmtrNetworkingMode"),
        ("TRAPEZE-NETWORKS-INFO-RF-DETECT-MIB", "trpzInfoRFDetectXmtrClassification"),
        ("TRAPEZE-NETWORKS-INFO-RF-DETECT-MIB", "trpzInfoRFDetectXmtrClassificationReason"))
)
if mibBuilder.loadTexts:
    trpzInfoRFDetectXmtrClassificationGroup.setStatus("current")

trpzInfoRFDetectCurrentXmtrTableSizeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14525, 4, 9, 1, 2, 2, 3)
)
trpzInfoRFDetectCurrentXmtrTableSizeGroup.setObjects(
    ("TRAPEZE-NETWORKS-INFO-RF-DETECT-MIB", "trpzInfoRFDetectCurrentXmtrTableSize")
)
if mibBuilder.loadTexts:
    trpzInfoRFDetectCurrentXmtrTableSizeGroup.setStatus("current")

trpzInfoRFDetectClientGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14525, 4, 9, 1, 2, 2, 4)
)
trpzInfoRFDetectClientGroup.setObjects(
      *(("TRAPEZE-NETWORKS-INFO-RF-DETECT-MIB", "trpzInfoRFDetectClientConnectedBssid"),
        ("TRAPEZE-NETWORKS-INFO-RF-DETECT-MIB", "trpzInfoRFDetectClientApNum"),
        ("TRAPEZE-NETWORKS-INFO-RF-DETECT-MIB", "trpzInfoRFDetectClientApRadioIndex"),
        ("TRAPEZE-NETWORKS-INFO-RF-DETECT-MIB", "trpzInfoRFDetectClientModulation"),
        ("TRAPEZE-NETWORKS-INFO-RF-DETECT-MIB", "trpzInfoRFDetectClientChannelNum"),
        ("TRAPEZE-NETWORKS-INFO-RF-DETECT-MIB", "trpzInfoRFDetectClientRate"),
        ("TRAPEZE-NETWORKS-INFO-RF-DETECT-MIB", "trpzInfoRFDetectClientRssi"),
        ("TRAPEZE-NETWORKS-INFO-RF-DETECT-MIB", "trpzInfoRFDetectClientClassification"))
)
if mibBuilder.loadTexts:
    trpzInfoRFDetectClientGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

trpzInfoRFDetectCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 14525, 4, 9, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    trpzInfoRFDetectCompliance.setStatus(
        "obsolete"
    )

trpzInfoRFDetectComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 14525, 4, 9, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    trpzInfoRFDetectComplianceRev2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TRAPEZE-NETWORKS-INFO-RF-DETECT-MIB",
    **{"trpzInfoRFDetectMib": trpzInfoRFDetectMib,
       "trpzInfoRFDetectObjects": trpzInfoRFDetectObjects,
       "trpzInfoRFDetectDataObjects": trpzInfoRFDetectDataObjects,
       "trpzInfoRFDetectXmtrTable": trpzInfoRFDetectXmtrTable,
       "trpzInfoRFDetectXmtrEntry": trpzInfoRFDetectXmtrEntry,
       "trpzInfoRFDetectXmtrTransmitterMacAddress": trpzInfoRFDetectXmtrTransmitterMacAddress,
       "trpzInfoRFDetectXmtrListenerMacAddress": trpzInfoRFDetectXmtrListenerMacAddress,
       "trpzInfoRFDetectXmtrChannelNum": trpzInfoRFDetectXmtrChannelNum,
       "trpzInfoRFDetectXmtrRssi": trpzInfoRFDetectXmtrRssi,
       "trpzInfoRFDetectXmtrSsid": trpzInfoRFDetectXmtrSsid,
       "trpzInfoRFDetectXmtrNetworkingMode": trpzInfoRFDetectXmtrNetworkingMode,
       "trpzInfoRFDetectXmtrClassification": trpzInfoRFDetectXmtrClassification,
       "trpzInfoRFDetectXmtrClassificationReason": trpzInfoRFDetectXmtrClassificationReason,
       "trpzInfoRFDetectCurrentXmtrTableSize": trpzInfoRFDetectCurrentXmtrTableSize,
       "trpzInfoRFDetectClientTable": trpzInfoRFDetectClientTable,
       "trpzInfoRFDetectClientEntry": trpzInfoRFDetectClientEntry,
       "trpzInfoRFDetectClientMacAddress": trpzInfoRFDetectClientMacAddress,
       "trpzInfoRFDetectClientListenerMacAddress": trpzInfoRFDetectClientListenerMacAddress,
       "trpzInfoRFDetectClientConnectedBssid": trpzInfoRFDetectClientConnectedBssid,
       "trpzInfoRFDetectClientApNum": trpzInfoRFDetectClientApNum,
       "trpzInfoRFDetectClientApRadioIndex": trpzInfoRFDetectClientApRadioIndex,
       "trpzInfoRFDetectClientModulation": trpzInfoRFDetectClientModulation,
       "trpzInfoRFDetectClientChannelNum": trpzInfoRFDetectClientChannelNum,
       "trpzInfoRFDetectClientRate": trpzInfoRFDetectClientRate,
       "trpzInfoRFDetectClientRssi": trpzInfoRFDetectClientRssi,
       "trpzInfoRFDetectClientClassification": trpzInfoRFDetectClientClassification,
       "trpzInfoRFDetectConformance": trpzInfoRFDetectConformance,
       "trpzInfoRFDetectCompliances": trpzInfoRFDetectCompliances,
       "trpzInfoRFDetectCompliance": trpzInfoRFDetectCompliance,
       "trpzInfoRFDetectComplianceRev2": trpzInfoRFDetectComplianceRev2,
       "trpzInfoRFDetectGroups": trpzInfoRFDetectGroups,
       "trpzInfoRFDetectXmtrGroup": trpzInfoRFDetectXmtrGroup,
       "trpzInfoRFDetectXmtrClassificationGroup": trpzInfoRFDetectXmtrClassificationGroup,
       "trpzInfoRFDetectCurrentXmtrTableSizeGroup": trpzInfoRFDetectCurrentXmtrTableSizeGroup,
       "trpzInfoRFDetectClientGroup": trpzInfoRFDetectClientGroup}
)
