# SNMP MIB module (A3COM0073IGMP-SNOOP) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM0073IGMP-SNOOP
# Produced by pysmi-1.5.4 at Mon Oct 14 20:31:01 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class TruthValue(Integer32):
    """Custom type TruthValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_A3Com_ObjectIdentity = ObjectIdentity
a3Com = _A3Com_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43)
)
_Generic_ObjectIdentity = ObjectIdentity
generic = _Generic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10)
)
_IgmpMib_ObjectIdentity = ObjectIdentity
igmpMib = _IgmpMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 37)
)
_IgmpSnoop_ObjectIdentity = ObjectIdentity
igmpSnoop = _IgmpSnoop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 37, 1)
)


class _IgmpSnoopEnabled_Type(TruthValue):
    """Custom type igmpSnoopEnabled based on TruthValue"""


_IgmpSnoopEnabled_Object = MibScalar
igmpSnoopEnabled = _IgmpSnoopEnabled_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 37, 1, 1),
    _IgmpSnoopEnabled_Type()
)
igmpSnoopEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopEnabled.setStatus("mandatory")


class _IgmpSnoopRobustness_Type(Integer32):
    """Custom type igmpSnoopRobustness based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_IgmpSnoopRobustness_Type.__name__ = "Integer32"
_IgmpSnoopRobustness_Object = MibScalar
igmpSnoopRobustness = _IgmpSnoopRobustness_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 37, 1, 2),
    _IgmpSnoopRobustness_Type()
)
igmpSnoopRobustness.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopRobustness.setStatus("mandatory")


class _IgmpSnoopLeaveEnabled_Type(TruthValue):
    """Custom type igmpSnoopLeaveEnabled based on TruthValue"""


_IgmpSnoopLeaveEnabled_Object = MibScalar
igmpSnoopLeaveEnabled = _IgmpSnoopLeaveEnabled_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 37, 1, 3),
    _IgmpSnoopLeaveEnabled_Type()
)
igmpSnoopLeaveEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopLeaveEnabled.setStatus("mandatory")


class _IgmpSnoopQueryTimeout_Type(Integer32):
    """Custom type igmpSnoopQueryTimeout based on Integer32"""
    defaultValue = 125

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 125),
    )


_IgmpSnoopQueryTimeout_Type.__name__ = "Integer32"
_IgmpSnoopQueryTimeout_Object = MibScalar
igmpSnoopQueryTimeout = _IgmpSnoopQueryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 37, 1, 4),
    _IgmpSnoopQueryTimeout_Type()
)
igmpSnoopQueryTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopQueryTimeout.setStatus("mandatory")


class _IgmpSnoopQueryMaxResponseTime_Type(Integer32):
    """Custom type igmpSnoopQueryMaxResponseTime based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 100),
    )


_IgmpSnoopQueryMaxResponseTime_Type.__name__ = "Integer32"
_IgmpSnoopQueryMaxResponseTime_Object = MibScalar
igmpSnoopQueryMaxResponseTime = _IgmpSnoopQueryMaxResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 37, 1, 5),
    _IgmpSnoopQueryMaxResponseTime_Type()
)
igmpSnoopQueryMaxResponseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopQueryMaxResponseTime.setStatus("mandatory")


class _IgmpSnoopLastMemberQueryTimeout_Type(Integer32):
    """Custom type igmpSnoopLastMemberQueryTimeout based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_IgmpSnoopLastMemberQueryTimeout_Type.__name__ = "Integer32"
_IgmpSnoopLastMemberQueryTimeout_Object = MibScalar
igmpSnoopLastMemberQueryTimeout = _IgmpSnoopLastMemberQueryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 37, 1, 6),
    _IgmpSnoopLastMemberQueryTimeout_Type()
)
igmpSnoopLastMemberQueryTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopLastMemberQueryTimeout.setStatus("mandatory")


class _IgmpSnoopLastMemberQueryCount_Type(Integer32):
    """Custom type igmpSnoopLastMemberQueryCount based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 5),
    )


_IgmpSnoopLastMemberQueryCount_Type.__name__ = "Integer32"
_IgmpSnoopLastMemberQueryCount_Object = MibScalar
igmpSnoopLastMemberQueryCount = _IgmpSnoopLastMemberQueryCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 37, 1, 7),
    _IgmpSnoopLastMemberQueryCount_Type()
)
igmpSnoopLastMemberQueryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopLastMemberQueryCount.setStatus("mandatory")


class _IgmpSnoopRouterPortRefreshTimeout_Type(Integer32):
    """Custom type igmpSnoopRouterPortRefreshTimeout based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(70, 100),
    )


