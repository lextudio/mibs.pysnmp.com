# SNMP MIB module (ENTERASYS-ESWITCH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ENTERASYS-ESWITCH-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:38:50 2024
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

(etsysModules,) = mibBuilder.importSymbols(
    "ENTERASYS-MIB-NAMES",
    "etsysModules")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

enterasysESwitchMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 10)
)
enterasysESwitchMIB.setRevisions(
        ("2002-03-07 19:50",
         "2001-02-13 11:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EtsysESwitchObjects_ObjectIdentity = ObjectIdentity
etsysESwitchObjects = _EtsysESwitchObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 10, 1)
)
_EtsysESwitchParams_ObjectIdentity = ObjectIdentity
etsysESwitchParams = _EtsysESwitchParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 10, 1, 1)
)
_EtsysESwitchAdminStatus_Type = EnabledStatus
_EtsysESwitchAdminStatus_Object = MibScalar
etsysESwitchAdminStatus = _EtsysESwitchAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 10, 1, 1, 1),
    _EtsysESwitchAdminStatus_Type()
)
etsysESwitchAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysESwitchAdminStatus.setStatus("current")
_EtsysESwitchRateLimiting_ObjectIdentity = ObjectIdentity
etsysESwitchRateLimiting = _EtsysESwitchRateLimiting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 10, 1, 2)
)
_EtsysESwitchRateLimitingTable_Object = MibTable
etsysESwitchRateLimitingTable = _EtsysESwitchRateLimitingTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 10, 1, 2, 1)
)
if mibBuilder.loadTexts:
    etsysESwitchRateLimitingTable.setStatus("current")
_EtsysESwitchRateLimitingEntry_Object = MibTableRow
etsysESwitchRateLimitingEntry = _EtsysESwitchRateLimitingEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 10, 1, 2, 1, 1)
)
etsysESwitchRateLimitingEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    etsysESwitchRateLimitingEntry.setStatus("current")
_EtsysESwitchRateLimitSwitch_Type = TruthValue
_EtsysESwitchRateLimitSwitch_Object = MibTableColumn
etsysESwitchRateLimitSwitch = _EtsysESwitchRateLimitSwitch_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 10, 1, 2, 1, 1, 1),
    _EtsysESwitchRateLimitSwitch_Type()
)
etsysESwitchRateLimitSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysESwitchRateLimitSwitch.setStatus("current")
_EtsysESwitchRateLimit_Type = Unsigned32
_EtsysESwitchRateLimit_Object = MibTableColumn
etsysESwitchRateLimit = _EtsysESwitchRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 10, 1, 2, 1, 1, 2),
    _EtsysESwitchRateLimit_Type()
)
etsysESwitchRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysESwitchRateLimit.setStatus("current")
_EtsysESwitchFilter_ObjectIdentity = ObjectIdentity
etsysESwitchFilter = _EtsysESwitchFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 10, 1, 3)
)
_EtsysESwitchAddrFilterTable_Object = MibTable
etsysESwitchAddrFilterTable = _EtsysESwitchAddrFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 10, 1, 3, 1)
)
if mibBuilder.loadTexts:
    etsysESwitchAddrFilterTable.setStatus("current")
_EtsysESwitchAddrFilterEntry_Object = MibTableRow
etsysESwitchAddrFilterEntry = _EtsysESwitchAddrFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 10, 1, 3, 1, 1)
)
etsysESwitchAddrFilterEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    etsysESwitchAddrFilterEntry.setStatus("current")
_EtsysESwitchAddressFilter_Type = TruthValue
_EtsysESwitchAddressFilter_Object = MibTableColumn
etsysESwitchAddressFilter = _EtsysESwitchAddressFilter_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 10, 1, 3, 1, 1, 1),
    _EtsysESwitchAddressFilter_Type()
)
etsysESwitchAddressFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysESwitchAddressFilter.setStatus("current")
_EtsysESwitchProtocolObjects_ObjectIdentity = ObjectIdentity
etsysESwitchProtocolObjects = _EtsysESwitchProtocolObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 10, 1, 4)
)
_EtsysESwitchEtherTypeTable_Object = MibTable
etsysESwitchEtherTypeTable = _EtsysESwitchEtherTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 10, 1, 4, 1)
)
if mibBuilder.loadTexts:
    etsysESwitchEtherTypeTable.setStatus("current")
_EtsysESwitchEtherTypeEntry_Object = MibTableRow
etsysESwitchEtherTypeEntry = _EtsysESwitchEtherTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 10, 1, 4, 1, 1)
)
etsysESwitchEtherTypeEntry.setIndexNames(
    (0, "ENTERASYS-ESWITCH-MIB", "etsysESwitchEtherTypeIndex"),
)
if mibBuilder.loadTexts:
    etsysESwitchEtherTypeEntry.setStatus("current")


