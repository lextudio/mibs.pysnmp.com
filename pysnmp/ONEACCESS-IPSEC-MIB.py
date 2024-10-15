# SNMP MIB module (ONEACCESS-IPSEC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ONEACCESS-IPSEC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:34:56 2024
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

(oacExpIMIPSec,
 oacExpIMIp,
 oacMIBModules) = mibBuilder.importSymbols(
    "ONEACCESS-GLOBAL-REG",
    "oacExpIMIPSec",
    "oacExpIMIp",
    "oacMIBModules")

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
 TimeInterval) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeInterval")


# MODULE-IDENTITY

oacNatMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 1, 100, 675)
)
oacNatMIBModule.setRevisions(
        ("2011-10-27 00:00",
         "2010-07-08 10:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OacIPSecNotifications_ObjectIdentity = ObjectIdentity
oacIPSecNotifications = _OacIPSecNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 4, 1)
)
_OacIsakmpNotifications_ObjectIdentity = ObjectIdentity
oacIsakmpNotifications = _OacIsakmpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 4, 2)
)

# Managed Objects groups


# Notification objects

oacIPSecSAcreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    oacIPSecSAcreated.setStatus(
        "current"
    )

oacIPSecSAremoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 4, 1, 2)
)
if mibBuilder.loadTexts:
    oacIPSecSAremoved.setStatus(
        "current"
    )

oacIPSecCmapEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 4, 1, 3)
)
if mibBuilder.loadTexts:
    oacIPSecCmapEnabled.setStatus(
        "current"
    )

oacIPSecCmapDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 4, 1, 4)
)
if mibBuilder.loadTexts:
    oacIPSecCmapDisabled.setStatus(
        "current"
    )

oacIPSecCpolEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 4, 1, 5)
)
if mibBuilder.loadTexts:
    oacIPSecCpolEnabled.setStatus(
        "current"
    )

oacIPSecCpolDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 4, 1, 6)
)
if mibBuilder.loadTexts:
    oacIPSecCpolDisabled.setStatus(
        "current"
    )

oacIPSecHwModuleDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 4, 1, 7)
)
if mibBuilder.loadTexts:
    oacIPSecHwModuleDown.setStatus(
        "current"
    )

oacISAKMPBadProposal = NotificationType(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    oacISAKMPBadProposal.setStatus(
        "current"
    )

oacISAKMPNoResponse = NotificationType(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 4, 2, 2)
)
if mibBuilder.loadTexts:
    oacISAKMPNoResponse.setStatus(
        "current"
    )

oacISAKMPConnectionEstablished = NotificationType(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 4, 2, 3)
)
if mibBuilder.loadTexts:
    oacISAKMPConnectionEstablished.setStatus(
        "current"
    )

oacISAKMPConnectionRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 4, 2, 4)
)
if mibBuilder.loadTexts:
    oacISAKMPConnectionRemoved.setStatus(
        "current"
    )

oacISAMPIPSecConnectionEstablished = NotificationType(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 4, 2, 5)
)
if mibBuilder.loadTexts:
    oacISAMPIPSecConnectionEstablished.setStatus(
        "current"
    )

oacISAKMPIPSecConnectionRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 4, 2, 6)
)
if mibBuilder.loadTexts:
    oacISAKMPIPSecConnectionRemoved.setStatus(
        "current"
    )

oacISAKMPUnknownPeer = NotificationType(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 4, 2, 7)
)
if mibBuilder.loadTexts:
    oacISAKMPUnknownPeer.setStatus(
        "current"
    )

oacISAKMPNotificationMsgReceived = NotificationType(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 4, 2, 8)
)
if mibBuilder.loadTexts:
    oacISAKMPNotificationMsgReceived.setStatus(
        "current"
    )

oacISAKMPNotificationMsgSent = NotificationType(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 4, 2, 9)
)
if mibBuilder.loadTexts:
    oacISAKMPNotificationMsgSent.setStatus(
        "current"
    )

oacISAKMPDeadPeerDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 4, 2, 10)
)
if mibBuilder.loadTexts:
    oacISAKMPDeadPeerDetected.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ONEACCESS-IPSEC-MIB",
    **{"oacNatMIBModule": oacNatMIBModule,
       "oacIPSecNotifications": oacIPSecNotifications,
       "oacIPSecSAcreated": oacIPSecSAcreated,
       "oacIPSecSAremoved": oacIPSecSAremoved,
       "oacIPSecCmapEnabled": oacIPSecCmapEnabled,
       "oacIPSecCmapDisabled": oacIPSecCmapDisabled,
       "oacIPSecCpolEnabled": oacIPSecCpolEnabled,
       "oacIPSecCpolDisabled": oacIPSecCpolDisabled,
       "oacIPSecHwModuleDown": oacIPSecHwModuleDown,
       "oacIsakmpNotifications": oacIsakmpNotifications,
       "oacISAKMPBadProposal": oacISAKMPBadProposal,
       "oacISAKMPNoResponse": oacISAKMPNoResponse,
       "oacISAKMPConnectionEstablished": oacISAKMPConnectionEstablished,
       "oacISAKMPConnectionRemoved": oacISAKMPConnectionRemoved,
       "oacISAMPIPSecConnectionEstablished": oacISAMPIPSecConnectionEstablished,
       "oacISAKMPIPSecConnectionRemoved": oacISAKMPIPSecConnectionRemoved,
       "oacISAKMPUnknownPeer": oacISAKMPUnknownPeer,
       "oacISAKMPNotificationMsgReceived": oacISAKMPNotificationMsgReceived,
       "oacISAKMPNotificationMsgSent": oacISAKMPNotificationMsgSent,
       "oacISAKMPDeadPeerDetected": oacISAKMPDeadPeerDetected}
)
