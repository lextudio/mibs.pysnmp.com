# SNMP MIB module (GWMONITOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/GWMONITOR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:49:24 2024
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

_Novell_ObjectIdentity = ObjectIdentity
novell = _Novell_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23)
)
_MibDoc_ObjectIdentity = ObjectIdentity
mibDoc = _MibDoc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2)
)
_Gwmontr_ObjectIdentity = ObjectIdentity
gwmontr = _Gwmontr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 40)
)
_Gwmonserver_ObjectIdentity = ObjectIdentity
gwmonserver = _Gwmonserver_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 40, 5)
)
_GwmonTrapInfo_ObjectIdentity = ObjectIdentity
gwmonTrapInfo = _GwmonTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 40, 5, 1)
)
_GwmonTrapTime_Type = Integer32
_GwmonTrapTime_Object = MibScalar
gwmonTrapTime = _GwmonTrapTime_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 40, 5, 1, 1),
    _GwmonTrapTime_Type()
)
gwmonTrapTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gwmonTrapTime.setStatus("mandatory")


class _GwmonAgentName_Type(DisplayString):
    """Custom type gwmonAgentName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GwmonAgentName_Type.__name__ = "DisplayString"
_GwmonAgentName_Object = MibScalar
gwmonAgentName = _GwmonAgentName_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 40, 5, 1, 2),
    _GwmonAgentName_Type()
)
gwmonAgentName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gwmonAgentName.setStatus("mandatory")


class _GwmonAgentType_Type(DisplayString):
    """Custom type gwmonAgentType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GwmonAgentType_Type.__name__ = "DisplayString"
_GwmonAgentType_Object = MibScalar
gwmonAgentType = _GwmonAgentType_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 40, 5, 1, 3),
    _GwmonAgentType_Type()
)
gwmonAgentType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gwmonAgentType.setStatus("mandatory")


class _GwmonStatus_Type(DisplayString):
    """Custom type gwmonStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GwmonStatus_Type.__name__ = "DisplayString"
_GwmonStatus_Object = MibScalar
gwmonStatus = _GwmonStatus_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 40, 5, 1, 4),
    _GwmonStatus_Type()
)
gwmonStatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gwmonStatus.setStatus("mandatory")
_GwmonStatusDuration_Type = TimeTicks
_GwmonStatusDuration_Object = MibScalar
gwmonStatusDuration = _GwmonStatusDuration_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 40, 5, 1, 5),
    _GwmonStatusDuration_Type()
)
gwmonStatusDuration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gwmonStatusDuration.setStatus("mandatory")


class _GwmonThreshold_Type(DisplayString):
    """Custom type gwmonThreshold based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GwmonThreshold_Type.__name__ = "DisplayString"
_GwmonThreshold_Object = MibScalar
gwmonThreshold = _GwmonThreshold_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 40, 5, 1, 6),
    _GwmonThreshold_Type()
)
gwmonThreshold.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gwmonThreshold.setStatus("mandatory")


class _GwmonThresholdValues_Type(DisplayString):
    """Custom type gwmonThresholdValues based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GwmonThresholdValues_Type.__name__ = "DisplayString"
_GwmonThresholdValues_Object = MibScalar
gwmonThresholdValues = _GwmonThresholdValues_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 40, 5, 1, 7),
    _GwmonThresholdValues_Type()
)
gwmonThresholdValues.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gwmonThresholdValues.setStatus("mandatory")


class _GwmonThresholdSeverity_Type(DisplayString):
    """Custom type gwmonThresholdSeverity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GwmonThresholdSeverity_Type.__name__ = "DisplayString"
_GwmonThresholdSeverity_Object = MibScalar
gwmonThresholdSeverity = _GwmonThresholdSeverity_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 40, 5, 1, 8),
    _GwmonThresholdSeverity_Type()
)
gwmonThresholdSeverity.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gwmonThresholdSeverity.setStatus("mandatory")


class _GwmonServerName_Type(DisplayString):
    """Custom type gwmonServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GwmonServerName_Type.__name__ = "DisplayString"
_GwmonServerName_Object = MibScalar
gwmonServerName = _GwmonServerName_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 40, 5, 1, 9),
    _GwmonServerName_Type()
)
gwmonServerName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gwmonServerName.setStatus("mandatory")


class _GwmonServerIPAddress_Type(DisplayString):
    """Custom type gwmonServerIPAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GwmonServerIPAddress_Type.__name__ = "DisplayString"
