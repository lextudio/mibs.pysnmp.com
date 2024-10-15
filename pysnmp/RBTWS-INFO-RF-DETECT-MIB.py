# SNMP MIB module (RBTWS-INFO-RF-DETECT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RBTWS-INFO-RF-DETECT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:45:35 2024
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

(RbtwsChannelNum,
 RbtwsRssi) = mibBuilder.importSymbols(
    "RBTWS-AP-TC",
    "RbtwsChannelNum",
    "RbtwsRssi")

(RbtwsRFDetectClassification,
 RbtwsRFDetectClassificationReason,
 RbtwsRFDetectNetworkingMode) = mibBuilder.importSymbols(
    "RBTWS-RF-DETECT-TC",
    "RbtwsRFDetectClassification",
    "RbtwsRFDetectClassificationReason",
    "RbtwsRFDetectNetworkingMode")

(rbtwsMibs,) = mibBuilder.importSymbols(
    "RBTWS-ROOT-MIB",
    "rbtwsMibs")

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

rbtwsInfoRFDetectMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 9)
)
rbtwsInfoRFDetectMib.setRevisions(
        ("2007-06-27 00:11",
         "2007-04-18 00:10",
         "2006-10-11 00:03")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RbtwsInfoRFDetectObjects_ObjectIdentity = ObjectIdentity
rbtwsInfoRFDetectObjects = _RbtwsInfoRFDetectObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 9, 1)
)
_RbtwsInfoRFDetectDataObjects_ObjectIdentity = ObjectIdentity
rbtwsInfoRFDetectDataObjects = _RbtwsInfoRFDetectDataObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 9, 1, 1)
)
_RbtwsInfoRFDetectXmtrTable_Object = MibTable
rbtwsInfoRFDetectXmtrTable = _RbtwsInfoRFDetectXmtrTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 9, 1, 1, 1)
)
if mibBuilder.loadTexts:
    rbtwsInfoRFDetectXmtrTable.setStatus("current")
_RbtwsInfoRFDetectXmtrEntry_Object = MibTableRow
rbtwsInfoRFDetectXmtrEntry = _RbtwsInfoRFDetectXmtrEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 9, 1, 1, 1, 1)
)
rbtwsInfoRFDetectXmtrEntry.setIndexNames(
    (0, "RBTWS-INFO-RF-DETECT-MIB", "rbtwsInfoRFDetectXmtrTransmitterMacAddress"),
    (0, "RBTWS-INFO-RF-DETECT-MIB", "rbtwsInfoRFDetectXmtrListenerMacAddress"),
    (0, "RBTWS-INFO-RF-DETECT-MIB", "rbtwsInfoRFDetectXmtrChannelNum"),
)
if mibBuilder.loadTexts:
    rbtwsInfoRFDetectXmtrEntry.setStatus("current")
_RbtwsInfoRFDetectXmtrTransmitterMacAddress_Type = MacAddress
_RbtwsInfoRFDetectXmtrTransmitterMacAddress_Object = MibTableColumn
rbtwsInfoRFDetectXmtrTransmitterMacAddress = _RbtwsInfoRFDetectXmtrTransmitterMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 9, 1, 1, 1, 1, 1),
    _RbtwsInfoRFDetectXmtrTransmitterMacAddress_Type()
)
rbtwsInfoRFDetectXmtrTransmitterMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbtwsInfoRFDetectXmtrTransmitterMacAddress.setStatus("current")
_RbtwsInfoRFDetectXmtrListenerMacAddress_Type = MacAddress
_RbtwsInfoRFDetectXmtrListenerMacAddress_Object = MibTableColumn
rbtwsInfoRFDetectXmtrListenerMacAddress = _RbtwsInfoRFDetectXmtrListenerMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 9, 1, 1, 1, 1, 2),
    _RbtwsInfoRFDetectXmtrListenerMacAddress_Type()
)
rbtwsInfoRFDetectXmtrListenerMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbtwsInfoRFDetectXmtrListenerMacAddress.setStatus("current")
_RbtwsInfoRFDetectXmtrChannelNum_Type = RbtwsChannelNum
_RbtwsInfoRFDetectXmtrChannelNum_Object = MibTableColumn
rbtwsInfoRFDetectXmtrChannelNum = _RbtwsInfoRFDetectXmtrChannelNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 9, 1, 1, 1, 1, 3),
    _RbtwsInfoRFDetectXmtrChannelNum_Type()
)
rbtwsInfoRFDetectXmtrChannelNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbtwsInfoRFDetectXmtrChannelNum.setStatus("current")
_RbtwsInfoRFDetectXmtrRssi_Type = RbtwsRssi
_RbtwsInfoRFDetectXmtrRssi_Object = MibTableColumn
rbtwsInfoRFDetectXmtrRssi = _RbtwsInfoRFDetectXmtrRssi_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 9, 1, 1, 1, 1, 4),
    _RbtwsInfoRFDetectXmtrRssi_Type()
)
rbtwsInfoRFDetectXmtrRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsInfoRFDetectXmtrRssi.setStatus("current")


