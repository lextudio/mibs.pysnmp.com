# SNMP MIB module (ENTERASYS-IETF-BRIDGE-MIB-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ENTERASYS-IETF-BRIDGE-MIB-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:38:57 2024
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

(dot1dBaseBridgeAddress,
 dot1dBasePort,
 dot1dBasePortEntry,
 dot1dBasePortIfIndex,
 dot1dStpDesignatedRoot,
 dot1dStpPort,
 dot1dStpPortEntry) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dBaseBridgeAddress",
    "dot1dBasePort",
    "dot1dBasePortEntry",
    "dot1dBasePortIfIndex",
    "dot1dStpDesignatedRoot",
    "dot1dStpPort",
    "dot1dStpPortEntry")

(etsysModules,) = mibBuilder.importSymbols(
    "ENTERASYS-MIB-NAMES",
    "etsysModules")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(dot1qTpFdbPort,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "dot1qTpFdbPort")

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

etsysIetfBridgeMibExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 31)
)
etsysIetfBridgeMibExtMIB.setRevisions(
        ("2007-07-31 18:19",
         "2007-03-21 21:02",
         "2006-11-09 16:37",
         "2006-10-04 19:51",
         "2004-11-04 14:47",
         "2004-05-28 15:08",
         "2004-04-08 20:04",
         "2004-03-04 19:39",
         "2004-03-01 22:29",
         "2003-11-14 18:31",
         "2003-06-19 19:36",
         "2002-12-13 21:20")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EtsysIetfBridgeMibExt_ObjectIdentity = ObjectIdentity
etsysIetfBridgeMibExt = _EtsysIetfBridgeMibExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 31, 1)
)
_EtsysIetfBridgeDot1Notifications_ObjectIdentity = ObjectIdentity
etsysIetfBridgeDot1Notifications = _EtsysIetfBridgeDot1Notifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 31, 1, 0)
)
_EtsysIetfBridgeDot1dStp_ObjectIdentity = ObjectIdentity
etsysIetfBridgeDot1dStp = _EtsysIetfBridgeDot1dStp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 31, 1, 1)
)
_EtsysIetfBridgeDot1dStpPortTable_Object = MibTable
etsysIetfBridgeDot1dStpPortTable = _EtsysIetfBridgeDot1dStpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 31, 1, 1, 1)
)
if mibBuilder.loadTexts:
    etsysIetfBridgeDot1dStpPortTable.setStatus("current")
_EtsysIetfBridgeDot1dStpPortEntry_Object = MibTableRow
etsysIetfBridgeDot1dStpPortEntry = _EtsysIetfBridgeDot1dStpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 31, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    etsysIetfBridgeDot1dStpPortEntry.setStatus("current")


class _EtsysIetfBridgeDot1dStpPortStpEnable_Type(EnabledStatus):
    """Custom type etsysIetfBridgeDot1dStpPortStpEnable based on EnabledStatus"""


_EtsysIetfBridgeDot1dStpPortStpEnable_Object = MibTableColumn
etsysIetfBridgeDot1dStpPortStpEnable = _EtsysIetfBridgeDot1dStpPortStpEnable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 31, 1, 1, 1, 1, 1),
    _EtsysIetfBridgeDot1dStpPortStpEnable_Type()
)
etsysIetfBridgeDot1dStpPortStpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysIetfBridgeDot1dStpPortStpEnable.setStatus("current")


class _EtsysIetfBridgeDot1dStpPortSpanGuardBlocking_Type(TruthValue):
    """Custom type etsysIetfBridgeDot1dStpPortSpanGuardBlocking based on TruthValue"""


_EtsysIetfBridgeDot1dStpPortSpanGuardBlocking_Object = MibTableColumn
etsysIetfBridgeDot1dStpPortSpanGuardBlocking = _EtsysIetfBridgeDot1dStpPortSpanGuardBlocking_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 31, 1, 1, 1, 1, 2),
    _EtsysIetfBridgeDot1dStpPortSpanGuardBlocking_Type()
)
etsysIetfBridgeDot1dStpPortSpanGuardBlocking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysIetfBridgeDot1dStpPortSpanGuardBlocking.setStatus("current")


class _EtsysIetfBridgeDot1dStpPortCistRoleValue_Type(Integer32):
    """Custom type etsysIetfBridgeDot1dStpPortCistRoleValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("alternate", 4),
          ("backUp", 5),
          ("designated", 3),
          ("disabled", 1),
          ("root", 2))
    )


_EtsysIetfBridgeDot1dStpPortCistRoleValue_Type.__name__ = "Integer32"
_EtsysIetfBridgeDot1dStpPortCistRoleValue_Object = MibTableColumn
etsysIetfBridgeDot1dStpPortCistRoleValue = _EtsysIetfBridgeDot1dStpPortCistRoleValue_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 31, 1, 1, 1, 1, 3),
    _EtsysIetfBridgeDot1dStpPortCistRoleValue_Type()
)
etsysIetfBridgeDot1dStpPortCistRoleValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysIetfBridgeDot1dStpPortCistRoleValue.setStatus("current")


class _EtsysIetfBridgeDot1dStpPortCistNonForwardingReason_Type(Integer32):
    """Custom type etsysIetfBridgeDot1dStpPortCistNonForwardingReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("disputed", 2),
          ("loopProtectAdvisory", 5),
          ("loopProtectEvent", 4),
          ("loopbackDetected", 6),
          ("none", 1),
          ("spanGuardLocked", 3))
    )