_GwmonServerIPAddress_Object = MibScalar
gwmonServerIPAddress = _GwmonServerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 40, 5, 1, 10),
    _GwmonServerIPAddress_Type()
)
gwmonServerIPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gwmonServerIPAddress.setStatus("mandatory")
_GwmonTraps_ObjectIdentity = ObjectIdentity
gwmonTraps = _GwmonTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 40, 5, 2)
)

# Managed Objects groups


# Notification objects

gwmonThresholdExceededTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 40, 5, 2, 0, 1)
)
gwmonThresholdExceededTrap.setObjects(
      *(("GWMONITOR-MIB", "gwmonTrapTime"),
        ("GWMONITOR-MIB", "gwmonAgentType"),
        ("GWMONITOR-MIB", "gwmonAgentName"),
        ("GWMONITOR-MIB", "gwmonServerName"),
        ("GWMONITOR-MIB", "gwmonServerIPAddress"),
        ("GWMONITOR-MIB", "gwmonThresholdValues"),
        ("GWMONITOR-MIB", "gwmonThresholdSeverity"))
)
if mibBuilder.loadTexts:
    gwmonThresholdExceededTrap.setStatus(
        ""
    )

gwmonThresholdRecoveredTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 40, 5, 2, 0, 2)
)
gwmonThresholdRecoveredTrap.setObjects(
      *(("GWMONITOR-MIB", "gwmonTrapTime"),
        ("GWMONITOR-MIB", "gwmonAgentType"),
        ("GWMONITOR-MIB", "gwmonAgentName"),
        ("GWMONITOR-MIB", "gwmonServerName"),
        ("GWMONITOR-MIB", "gwmonServerIPAddress"))
)
if mibBuilder.loadTexts:
    gwmonThresholdRecoveredTrap.setStatus(
        ""
    )

gwmonAgentDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 40, 5, 2, 0, 3)
)
gwmonAgentDownTrap.setObjects(
      *(("GWMONITOR-MIB", "gwmonTrapTime"),
        ("GWMONITOR-MIB", "gwmonAgentType"),
        ("GWMONITOR-MIB", "gwmonAgentName"),
        ("GWMONITOR-MIB", "gwmonServerName"),
        ("GWMONITOR-MIB", "gwmonServerIPAddress"))
)
if mibBuilder.loadTexts:
    gwmonAgentDownTrap.setStatus(
        ""
    )

gwmonAgentUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 40, 5, 2, 0, 4)
)
gwmonAgentUpTrap.setObjects(
      *(("GWMONITOR-MIB", "gwmonTrapTime"),
        ("GWMONITOR-MIB", "gwmonAgentType"),
        ("GWMONITOR-MIB", "gwmonAgentName"),
        ("GWMONITOR-MIB", "gwmonServerName"),
        ("GWMONITOR-MIB", "gwmonServerIPAddress"))
)
if mibBuilder.loadTexts:
    gwmonAgentUpTrap.setStatus(
        ""
    )

gwmonTestTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 40, 5, 2, 0, 5)
)
gwmonTestTrap.setObjects(
    ("GWMONITOR-MIB", "gwmonTrapTime")
)
if mibBuilder.loadTexts:
    gwmonTestTrap.setStatus(
        ""
    )

gwmonPeriodicTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 40, 5, 2, 0, 6)
)
gwmonPeriodicTrap.setObjects(
    ("GWMONITOR-MIB", "gwmonTrapTime")
)
if mibBuilder.loadTexts:
    gwmonPeriodicTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GWMONITOR-MIB",
    **{"novell": novell,
       "mibDoc": mibDoc,
       "gwmontr": gwmontr,
       "gwmonserver": gwmonserver,
       "gwmonTrapInfo": gwmonTrapInfo,
       "gwmonTrapTime": gwmonTrapTime,
       "gwmonAgentName": gwmonAgentName,
       "gwmonAgentType": gwmonAgentType,
       "gwmonStatus": gwmonStatus,
       "gwmonStatusDuration": gwmonStatusDuration,
       "gwmonThreshold": gwmonThreshold,
       "gwmonThresholdValues": gwmonThresholdValues,
       "gwmonThresholdSeverity": gwmonThresholdSeverity,
       "gwmonServerName": gwmonServerName,
       "gwmonServerIPAddress": gwmonServerIPAddress,
       "gwmonTraps": gwmonTraps,
       "gwmonThresholdExceededTrap": gwmonThresholdExceededTrap,
       "gwmonThresholdRecoveredTrap": gwmonThresholdRecoveredTrap,
       "gwmonAgentDownTrap": gwmonAgentDownTrap,
       "gwmonAgentUpTrap": gwmonAgentUpTrap,
       "gwmonTestTrap": gwmonTestTrap,
       "gwmonPeriodicTrap": gwmonPeriodicTrap}
)
