# SNMP MIB module (WL400-SNMPGEN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WL400-SNMPGEN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:14:02 2024
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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")

(wl400Generic,
 wl400Modules) = mibBuilder.importSymbols(
    "WL400-GLOBAL-REG",
    "wl400Generic",
    "wl400Modules")


# MODULE-IDENTITY

snmpGenMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 232, 143, 1, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SnmpGenMIB_ObjectIdentity = ObjectIdentity
snmpGenMIB = _SnmpGenMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 144, 1)
)
_SnmpGenConf_ObjectIdentity = ObjectIdentity
snmpGenConf = _SnmpGenConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 144, 1, 1)
)
_SnmpGenGroups_ObjectIdentity = ObjectIdentity
snmpGenGroups = _SnmpGenGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 144, 1, 1, 1)
)
_SnmpGenCompl_ObjectIdentity = ObjectIdentity
snmpGenCompl = _SnmpGenCompl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 144, 1, 1, 2)
)
_SnmpGenObjs_ObjectIdentity = ObjectIdentity
snmpGenObjs = _SnmpGenObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 144, 1, 2)
)


class _SnmpGenReadCommunityString_Type(OctetString):
    """Custom type snmpGenReadCommunityString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SnmpGenReadCommunityString_Type.__name__ = "OctetString"
_SnmpGenReadCommunityString_Object = MibScalar
snmpGenReadCommunityString = _SnmpGenReadCommunityString_Object(
    (1, 3, 6, 1, 4, 1, 232, 144, 1, 2, 1),
    _SnmpGenReadCommunityString_Type()
)
snmpGenReadCommunityString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpGenReadCommunityString.setStatus("current")


class _SnmpGenWriteCommunityString_Type(OctetString):
    """Custom type snmpGenWriteCommunityString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SnmpGenWriteCommunityString_Type.__name__ = "OctetString"
_SnmpGenWriteCommunityString_Object = MibScalar
snmpGenWriteCommunityString = _SnmpGenWriteCommunityString_Object(
    (1, 3, 6, 1, 4, 1, 232, 144, 1, 2, 2),
    _SnmpGenWriteCommunityString_Type()
)
snmpGenWriteCommunityString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpGenWriteCommunityString.setStatus("current")
_SnmpGenTrapDstMaxTableLength_Type = Integer32
_SnmpGenTrapDstMaxTableLength_Object = MibScalar
snmpGenTrapDstMaxTableLength = _SnmpGenTrapDstMaxTableLength_Object(
    (1, 3, 6, 1, 4, 1, 232, 144, 1, 2, 3),
    _SnmpGenTrapDstMaxTableLength_Type()
)
snmpGenTrapDstMaxTableLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpGenTrapDstMaxTableLength.setStatus("current")
_SnmpGenTrapDstTable_Object = MibTable
snmpGenTrapDstTable = _SnmpGenTrapDstTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 144, 1, 2, 4)
)
if mibBuilder.loadTexts:
    snmpGenTrapDstTable.setStatus("current")
_SnmpGenTrapDstEntry_Object = MibTableRow
snmpGenTrapDstEntry = _SnmpGenTrapDstEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 144, 1, 2, 4, 1)
)
snmpGenTrapDstEntry.setIndexNames(
    (0, "WL400-SNMPGEN-MIB", "snmpGenTrapDstIndex"),
)
if mibBuilder.loadTexts:
    snmpGenTrapDstEntry.setStatus("current")


class _SnmpGenTrapDstIndex_Type(Integer32):
    """Custom type snmpGenTrapDstIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_SnmpGenTrapDstIndex_Type.__name__ = "Integer32"
_SnmpGenTrapDstIndex_Object = MibTableColumn
snmpGenTrapDstIndex = _SnmpGenTrapDstIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 144, 1, 2, 4, 1, 1),
    _SnmpGenTrapDstIndex_Type()
)
snmpGenTrapDstIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snmpGenTrapDstIndex.setStatus("current")
_SnmpGenTrapDstIpAddress_Type = IpAddress
_SnmpGenTrapDstIpAddress_Object = MibTableColumn
snmpGenTrapDstIpAddress = _SnmpGenTrapDstIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 232, 144, 1, 2, 4, 1, 2),
    _SnmpGenTrapDstIpAddress_Type()
)
snmpGenTrapDstIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpGenTrapDstIpAddress.setStatus("current")


class _SnmpGenTrapDstType_Type(Integer32):
    """Custom type snmpGenTrapDstType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("syslogOnly", 2),
          ("trapAndSyslog", 3),
          ("trapOnly", 1))
    )


