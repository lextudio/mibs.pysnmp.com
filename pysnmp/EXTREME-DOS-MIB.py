# SNMP MIB module (EXTREME-DOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EXTREME-BASE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:41:20 2024
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

(extremeAgent,
 extremeV2Traps,
 extremenetworks) = mibBuilder.importSymbols(
    "EXTREME-BASE-MIB",
    "extremeAgent",
    "extremeV2Traps",
    "extremenetworks")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

extremeDosMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 28)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ExtremeDosProtect_ObjectIdentity = ObjectIdentity
extremeDosProtect = _ExtremeDosProtect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 28, 1)
)


class _ExtremeDosEnable_Type(TruthValue):
    """Custom type extremeDosEnable based on TruthValue"""


_ExtremeDosEnable_Object = MibScalar
extremeDosEnable = _ExtremeDosEnable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 28, 1, 1),
    _ExtremeDosEnable_Type()
)
extremeDosEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeDosEnable.setStatus("current")


class _ExtremeDosNoticeLevel_Type(Integer32):
    """Custom type extremeDosNoticeLevel based on Integer32"""
    defaultValue = 4000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(150, 100000),
    )


_ExtremeDosNoticeLevel_Type.__name__ = "Integer32"
_ExtremeDosNoticeLevel_Object = MibScalar
extremeDosNoticeLevel = _ExtremeDosNoticeLevel_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 28, 1, 2),
    _ExtremeDosNoticeLevel_Type()
)
extremeDosNoticeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeDosNoticeLevel.setStatus("current")


class _ExtremeDosAlertLevel_Type(Integer32):
    """Custom type extremeDosAlertLevel based on Integer32"""
    defaultValue = 4000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(150, 100000),
    )


_ExtremeDosAlertLevel_Type.__name__ = "Integer32"
_ExtremeDosAlertLevel_Object = MibScalar
extremeDosAlertLevel = _ExtremeDosAlertLevel_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 28, 1, 3),
    _ExtremeDosAlertLevel_Type()
)
extremeDosAlertLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeDosAlertLevel.setStatus("current")


class _ExtremeDosFilterType_Type(Integer32):
    """Custom type extremeDosFilterType based on Integer32"""
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
        *(("destination", 1),
          ("destinationAndSource", 3),
          ("source", 2))
    )


_ExtremeDosFilterType_Type.__name__ = "Integer32"
_ExtremeDosFilterType_Object = MibScalar
extremeDosFilterType = _ExtremeDosFilterType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 28, 1, 4),
    _ExtremeDosFilterType_Type()
)
extremeDosFilterType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeDosFilterType.setStatus("current")


class _ExtremeDosAclTimeout_Type(Integer32):
    """Custom type extremeDosAclTimeout based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 300),
    )


_ExtremeDosAclTimeout_Type.__name__ = "Integer32"
_ExtremeDosAclTimeout_Object = MibScalar
extremeDosAclTimeout = _ExtremeDosAclTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 28, 1, 5),
    _ExtremeDosAclTimeout_Type()
)
extremeDosAclTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeDosAclTimeout.setStatus("current")


class _ExtremeDosAclRulePrecedence_Type(Integer32):
    """Custom type extremeDosAclRulePrecedence based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 25588),
    )


_ExtremeDosAclRulePrecedence_Type.__name__ = "Integer32"
_ExtremeDosAclRulePrecedence_Object = MibScalar
extremeDosAclRulePrecedence = _ExtremeDosAclRulePrecedence_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 28, 1, 6),
    _ExtremeDosAclRulePrecedence_Type()
)
extremeDosAclRulePrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeDosAclRulePrecedence.setStatus("current")


class _ExtremeDosMessagesEnable_Type(TruthValue):
    """Custom type extremeDosMessagesEnable based on TruthValue"""