class _EtsysESwitchEtherTypeIndex_Type(Integer32):
    """Custom type etsysESwitchEtherTypeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_EtsysESwitchEtherTypeIndex_Type.__name__ = "Integer32"
_EtsysESwitchEtherTypeIndex_Object = MibTableColumn
etsysESwitchEtherTypeIndex = _EtsysESwitchEtherTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 10, 1, 4, 1, 1, 1),
    _EtsysESwitchEtherTypeIndex_Type()
)
etsysESwitchEtherTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysESwitchEtherTypeIndex.setStatus("current")


class _EtsysESwitchEtherTypeValue_Type(OctetString):
    """Custom type etsysESwitchEtherTypeValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_EtsysESwitchEtherTypeValue_Type.__name__ = "OctetString"
_EtsysESwitchEtherTypeValue_Object = MibTableColumn
etsysESwitchEtherTypeValue = _EtsysESwitchEtherTypeValue_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 10, 1, 4, 1, 1, 2),
    _EtsysESwitchEtherTypeValue_Type()
)
etsysESwitchEtherTypeValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysESwitchEtherTypeValue.setStatus("current")


class _EtsysESwitchEtherTypeStatus_Type(Integer32):
    """Custom type etsysESwitchEtherTypeStatus based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("deleteOnReset", 4),
          ("invalid", 2),
          ("other", 1),
          ("permanent", 3))
    )


_EtsysESwitchEtherTypeStatus_Type.__name__ = "Integer32"
_EtsysESwitchEtherTypeStatus_Object = MibTableColumn
etsysESwitchEtherTypeStatus = _EtsysESwitchEtherTypeStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 10, 1, 4, 1, 1, 3),
    _EtsysESwitchEtherTypeStatus_Type()
)
etsysESwitchEtherTypeStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysESwitchEtherTypeStatus.setStatus("current")
_EtsysESwitchEtherTypePreempted_Type = TruthValue
_EtsysESwitchEtherTypePreempted_Object = MibTableColumn
etsysESwitchEtherTypePreempted = _EtsysESwitchEtherTypePreempted_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 10, 1, 4, 1, 1, 4),
    _EtsysESwitchEtherTypePreempted_Type()
)
etsysESwitchEtherTypePreempted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysESwitchEtherTypePreempted.setStatus("current")
_EtsysESwitchProtocolTable_Object = MibTable
etsysESwitchProtocolTable = _EtsysESwitchProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 10, 1, 4, 2)
)
if mibBuilder.loadTexts:
    etsysESwitchProtocolTable.setStatus("current")
_EtsysESwitchProtocolEntry_Object = MibTableRow
etsysESwitchProtocolEntry = _EtsysESwitchProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 10, 1, 4, 2, 1)
)
etsysESwitchProtocolEntry.setIndexNames(
    (0, "ENTERASYS-ESWITCH-MIB", "etsysESwitchProtocolReceivePort"),
    (0, "ENTERASYS-ESWITCH-MIB", "etsysESwitchProtocolType"),
    (0, "ENTERASYS-ESWITCH-MIB", "etsysESwitchProtocolIndex"),
)
if mibBuilder.loadTexts:
    etsysESwitchProtocolEntry.setStatus("current")


class _EtsysESwitchProtocolReceivePort_Type(Integer32):
    """Custom type etsysESwitchProtocolReceivePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EtsysESwitchProtocolReceivePort_Type.__name__ = "Integer32"
_EtsysESwitchProtocolReceivePort_Object = MibTableColumn
etsysESwitchProtocolReceivePort = _EtsysESwitchProtocolReceivePort_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 10, 1, 4, 2, 1, 1),
    _EtsysESwitchProtocolReceivePort_Type()
)
etsysESwitchProtocolReceivePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysESwitchProtocolReceivePort.setStatus("current")


class _EtsysESwitchProtocolType_Type(Integer32):
    """Custom type etsysESwitchProtocolType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("decnet", 9),
          ("ipv4", 2),
          ("ipv6", 10),
          ("ipxEthernet", 3),
          ("ipxLlc", 5),
          ("ipxRaw", 4),
          ("ipxSnap", 6),
          ("netBios", 8),
          ("sna", 7),
          ("userEtherType", 1))
    )


_EtsysESwitchProtocolType_Type.__name__ = "Integer32"
_EtsysESwitchProtocolType_Object = MibTableColumn
etsysESwitchProtocolType = _EtsysESwitchProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 10, 1, 4, 2, 1, 2),
    _EtsysESwitchProtocolType_Type()
)
etsysESwitchProtocolType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysESwitchProtocolType.setStatus("current")


class _EtsysESwitchProtocolIndex_Type(Integer32):
    """Custom type etsysESwitchProtocolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_EtsysESwitchProtocolIndex_Type.__name__ = "Integer32"