_SnmpGenTrapDstType_Type.__name__ = "Integer32"
_SnmpGenTrapDstType_Object = MibTableColumn
snmpGenTrapDstType = _SnmpGenTrapDstType_Object(
    (1, 3, 6, 1, 4, 1, 232, 144, 1, 2, 4, 1, 3),
    _SnmpGenTrapDstType_Type()
)
snmpGenTrapDstType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpGenTrapDstType.setStatus("current")
_SnmpGenTrapDstRowStatus_Type = RowStatus
_SnmpGenTrapDstRowStatus_Object = MibTableColumn
snmpGenTrapDstRowStatus = _SnmpGenTrapDstRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 144, 1, 2, 4, 1, 4),
    _SnmpGenTrapDstRowStatus_Type()
)
snmpGenTrapDstRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpGenTrapDstRowStatus.setStatus("current")


class _SnmpGenLockStatus_Type(Integer32):
    """Custom type snmpGenLockStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 1),
          ("unlocked", 2))
    )


_SnmpGenLockStatus_Type.__name__ = "Integer32"
_SnmpGenLockStatus_Object = MibScalar
snmpGenLockStatus = _SnmpGenLockStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 144, 1, 2, 5),
    _SnmpGenLockStatus_Type()
)
snmpGenLockStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpGenLockStatus.setStatus("current")


class _SnmpGenChangeIPAddress_Type(OctetString):
    """Custom type snmpGenChangeIPAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(18, 18),
    )


_SnmpGenChangeIPAddress_Type.__name__ = "OctetString"
_SnmpGenChangeIPAddress_Object = MibScalar
snmpGenChangeIPAddress = _SnmpGenChangeIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 232, 144, 1, 2, 6),
    _SnmpGenChangeIPAddress_Type()
)
snmpGenChangeIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpGenChangeIPAddress.setStatus("current")


class _SnmpGenUseDHCP_Type(Integer32):
    """Custom type snmpGenUseDHCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("always", 1),
          ("never", 3),
          ("smart", 2))
    )


_SnmpGenUseDHCP_Type.__name__ = "Integer32"
_SnmpGenUseDHCP_Object = MibScalar
snmpGenUseDHCP = _SnmpGenUseDHCP_Object(
    (1, 3, 6, 1, 4, 1, 232, 144, 1, 2, 7),
    _SnmpGenUseDHCP_Type()
)
snmpGenUseDHCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpGenUseDHCP.setStatus("current")

# Managed Objects groups

snmpGenBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 232, 144, 1, 1, 1, 1)
)
snmpGenBasicGroup.setObjects(
      *(("WL400-SNMPGEN-MIB", "snmpGenReadCommunityString"),
        ("WL400-SNMPGEN-MIB", "snmpGenWriteCommunityString"),
        ("WL400-SNMPGEN-MIB", "snmpGenTrapDstMaxTableLength"),
        ("WL400-SNMPGEN-MIB", "snmpGenTrapDstIpAddress"),
        ("WL400-SNMPGEN-MIB", "snmpGenTrapDstType"),
        ("WL400-SNMPGEN-MIB", "snmpGenTrapDstRowStatus"),
        ("WL400-SNMPGEN-MIB", "snmpGenLockStatus"),
        ("WL400-SNMPGEN-MIB", "snmpGenChangeIPAddress"),
        ("WL400-SNMPGEN-MIB", "snmpGenUseDHCP"))
)
if mibBuilder.loadTexts:
    snmpGenBasicGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

snmpGenBasicCompl = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 232, 144, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    snmpGenBasicCompl.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WL400-SNMPGEN-MIB",
    **{"snmpGenMIBModule": snmpGenMIBModule,
       "snmpGenMIB": snmpGenMIB,
       "snmpGenConf": snmpGenConf,
       "snmpGenGroups": snmpGenGroups,
       "snmpGenBasicGroup": snmpGenBasicGroup,
       "snmpGenCompl": snmpGenCompl,
       "snmpGenBasicCompl": snmpGenBasicCompl,
       "snmpGenObjs": snmpGenObjs,
       "snmpGenReadCommunityString": snmpGenReadCommunityString,
       "snmpGenWriteCommunityString": snmpGenWriteCommunityString,
       "snmpGenTrapDstMaxTableLength": snmpGenTrapDstMaxTableLength,
       "snmpGenTrapDstTable": snmpGenTrapDstTable,
       "snmpGenTrapDstEntry": snmpGenTrapDstEntry,
       "snmpGenTrapDstIndex": snmpGenTrapDstIndex,
       "snmpGenTrapDstIpAddress": snmpGenTrapDstIpAddress,
       "snmpGenTrapDstType": snmpGenTrapDstType,
       "snmpGenTrapDstRowStatus": snmpGenTrapDstRowStatus,
       "snmpGenLockStatus": snmpGenLockStatus,
       "snmpGenChangeIPAddress": snmpGenChangeIPAddress,
       "snmpGenUseDHCP": snmpGenUseDHCP}
)