_IgmpSnoopRouterPortRefreshTimeout_Type.__name__ = "Integer32"
_IgmpSnoopRouterPortRefreshTimeout_Object = MibScalar
igmpSnoopRouterPortRefreshTimeout = _IgmpSnoopRouterPortRefreshTimeout_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 37, 1, 8),
    _IgmpSnoopRouterPortRefreshTimeout_Type()
)
igmpSnoopRouterPortRefreshTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopRouterPortRefreshTimeout.setStatus("mandatory")
_IgmpSnoopVLANTable_Object = MibTable
igmpSnoopVLANTable = _IgmpSnoopVLANTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 37, 1, 9)
)
if mibBuilder.loadTexts:
    igmpSnoopVLANTable.setStatus("mandatory")
_IgmpSnoopVLANEntry_Object = MibTableRow
igmpSnoopVLANEntry = _IgmpSnoopVLANEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 37, 1, 9, 1)
)
igmpSnoopVLANEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    igmpSnoopVLANEntry.setStatus("mandatory")
_IgmpSnoopVLANJoins_Type = Counter32
_IgmpSnoopVLANJoins_Object = MibTableColumn
igmpSnoopVLANJoins = _IgmpSnoopVLANJoins_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 37, 1, 9, 1, 1),
    _IgmpSnoopVLANJoins_Type()
)
igmpSnoopVLANJoins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopVLANJoins.setStatus("mandatory")
_IgmpSnoopVLANLeaves_Type = Counter32
_IgmpSnoopVLANLeaves_Object = MibTableColumn
igmpSnoopVLANLeaves = _IgmpSnoopVLANLeaves_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 37, 1, 9, 1, 2),
    _IgmpSnoopVLANLeaves_Type()
)
igmpSnoopVLANLeaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopVLANLeaves.setStatus("mandatory")


class _IgmpQueryEnabled_Type(TruthValue):
    """Custom type igmpQueryEnabled based on TruthValue"""


_IgmpQueryEnabled_Object = MibScalar
igmpQueryEnabled = _IgmpQueryEnabled_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 37, 1, 10),
    _IgmpQueryEnabled_Type()
)
igmpQueryEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpQueryEnabled.setStatus("mandatory")
_IgmpQueryIpAddress_Type = IpAddress
_IgmpQueryIpAddress_Object = MibScalar
igmpQueryIpAddress = _IgmpQueryIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 37, 1, 11),
    _IgmpQueryIpAddress_Type()
)
igmpQueryIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpQueryIpAddress.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM0073IGMP-SNOOP",
    **{"TruthValue": TruthValue,
       "a3Com": a3Com,
       "generic": generic,
       "igmpMib": igmpMib,
       "igmpSnoop": igmpSnoop,
       "igmpSnoopEnabled": igmpSnoopEnabled,
       "igmpSnoopRobustness": igmpSnoopRobustness,
       "igmpSnoopLeaveEnabled": igmpSnoopLeaveEnabled,
       "igmpSnoopQueryTimeout": igmpSnoopQueryTimeout,
       "igmpSnoopQueryMaxResponseTime": igmpSnoopQueryMaxResponseTime,
       "igmpSnoopLastMemberQueryTimeout": igmpSnoopLastMemberQueryTimeout,
       "igmpSnoopLastMemberQueryCount": igmpSnoopLastMemberQueryCount,
       "igmpSnoopRouterPortRefreshTimeout": igmpSnoopRouterPortRefreshTimeout,
       "igmpSnoopVLANTable": igmpSnoopVLANTable,
       "igmpSnoopVLANEntry": igmpSnoopVLANEntry,
       "igmpSnoopVLANJoins": igmpSnoopVLANJoins,
       "igmpSnoopVLANLeaves": igmpSnoopVLANLeaves,
       "igmpQueryEnabled": igmpQueryEnabled,
       "igmpQueryIpAddress": igmpQueryIpAddress}
)