_EtsysESwitchProtocolIndex_Object = MibTableColumn
etsysESwitchProtocolIndex = _EtsysESwitchProtocolIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 10, 1, 4, 2, 1, 3),
    _EtsysESwitchProtocolIndex_Type()
)
etsysESwitchProtocolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysESwitchProtocolIndex.setStatus("current")


class _EtsysESwitchProtocolConstraint_Type(Integer32):
    """Custom type etsysESwitchProtocolConstraint based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("portMask", 1),
          ("vlan", 2))
    )


_EtsysESwitchProtocolConstraint_Type.__name__ = "Integer32"
_EtsysESwitchProtocolConstraint_Object = MibTableColumn
etsysESwitchProtocolConstraint = _EtsysESwitchProtocolConstraint_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 10, 1, 4, 2, 1, 4),
    _EtsysESwitchProtocolConstraint_Type()
)
etsysESwitchProtocolConstraint.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysESwitchProtocolConstraint.setStatus("current")
_EtsysESwitchProtocolAllowedToGoTo_Type = PortList
_EtsysESwitchProtocolAllowedToGoTo_Object = MibTableColumn
etsysESwitchProtocolAllowedToGoTo = _EtsysESwitchProtocolAllowedToGoTo_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 10, 1, 4, 2, 1, 5),
    _EtsysESwitchProtocolAllowedToGoTo_Type()
)
etsysESwitchProtocolAllowedToGoTo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysESwitchProtocolAllowedToGoTo.setStatus("current")


class _EtsysESwitchProtocolVlanId_Type(Integer32):
    """Custom type etsysESwitchProtocolVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EtsysESwitchProtocolVlanId_Type.__name__ = "Integer32"
_EtsysESwitchProtocolVlanId_Object = MibTableColumn
etsysESwitchProtocolVlanId = _EtsysESwitchProtocolVlanId_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 10, 1, 4, 2, 1, 6),
    _EtsysESwitchProtocolVlanId_Type()
)
etsysESwitchProtocolVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysESwitchProtocolVlanId.setStatus("current")


