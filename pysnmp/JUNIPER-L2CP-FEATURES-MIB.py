# SNMP MIB module (JUNIPER-L2CP-FEATURES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-L2CP-FEATURES-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:13:25 2024
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

(dot1dStpPort,
 dot1dStpPortEntry) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dStpPort",
    "dot1dStpPortEntry")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(jnxL2cpMibRoot,) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxL2cpMibRoot")

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

jnxL2cpFeaturesMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 53, 1)
)
jnxL2cpFeaturesMIB.setRevisions(
        ("2012-06-25 00:00",
         "2012-08-15 00:00",
         "2010-06-11 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class LacpState(Bits, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_JnxL2cpObjects_ObjectIdentity = ObjectIdentity
jnxL2cpObjects = _JnxL2cpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 53, 1, 1)
)
_JnxL2cpStpProtectObjects_ObjectIdentity = ObjectIdentity
jnxL2cpStpProtectObjects = _JnxL2cpStpProtectObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 53, 1, 1, 1)
)
_JnxDot1dStpPortProtectTable_Object = MibTable
jnxDot1dStpPortProtectTable = _JnxDot1dStpPortProtectTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 53, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    jnxDot1dStpPortProtectTable.setStatus("current")
_JnxDot1dStpPortProtectEntry_Object = MibTableRow
jnxDot1dStpPortProtectEntry = _JnxDot1dStpPortProtectEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 53, 1, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    jnxDot1dStpPortProtectEntry.setStatus("current")
_JnxDot1dStpPortRootProtectEnabled_Type = TruthValue
_JnxDot1dStpPortRootProtectEnabled_Object = MibTableColumn
jnxDot1dStpPortRootProtectEnabled = _JnxDot1dStpPortRootProtectEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 53, 1, 1, 1, 1, 1, 1),
    _JnxDot1dStpPortRootProtectEnabled_Type()
)
jnxDot1dStpPortRootProtectEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDot1dStpPortRootProtectEnabled.setStatus("current")


class _JnxDot1dStpPortRootProtectState_Type(Integer32):
    """Custom type jnxDot1dStpPortRootProtectState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no-error", 0),
          ("root-prevented", 1))
    )


_JnxDot1dStpPortRootProtectState_Type.__name__ = "Integer32"
_JnxDot1dStpPortRootProtectState_Object = MibTableColumn
jnxDot1dStpPortRootProtectState = _JnxDot1dStpPortRootProtectState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 53, 1, 1, 1, 1, 1, 2),
    _JnxDot1dStpPortRootProtectState_Type()
)
jnxDot1dStpPortRootProtectState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDot1dStpPortRootProtectState.setStatus("current")
_JnxDot1dStpPortLoopProtectEnabled_Type = TruthValue
_JnxDot1dStpPortLoopProtectEnabled_Object = MibTableColumn
jnxDot1dStpPortLoopProtectEnabled = _JnxDot1dStpPortLoopProtectEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 53, 1, 1, 1, 1, 1, 3),
    _JnxDot1dStpPortLoopProtectEnabled_Type()
)
jnxDot1dStpPortLoopProtectEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDot1dStpPortLoopProtectEnabled.setStatus("current")


class _JnxDot1dStpPortLoopProtectState_Type(Integer32):
    """Custom type jnxDot1dStpPortLoopProtectState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("loop-prevented", 1),
          ("no-error", 0))
    )


