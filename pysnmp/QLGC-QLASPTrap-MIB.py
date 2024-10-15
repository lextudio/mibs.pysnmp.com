# SNMP MIB module (QLGC-QLASPTrap-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/QLGC-QLASPTrap-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:40:51 2024
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
 NotificationType,
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
    "NotificationType",
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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Qlogic_ObjectIdentity = ObjectIdentity
qlogic = _Qlogic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3873)
)
_Enet_ObjectIdentity = ObjectIdentity
enet = _Enet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3873, 1)
)
_Qlasp_ObjectIdentity = ObjectIdentity
qlasp = _Qlasp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3873, 1, 2)
)
_QlaspConfig_ObjectIdentity = ObjectIdentity
qlaspConfig = _QlaspConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3873, 1, 2, 1)
)
_QlaspStat_ObjectIdentity = ObjectIdentity
qlaspStat = _QlaspStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3873, 1, 2, 2)
)
_QlaspTrap_ObjectIdentity = ObjectIdentity
qlaspTrap = _QlaspTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3873, 1, 2, 3)
)
_TrapAdapterName_Type = DisplayString
_TrapAdapterName_Object = MibScalar
trapAdapterName = _TrapAdapterName_Object(
    (1, 3, 6, 1, 4, 1, 3873, 1, 2, 3, 1),
    _TrapAdapterName_Type()
)
trapAdapterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapAdapterName.setStatus("mandatory")
_TrapTeamName_Type = DisplayString
_TrapTeamName_Object = MibScalar
trapTeamName = _TrapTeamName_Object(
    (1, 3, 6, 1, 4, 1, 3873, 1, 2, 3, 2),
    _TrapTeamName_Type()
)
trapTeamName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapTeamName.setStatus("mandatory")


class _TrapCauseDirection_Type(Integer32):
    """Custom type trapCauseDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("adapterActive", 1),
          ("adapterInactive", 2))
    )


_TrapCauseDirection_Type.__name__ = "Integer32"
_TrapCauseDirection_Object = MibScalar
trapCauseDirection = _TrapCauseDirection_Object(
    (1, 3, 6, 1, 4, 1, 3873, 1, 2, 3, 3),
    _TrapCauseDirection_Type()
)
trapCauseDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapCauseDirection.setStatus("mandatory")


class _TrapAdapterActivityCause_Type(Integer32):
    """Custom type trapAdapterActivityCause based on Integer32"""
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
        *(("adapterAddedOrRemoved", 4),
          ("adapterEnabledOrDisabled", 3),
          ("linkChange", 2),
          ("none", 1))
    )


_TrapAdapterActivityCause_Type.__name__ = "Integer32"
_TrapAdapterActivityCause_Object = MibScalar
trapAdapterActivityCause = _TrapAdapterActivityCause_Object(
    (1, 3, 6, 1, 4, 1, 3873, 1, 2, 3, 4),
    _TrapAdapterActivityCause_Type()
)
trapAdapterActivityCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapAdapterActivityCause.setStatus("mandatory")

# Managed Objects groups


# Notification objects

failoverEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3873, 1, 2, 3, 0, 1)
)
failoverEvent.setObjects(
      *(("QLGC-QLASPTrap-MIB", "trapAdapterName"),
        ("QLGC-QLASPTrap-MIB", "trapTeamName"),
        ("QLGC-QLASPTrap-MIB", "trapCauseDirection"),
        ("QLGC-QLASPTrap-MIB", "trapAdapterActivityCause"))
)
if mibBuilder.loadTexts:
    failoverEvent.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QLGC-QLASPTrap-MIB",
    **{"qlogic": qlogic,
       "enet": enet,
       "qlasp": qlasp,
       "qlaspConfig": qlaspConfig,
       "qlaspStat": qlaspStat,
       "qlaspTrap": qlaspTrap,
       "failoverEvent": failoverEvent,
       "trapAdapterName": trapAdapterName,
       "trapTeamName": trapTeamName,
       "trapCauseDirection": trapCauseDirection,
       "trapAdapterActivityCause": trapAdapterActivityCause}
)
