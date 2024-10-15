# SNMP MIB module (TRANGO-APEX-TRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TRANGO-APEX-TRAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:07:20 2024
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

(ModuleIdentity,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 Unsigned32,
 apex) = mibBuilder.importSymbols(
    "TRANGO-APEX-MIB",
    "ModuleIdentity",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "Unsigned32",
    "apex")


# MODULE-IDENTITY


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Trangotrap_ObjectIdentity = ObjectIdentity
trangotrap = _Trangotrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5454, 1, 60, 6)
)
_Traplock_ObjectIdentity = ObjectIdentity
traplock = _Traplock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5454, 1, 60, 6, 3)
)
_Trapthreshold_ObjectIdentity = ObjectIdentity
trapthreshold = _Trapthreshold_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5454, 1, 60, 6, 4)
)
_Trapmse_ObjectIdentity = ObjectIdentity
trapmse = _Trapmse_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5454, 1, 60, 6, 4, 1)
)
_Trapber_ObjectIdentity = ObjectIdentity
trapber = _Trapber_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5454, 1, 60, 6, 4, 2)
)
_Trapfer_ObjectIdentity = ObjectIdentity
trapfer = _Trapfer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5454, 1, 60, 6, 4, 3)
)
_Traprssi_ObjectIdentity = ObjectIdentity
traprssi = _Traprssi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5454, 1, 60, 6, 4, 4)
)
_Trapidutemp_ObjectIdentity = ObjectIdentity
trapidutemp = _Trapidutemp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5454, 1, 60, 6, 4, 5)
)
_Trapodutemp_ObjectIdentity = ObjectIdentity
trapodutemp = _Trapodutemp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5454, 1, 60, 6, 4, 6)
)
_Trapinport_ObjectIdentity = ObjectIdentity
trapinport = _Trapinport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5454, 1, 60, 6, 4, 7)
)
_Trapoutport_ObjectIdentity = ObjectIdentity
trapoutport = _Trapoutport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5454, 1, 60, 6, 4, 8)
)
_Trapstandby_ObjectIdentity = ObjectIdentity
trapstandby = _Trapstandby_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5454, 1, 60, 6, 5)
)
_Trapeth_ObjectIdentity = ObjectIdentity
trapeth = _Trapeth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5454, 1, 60, 6, 6)
)
_Trapethstatus_ObjectIdentity = ObjectIdentity
trapethstatus = _Trapethstatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5454, 1, 60, 6, 6, 1)
)

# Managed Objects groups


# Notification objects

trapReboot = NotificationType(
    (1, 3, 6, 1, 4, 1, 5454, 1, 60, 6, 1)
)
if mibBuilder.loadTexts:
    trapReboot.setStatus(
        "current"
    )

trapStartUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 5454, 1, 60, 6, 2)
)
if mibBuilder.loadTexts:
    trapStartUp.setStatus(
        "current"
    )

trapModemLock = NotificationType(
    (1, 3, 6, 1, 4, 1, 5454, 1, 60, 6, 3, 1)
)
if mibBuilder.loadTexts:
    trapModemLock.setStatus(
        "current"
    )

trapTimingLock = NotificationType(
    (1, 3, 6, 1, 4, 1, 5454, 1, 60, 6, 3, 2)
)
if mibBuilder.loadTexts:
    trapTimingLock.setStatus(
        "current"
    )

trapInnerCodeLock = NotificationType(
    (1, 3, 6, 1, 4, 1, 5454, 1, 60, 6, 3, 3)
)
if mibBuilder.loadTexts:
    trapInnerCodeLock.setStatus(
        "current"
    )

trapEqualizerLock = NotificationType(
    (1, 3, 6, 1, 4, 1, 5454, 1, 60, 6, 3, 4)
)
if mibBuilder.loadTexts:
    trapEqualizerLock.setStatus(
        "current"
    )

trapFrameSyncLock = NotificationType(
    (1, 3, 6, 1, 4, 1, 5454, 1, 60, 6, 3, 5)
)
if mibBuilder.loadTexts:
    trapFrameSyncLock.setStatus(
        "current"
    )

trapMSEMinThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 5454, 1, 60, 6, 4, 1, 1)
)
if mibBuilder.loadTexts:
    trapMSEMinThreshold.setStatus(
        "current"
    )

trapMSEMaxThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 5454, 1, 60, 6, 4, 1, 2)
)
if mibBuilder.loadTexts:
    trapMSEMaxThreshold.setStatus(
        "current"
    )

trapBERMinThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 5454, 1, 60, 6, 4, 2, 1)
)
if mibBuilder.loadTexts:
    trapBERMinThreshold.setStatus(
        "current"
    )

trapBERMaxThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 5454, 1, 60, 6, 4, 2, 2)
)
if mibBuilder.loadTexts:
    trapBERMaxThreshold.setStatus(
        "current"
    )

trapFERMinThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 5454, 1, 60, 6, 4, 3, 1)
)
if mibBuilder.loadTexts:
    trapFERMinThreshold.setStatus(
        "current"
    )

trapFERMaxThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 5454, 1, 60, 6, 4, 3, 2)
)
if mibBuilder.loadTexts:
    trapFERMaxThreshold.setStatus(
        "current"
    )

trapRSSIMinThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 5454, 1, 60, 6, 4, 4, 1)
)
if mibBuilder.loadTexts:
    trapRSSIMinThreshold.setStatus(
        "current"
    )

trapRSSIMaxThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 5454, 1, 60, 6, 4, 4, 2)
)
if mibBuilder.loadTexts:
    trapRSSIMaxThreshold.setStatus(
        "current"
    )

trapIDUTempMinThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 5454, 1, 60, 6, 4, 5, 1)
)
if mibBuilder.loadTexts:
    trapIDUTempMinThreshold.setStatus(
        "current"
    )

trapIDUTempMaxThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 5454, 1, 60, 6, 4, 5, 2)
)
if mibBuilder.loadTexts:
    trapIDUTempMaxThreshold.setStatus(
        "current"
    )

trapODUTempMinThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 5454, 1, 60, 6, 4, 6, 1)
)
if mibBuilder.loadTexts:
    trapODUTempMinThreshold.setStatus(
        "current"
    )

trapODUTempMaxThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 5454, 1, 60, 6, 4, 6, 2)
)
if mibBuilder.loadTexts:
    trapODUTempMaxThreshold.setStatus(
        "current"
    )

trapInPortUtilMinThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 5454, 1, 60, 6, 4, 7, 1)
)
if mibBuilder.loadTexts:
    trapInPortUtilMinThreshold.setStatus(
        "current"
    )

trapInPortUtilMaxThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 5454, 1, 60, 6, 4, 7, 2)
)
if mibBuilder.loadTexts:
    trapInPortUtilMaxThreshold.setStatus(
        "current"
    )

trapOutPortUtilMinThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 5454, 1, 60, 6, 4, 8, 1)
)
if mibBuilder.loadTexts:
    trapOutPortUtilMinThreshold.setStatus(
        "current"
    )

trapOutPortUtilMaxThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 5454, 1, 60, 6, 4, 8, 2)
)
if mibBuilder.loadTexts:
    trapOutPortUtilMaxThreshold.setStatus(
        "current"
    )

trapStandbyLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 5454, 1, 60, 6, 5, 1)
)
if mibBuilder.loadTexts:
    trapStandbyLinkDown.setStatus(
        "current"
    )

trapStandbyLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 5454, 1, 60, 6, 5, 2)
)
if mibBuilder.loadTexts:
    trapStandbyLinkUp.setStatus(
        "current"
    )

trapSwitchover = NotificationType(
    (1, 3, 6, 1, 4, 1, 5454, 1, 60, 6, 5, 3)
)
if mibBuilder.loadTexts:
    trapSwitchover.setStatus(
        "current"
    )

trapEth1StatusUpdate = NotificationType(
    (1, 3, 6, 1, 4, 1, 5454, 1, 60, 6, 6, 1, 1)
)
if mibBuilder.loadTexts:
    trapEth1StatusUpdate.setStatus(
        "current"
    )