class _RbtwsInfoRFDetectXmtrSsid_Type(DisplayString):
    """Custom type rbtwsInfoRFDetectXmtrSsid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RbtwsInfoRFDetectXmtrSsid_Type.__name__ = "DisplayString"
_RbtwsInfoRFDetectXmtrSsid_Object = MibTableColumn
rbtwsInfoRFDetectXmtrSsid = _RbtwsInfoRFDetectXmtrSsid_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 9, 1, 1, 1, 1, 5),
    _RbtwsInfoRFDetectXmtrSsid_Type()
)
rbtwsInfoRFDetectXmtrSsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsInfoRFDetectXmtrSsid.setStatus("current")
_RbtwsInfoRFDetectXmtrNetworkingMode_Type = RbtwsRFDetectNetworkingMode
_RbtwsInfoRFDetectXmtrNetworkingMode_Object = MibTableColumn
rbtwsInfoRFDetectXmtrNetworkingMode = _RbtwsInfoRFDetectXmtrNetworkingMode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 9, 1, 1, 1, 1, 6),
    _RbtwsInfoRFDetectXmtrNetworkingMode_Type()
)
rbtwsInfoRFDetectXmtrNetworkingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsInfoRFDetectXmtrNetworkingMode.setStatus("current")
_RbtwsInfoRFDetectXmtrClassification_Type = RbtwsRFDetectClassification
_RbtwsInfoRFDetectXmtrClassification_Object = MibTableColumn
rbtwsInfoRFDetectXmtrClassification = _RbtwsInfoRFDetectXmtrClassification_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 9, 1, 1, 1, 1, 7),
    _RbtwsInfoRFDetectXmtrClassification_Type()
)
rbtwsInfoRFDetectXmtrClassification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsInfoRFDetectXmtrClassification.setStatus("current")
_RbtwsInfoRFDetectXmtrClassificationReason_Type = RbtwsRFDetectClassificationReason
_RbtwsInfoRFDetectXmtrClassificationReason_Object = MibTableColumn
rbtwsInfoRFDetectXmtrClassificationReason = _RbtwsInfoRFDetectXmtrClassificationReason_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 9, 1, 1, 1, 1, 8),
    _RbtwsInfoRFDetectXmtrClassificationReason_Type()
)
rbtwsInfoRFDetectXmtrClassificationReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsInfoRFDetectXmtrClassificationReason.setStatus("current")
_RbtwsInfoRFDetectCurrentXmtrTableSize_Type = Gauge32
_RbtwsInfoRFDetectCurrentXmtrTableSize_Object = MibScalar
rbtwsInfoRFDetectCurrentXmtrTableSize = _RbtwsInfoRFDetectCurrentXmtrTableSize_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 9, 1, 1, 2),
    _RbtwsInfoRFDetectCurrentXmtrTableSize_Type()
)
rbtwsInfoRFDetectCurrentXmtrTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsInfoRFDetectCurrentXmtrTableSize.setStatus("current")
_RbtwsInfoRFDetectConformance_ObjectIdentity = ObjectIdentity
rbtwsInfoRFDetectConformance = _RbtwsInfoRFDetectConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 9, 1, 2)
)
_RbtwsInfoRFDetectCompliances_ObjectIdentity = ObjectIdentity
rbtwsInfoRFDetectCompliances = _RbtwsInfoRFDetectCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 9, 1, 2, 1)
)
_RbtwsInfoRFDetectGroups_ObjectIdentity = ObjectIdentity
rbtwsInfoRFDetectGroups = _RbtwsInfoRFDetectGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 9, 1, 2, 2)
)

# Managed Objects groups

rbtwsInfoRFDetectXmtrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 9, 1, 2, 2, 1)
)
rbtwsInfoRFDetectXmtrGroup.setObjects(
      *(("RBTWS-INFO-RF-DETECT-MIB", "rbtwsInfoRFDetectXmtrRssi"),
        ("RBTWS-INFO-RF-DETECT-MIB", "rbtwsInfoRFDetectXmtrSsid"))
)
if mibBuilder.loadTexts:
    rbtwsInfoRFDetectXmtrGroup.setStatus("current")

rbtwsInfoRFDetectXmtrClassificationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 9, 1, 2, 2, 2)
)
rbtwsInfoRFDetectXmtrClassificationGroup.setObjects(
      *(("RBTWS-INFO-RF-DETECT-MIB", "rbtwsInfoRFDetectXmtrNetworkingMode"),
        ("RBTWS-INFO-RF-DETECT-MIB", "rbtwsInfoRFDetectXmtrClassification"),
        ("RBTWS-INFO-RF-DETECT-MIB", "rbtwsInfoRFDetectXmtrClassificationReason"))
)
if mibBuilder.loadTexts:
    rbtwsInfoRFDetectXmtrClassificationGroup.setStatus("current")

rbtwsInfoRFDetectCurrentXmtrTableSizeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 9, 1, 2, 2, 3)
)
rbtwsInfoRFDetectCurrentXmtrTableSizeGroup.setObjects(
    ("RBTWS-INFO-RF-DETECT-MIB", "rbtwsInfoRFDetectCurrentXmtrTableSize")
)
if mibBuilder.loadTexts:
    rbtwsInfoRFDetectCurrentXmtrTableSizeGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

rbtwsInfoRFDetectCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 9, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    rbtwsInfoRFDetectCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RBTWS-INFO-RF-DETECT-MIB",
    **{"rbtwsInfoRFDetectMib": rbtwsInfoRFDetectMib,
       "rbtwsInfoRFDetectObjects": rbtwsInfoRFDetectObjects,
       "rbtwsInfoRFDetectDataObjects": rbtwsInfoRFDetectDataObjects,
       "rbtwsInfoRFDetectXmtrTable": rbtwsInfoRFDetectXmtrTable,
       "rbtwsInfoRFDetectXmtrEntry": rbtwsInfoRFDetectXmtrEntry,
       "rbtwsInfoRFDetectXmtrTransmitterMacAddress": rbtwsInfoRFDetectXmtrTransmitterMacAddress,
       "rbtwsInfoRFDetectXmtrListenerMacAddress": rbtwsInfoRFDetectXmtrListenerMacAddress,
       "rbtwsInfoRFDetectXmtrChannelNum": rbtwsInfoRFDetectXmtrChannelNum,
       "rbtwsInfoRFDetectXmtrRssi": rbtwsInfoRFDetectXmtrRssi,
       "rbtwsInfoRFDetectXmtrSsid": rbtwsInfoRFDetectXmtrSsid,
       "rbtwsInfoRFDetectXmtrNetworkingMode": rbtwsInfoRFDetectXmtrNetworkingMode,
       "rbtwsInfoRFDetectXmtrClassification": rbtwsInfoRFDetectXmtrClassification,
       "rbtwsInfoRFDetectXmtrClassificationReason": rbtwsInfoRFDetectXmtrClassificationReason,
       "rbtwsInfoRFDetectCurrentXmtrTableSize": rbtwsInfoRFDetectCurrentXmtrTableSize,
       "rbtwsInfoRFDetectConformance": rbtwsInfoRFDetectConformance,
       "rbtwsInfoRFDetectCompliances": rbtwsInfoRFDetectCompliances,
       "rbtwsInfoRFDetectCompliance": rbtwsInfoRFDetectCompliance,
       "rbtwsInfoRFDetectGroups": rbtwsInfoRFDetectGroups,
       "rbtwsInfoRFDetectXmtrGroup": rbtwsInfoRFDetectXmtrGroup,
       "rbtwsInfoRFDetectXmtrClassificationGroup": rbtwsInfoRFDetectXmtrClassificationGroup,
       "rbtwsInfoRFDetectCurrentXmtrTableSizeGroup": rbtwsInfoRFDetectCurrentXmtrTableSizeGroup}
)