class _EtsysESwitchProtocolStatus_Type(Integer32):
    """Custom type etsysESwitchProtocolStatus based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("deleteOnReset", 4),
          ("invalid", 2),
          ("other", 1),
          ("permanent", 3))
    )


_EtsysESwitchProtocolStatus_Type.__name__ = "Integer32"
_EtsysESwitchProtocolStatus_Object = MibTableColumn
etsysESwitchProtocolStatus = _EtsysESwitchProtocolStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 10, 1, 4, 2, 1, 7),
    _EtsysESwitchProtocolStatus_Type()
)
etsysESwitchProtocolStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysESwitchProtocolStatus.setStatus("current")
_EtsysESwitchProtocolPreempted_Type = TruthValue
_EtsysESwitchProtocolPreempted_Object = MibTableColumn
etsysESwitchProtocolPreempted = _EtsysESwitchProtocolPreempted_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 10, 1, 4, 2, 1, 8),
    _EtsysESwitchProtocolPreempted_Type()
)
etsysESwitchProtocolPreempted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysESwitchProtocolPreempted.setStatus("current")
_EtsysESwitchConformance_ObjectIdentity = ObjectIdentity
etsysESwitchConformance = _EtsysESwitchConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 10, 2)
)
_EtsysESwitchGroups_ObjectIdentity = ObjectIdentity
etsysESwitchGroups = _EtsysESwitchGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 10, 2, 1)
)
_EtsysESwitchCompliances_ObjectIdentity = ObjectIdentity
etsysESwitchCompliances = _EtsysESwitchCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 10, 2, 2)
)

# Managed Objects groups

etsysESwitchBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 10, 2, 1, 1)
)
etsysESwitchBaseGroup.setObjects(
      *(("ENTERASYS-ESWITCH-MIB", "etsysESwitchAdminStatus"),
        ("ENTERASYS-ESWITCH-MIB", "etsysESwitchRateLimitSwitch"),
        ("ENTERASYS-ESWITCH-MIB", "etsysESwitchRateLimit"),
        ("ENTERASYS-ESWITCH-MIB", "etsysESwitchAddressFilter"))
)
if mibBuilder.loadTexts:
    etsysESwitchBaseGroup.setStatus("current")

etsysESwitchEtherTypeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 10, 2, 1, 2)
)
etsysESwitchEtherTypeGroup.setObjects(
      *(("ENTERASYS-ESWITCH-MIB", "etsysESwitchEtherTypeValue"),
        ("ENTERASYS-ESWITCH-MIB", "etsysESwitchEtherTypeStatus"),
        ("ENTERASYS-ESWITCH-MIB", "etsysESwitchEtherTypePreempted"))
)
if mibBuilder.loadTexts:
    etsysESwitchEtherTypeGroup.setStatus("current")

etsysESwitchProtocolGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 10, 2, 1, 3)
)
etsysESwitchProtocolGroup.setObjects(
      *(("ENTERASYS-ESWITCH-MIB", "etsysESwitchProtocolConstraint"),
        ("ENTERASYS-ESWITCH-MIB", "etsysESwitchProtocolAllowedToGoTo"),
        ("ENTERASYS-ESWITCH-MIB", "etsysESwitchProtocolVlanId"),
        ("ENTERASYS-ESWITCH-MIB", "etsysESwitchProtocolStatus"),
        ("ENTERASYS-ESWITCH-MIB", "etsysESwitchProtocolPreempted"))
)
if mibBuilder.loadTexts:
    etsysESwitchProtocolGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

etsysESwitchCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 10, 2, 2, 1)
)
if mibBuilder.loadTexts:
    etsysESwitchCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTERASYS-ESWITCH-MIB",
    **{"enterasysESwitchMIB": enterasysESwitchMIB,
       "etsysESwitchObjects": etsysESwitchObjects,
       "etsysESwitchParams": etsysESwitchParams,
       "etsysESwitchAdminStatus": etsysESwitchAdminStatus,
       "etsysESwitchRateLimiting": etsysESwitchRateLimiting,
       "etsysESwitchRateLimitingTable": etsysESwitchRateLimitingTable,
       "etsysESwitchRateLimitingEntry": etsysESwitchRateLimitingEntry,
       "etsysESwitchRateLimitSwitch": etsysESwitchRateLimitSwitch,
       "etsysESwitchRateLimit": etsysESwitchRateLimit,
       "etsysESwitchFilter": etsysESwitchFilter,
       "etsysESwitchAddrFilterTable": etsysESwitchAddrFilterTable,
       "etsysESwitchAddrFilterEntry": etsysESwitchAddrFilterEntry,
       "etsysESwitchAddressFilter": etsysESwitchAddressFilter,
       "etsysESwitchProtocolObjects": etsysESwitchProtocolObjects,
       "etsysESwitchEtherTypeTable": etsysESwitchEtherTypeTable,
       "etsysESwitchEtherTypeEntry": etsysESwitchEtherTypeEntry,
       "etsysESwitchEtherTypeIndex": etsysESwitchEtherTypeIndex,
       "etsysESwitchEtherTypeValue": etsysESwitchEtherTypeValue,
       "etsysESwitchEtherTypeStatus": etsysESwitchEtherTypeStatus,
       "etsysESwitchEtherTypePreempted": etsysESwitchEtherTypePreempted,
       "etsysESwitchProtocolTable": etsysESwitchProtocolTable,
       "etsysESwitchProtocolEntry": etsysESwitchProtocolEntry,
       "etsysESwitchProtocolReceivePort": etsysESwitchProtocolReceivePort,
       "etsysESwitchProtocolType": etsysESwitchProtocolType,
       "etsysESwitchProtocolIndex": etsysESwitchProtocolIndex,
       "etsysESwitchProtocolConstraint": etsysESwitchProtocolConstraint,
       "etsysESwitchProtocolAllowedToGoTo": etsysESwitchProtocolAllowedToGoTo,
       "etsysESwitchProtocolVlanId": etsysESwitchProtocolVlanId,
       "etsysESwitchProtocolStatus": etsysESwitchProtocolStatus,
       "etsysESwitchProtocolPreempted": etsysESwitchProtocolPreempted,
       "etsysESwitchConformance": etsysESwitchConformance,
       "etsysESwitchGroups": etsysESwitchGroups,
       "etsysESwitchBaseGroup": etsysESwitchBaseGroup,
       "etsysESwitchEtherTypeGroup": etsysESwitchEtherTypeGroup,
       "etsysESwitchProtocolGroup": etsysESwitchProtocolGroup,
       "etsysESwitchCompliances": etsysESwitchCompliances,
       "etsysESwitchCompliance": etsysESwitchCompliance}
)