_EtsysIetfBridgeDot1dStpPortCistNonForwardingReason_Type.__name__ = "Integer32"
_EtsysIetfBridgeDot1dStpPortCistNonForwardingReason_Object = MibTableColumn
etsysIetfBridgeDot1dStpPortCistNonForwardingReason = _EtsysIetfBridgeDot1dStpPortCistNonForwardingReason_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 31, 1, 1, 1, 1, 4),
    _EtsysIetfBridgeDot1dStpPortCistNonForwardingReason_Type()
)
etsysIetfBridgeDot1dStpPortCistNonForwardingReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysIetfBridgeDot1dStpPortCistNonForwardingReason.setStatus("current")


class _EtsysIetfBridgeDot1dStpTopChangeTrapEnable_Type(Integer32):
    """Custom type etsysIetfBridgeDot1dStpTopChangeTrapEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("edgePortDisabled", 3),
          ("enabled", 1))
    )


_EtsysIetfBridgeDot1dStpTopChangeTrapEnable_Type.__name__ = "Integer32"
_EtsysIetfBridgeDot1dStpTopChangeTrapEnable_Object = MibScalar
etsysIetfBridgeDot1dStpTopChangeTrapEnable = _EtsysIetfBridgeDot1dStpTopChangeTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 31, 1, 1, 2),
    _EtsysIetfBridgeDot1dStpTopChangeTrapEnable_Type()
)
etsysIetfBridgeDot1dStpTopChangeTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysIetfBridgeDot1dStpTopChangeTrapEnable.setStatus("current")


class _EtsysIetfBridgeDot1dStpNewRootTrapEnable_Type(EnabledStatus):
    """Custom type etsysIetfBridgeDot1dStpNewRootTrapEnable based on EnabledStatus"""


_EtsysIetfBridgeDot1dStpNewRootTrapEnable_Object = MibScalar
etsysIetfBridgeDot1dStpNewRootTrapEnable = _EtsysIetfBridgeDot1dStpNewRootTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 31, 1, 1, 3),
    _EtsysIetfBridgeDot1dStpNewRootTrapEnable_Type()
)
etsysIetfBridgeDot1dStpNewRootTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysIetfBridgeDot1dStpNewRootTrapEnable.setStatus("current")


class _EtsysIetfBridgeDot1dStpBridgePriorityDefault_Type(Integer32):
    """Custom type etsysIetfBridgeDot1dStpBridgePriorityDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stp8021d1998", 1),
          ("stp8021t2001", 2))
    )


_EtsysIetfBridgeDot1dStpBridgePriorityDefault_Type.__name__ = "Integer32"
_EtsysIetfBridgeDot1dStpBridgePriorityDefault_Object = MibScalar
etsysIetfBridgeDot1dStpBridgePriorityDefault = _EtsysIetfBridgeDot1dStpBridgePriorityDefault_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 31, 1, 1, 4),
    _EtsysIetfBridgeDot1dStpBridgePriorityDefault_Type()
)
etsysIetfBridgeDot1dStpBridgePriorityDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysIetfBridgeDot1dStpBridgePriorityDefault.setStatus("current")
_EtsysIetfBridgeDot1dBase_ObjectIdentity = ObjectIdentity
etsysIetfBridgeDot1dBase = _EtsysIetfBridgeDot1dBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 31, 1, 2)
)
_EtsysIetfBridgeDot1dBasePortTable_Object = MibTable
etsysIetfBridgeDot1dBasePortTable = _EtsysIetfBridgeDot1dBasePortTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 31, 1, 2, 1)
)
if mibBuilder.loadTexts:
    etsysIetfBridgeDot1dBasePortTable.setStatus("current")
_EtsysIetfBridgeDot1dBasePortEntry_Object = MibTableRow
etsysIetfBridgeDot1dBasePortEntry = _EtsysIetfBridgeDot1dBasePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 31, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    etsysIetfBridgeDot1dBasePortEntry.setStatus("current")


class _EtsysIetfBridgeDot1dBasePortNewLearnedAddrTrap_Type(EnabledStatus):
    """Custom type etsysIetfBridgeDot1dBasePortNewLearnedAddrTrap based on EnabledStatus"""


_EtsysIetfBridgeDot1dBasePortNewLearnedAddrTrap_Object = MibTableColumn
etsysIetfBridgeDot1dBasePortNewLearnedAddrTrap = _EtsysIetfBridgeDot1dBasePortNewLearnedAddrTrap_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 31, 1, 2, 1, 1, 1),
    _EtsysIetfBridgeDot1dBasePortNewLearnedAddrTrap_Type()
)
etsysIetfBridgeDot1dBasePortNewLearnedAddrTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysIetfBridgeDot1dBasePortNewLearnedAddrTrap.setStatus("current")


class _EtsysIetfBridgeDot1dBasePortMovedAddrTrap_Type(EnabledStatus):
    """Custom type etsysIetfBridgeDot1dBasePortMovedAddrTrap based on EnabledStatus"""


_EtsysIetfBridgeDot1dBasePortMovedAddrTrap_Object = MibTableColumn
etsysIetfBridgeDot1dBasePortMovedAddrTrap = _EtsysIetfBridgeDot1dBasePortMovedAddrTrap_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 31, 1, 2, 1, 1, 2),
    _EtsysIetfBridgeDot1dBasePortMovedAddrTrap_Type()
)
etsysIetfBridgeDot1dBasePortMovedAddrTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysIetfBridgeDot1dBasePortMovedAddrTrap.setStatus("current")
_EtsysIetfBridgeDot1qBase_ObjectIdentity = ObjectIdentity
etsysIetfBridgeDot1qBase = _EtsysIetfBridgeDot1qBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 31, 1, 3)
)