_JnxDot1dStpPortLoopProtectState_Type.__name__ = "Integer32"
_JnxDot1dStpPortLoopProtectState_Object = MibTableColumn
jnxDot1dStpPortLoopProtectState = _JnxDot1dStpPortLoopProtectState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 53, 1, 1, 1, 1, 1, 4),
    _JnxDot1dStpPortLoopProtectState_Type()
)
jnxDot1dStpPortLoopProtectState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDot1dStpPortLoopProtectState.setStatus("current")
_JnxL2cpBpduProtectObjects_ObjectIdentity = ObjectIdentity
jnxL2cpBpduProtectObjects = _JnxL2cpBpduProtectObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 53, 1, 1, 2)
)
_JnxL2cpBpduProtectPortTable_Object = MibTable
jnxL2cpBpduProtectPortTable = _JnxL2cpBpduProtectPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 53, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    jnxL2cpBpduProtectPortTable.setStatus("current")
_JnxL2cpBpduProtectPortEntry_Object = MibTableRow
jnxL2cpBpduProtectPortEntry = _JnxL2cpBpduProtectPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 53, 1, 1, 2, 1, 1)
)
jnxL2cpBpduProtectPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    jnxL2cpBpduProtectPortEntry.setStatus("current")
_JnxL2cpBpduProtectPortEnabled_Type = TruthValue
_JnxL2cpBpduProtectPortEnabled_Object = MibTableColumn
jnxL2cpBpduProtectPortEnabled = _JnxL2cpBpduProtectPortEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 53, 1, 1, 2, 1, 1, 1),
    _JnxL2cpBpduProtectPortEnabled_Type()
)
jnxL2cpBpduProtectPortEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2cpBpduProtectPortEnabled.setStatus("current")