trapEth2StatusUpdate = NotificationType(
    (1, 3, 6, 1, 4, 1, 5454, 1, 60, 6, 6, 1, 2)
)
if mibBuilder.loadTexts:
    trapEth2StatusUpdate.setStatus(
        "current"
    )

trapEth3StatusUpdate = NotificationType(
    (1, 3, 6, 1, 4, 1, 5454, 1, 60, 6, 6, 1, 3)
)
if mibBuilder.loadTexts:
    trapEth3StatusUpdate.setStatus(
        "current"
    )

trapEth4StatusUpdate = NotificationType(
    (1, 3, 6, 1, 4, 1, 5454, 1, 60, 6, 6, 1, 4)
)
if mibBuilder.loadTexts:
    trapEth4StatusUpdate.setStatus(
        "current"
    )

trapDownShift = NotificationType(
    (1, 3, 6, 1, 4, 1, 5454, 1, 60, 6, 8)
)
if mibBuilder.loadTexts:
    trapDownShift.setStatus(
        "current"
    )

trapRapidPortShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 5454, 1, 60, 6, 9)
)
if mibBuilder.loadTexts:
    trapRapidPortShutdown.setStatus(
        "current"
    )

trapRPSPortUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 5454, 1, 60, 6, 10)
)
if mibBuilder.loadTexts:
    trapRPSPortUp.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TRANGO-APEX-TRAP-MIB",
    **{"DisplayString": DisplayString,
       "trangotrap": trangotrap,
       "trapReboot": trapReboot,
       "trapStartUp": trapStartUp,
       "traplock": traplock,
       "trapModemLock": trapModemLock,
       "trapTimingLock": trapTimingLock,
       "trapInnerCodeLock": trapInnerCodeLock,
       "trapEqualizerLock": trapEqualizerLock,
       "trapFrameSyncLock": trapFrameSyncLock,
       "trapthreshold": trapthreshold,
       "trapmse": trapmse,
       "trapMSEMinThreshold": trapMSEMinThreshold,
       "trapMSEMaxThreshold": trapMSEMaxThreshold,
       "trapber": trapber,
       "trapBERMinThreshold": trapBERMinThreshold,
       "trapBERMaxThreshold": trapBERMaxThreshold,
       "trapfer": trapfer,
       "trapFERMinThreshold": trapFERMinThreshold,
       "trapFERMaxThreshold": trapFERMaxThreshold,
       "traprssi": traprssi,
       "trapRSSIMinThreshold": trapRSSIMinThreshold,
       "trapRSSIMaxThreshold": trapRSSIMaxThreshold,
       "trapidutemp": trapidutemp,
       "trapIDUTempMinThreshold": trapIDUTempMinThreshold,
       "trapIDUTempMaxThreshold": trapIDUTempMaxThreshold,
       "trapodutemp": trapodutemp,
       "trapODUTempMinThreshold": trapODUTempMinThreshold,
       "trapODUTempMaxThreshold": trapODUTempMaxThreshold,
       "trapinport": trapinport,
       "trapInPortUtilMinThreshold": trapInPortUtilMinThreshold,
       "trapInPortUtilMaxThreshold": trapInPortUtilMaxThreshold,
       "trapoutport": trapoutport,
       "trapOutPortUtilMinThreshold": trapOutPortUtilMinThreshold,
       "trapOutPortUtilMaxThreshold": trapOutPortUtilMaxThreshold,
       "trapstandby": trapstandby,
       "trapStandbyLinkDown": trapStandbyLinkDown,
       "trapStandbyLinkUp": trapStandbyLinkUp,
       "trapSwitchover": trapSwitchover,
       "trapeth": trapeth,
       "trapethstatus": trapethstatus,
       "trapEth1StatusUpdate": trapEth1StatusUpdate,
       "trapEth2StatusUpdate": trapEth2StatusUpdate,
       "trapEth3StatusUpdate": trapEth3StatusUpdate,
       "trapEth4StatusUpdate": trapEth4StatusUpdate,
       "trapDownShift": trapDownShift,
       "trapRapidPortShutdown": trapRapidPortShutdown,
       "trapRPSPortUp": trapRPSPortUp}
)