class _EtsysIetfBridgeDot1qNewLearnedAddrTrapEnable_Type(EnabledStatus):
    """Custom type etsysIetfBridgeDot1qNewLearnedAddrTrapEnable based on EnabledStatus"""


_EtsysIetfBridgeDot1qNewLearnedAddrTrapEnable_Object = MibScalar
etsysIetfBridgeDot1qNewLearnedAddrTrapEnable = _EtsysIetfBridgeDot1qNewLearnedAddrTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 31, 1, 3, 1),
    _EtsysIetfBridgeDot1qNewLearnedAddrTrapEnable_Type()
)
etsysIetfBridgeDot1qNewLearnedAddrTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysIetfBridgeDot1qNewLearnedAddrTrapEnable.setStatus("current")


class _EtsysIetfBridgeDot1qMovedAddrTrapEnable_Type(EnabledStatus):
    """Custom type etsysIetfBridgeDot1qMovedAddrTrapEnable based on EnabledStatus"""


_EtsysIetfBridgeDot1qMovedAddrTrapEnable_Object = MibScalar
etsysIetfBridgeDot1qMovedAddrTrapEnable = _EtsysIetfBridgeDot1qMovedAddrTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 31, 1, 3, 2),
    _EtsysIetfBridgeDot1qMovedAddrTrapEnable_Type()
)
etsysIetfBridgeDot1qMovedAddrTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysIetfBridgeDot1qMovedAddrTrapEnable.setStatus("current")


class _EtsysIetfBridgeDot1qStaticUcastAsMcast_Type(EnabledStatus):
    """Custom type etsysIetfBridgeDot1qStaticUcastAsMcast based on EnabledStatus"""


_EtsysIetfBridgeDot1qStaticUcastAsMcast_Object = MibScalar
etsysIetfBridgeDot1qStaticUcastAsMcast = _EtsysIetfBridgeDot1qStaticUcastAsMcast_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 31, 1, 3, 3),
    _EtsysIetfBridgeDot1qStaticUcastAsMcast_Type()
)
etsysIetfBridgeDot1qStaticUcastAsMcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysIetfBridgeDot1qStaticUcastAsMcast.setStatus("current")
_EtsysIetfBridgeDot1dSpanGuard_ObjectIdentity = ObjectIdentity
etsysIetfBridgeDot1dSpanGuard = _EtsysIetfBridgeDot1dSpanGuard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 31, 1, 4)
)


class _EtsysIetfBridgeDot1dStpSpanGuardEnable_Type(EnabledStatus):
    """Custom type etsysIetfBridgeDot1dStpSpanGuardEnable based on EnabledStatus"""


_EtsysIetfBridgeDot1dStpSpanGuardEnable_Object = MibScalar
etsysIetfBridgeDot1dStpSpanGuardEnable = _EtsysIetfBridgeDot1dStpSpanGuardEnable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 31, 1, 4, 1),
    _EtsysIetfBridgeDot1dStpSpanGuardEnable_Type()
)
etsysIetfBridgeDot1dStpSpanGuardEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysIetfBridgeDot1dStpSpanGuardEnable.setStatus("current")


class _EtsysIetfBridgeDot1dStpSpanGuardTrapEnable_Type(EnabledStatus):
    """Custom type etsysIetfBridgeDot1dStpSpanGuardTrapEnable based on EnabledStatus"""


_EtsysIetfBridgeDot1dStpSpanGuardTrapEnable_Object = MibScalar
etsysIetfBridgeDot1dStpSpanGuardTrapEnable = _EtsysIetfBridgeDot1dStpSpanGuardTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 31, 1, 4, 2),
    _EtsysIetfBridgeDot1dStpSpanGuardTrapEnable_Type()
)
etsysIetfBridgeDot1dStpSpanGuardTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysIetfBridgeDot1dStpSpanGuardTrapEnable.setStatus("current")