class _JnxL2cpPortBpduError_Type(Integer32):
    """Custom type jnxL2cpPortBpduError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("detected", 1),
          ("no-error", 0))
    )


_JnxL2cpPortBpduError_Type.__name__ = "Integer32"
_JnxL2cpPortBpduError_Object = MibTableColumn
jnxL2cpPortBpduError = _JnxL2cpPortBpduError_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 53, 1, 1, 2, 1, 1, 2),
    _JnxL2cpPortBpduError_Type()
)
jnxL2cpPortBpduError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2cpPortBpduError.setStatus("current")
_JnxL2cpBpduProtectDisableTimeout_Type = Integer32
_JnxL2cpBpduProtectDisableTimeout_Object = MibScalar
jnxL2cpBpduProtectDisableTimeout = _JnxL2cpBpduProtectDisableTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 53, 1, 1, 2, 2),
    _JnxL2cpBpduProtectDisableTimeout_Type()
)
jnxL2cpBpduProtectDisableTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2cpBpduProtectDisableTimeout.setStatus("current")
_JnxLacpNotifyVars_ObjectIdentity = ObjectIdentity
jnxLacpNotifyVars = _JnxLacpNotifyVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 53, 1, 1, 3)
)
_JnxLacpInterfaceName_Type = DisplayString
_JnxLacpInterfaceName_Object = MibScalar
jnxLacpInterfaceName = _JnxLacpInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 53, 1, 1, 3, 1),
    _JnxLacpInterfaceName_Type()
)
jnxLacpInterfaceName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxLacpInterfaceName.setStatus("current")
_JnxLacpifIndex_Type = InterfaceIndex
_JnxLacpifIndex_Object = MibScalar
jnxLacpifIndex = _JnxLacpifIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 53, 1, 1, 3, 2),
    _JnxLacpifIndex_Type()
)
jnxLacpifIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxLacpifIndex.setStatus("current")
_JnxLacpAggregateInterfaceName_Type = DisplayString
_JnxLacpAggregateInterfaceName_Object = MibScalar
jnxLacpAggregateInterfaceName = _JnxLacpAggregateInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 53, 1, 1, 3, 3),
    _JnxLacpAggregateInterfaceName_Type()
)
jnxLacpAggregateInterfaceName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxLacpAggregateInterfaceName.setStatus("current")
_JnxLacpAggregateifIndex_Type = InterfaceIndex
_JnxLacpAggregateifIndex_Object = MibScalar
jnxLacpAggregateifIndex = _JnxLacpAggregateifIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 53, 1, 1, 3, 4),
    _JnxLacpAggregateifIndex_Type()
)
jnxLacpAggregateifIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxLacpAggregateifIndex.setStatus("current")
_JnxLacpAggPortActorOperState_Type = DisplayString
_JnxLacpAggPortActorOperState_Object = MibScalar
jnxLacpAggPortActorOperState = _JnxLacpAggPortActorOperState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 53, 1, 1, 3, 5),
    _JnxLacpAggPortActorOperState_Type()
)
jnxLacpAggPortActorOperState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxLacpAggPortActorOperState.setStatus("current")
_JnxLacpAggTimeout_ObjectIdentity = ObjectIdentity
jnxLacpAggTimeout = _JnxLacpAggTimeout_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 53, 1, 1, 4)
)
_Dot3adAggPortTimeoutTable_Object = MibTable
dot3adAggPortTimeoutTable = _Dot3adAggPortTimeoutTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 53, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    dot3adAggPortTimeoutTable.setStatus("current")
_Dot3adAggPortTimeoutEntry_Object = MibTableRow
dot3adAggPortTimeoutEntry = _Dot3adAggPortTimeoutEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 53, 1, 1, 4, 1, 1)
)
dot3adAggPortTimeoutEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot3adAggPortTimeoutEntry.setStatus("current")
_Dot3adInterfaceName_Type = DisplayString
_Dot3adInterfaceName_Object = MibTableColumn
dot3adInterfaceName = _Dot3adInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 53, 1, 1, 4, 1, 1, 1),
    _Dot3adInterfaceName_Type()
)
dot3adInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adInterfaceName.setStatus("current")
_Dot3adOperState_Type = LacpState
_Dot3adOperState_Object = MibTableColumn
dot3adOperState = _Dot3adOperState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 53, 1, 1, 4, 1, 1, 2),
    _Dot3adOperState_Type()
)
dot3adOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adOperState.setStatus("current")
_Dot3adAggname_Type = DisplayString
_Dot3adAggname_Object = MibTableColumn
dot3adAggname = _Dot3adAggname_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 53, 1, 1, 4, 1, 1, 3),
    _Dot3adAggname_Type()
)
dot3adAggname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggname.setStatus("current")
_Dot3adInterfaceTimeout_Type = TimeTicks
_Dot3adInterfaceTimeout_Object = MibTableColumn
dot3adInterfaceTimeout = _Dot3adInterfaceTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 53, 1, 1, 4, 1, 1, 4),
    _Dot3adInterfaceTimeout_Type()
)
dot3adInterfaceTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adInterfaceTimeout.setStatus("current")
_JnxL2cpNotifications_ObjectIdentity = ObjectIdentity
jnxL2cpNotifications = _JnxL2cpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 53, 1, 2)
)
_JnxL2cpProtectTraps_ObjectIdentity = ObjectIdentity
jnxL2cpProtectTraps = _JnxL2cpProtectTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 53, 1, 2, 0)
)
_JnxLacpNotificationsPrefix_ObjectIdentity = ObjectIdentity
jnxLacpNotificationsPrefix = _JnxLacpNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 53, 1, 2, 1)
)
dot1dStpPortEntry.registerAugmentions(
    ("JUNIPER-L2CP-FEATURES-MIB",
     "jnxDot1dStpPortProtectEntry")
)
jnxDot1dStpPortProtectEntry.setIndexNames(*dot1dStpPortEntry.getIndexNames())

# Managed Objects groups


# Notification objects

jnxPortRootProtectStateChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 53, 1, 2, 0, 1)
)
jnxPortRootProtectStateChangeTrap.setObjects(
    ("JUNIPER-L2CP-FEATURES-MIB", "jnxDot1dStpPortRootProtectState")
)
if mibBuilder.loadTexts:
    jnxPortRootProtectStateChangeTrap.setStatus(
        "current"
    )

jnxPortLoopProtectStateChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 53, 1, 2, 0, 2)
)
jnxPortLoopProtectStateChangeTrap.setObjects(
    ("JUNIPER-L2CP-FEATURES-MIB", "jnxDot1dStpPortLoopProtectState")
)
if mibBuilder.loadTexts:
    jnxPortLoopProtectStateChangeTrap.setStatus(
        "current"
    )

jnxPortBpduErrorStatusChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 53, 1, 2, 0, 3)
)
jnxPortBpduErrorStatusChangeTrap.setObjects(
    ("JUNIPER-L2CP-FEATURES-MIB", "jnxL2cpPortBpduError")
)
if mibBuilder.loadTexts:
    jnxPortBpduErrorStatusChangeTrap.setStatus(
        "current"
    )

jnxLacpTimeOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 53, 1, 2, 1, 1)
)
jnxLacpTimeOut.setObjects(
      *(("JUNIPER-L2CP-FEATURES-MIB", "jnxLacpInterfaceName"),
        ("JUNIPER-L2CP-FEATURES-MIB", "jnxLacpifIndex"),
        ("JUNIPER-L2CP-FEATURES-MIB", "jnxLacpAggregateInterfaceName"),
        ("JUNIPER-L2CP-FEATURES-MIB", "jnxLacpAggregateifIndex"),
        ("JUNIPER-L2CP-FEATURES-MIB", "jnxLacpAggPortActorOperState"))
)
if mibBuilder.loadTexts:
    jnxLacpTimeOut.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-L2CP-FEATURES-MIB",
    **{"LacpState": LacpState,
       "jnxL2cpFeaturesMIB": jnxL2cpFeaturesMIB,
       "jnxL2cpObjects": jnxL2cpObjects,
       "jnxL2cpStpProtectObjects": jnxL2cpStpProtectObjects,
       "jnxDot1dStpPortProtectTable": jnxDot1dStpPortProtectTable,
       "jnxDot1dStpPortProtectEntry": jnxDot1dStpPortProtectEntry,
       "jnxDot1dStpPortRootProtectEnabled": jnxDot1dStpPortRootProtectEnabled,
       "jnxDot1dStpPortRootProtectState": jnxDot1dStpPortRootProtectState,
       "jnxDot1dStpPortLoopProtectEnabled": jnxDot1dStpPortLoopProtectEnabled,
       "jnxDot1dStpPortLoopProtectState": jnxDot1dStpPortLoopProtectState,
       "jnxL2cpBpduProtectObjects": jnxL2cpBpduProtectObjects,
       "jnxL2cpBpduProtectPortTable": jnxL2cpBpduProtectPortTable,
       "jnxL2cpBpduProtectPortEntry": jnxL2cpBpduProtectPortEntry,
       "jnxL2cpBpduProtectPortEnabled": jnxL2cpBpduProtectPortEnabled,
       "jnxL2cpPortBpduError": jnxL2cpPortBpduError,
       "jnxL2cpBpduProtectDisableTimeout": jnxL2cpBpduProtectDisableTimeout,
       "jnxLacpNotifyVars": jnxLacpNotifyVars,
       "jnxLacpInterfaceName": jnxLacpInterfaceName,
       "jnxLacpifIndex": jnxLacpifIndex,
       "jnxLacpAggregateInterfaceName": jnxLacpAggregateInterfaceName,
       "jnxLacpAggregateifIndex": jnxLacpAggregateifIndex,
       "jnxLacpAggPortActorOperState": jnxLacpAggPortActorOperState,
       "jnxLacpAggTimeout": jnxLacpAggTimeout,
       "dot3adAggPortTimeoutTable": dot3adAggPortTimeoutTable,
       "dot3adAggPortTimeoutEntry": dot3adAggPortTimeoutEntry,
       "dot3adInterfaceName": dot3adInterfaceName,
       "dot3adOperState": dot3adOperState,
       "dot3adAggname": dot3adAggname,
       "dot3adInterfaceTimeout": dot3adInterfaceTimeout,
       "jnxL2cpNotifications": jnxL2cpNotifications,
       "jnxL2cpProtectTraps": jnxL2cpProtectTraps,
       "jnxPortRootProtectStateChangeTrap": jnxPortRootProtectStateChangeTrap,
       "jnxPortLoopProtectStateChangeTrap": jnxPortLoopProtectStateChangeTrap,
       "jnxPortBpduErrorStatusChangeTrap": jnxPortBpduErrorStatusChangeTrap,
       "jnxLacpNotificationsPrefix": jnxLacpNotificationsPrefix,
       "jnxLacpTimeOut": jnxLacpTimeOut}
)
