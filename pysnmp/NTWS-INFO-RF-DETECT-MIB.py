# SNMP MIB module (NTWS-INFO-RF-DETECT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NTWS-INFO-RF-DETECT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:29:56 2024
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

(NtwsChannelNum,
 NtwsRssi) = mibBuilder.importSymbols(
    "NTWS-AP-TC",
    "NtwsChannelNum",
    "NtwsRssi")

(NtwsRFDetectClassification,
 NtwsRFDetectClassificationReason,
 NtwsRFDetectNetworkingMode) = mibBuilder.importSymbols(
    "NTWS-RF-DETECT-TC",
    "NtwsRFDetectClassification",
    "NtwsRFDetectClassificationReason",
    "NtwsRFDetectNetworkingMode")

(ntwsMibs,) = mibBuilder.importSymbols(
    "NTWS-ROOT-MIB",
    "ntwsMibs")

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


# MODULE-IDENTITY

ntwsInfoRFDetectMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 9)
)
ntwsInfoRFDetectMib.setRevisions(
        ("2007-09-25 00:12",
         "2007-06-27 00:11",
         "2007-04-18 00:10",
         "2006-10-11 00:03")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NtwsInfoRFDetectObjects_ObjectIdentity = ObjectIdentity
ntwsInfoRFDetectObjects = _NtwsInfoRFDetectObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 9, 1)
)
_NtwsInfoRFDetectDataObjects_ObjectIdentity = ObjectIdentity
ntwsInfoRFDetectDataObjects = _NtwsInfoRFDetectDataObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 9, 1, 1)
)
_NtwsInfoRFDetectXmtrTable_Object = MibTable
ntwsInfoRFDetectXmtrTable = _NtwsInfoRFDetectXmtrTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 9, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ntwsInfoRFDetectXmtrTable.setStatus("current")
_NtwsInfoRFDetectXmtrEntry_Object = MibTableRow
ntwsInfoRFDetectXmtrEntry = _NtwsInfoRFDetectXmtrEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 9, 1, 1, 1, 1)
)
ntwsInfoRFDetectXmtrEntry.setIndexNames(
    (0, "NTWS-INFO-RF-DETECT-MIB", "ntwsInfoRFDetectXmtrTransmitterMacAddress"),
    (0, "NTWS-INFO-RF-DETECT-MIB", "ntwsInfoRFDetectXmtrListenerMacAddress"),
    (0, "NTWS-INFO-RF-DETECT-MIB", "ntwsInfoRFDetectXmtrChannelNum"),
)
if mibBuilder.loadTexts:
    ntwsInfoRFDetectXmtrEntry.setStatus("current")
_NtwsInfoRFDetectXmtrTransmitterMacAddress_Type = MacAddress
_NtwsInfoRFDetectXmtrTransmitterMacAddress_Object = MibTableColumn
ntwsInfoRFDetectXmtrTransmitterMacAddress = _NtwsInfoRFDetectXmtrTransmitterMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 9, 1, 1, 1, 1, 1),
    _NtwsInfoRFDetectXmtrTransmitterMacAddress_Type()
)
ntwsInfoRFDetectXmtrTransmitterMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntwsInfoRFDetectXmtrTransmitterMacAddress.setStatus("current")
_NtwsInfoRFDetectXmtrListenerMacAddress_Type = MacAddress
_NtwsInfoRFDetectXmtrListenerMacAddress_Object = MibTableColumn
ntwsInfoRFDetectXmtrListenerMacAddress = _NtwsInfoRFDetectXmtrListenerMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 9, 1, 1, 1, 1, 2),
    _NtwsInfoRFDetectXmtrListenerMacAddress_Type()
)
ntwsInfoRFDetectXmtrListenerMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntwsInfoRFDetectXmtrListenerMacAddress.setStatus("current")
_NtwsInfoRFDetectXmtrChannelNum_Type = NtwsChannelNum
_NtwsInfoRFDetectXmtrChannelNum_Object = MibTableColumn
ntwsInfoRFDetectXmtrChannelNum = _NtwsInfoRFDetectXmtrChannelNum_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 9, 1, 1, 1, 1, 3),
    _NtwsInfoRFDetectXmtrChannelNum_Type()
)
ntwsInfoRFDetectXmtrChannelNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntwsInfoRFDetectXmtrChannelNum.setStatus("current")
_NtwsInfoRFDetectXmtrRssi_Type = NtwsRssi
_NtwsInfoRFDetectXmtrRssi_Object = MibTableColumn
ntwsInfoRFDetectXmtrRssi = _NtwsInfoRFDetectXmtrRssi_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 9, 1, 1, 1, 1, 4),
    _NtwsInfoRFDetectXmtrRssi_Type()
)
ntwsInfoRFDetectXmtrRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsInfoRFDetectXmtrRssi.setStatus("current")