class _EtsysIetfBridgeDot1dStpSpanGuardBlockTime_Type(Integer32):
    """Custom type etsysIetfBridgeDot1dStpSpanGuardBlockTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 65535),
    )


_EtsysIetfBridgeDot1dStpSpanGuardBlockTime_Type.__name__ = "Integer32"
_EtsysIetfBridgeDot1dStpSpanGuardBlockTime_Object = MibScalar
etsysIetfBridgeDot1dStpSpanGuardBlockTime = _EtsysIetfBridgeDot1dStpSpanGuardBlockTime_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 31, 1, 4, 3),
    _EtsysIetfBridgeDot1dStpSpanGuardBlockTime_Type()
)
etsysIetfBridgeDot1dStpSpanGuardBlockTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysIetfBridgeDot1dStpSpanGuardBlockTime.setStatus("current")
if mibBuilder.loadTexts:
    etsysIetfBridgeDot1dStpSpanGuardBlockTime.setUnits("seconds")
_EtsysIetfBridgeDot1dBackupRoot_ObjectIdentity = ObjectIdentity
etsysIetfBridgeDot1dBackupRoot = _EtsysIetfBridgeDot1dBackupRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 31, 1, 5)
)


class _EtsysIetfBridgeDot1dStpBackupRootEnable_Type(EnabledStatus):
    """Custom type etsysIetfBridgeDot1dStpBackupRootEnable based on EnabledStatus"""


_EtsysIetfBridgeDot1dStpBackupRootEnable_Object = MibScalar
etsysIetfBridgeDot1dStpBackupRootEnable = _EtsysIetfBridgeDot1dStpBackupRootEnable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 31, 1, 5, 1),
    _EtsysIetfBridgeDot1dStpBackupRootEnable_Type()
)
etsysIetfBridgeDot1dStpBackupRootEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysIetfBridgeDot1dStpBackupRootEnable.setStatus("current")


class _EtsysIetfBridgeDot1dStpBackupRootTrapEnable_Type(EnabledStatus):
    """Custom type etsysIetfBridgeDot1dStpBackupRootTrapEnable based on EnabledStatus"""


_EtsysIetfBridgeDot1dStpBackupRootTrapEnable_Object = MibScalar
etsysIetfBridgeDot1dStpBackupRootTrapEnable = _EtsysIetfBridgeDot1dStpBackupRootTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 31, 1, 5, 2),
    _EtsysIetfBridgeDot1dStpBackupRootTrapEnable_Type()
)
etsysIetfBridgeDot1dStpBackupRootTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysIetfBridgeDot1dStpBackupRootTrapEnable.setStatus("current")
_EtsysIetfBridgeDot1dLoopProtect_ObjectIdentity = ObjectIdentity
etsysIetfBridgeDot1dLoopProtect = _EtsysIetfBridgeDot1dLoopProtect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 31, 1, 6)
)
_EtsysIetfBridgeDot1dStpLoopProtectPortTable_Object = MibTable
etsysIetfBridgeDot1dStpLoopProtectPortTable = _EtsysIetfBridgeDot1dStpLoopProtectPortTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 31, 1, 6, 1)
)
if mibBuilder.loadTexts:
    etsysIetfBridgeDot1dStpLoopProtectPortTable.setStatus("current")
_EtsysIetfBridgeDot1dStpLoopProtectPortEntry_Object = MibTableRow
etsysIetfBridgeDot1dStpLoopProtectPortEntry = _EtsysIetfBridgeDot1dStpLoopProtectPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 31, 1, 6, 1, 1)
)
if mibBuilder.loadTexts:
    etsysIetfBridgeDot1dStpLoopProtectPortEntry.setStatus("current")


class _EtsysIetfBridgeDot1dStpLoopProtectPortCistEnable_Type(EnabledStatus):
    """Custom type etsysIetfBridgeDot1dStpLoopProtectPortCistEnable based on EnabledStatus"""


_EtsysIetfBridgeDot1dStpLoopProtectPortCistEnable_Object = MibTableColumn
etsysIetfBridgeDot1dStpLoopProtectPortCistEnable = _EtsysIetfBridgeDot1dStpLoopProtectPortCistEnable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 31, 1, 6, 1, 1, 1),
    _EtsysIetfBridgeDot1dStpLoopProtectPortCistEnable_Type()
)
etsysIetfBridgeDot1dStpLoopProtectPortCistEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysIetfBridgeDot1dStpLoopProtectPortCistEnable.setStatus("current")


class _EtsysIetfBridgeDot1dStpLoopProtectPortCistBlocking_Type(TruthValue):
    """Custom type etsysIetfBridgeDot1dStpLoopProtectPortCistBlocking based on TruthValue"""


_EtsysIetfBridgeDot1dStpLoopProtectPortCistBlocking_Object = MibTableColumn
etsysIetfBridgeDot1dStpLoopProtectPortCistBlocking = _EtsysIetfBridgeDot1dStpLoopProtectPortCistBlocking_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 31, 1, 6, 1, 1, 2),
    _EtsysIetfBridgeDot1dStpLoopProtectPortCistBlocking_Type()
)
etsysIetfBridgeDot1dStpLoopProtectPortCistBlocking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysIetfBridgeDot1dStpLoopProtectPortCistBlocking.setStatus("current")


class _EtsysIetfBridgeDot1dStpLoopProtectPortPartnerCapable_Type(TruthValue):
    """Custom type etsysIetfBridgeDot1dStpLoopProtectPortPartnerCapable based on TruthValue"""


_EtsysIetfBridgeDot1dStpLoopProtectPortPartnerCapable_Object = MibTableColumn
etsysIetfBridgeDot1dStpLoopProtectPortPartnerCapable = _EtsysIetfBridgeDot1dStpLoopProtectPortPartnerCapable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 31, 1, 6, 1, 1, 3),
    _EtsysIetfBridgeDot1dStpLoopProtectPortPartnerCapable_Type()
)
etsysIetfBridgeDot1dStpLoopProtectPortPartnerCapable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysIetfBridgeDot1dStpLoopProtectPortPartnerCapable.setStatus("current")


class _EtsysIetfBridgeDot1dStpLoopProtectEventThreshold_Type(Unsigned32):
    """Custom type etsysIetfBridgeDot1dStpLoopProtectEventThreshold based on Unsigned32"""
    defaultValue = 3


_EtsysIetfBridgeDot1dStpLoopProtectEventThreshold_Object = MibScalar
etsysIetfBridgeDot1dStpLoopProtectEventThreshold = _EtsysIetfBridgeDot1dStpLoopProtectEventThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 31, 1, 6, 2),
    _EtsysIetfBridgeDot1dStpLoopProtectEventThreshold_Type()
)
etsysIetfBridgeDot1dStpLoopProtectEventThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysIetfBridgeDot1dStpLoopProtectEventThreshold.setStatus("current")


class _EtsysIetfBridgeDot1dStpLoopProtectEventWindow_Type(Unsigned32):
    """Custom type etsysIetfBridgeDot1dStpLoopProtectEventWindow based on Unsigned32"""
    defaultValue = 180


_EtsysIetfBridgeDot1dStpLoopProtectEventWindow_Object = MibScalar
etsysIetfBridgeDot1dStpLoopProtectEventWindow = _EtsysIetfBridgeDot1dStpLoopProtectEventWindow_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 31, 1, 6, 3),
    _EtsysIetfBridgeDot1dStpLoopProtectEventWindow_Type()
)
etsysIetfBridgeDot1dStpLoopProtectEventWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysIetfBridgeDot1dStpLoopProtectEventWindow.setStatus("current")


class _EtsysIetfBridgeDot1dStpLoopProtectEventTrapEnable_Type(EnabledStatus):
    """Custom type etsysIetfBridgeDot1dStpLoopProtectEventTrapEnable based on EnabledStatus"""


_EtsysIetfBridgeDot1dStpLoopProtectEventTrapEnable_Object = MibScalar
etsysIetfBridgeDot1dStpLoopProtectEventTrapEnable = _EtsysIetfBridgeDot1dStpLoopProtectEventTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 31, 1, 6, 4),
    _EtsysIetfBridgeDot1dStpLoopProtectEventTrapEnable_Type()
)
etsysIetfBridgeDot1dStpLoopProtectEventTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysIetfBridgeDot1dStpLoopProtectEventTrapEnable.setStatus("current")
_EtsysIetfBridgeConformance_ObjectIdentity = ObjectIdentity
etsysIetfBridgeConformance = _EtsysIetfBridgeConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 31, 2)
)
_EtsysIetfBridgeGroups_ObjectIdentity = ObjectIdentity
etsysIetfBridgeGroups = _EtsysIetfBridgeGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 31, 2, 1)
)
_EtsysIetfBridgeCompliances_ObjectIdentity = ObjectIdentity
etsysIetfBridgeCompliances = _EtsysIetfBridgeCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 31, 2, 2)
)
dot1dStpPortEntry.registerAugmentions(
    ("ENTERASYS-IETF-BRIDGE-MIB-EXT-MIB",
     "etsysIetfBridgeDot1dStpPortEntry")
)
etsysIetfBridgeDot1dStpPortEntry.setIndexNames(*dot1dStpPortEntry.getIndexNames())
dot1dBasePortEntry.registerAugmentions(
    ("ENTERASYS-IETF-BRIDGE-MIB-EXT-MIB",
     "etsysIetfBridgeDot1dBasePortEntry")
)
etsysIetfBridgeDot1dBasePortEntry.setIndexNames(*dot1dBasePortEntry.getIndexNames())
dot1dStpPortEntry.registerAugmentions(
    ("ENTERASYS-IETF-BRIDGE-MIB-EXT-MIB",
     "etsysIetfBridgeDot1dStpLoopProtectPortEntry")
)
etsysIetfBridgeDot1dStpLoopProtectPortEntry.setIndexNames(*dot1dStpPortEntry.getIndexNames())

# Managed Objects groups

etsysIetfBridgeStpPort = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 31, 2, 1, 1)
)
etsysIetfBridgeStpPort.setObjects(
    ("ENTERASYS-IETF-BRIDGE-MIB-EXT-MIB", "etsysIetfBridgeDot1dStpPortStpEnable")
)
if mibBuilder.loadTexts:
    etsysIetfBridgeStpPort.setStatus("current")

etsysIetfBridgeStpTrap = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 31, 2, 1, 2)
)
etsysIetfBridgeStpTrap.setObjects(
      *(("ENTERASYS-IETF-BRIDGE-MIB-EXT-MIB", "etsysIetfBridgeDot1dStpTopChangeTrapEnable"),
        ("ENTERASYS-IETF-BRIDGE-MIB-EXT-MIB", "etsysIetfBridgeDot1dStpNewRootTrapEnable"))
)
if mibBuilder.loadTexts:
    etsysIetfBridgeStpTrap.setStatus("current")

etsysIetfBridgeBase = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 31, 2, 1, 3)
)
etsysIetfBridgeBase.setObjects(
      *(("ENTERASYS-IETF-BRIDGE-MIB-EXT-MIB", "etsysIetfBridgeDot1qNewLearnedAddrTrapEnable"),
        ("ENTERASYS-IETF-BRIDGE-MIB-EXT-MIB", "etsysIetfBridgeDot1dBasePortNewLearnedAddrTrap"))
)
if mibBuilder.loadTexts:
    etsysIetfBridgeBase.setStatus("current")

etsysIetfBridgeDot1dStpBridgePriority = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 31, 2, 1, 5)
)
etsysIetfBridgeDot1dStpBridgePriority.setObjects(
    ("ENTERASYS-IETF-BRIDGE-MIB-EXT-MIB", "etsysIetfBridgeDot1dStpBridgePriorityDefault")
)
if mibBuilder.loadTexts:
    etsysIetfBridgeDot1dStpBridgePriority.setStatus("current")

etsysIetfBridgeSpanGuard = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 31, 2, 1, 6)
)
etsysIetfBridgeSpanGuard.setObjects(
      *(("ENTERASYS-IETF-BRIDGE-MIB-EXT-MIB", "etsysIetfBridgeDot1dStpSpanGuardEnable"),
        ("ENTERASYS-IETF-BRIDGE-MIB-EXT-MIB", "etsysIetfBridgeDot1dStpSpanGuardBlockTime"),
        ("ENTERASYS-IETF-BRIDGE-MIB-EXT-MIB", "etsysIetfBridgeDot1dStpSpanGuardTrapEnable"),
        ("ENTERASYS-IETF-BRIDGE-MIB-EXT-MIB", "etsysIetfBridgeDot1dStpPortSpanGuardBlocking"))
)
if mibBuilder.loadTexts:
    etsysIetfBridgeSpanGuard.setStatus("current")

etsysIetfBridgeBackupRoot = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 31, 2, 1, 8)
)
etsysIetfBridgeBackupRoot.setObjects(
      *(("ENTERASYS-IETF-BRIDGE-MIB-EXT-MIB", "etsysIetfBridgeDot1dStpBackupRootEnable"),
        ("ENTERASYS-IETF-BRIDGE-MIB-EXT-MIB", "etsysIetfBridgeDot1dStpBackupRootTrapEnable"))
)
if mibBuilder.loadTexts:
    etsysIetfBridgeBackupRoot.setStatus("current")

etsysIetfBridgePortCistRoleValue = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 31, 2, 1, 10)
)
etsysIetfBridgePortCistRoleValue.setObjects(
    ("ENTERASYS-IETF-BRIDGE-MIB-EXT-MIB", "etsysIetfBridgeDot1dStpPortCistRoleValue")
)
if mibBuilder.loadTexts:
    etsysIetfBridgePortCistRoleValue.setStatus("current")

etsysIetfBridgeMovedAddr = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 31, 2, 1, 11)
)
etsysIetfBridgeMovedAddr.setObjects(
      *(("ENTERASYS-IETF-BRIDGE-MIB-EXT-MIB", "etsysIetfBridgeDot1qMovedAddrTrapEnable"),
        ("ENTERASYS-IETF-BRIDGE-MIB-EXT-MIB", "etsysIetfBridgeDot1dBasePortMovedAddrTrap"))
)
if mibBuilder.loadTexts:
    etsysIetfBridgeMovedAddr.setStatus("current")

etsysIetfBridgeLoopProtect = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 31, 2, 1, 13)
)
etsysIetfBridgeLoopProtect.setObjects(
      *(("ENTERASYS-IETF-BRIDGE-MIB-EXT-MIB", "etsysIetfBridgeDot1dStpLoopProtectPortCistEnable"),
        ("ENTERASYS-IETF-BRIDGE-MIB-EXT-MIB", "etsysIetfBridgeDot1dStpLoopProtectPortCistBlocking"),
        ("ENTERASYS-IETF-BRIDGE-MIB-EXT-MIB", "etsysIetfBridgeDot1dStpLoopProtectPortPartnerCapable"),
        ("ENTERASYS-IETF-BRIDGE-MIB-EXT-MIB", "etsysIetfBridgeDot1dStpLoopProtectEventThreshold"),
        ("ENTERASYS-IETF-BRIDGE-MIB-EXT-MIB", "etsysIetfBridgeDot1dStpLoopProtectEventWindow"),
        ("ENTERASYS-IETF-BRIDGE-MIB-EXT-MIB", "etsysIetfBridgeDot1dStpLoopProtectEventTrapEnable"))
)
if mibBuilder.loadTexts:
    etsysIetfBridgeLoopProtect.setStatus("current")

etsysIetfBridgeStpCistNonForwardingReason = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 31, 2, 1, 15)
)
etsysIetfBridgeStpCistNonForwardingReason.setObjects(
    ("ENTERASYS-IETF-BRIDGE-MIB-EXT-MIB", "etsysIetfBridgeDot1dStpPortCistNonForwardingReason")
)
if mibBuilder.loadTexts:
    etsysIetfBridgeStpCistNonForwardingReason.setStatus("current")

etsysIetfBridgeStaticUcastAsMcast = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 31, 2, 1, 16)
)
etsysIetfBridgeStaticUcastAsMcast.setObjects(
    ("ENTERASYS-IETF-BRIDGE-MIB-EXT-MIB", "etsysIetfBridgeDot1qStaticUcastAsMcast")
)
if mibBuilder.loadTexts:
    etsysIetfBridgeStaticUcastAsMcast.setStatus("current")


# Notification objects

etsysIetfBridgeDot1qFdbNewLearnedAddr = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 31, 1, 0, 1)
)
etsysIetfBridgeDot1qFdbNewLearnedAddr.setObjects(
    ("Q-BRIDGE-MIB", "dot1qTpFdbPort")
)
if mibBuilder.loadTexts:
    etsysIetfBridgeDot1qFdbNewLearnedAddr.setStatus(
        "current"
    )

etsysIetfBridgeDot1dSpanGuardPortBlocked = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 31, 1, 0, 2)
)
etsysIetfBridgeDot1dSpanGuardPortBlocked.setObjects(
      *(("BRIDGE-MIB", "dot1dBasePort"),
        ("BRIDGE-MIB", "dot1dBasePortIfIndex"))
)
if mibBuilder.loadTexts:
    etsysIetfBridgeDot1dSpanGuardPortBlocked.setStatus(
        "current"
    )

etsysIetfBridgeDot1dBackupRootActivation = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 31, 1, 0, 3)
)
etsysIetfBridgeDot1dBackupRootActivation.setObjects(
      *(("BRIDGE-MIB", "dot1dBaseBridgeAddress"),
        ("BRIDGE-MIB", "dot1dStpDesignatedRoot"))
)
if mibBuilder.loadTexts:
    etsysIetfBridgeDot1dBackupRootActivation.setStatus(
        "current"
    )

etsysIetfBridgeDot1qFdbMovedAddr = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 31, 1, 0, 4)
)
etsysIetfBridgeDot1qFdbMovedAddr.setObjects(
    ("Q-BRIDGE-MIB", "dot1qTpFdbPort")
)
if mibBuilder.loadTexts:
    etsysIetfBridgeDot1qFdbMovedAddr.setStatus(
        "current"
    )

etsysIetfBridgeDot1dCistLoopProtectEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 31, 1, 0, 5)
)
etsysIetfBridgeDot1dCistLoopProtectEvent.setObjects(
      *(("BRIDGE-MIB", "dot1dStpPort"),
        ("ENTERASYS-IETF-BRIDGE-MIB-EXT-MIB", "etsysIetfBridgeDot1dStpLoopProtectPortCistBlocking"))
)
if mibBuilder.loadTexts:
    etsysIetfBridgeDot1dCistLoopProtectEvent.setStatus(
        "current"
    )


# Notifications groups

etsysIetfBridgeDot1qFdbNewAddrNotification = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 31, 2, 1, 4)
)
etsysIetfBridgeDot1qFdbNewAddrNotification.setObjects(
    ("ENTERASYS-IETF-BRIDGE-MIB-EXT-MIB", "etsysIetfBridgeDot1qFdbNewLearnedAddr")
)
if mibBuilder.loadTexts:
    etsysIetfBridgeDot1qFdbNewAddrNotification.setStatus(
        "current"
    )

etsysIetfBridgeSpanGuardNotification = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 31, 2, 1, 7)
)
etsysIetfBridgeSpanGuardNotification.setObjects(
    ("ENTERASYS-IETF-BRIDGE-MIB-EXT-MIB", "etsysIetfBridgeDot1dSpanGuardPortBlocked")
)
if mibBuilder.loadTexts:
    etsysIetfBridgeSpanGuardNotification.setStatus(
        "current"
    )

etsysIetfBridgeBackupRootNotification = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 31, 2, 1, 9)
)
etsysIetfBridgeBackupRootNotification.setObjects(
    ("ENTERASYS-IETF-BRIDGE-MIB-EXT-MIB", "etsysIetfBridgeDot1dBackupRootActivation")
)
if mibBuilder.loadTexts:
    etsysIetfBridgeBackupRootNotification.setStatus(
        "current"
    )

etsysIetfBridgeDot1qFdbMovedAddrNotification = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 31, 2, 1, 12)
)
etsysIetfBridgeDot1qFdbMovedAddrNotification.setObjects(
    ("ENTERASYS-IETF-BRIDGE-MIB-EXT-MIB", "etsysIetfBridgeDot1qFdbMovedAddr")
)
if mibBuilder.loadTexts:
    etsysIetfBridgeDot1qFdbMovedAddrNotification.setStatus(
        "current"
    )

etsysIetfBridgeLoopProtectNotification = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 31, 2, 1, 14)
)
etsysIetfBridgeLoopProtectNotification.setObjects(
    ("ENTERASYS-IETF-BRIDGE-MIB-EXT-MIB", "etsysIetfBridgeDot1dCistLoopProtectEvent")
)
if mibBuilder.loadTexts:
    etsysIetfBridgeLoopProtectNotification.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

etsysIetfBridgeCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 31, 2, 2, 1)
)
if mibBuilder.loadTexts:
    etsysIetfBridgeCompliance.setStatus(
        "current"
    )

etsysIetfBridgeStaticUcastAsMcastCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 31, 2, 2, 2)
)
if mibBuilder.loadTexts:
    etsysIetfBridgeStaticUcastAsMcastCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTERASYS-IETF-BRIDGE-MIB-EXT-MIB",
    **{"etsysIetfBridgeMibExtMIB": etsysIetfBridgeMibExtMIB,
       "etsysIetfBridgeMibExt": etsysIetfBridgeMibExt,
       "etsysIetfBridgeDot1Notifications": etsysIetfBridgeDot1Notifications,
       "etsysIetfBridgeDot1qFdbNewLearnedAddr": etsysIetfBridgeDot1qFdbNewLearnedAddr,
       "etsysIetfBridgeDot1dSpanGuardPortBlocked": etsysIetfBridgeDot1dSpanGuardPortBlocked,
       "etsysIetfBridgeDot1dBackupRootActivation": etsysIetfBridgeDot1dBackupRootActivation,
       "etsysIetfBridgeDot1qFdbMovedAddr": etsysIetfBridgeDot1qFdbMovedAddr,
       "etsysIetfBridgeDot1dCistLoopProtectEvent": etsysIetfBridgeDot1dCistLoopProtectEvent,
       "etsysIetfBridgeDot1dStp": etsysIetfBridgeDot1dStp,
       "etsysIetfBridgeDot1dStpPortTable": etsysIetfBridgeDot1dStpPortTable,
       "etsysIetfBridgeDot1dStpPortEntry": etsysIetfBridgeDot1dStpPortEntry,
       "etsysIetfBridgeDot1dStpPortStpEnable": etsysIetfBridgeDot1dStpPortStpEnable,
       "etsysIetfBridgeDot1dStpPortSpanGuardBlocking": etsysIetfBridgeDot1dStpPortSpanGuardBlocking,
       "etsysIetfBridgeDot1dStpPortCistRoleValue": etsysIetfBridgeDot1dStpPortCistRoleValue,
       "etsysIetfBridgeDot1dStpPortCistNonForwardingReason": etsysIetfBridgeDot1dStpPortCistNonForwardingReason,
       "etsysIetfBridgeDot1dStpTopChangeTrapEnable": etsysIetfBridgeDot1dStpTopChangeTrapEnable,
       "etsysIetfBridgeDot1dStpNewRootTrapEnable": etsysIetfBridgeDot1dStpNewRootTrapEnable,
       "etsysIetfBridgeDot1dStpBridgePriorityDefault": etsysIetfBridgeDot1dStpBridgePriorityDefault,
       "etsysIetfBridgeDot1dBase": etsysIetfBridgeDot1dBase,
       "etsysIetfBridgeDot1dBasePortTable": etsysIetfBridgeDot1dBasePortTable,
       "etsysIetfBridgeDot1dBasePortEntry": etsysIetfBridgeDot1dBasePortEntry,
       "etsysIetfBridgeDot1dBasePortNewLearnedAddrTrap": etsysIetfBridgeDot1dBasePortNewLearnedAddrTrap,
       "etsysIetfBridgeDot1dBasePortMovedAddrTrap": etsysIetfBridgeDot1dBasePortMovedAddrTrap,
       "etsysIetfBridgeDot1qBase": etsysIetfBridgeDot1qBase,
       "etsysIetfBridgeDot1qNewLearnedAddrTrapEnable": etsysIetfBridgeDot1qNewLearnedAddrTrapEnable,
       "etsysIetfBridgeDot1qMovedAddrTrapEnable": etsysIetfBridgeDot1qMovedAddrTrapEnable,
       "etsysIetfBridgeDot1qStaticUcastAsMcast": etsysIetfBridgeDot1qStaticUcastAsMcast,
       "etsysIetfBridgeDot1dSpanGuard": etsysIetfBridgeDot1dSpanGuard,
       "etsysIetfBridgeDot1dStpSpanGuardEnable": etsysIetfBridgeDot1dStpSpanGuardEnable,
       "etsysIetfBridgeDot1dStpSpanGuardTrapEnable": etsysIetfBridgeDot1dStpSpanGuardTrapEnable,
       "etsysIetfBridgeDot1dStpSpanGuardBlockTime": etsysIetfBridgeDot1dStpSpanGuardBlockTime,
       "etsysIetfBridgeDot1dBackupRoot": etsysIetfBridgeDot1dBackupRoot,
       "etsysIetfBridgeDot1dStpBackupRootEnable": etsysIetfBridgeDot1dStpBackupRootEnable,
       "etsysIetfBridgeDot1dStpBackupRootTrapEnable": etsysIetfBridgeDot1dStpBackupRootTrapEnable,
       "etsysIetfBridgeDot1dLoopProtect": etsysIetfBridgeDot1dLoopProtect,
       "etsysIetfBridgeDot1dStpLoopProtectPortTable": etsysIetfBridgeDot1dStpLoopProtectPortTable,
       "etsysIetfBridgeDot1dStpLoopProtectPortEntry": etsysIetfBridgeDot1dStpLoopProtectPortEntry,
       "etsysIetfBridgeDot1dStpLoopProtectPortCistEnable": etsysIetfBridgeDot1dStpLoopProtectPortCistEnable,
       "etsysIetfBridgeDot1dStpLoopProtectPortCistBlocking": etsysIetfBridgeDot1dStpLoopProtectPortCistBlocking,
       "etsysIetfBridgeDot1dStpLoopProtectPortPartnerCapable": etsysIetfBridgeDot1dStpLoopProtectPortPartnerCapable,
       "etsysIetfBridgeDot1dStpLoopProtectEventThreshold": etsysIetfBridgeDot1dStpLoopProtectEventThreshold,
       "etsysIetfBridgeDot1dStpLoopProtectEventWindow": etsysIetfBridgeDot1dStpLoopProtectEventWindow,
       "etsysIetfBridgeDot1dStpLoopProtectEventTrapEnable": etsysIetfBridgeDot1dStpLoopProtectEventTrapEnable,
       "etsysIetfBridgeConformance": etsysIetfBridgeConformance,
       "etsysIetfBridgeGroups": etsysIetfBridgeGroups,
       "etsysIetfBridgeStpPort": etsysIetfBridgeStpPort,
       "etsysIetfBridgeStpTrap": etsysIetfBridgeStpTrap,
       "etsysIetfBridgeBase": etsysIetfBridgeBase,
       "etsysIetfBridgeDot1qFdbNewAddrNotification": etsysIetfBridgeDot1qFdbNewAddrNotification,
       "etsysIetfBridgeDot1dStpBridgePriority": etsysIetfBridgeDot1dStpBridgePriority,
       "etsysIetfBridgeSpanGuard": etsysIetfBridgeSpanGuard,
       "etsysIetfBridgeSpanGuardNotification": etsysIetfBridgeSpanGuardNotification,
       "etsysIetfBridgeBackupRoot": etsysIetfBridgeBackupRoot,
       "etsysIetfBridgeBackupRootNotification": etsysIetfBridgeBackupRootNotification,
       "etsysIetfBridgePortCistRoleValue": etsysIetfBridgePortCistRoleValue,
       "etsysIetfBridgeMovedAddr": etsysIetfBridgeMovedAddr,
       "etsysIetfBridgeDot1qFdbMovedAddrNotification": etsysIetfBridgeDot1qFdbMovedAddrNotification,
       "etsysIetfBridgeLoopProtect": etsysIetfBridgeLoopProtect,
       "etsysIetfBridgeLoopProtectNotification": etsysIetfBridgeLoopProtectNotification,
       "etsysIetfBridgeStpCistNonForwardingReason": etsysIetfBridgeStpCistNonForwardingReason,
       "etsysIetfBridgeStaticUcastAsMcast": etsysIetfBridgeStaticUcastAsMcast,
       "etsysIetfBridgeCompliances": etsysIetfBridgeCompliances,
       "etsysIetfBridgeCompliance": etsysIetfBridgeCompliance,
       "etsysIetfBridgeStaticUcastAsMcastCompliance": etsysIetfBridgeStaticUcastAsMcastCompliance}
)