_ExtremeDosMessagesEnable_Object = MibScalar
extremeDosMessagesEnable = _ExtremeDosMessagesEnable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 28, 1, 7),
    _ExtremeDosMessagesEnable_Type()
)
extremeDosMessagesEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeDosMessagesEnable.setStatus("current")
_ExtremeDosPortTable_Object = MibTable
extremeDosPortTable = _ExtremeDosPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 28, 1, 8)
)
if mibBuilder.loadTexts:
    extremeDosPortTable.setStatus("current")
_ExtremeDosPortEntry_Object = MibTableRow
extremeDosPortEntry = _ExtremeDosPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 28, 1, 8, 1)
)
extremeDosPortEntry.setIndexNames(
    (0, "EXTREME-DOS-MIB", "extremeDosIfIndex"),
)
if mibBuilder.loadTexts:
    extremeDosPortEntry.setStatus("current")
_ExtremeDosIfIndex_Type = Integer32
_ExtremeDosIfIndex_Object = MibTableColumn
extremeDosIfIndex = _ExtremeDosIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 28, 1, 8, 1, 1),
    _ExtremeDosIfIndex_Type()
)
extremeDosIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeDosIfIndex.setStatus("current")


class _ExtremeDosPortTrusted_Type(TruthValue):
    """Custom type extremeDosPortTrusted based on TruthValue"""


_ExtremeDosPortTrusted_Object = MibTableColumn
extremeDosPortTrusted = _ExtremeDosPortTrusted_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 28, 1, 8, 1, 2),
    _ExtremeDosPortTrusted_Type()
)
extremeDosPortTrusted.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeDosPortTrusted.setStatus("current")
_ExtremeDosIsDosActive_Type = TruthValue
_ExtremeDosIsDosActive_Object = MibTableColumn
extremeDosIsDosActive = _ExtremeDosIsDosActive_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 28, 1, 8, 1, 3),
    _ExtremeDosIsDosActive_Type()
)
extremeDosIsDosActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeDosIsDosActive.setStatus("current")
_ExtremeDosTraps_ObjectIdentity = ObjectIdentity
extremeDosTraps = _ExtremeDosTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 4, 14)
)
_ExtremeDosTrapsPrefix_ObjectIdentity = ObjectIdentity
extremeDosTrapsPrefix = _ExtremeDosTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 4, 14, 0)
)

# Managed Objects groups


# Notification objects

extremeDosThresholdCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 4, 14, 0, 1)
)
extremeDosThresholdCleared.setObjects(
    ("EXTREME-DOS-MIB", "extremeDosAlertLevel")
)
if mibBuilder.loadTexts:
    extremeDosThresholdCleared.setStatus(
        "current"
    )

extremeDosThresholdReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 4, 14, 0, 2)
)
extremeDosThresholdReached.setObjects(
    ("EXTREME-DOS-MIB", "extremeDosAlertLevel")
)
if mibBuilder.loadTexts:
    extremeDosThresholdReached.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EXTREME-DOS-MIB",
    **{"extremeDosMib": extremeDosMib,
       "extremeDosProtect": extremeDosProtect,
       "extremeDosEnable": extremeDosEnable,
       "extremeDosNoticeLevel": extremeDosNoticeLevel,
       "extremeDosAlertLevel": extremeDosAlertLevel,
       "extremeDosFilterType": extremeDosFilterType,
       "extremeDosAclTimeout": extremeDosAclTimeout,
       "extremeDosAclRulePrecedence": extremeDosAclRulePrecedence,
       "extremeDosMessagesEnable": extremeDosMessagesEnable,
       "extremeDosPortTable": extremeDosPortTable,
       "extremeDosPortEntry": extremeDosPortEntry,
       "extremeDosIfIndex": extremeDosIfIndex,
       "extremeDosPortTrusted": extremeDosPortTrusted,
       "extremeDosIsDosActive": extremeDosIsDosActive,
       "extremeDosTraps": extremeDosTraps,
       "extremeDosTrapsPrefix": extremeDosTrapsPrefix,
       "extremeDosThresholdCleared": extremeDosThresholdCleared,
       "extremeDosThresholdReached": extremeDosThresholdReached}
)