class _NtwsInfoRFDetectXmtrSsid_Type(DisplayString):
    """Custom type ntwsInfoRFDetectXmtrSsid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NtwsInfoRFDetectXmtrSsid_Type.__name__ = "DisplayString"
_NtwsInfoRFDetectXmtrSsid_Object = MibTableColumn
ntwsInfoRFDetectXmtrSsid = _NtwsInfoRFDetectXmtrSsid_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 9, 1, 1, 1, 1, 5),
    _NtwsInfoRFDetectXmtrSsid_Type()
)
ntwsInfoRFDetectXmtrSsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsInfoRFDetectXmtrSsid.setStatus("current")
_NtwsInfoRFDetectXmtrNetworkingMode_Type = NtwsRFDetectNetworkingMode
_NtwsInfoRFDetectXmtrNetworkingMode_Object = MibTableColumn
ntwsInfoRFDetectXmtrNetworkingMode = _NtwsInfoRFDetectXmtrNetworkingMode_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 9, 1, 1, 1, 1, 6),
    _NtwsInfoRFDetectXmtrNetworkingMode_Type()
)
ntwsInfoRFDetectXmtrNetworkingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsInfoRFDetectXmtrNetworkingMode.setStatus("current")
_NtwsInfoRFDetectXmtrClassification_Type = NtwsRFDetectClassification
_NtwsInfoRFDetectXmtrClassification_Object = MibTableColumn
ntwsInfoRFDetectXmtrClassification = _NtwsInfoRFDetectXmtrClassification_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 9, 1, 1, 1, 1, 7),
    _NtwsInfoRFDetectXmtrClassification_Type()
)
ntwsInfoRFDetectXmtrClassification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsInfoRFDetectXmtrClassification.setStatus("current")
_NtwsInfoRFDetectXmtrClassificationReason_Type = NtwsRFDetectClassificationReason
_NtwsInfoRFDetectXmtrClassificationReason_Object = MibTableColumn
ntwsInfoRFDetectXmtrClassificationReason = _NtwsInfoRFDetectXmtrClassificationReason_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 9, 1, 1, 1, 1, 8),
    _NtwsInfoRFDetectXmtrClassificationReason_Type()
)
ntwsInfoRFDetectXmtrClassificationReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsInfoRFDetectXmtrClassificationReason.setStatus("current")
_NtwsInfoRFDetectCurrentXmtrTableSize_Type = Gauge32
_NtwsInfoRFDetectCurrentXmtrTableSize_Object = MibScalar
ntwsInfoRFDetectCurrentXmtrTableSize = _NtwsInfoRFDetectCurrentXmtrTableSize_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 9, 1, 1, 2),
    _NtwsInfoRFDetectCurrentXmtrTableSize_Type()
)
ntwsInfoRFDetectCurrentXmtrTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsInfoRFDetectCurrentXmtrTableSize.setStatus("current")
_NtwsInfoRFDetectConformance_ObjectIdentity = ObjectIdentity
ntwsInfoRFDetectConformance = _NtwsInfoRFDetectConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 9, 1, 2)
)
_NtwsInfoRFDetectCompliances_ObjectIdentity = ObjectIdentity
ntwsInfoRFDetectCompliances = _NtwsInfoRFDetectCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 9, 1, 2, 1)
)
_NtwsInfoRFDetectGroups_ObjectIdentity = ObjectIdentity
ntwsInfoRFDetectGroups = _NtwsInfoRFDetectGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 9, 1, 2, 2)
)

# Managed Objects groups

ntwsInfoRFDetectXmtrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 9, 1, 2, 2, 1)
)
ntwsInfoRFDetectXmtrGroup.setObjects(
      *(("NTWS-INFO-RF-DETECT-MIB", "ntwsInfoRFDetectXmtrRssi"),
        ("NTWS-INFO-RF-DETECT-MIB", "ntwsInfoRFDetectXmtrSsid"))
)
if mibBuilder.loadTexts:
    ntwsInfoRFDetectXmtrGroup.setStatus("current")

ntwsInfoRFDetectXmtrClassificationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 9, 1, 2, 2, 2)
)
ntwsInfoRFDetectXmtrClassificationGroup.setObjects(
      *(("NTWS-INFO-RF-DETECT-MIB", "ntwsInfoRFDetectXmtrNetworkingMode"),
        ("NTWS-INFO-RF-DETECT-MIB", "ntwsInfoRFDetectXmtrClassification"),
        ("NTWS-INFO-RF-DETECT-MIB", "ntwsInfoRFDetectXmtrClassificationReason"))
)
if mibBuilder.loadTexts:
    ntwsInfoRFDetectXmtrClassificationGroup.setStatus("current")

ntwsInfoRFDetectCurrentXmtrTableSizeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 9, 1, 2, 2, 3)
)
ntwsInfoRFDetectCurrentXmtrTableSizeGroup.setObjects(
    ("NTWS-INFO-RF-DETECT-MIB", "ntwsInfoRFDetectCurrentXmtrTableSize")
)
if mibBuilder.loadTexts:
    ntwsInfoRFDetectCurrentXmtrTableSizeGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ntwsInfoRFDetectCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 9, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ntwsInfoRFDetectCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NTWS-INFO-RF-DETECT-MIB",
    **{"ntwsInfoRFDetectMib": ntwsInfoRFDetectMib,
       "ntwsInfoRFDetectObjects": ntwsInfoRFDetectObjects,
       "ntwsInfoRFDetectDataObjects": ntwsInfoRFDetectDataObjects,
       "ntwsInfoRFDetectXmtrTable": ntwsInfoRFDetectXmtrTable,
       "ntwsInfoRFDetectXmtrEntry": ntwsInfoRFDetectXmtrEntry,
       "ntwsInfoRFDetectXmtrTransmitterMacAddress": ntwsInfoRFDetectXmtrTransmitterMacAddress,
       "ntwsInfoRFDetectXmtrListenerMacAddress": ntwsInfoRFDetectXmtrListenerMacAddress,
       "ntwsInfoRFDetectXmtrChannelNum": ntwsInfoRFDetectXmtrChannelNum,
       "ntwsInfoRFDetectXmtrRssi": ntwsInfoRFDetectXmtrRssi,
       "ntwsInfoRFDetectXmtrSsid": ntwsInfoRFDetectXmtrSsid,
       "ntwsInfoRFDetectXmtrNetworkingMode": ntwsInfoRFDetectXmtrNetworkingMode,
       "ntwsInfoRFDetectXmtrClassification": ntwsInfoRFDetectXmtrClassification,
       "ntwsInfoRFDetectXmtrClassificationReason": ntwsInfoRFDetectXmtrClassificationReason,
       "ntwsInfoRFDetectCurrentXmtrTableSize": ntwsInfoRFDetectCurrentXmtrTableSize,
       "ntwsInfoRFDetectConformance": ntwsInfoRFDetectConformance,
       "ntwsInfoRFDetectCompliances": ntwsInfoRFDetectCompliances,
       "ntwsInfoRFDetectCompliance": ntwsInfoRFDetectCompliance,
       "ntwsInfoRFDetectGroups": ntwsInfoRFDetectGroups,
       "ntwsInfoRFDetectXmtrGroup": ntwsInfoRFDetectXmtrGroup,
       "ntwsInfoRFDetectXmtrClassificationGroup": ntwsInfoRFDetectXmtrClassificationGroup,
       "ntwsInfoRFDetectCurrentXmtrTableSizeGroup": ntwsInfoRFDetectCurrentXmtrTableSizeGroup}
)
