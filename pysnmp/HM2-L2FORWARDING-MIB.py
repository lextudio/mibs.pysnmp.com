# SNMP MIB module (HM2-L2FORWARDING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HM2-L2FORWARDING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:55:59 2024
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

(HmEnabledStatus,
 hm2ConfigurationMibs) = mibBuilder.importSymbols(
    "HM2-TC-MIB",
    "HmEnabledStatus",
    "hm2ConfigurationMibs")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

hm2L2ForwardingMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 30)
)
hm2L2ForwardingMib.setRevisions(
        ("2011-03-16 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hm2L2ForwardingMibNotifications_ObjectIdentity = ObjectIdentity
hm2L2ForwardingMibNotifications = _Hm2L2ForwardingMibNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 30, 0)
)
_Hm2L2ForwardingMibObjects_ObjectIdentity = ObjectIdentity
hm2L2ForwardingMibObjects = _Hm2L2ForwardingMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 30, 1)
)
_Hm2L2ForwGeneralGroup_ObjectIdentity = ObjectIdentity
hm2L2ForwGeneralGroup = _Hm2L2ForwGeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 30, 1, 1)
)


class _Hm2L2VlanUnawareModeAdminStatus_Type(HmEnabledStatus):
    """Custom type hm2L2VlanUnawareModeAdminStatus based on HmEnabledStatus"""


_Hm2L2VlanUnawareModeAdminStatus_Object = MibScalar
hm2L2VlanUnawareModeAdminStatus = _Hm2L2VlanUnawareModeAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 30, 1, 1, 1),
    _Hm2L2VlanUnawareModeAdminStatus_Type()
)
hm2L2VlanUnawareModeAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2L2VlanUnawareModeAdminStatus.setStatus("current")
_Hm2L2VlanUnawareModeOperStatus_Type = HmEnabledStatus
_Hm2L2VlanUnawareModeOperStatus_Object = MibScalar
hm2L2VlanUnawareModeOperStatus = _Hm2L2VlanUnawareModeOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 30, 1, 1, 2),
    _Hm2L2VlanUnawareModeOperStatus_Type()
)
hm2L2VlanUnawareModeOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2L2VlanUnawareModeOperStatus.setStatus("current")
_Hm2L2ForwClassOfServiceGroup_ObjectIdentity = ObjectIdentity
hm2L2ForwClassOfServiceGroup = _Hm2L2ForwClassOfServiceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 30, 1, 2)
)
_Hm2TrafficClassTable_Object = MibTable
hm2TrafficClassTable = _Hm2TrafficClassTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 30, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hm2TrafficClassTable.setStatus("current")
_Hm2TrafficClassEntry_Object = MibTableRow
hm2TrafficClassEntry = _Hm2TrafficClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 30, 1, 2, 1, 1)
)
hm2TrafficClassEntry.setIndexNames(
    (0, "HM2-L2FORWARDING-MIB", "hm2TrafficClassPriority"),
)
if mibBuilder.loadTexts:
    hm2TrafficClassEntry.setStatus("current")


class _Hm2TrafficClassPriority_Type(Integer32):
    """Custom type hm2TrafficClassPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Hm2TrafficClassPriority_Type.__name__ = "Integer32"
_Hm2TrafficClassPriority_Object = MibTableColumn
hm2TrafficClassPriority = _Hm2TrafficClassPriority_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 30, 1, 2, 1, 1, 1),
    _Hm2TrafficClassPriority_Type()
)
hm2TrafficClassPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2TrafficClassPriority.setStatus("current")


class _Hm2TrafficClass_Type(Integer32):
    """Custom type hm2TrafficClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Hm2TrafficClass_Type.__name__ = "Integer32"
_Hm2TrafficClass_Object = MibTableColumn
hm2TrafficClass = _Hm2TrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 30, 1, 2, 1, 1, 2),
    _Hm2TrafficClass_Type()
)
hm2TrafficClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2TrafficClass.setStatus("current")
_Hm2CosMapIpDscpTable_Object = MibTable
hm2CosMapIpDscpTable = _Hm2CosMapIpDscpTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 30, 1, 2, 2)
)
if mibBuilder.loadTexts:
    hm2CosMapIpDscpTable.setStatus("current")
_Hm2CosMapIpDscpEntry_Object = MibTableRow
hm2CosMapIpDscpEntry = _Hm2CosMapIpDscpEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 30, 1, 2, 2, 1)
)
hm2CosMapIpDscpEntry.setIndexNames(
    (0, "HM2-L2FORWARDING-MIB", "hm2CosMapIpDscpValue"),
)
if mibBuilder.loadTexts:
    hm2CosMapIpDscpEntry.setStatus("current")


class _Hm2CosMapIpDscpValue_Type(Unsigned32):
    """Custom type hm2CosMapIpDscpValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Hm2CosMapIpDscpValue_Type.__name__ = "Unsigned32"
_Hm2CosMapIpDscpValue_Object = MibTableColumn
hm2CosMapIpDscpValue = _Hm2CosMapIpDscpValue_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 30, 1, 2, 2, 1, 1),
    _Hm2CosMapIpDscpValue_Type()
)
hm2CosMapIpDscpValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2CosMapIpDscpValue.setStatus("current")


class _Hm2CosMapIpDscpTrafficClass_Type(Unsigned32):
    """Custom type hm2CosMapIpDscpTrafficClass based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Hm2CosMapIpDscpTrafficClass_Type.__name__ = "Unsigned32"
_Hm2CosMapIpDscpTrafficClass_Object = MibTableColumn
hm2CosMapIpDscpTrafficClass = _Hm2CosMapIpDscpTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 30, 1, 2, 2, 1, 2),
    _Hm2CosMapIpDscpTrafficClass_Type()
)
hm2CosMapIpDscpTrafficClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2CosMapIpDscpTrafficClass.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HM2-L2FORWARDING-MIB",
    **{"hm2L2ForwardingMib": hm2L2ForwardingMib,
       "hm2L2ForwardingMibNotifications": hm2L2ForwardingMibNotifications,
       "hm2L2ForwardingMibObjects": hm2L2ForwardingMibObjects,
       "hm2L2ForwGeneralGroup": hm2L2ForwGeneralGroup,
       "hm2L2VlanUnawareModeAdminStatus": hm2L2VlanUnawareModeAdminStatus,
       "hm2L2VlanUnawareModeOperStatus": hm2L2VlanUnawareModeOperStatus,
       "hm2L2ForwClassOfServiceGroup": hm2L2ForwClassOfServiceGroup,
       "hm2TrafficClassTable": hm2TrafficClassTable,
       "hm2TrafficClassEntry": hm2TrafficClassEntry,
       "hm2TrafficClassPriority": hm2TrafficClassPriority,
       "hm2TrafficClass": hm2TrafficClass,
       "hm2CosMapIpDscpTable": hm2CosMapIpDscpTable,
       "hm2CosMapIpDscpEntry": hm2CosMapIpDscpEntry,
       "hm2CosMapIpDscpValue": hm2CosMapIpDscpValue,
       "hm2CosMapIpDscpTrafficClass": hm2CosMapIpDscpTrafficClass}
)
