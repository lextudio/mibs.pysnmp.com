# SNMP MIB module (DANWARE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DANWARE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:22:54 2024
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

_Danware_ObjectIdentity = ObjectIdentity
danware = _Danware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8116)
)
_Netop_ObjectIdentity = ObjectIdentity
netop = _Netop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8116, 2)
)
_NetopManufacturer_Type = DisplayString
_NetopManufacturer_Object = MibScalar
netopManufacturer = _NetopManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 8116, 2, 1),
    _NetopManufacturer_Type()
)
netopManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netopManufacturer.setStatus("mandatory")


class _NetopProducts_Type(Integer32):
    """Custom type netopProducts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              10,
              20,
              21,
              22,
              23,
              24,
              25,
              30)
        )
    )
    namedValues = NamedValues(
        *(("accessserver", 24),
          ("classserver", 25),
          ("gateway", 22),
          ("guest", 1),
          ("host", 20),
          ("logserver", 23),
          ("nameserver", 21),
          ("student", 30),
          ("teacher", 10),
          ("unknown", 0))
    )


_NetopProducts_Type.__name__ = "Integer32"
_NetopProducts_Object = MibScalar
netopProducts = _NetopProducts_Object(
    (1, 3, 6, 1, 4, 1, 8116, 2, 2),
    _NetopProducts_Type()
)
netopProducts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netopProducts.setStatus("mandatory")
_NetopVersionNumber_Type = DisplayString
_NetopVersionNumber_Object = MibScalar
netopVersionNumber = _NetopVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 8116, 2, 3),
    _NetopVersionNumber_Type()
)
netopVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netopVersionNumber.setStatus("mandatory")
_NetopStatus_Type = DisplayString
_NetopStatus_Object = MibScalar
netopStatus = _NetopStatus_Object(
    (1, 3, 6, 1, 4, 1, 8116, 2, 4),
    _NetopStatus_Type()
)
netopStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netopStatus.setStatus("mandatory")
_NetopEvent_ObjectIdentity = ObjectIdentity
netopEvent = _NetopEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6)
)

# Managed Objects groups


# Notification objects

netopCallHost = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 0)
)
if mibBuilder.loadTexts:
    netopCallHost.setStatus(
        ""
    )

netopHangupHost = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 1)
)
if mibBuilder.loadTexts:
    netopHangupHost.setStatus(
        ""
    )

netopStartHelp = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 2)
)
if mibBuilder.loadTexts:
    netopStartHelp.setStatus(
        ""
    )

netopStopHelp = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 3)
)
if mibBuilder.loadTexts:
    netopStopHelp.setStatus(
        ""
    )

netopHelpDefined = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 4)
)
if mibBuilder.loadTexts:
    netopHelpDefined.setStatus(
        ""
    )

netopHelpDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 5)
)
if mibBuilder.loadTexts:
    netopHelpDeleted.setStatus(
        ""
    )

netopHelpReqReceived = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 6)
)
if mibBuilder.loadTexts:
    netopHelpReqReceived.setStatus(
        ""
    )

netopHelpReqCancel = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 7)
)
if mibBuilder.loadTexts:
    netopHelpReqCancel.setStatus(
        ""
    )

netopSesRecStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 8)
)
if mibBuilder.loadTexts:
    netopSesRecStarted.setStatus(
        ""
    )

netopSesRecStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 9)
)
if mibBuilder.loadTexts:
    netopSesRecStop.setStatus(
        ""
    )

netopACLogin = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 10)
)
if mibBuilder.loadTexts:
    netopACLogin.setStatus(
        ""
    )

netopACLogOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 11)
)
if mibBuilder.loadTexts:
    netopACLogOff.setStatus(
        ""
    )

netopUnknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 12)
)
if mibBuilder.loadTexts:
    netopUnknown.setStatus(
        ""
    )

netopHostStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 32)
)
if mibBuilder.loadTexts:
    netopHostStarted.setStatus(
        ""
    )

netopHostStopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 33)
)
if mibBuilder.loadTexts:
    netopHostStopped.setStatus(
        ""
    )

netopStartRemoteCtrl = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 34)
)
if mibBuilder.loadTexts:
    netopStartRemoteCtrl.setStatus(
        ""
    )

netopStopRemoteCtrl = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 35)
)
if mibBuilder.loadTexts:
    netopStopRemoteCtrl.setStatus(
        ""
    )

netopStartCallback = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 36)
)
if mibBuilder.loadTexts:
    netopStartCallback.setStatus(
        ""
    )

netopHelpReqSent = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 37)
)
if mibBuilder.loadTexts:
    netopHelpReqSent.setStatus(
        ""
    )

netopHstHelpReqCancel = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 38)
)
if mibBuilder.loadTexts:
    netopHstHelpReqCancel.setStatus(
        ""
    )

netopIndvSeqEnab = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 39)
)
if mibBuilder.loadTexts:
    netopIndvSeqEnab.setStatus(
        ""
    )

netopIndvSeqDisab = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 40)
)
if mibBuilder.loadTexts:
    netopIndvSeqDisab.setStatus(
        ""
    )

netopSecRoleAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 41)
)
if mibBuilder.loadTexts:
    netopSecRoleAdded.setStatus(
        ""
    )

netopSecRoleDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 42)
)
if mibBuilder.loadTexts:
    netopSecRoleDeleted.setStatus(
        ""
    )

netopSecRoleChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 43)
)
if mibBuilder.loadTexts:
    netopSecRoleChange.setStatus(
        ""
    )

netopGstGrpAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 44)
)
if mibBuilder.loadTexts:
    netopGstGrpAdded.setStatus(
        ""
    )

netopGstGrpDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 45)
)
if mibBuilder.loadTexts:
    netopGstGrpDeleted.setStatus(
        ""
    )

netopGstGrpChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 46)
)
if mibBuilder.loadTexts:
    netopGstGrpChange.setStatus(
        ""
    )

netopPWEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 47)
)
if mibBuilder.loadTexts:
    netopPWEnabled.setStatus(
        ""
    )

netopPWDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 48)
)
if mibBuilder.loadTexts:
    netopPWDisabled.setStatus(
        ""
    )

netopPWChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 49)
)
if mibBuilder.loadTexts:
    netopPWChange.setStatus(
        ""
    )

netopCallBEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 50)
)
if mibBuilder.loadTexts:
    netopCallBEnabled.setStatus(
        ""
    )

netopCallBDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 51)
)
if mibBuilder.loadTexts:
    netopCallBDisabled.setStatus(
        ""
    )

netopCallBChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 52)
)
if mibBuilder.loadTexts:
    netopCallBChange.setStatus(
        ""
    )

netopConfAccEnab = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 53)
)
if mibBuilder.loadTexts:
    netopConfAccEnab.setStatus(
        ""
    )

netopConfAccDisab = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 54)
)
if mibBuilder.loadTexts:
    netopConfAccDisab.setStatus(
        ""
    )

netopGatewCallb = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 64)
)
if mibBuilder.loadTexts:
    netopGatewCallb.setStatus(
        ""
    )

netopGatewIndvDef = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 65)
)
if mibBuilder.loadTexts:
    netopGatewIndvDef.setStatus(
        ""
    )

netopGatewIndvDEL = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 66)
)
if mibBuilder.loadTexts:
    netopGatewIndvDEL.setStatus(
        ""
    )

netopGatewGstAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 67)
)
if mibBuilder.loadTexts:
    netopGatewGstAdded.setStatus(
        ""
    )

netopGatewGstDelete = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 68)
)
if mibBuilder.loadTexts:
    netopGatewGstDelete.setStatus(
        ""
    )

netopGatewGstChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 69)
)
if mibBuilder.loadTexts:
    netopGatewGstChange.setStatus(
        ""
    )

netopGatewPWEnab = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 70)
)
if mibBuilder.loadTexts:
    netopGatewPWEnab.setStatus(
        ""
    )

netopGatewPWDisab = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 71)
)
if mibBuilder.loadTexts:
    netopGatewPWDisab.setStatus(
        ""
    )

netopGatewPWChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 72)
)
if mibBuilder.loadTexts:
    netopGatewPWChange.setStatus(
        ""
    )

netopGatewCallbEnab = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 73)
)
if mibBuilder.loadTexts:
    netopGatewCallbEnab.setStatus(
        ""
    )

netopGatewCallbDisab = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 74)
)
if mibBuilder.loadTexts:
    netopGatewCallbDisab.setStatus(
        ""
    )

netopGatewCallbChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 75)
)
if mibBuilder.loadTexts:
    netopGatewCallbChange.setStatus(
        ""
    )

netopFileReceive = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 96)
)
if mibBuilder.loadTexts:
    netopFileReceive.setStatus(
        ""
    )

netopFileSent = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 97)
)
if mibBuilder.loadTexts:
    netopFileSent.setStatus(
        ""
    )

netopBooted = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 98)
)
if mibBuilder.loadTexts:
    netopBooted.setStatus(
        ""
    )

netopConectionLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 99)
)
if mibBuilder.loadTexts:
    netopConectionLost.setStatus(
        ""
    )

netopPassWordRejected = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 100)
)
if mibBuilder.loadTexts:
    netopPassWordRejected.setStatus(
        ""
    )

netopConfAccessDenied = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 101)
)
if mibBuilder.loadTexts:
    netopConfAccessDenied.setStatus(
        ""
    )

netopASPWRejected = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 102)
)
if mibBuilder.loadTexts:
    netopASPWRejected.setStatus(
        ""
    )

netopASAdminChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 103)
)
if mibBuilder.loadTexts:
    netopASAdminChange.setStatus(
        ""
    )

netopEventLoggingFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 112)
)
if mibBuilder.loadTexts:
    netopEventLoggingFailed.setStatus(
        ""
    )

netopSNMPLoggingFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 113)
)
if mibBuilder.loadTexts:
    netopSNMPLoggingFailed.setStatus(
        ""
    )

netopRCStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 114)
)
if mibBuilder.loadTexts:
    netopRCStarted.setStatus(
        ""
    )

netopRCStopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 115)
)
if mibBuilder.loadTexts:
    netopRCStopped.setStatus(
        ""
    )

netopFileTrStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 116)
)
if mibBuilder.loadTexts:
    netopFileTrStarted.setStatus(
        ""
    )

netopFileTrStopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 117)
)
if mibBuilder.loadTexts:
    netopFileTrStopped.setStatus(
        ""
    )

netopGChatStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 118)
)
if mibBuilder.loadTexts:
    netopGChatStarted.setStatus(
        ""
    )

netopGChatStopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 119)
)
if mibBuilder.loadTexts:
    netopGChatStopped.setStatus(
        ""
    )

netopGAudioStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 120)
)
if mibBuilder.loadTexts:
    netopGAudioStarted.setStatus(
        ""
    )

netopGAudioStopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 121)
)
if mibBuilder.loadTexts:
    netopGAudioStopped.setStatus(
        ""
    )

netopClipReceived = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 122)
)
if mibBuilder.loadTexts:
    netopClipReceived.setStatus(
        ""
    )

netopClipSent = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 123)
)
if mibBuilder.loadTexts:
    netopClipSent.setStatus(
        ""
    )

netopRrintReceived = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 124)
)
if mibBuilder.loadTexts:
    netopRrintReceived.setStatus(
        ""
    )

netopPrintSent = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 125)
)
if mibBuilder.loadTexts:
    netopPrintSent.setStatus(
        ""
    )

netopCommProfileStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 126)
)
if mibBuilder.loadTexts:
    netopCommProfileStart.setStatus(
        ""
    )

netopCommProfileStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 127)
)
if mibBuilder.loadTexts:
    netopCommProfileStop.setStatus(
        ""
    )

netopLogLocalOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 128)
)
if mibBuilder.loadTexts:
    netopLogLocalOn.setStatus(
        ""
    )

netopLogLocalOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 129)
)
if mibBuilder.loadTexts:
    netopLogLocalOff.setStatus(
        ""
    )

netopLogLocalChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 130)
)
if mibBuilder.loadTexts:
    netopLogLocalChange.setStatus(
        ""
    )

netopLogServerOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 131)
)
if mibBuilder.loadTexts:
    netopLogServerOn.setStatus(
        ""
    )

netopLogServerOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 132)
)
if mibBuilder.loadTexts:
    netopLogServerOff.setStatus(
        ""
    )

netopIsLogServer = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 133)
)
if mibBuilder.loadTexts:
    netopIsLogServer.setStatus(
        ""
    )

netopIsNotLogServer = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 134)
)
if mibBuilder.loadTexts:
    netopIsNotLogServer.setStatus(
        ""
    )

netopLogEventlogOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 135)
)
if mibBuilder.loadTexts:
    netopLogEventlogOn.setStatus(
        ""
    )

netopLogEventlogOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 136)
)
if mibBuilder.loadTexts:
    netopLogEventlogOff.setStatus(
        ""
    )

netopLogSNMPOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 137)
)
if mibBuilder.loadTexts:
    netopLogSNMPOn.setStatus(
        ""
    )

netopLogSNMPOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 138)
)
if mibBuilder.loadTexts:
    netopLogSNMPOff.setStatus(
        ""
    )

netopKbdLock = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 139)
)
if mibBuilder.loadTexts:
    netopKbdLock.setStatus(
        ""
    )

netopKbdUnlock = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 140)
)
if mibBuilder.loadTexts:
    netopKbdUnlock.setStatus(
        ""
    )

netopScrBlank = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 141)
)
if mibBuilder.loadTexts:
    netopScrBlank.setStatus(
        ""
    )

netopScrUnblank = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 142)
)
if mibBuilder.loadTexts:
    netopScrUnblank.setStatus(
        ""
    )

netopLogoff = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 143)
)
if mibBuilder.loadTexts:
    netopLogoff.setStatus(
        ""
    )

netopGWLogin = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 144)
)
if mibBuilder.loadTexts:
    netopGWLogin.setStatus(
        ""
    )

netopOptWaitStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 145)
)
if mibBuilder.loadTexts:
    netopOptWaitStart.setStatus(
        ""
    )

netopOptLoadStar = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 146)
)
if mibBuilder.loadTexts:
    netopOptLoadStar.setStatus(
        ""
    )

netopOptMinStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 147)
)
if mibBuilder.loadTexts:
    netopOptMinStart.setStatus(
        ""
    )

netopOptStealth = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 148)
)
if mibBuilder.loadTexts:
    netopOptStealth.setStatus(
        ""
    )

netopOptMinConn = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 149)
)
if mibBuilder.loadTexts:
    netopOptMinConn.setStatus(
        ""
    )

netopOptOnTop = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 150)
)
if mibBuilder.loadTexts:
    netopOptOnTop.setStatus(
        ""
    )

netopOptShowFile = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 151)
)
if mibBuilder.loadTexts:
    netopOptShowFile.setStatus(
        ""
    )

netopOptKeepAlive = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 152)
)
if mibBuilder.loadTexts:
    netopOptKeepAlive.setStatus(
        ""
    )

netopOptBootHangUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 153)
)
if mibBuilder.loadTexts:
    netopOptBootHangUp.setStatus(
        ""
    )

netopOptLogOffHangUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 154)
)
if mibBuilder.loadTexts:
    netopOptLogOffHangUp.setStatus(
        ""
    )

netopOptNaming = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 155)
)
if mibBuilder.loadTexts:
    netopOptNaming.setStatus(
        ""
    )

netopOptPublic = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 156)
)
if mibBuilder.loadTexts:
    netopOptPublic.setStatus(
        ""
    )

netopOptNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 157)
)
if mibBuilder.loadTexts:
    netopOptNotification.setStatus(
        ""
    )

netopOptHlpDescr = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 158)
)
if mibBuilder.loadTexts:
    netopOptHlpDescr.setStatus(
        ""
    )

netopOptHlpProvid = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 159)
)
if mibBuilder.loadTexts:
    netopOptHlpProvid.setStatus(
        ""
    )

netopOptHlpComm = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 160)
)
if mibBuilder.loadTexts:
    netopOptHlpComm.setStatus(
        ""
    )

netopOptHlpAdr = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 161)
)
if mibBuilder.loadTexts:
    netopOptHlpAdr.setStatus(
        ""
    )

netopOptHlpIcon = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 162)
)
if mibBuilder.loadTexts:
    netopOptHlpIcon.setStatus(
        ""
    )

netopOptAudDuplex = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 163)
)
if mibBuilder.loadTexts:
    netopOptAudDuplex.setStatus(
        ""
    )

netopOptAudSilence = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 164)
)
if mibBuilder.loadTexts:
    netopOptAudSilence.setStatus(
        ""
    )

netopOptAudLineHold = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 165)
)
if mibBuilder.loadTexts:
    netopOptAudLineHold.setStatus(
        ""
    )

netopOptNNSChg = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 166)
)
if mibBuilder.loadTexts:
    netopOptNNSChg.setStatus(
        ""
    )

netopMaintGuest = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 167)
)
if mibBuilder.loadTexts:
    netopMaintGuest.setStatus(
        ""
    )

netopMaintGW = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 168)
)
if mibBuilder.loadTexts:
    netopMaintGW.setStatus(
        ""
    )

netopMaintOther = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 169)
)
if mibBuilder.loadTexts:
    netopMaintOther.setStatus(
        ""
    )

netopMaintExit = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 170)
)
if mibBuilder.loadTexts:
    netopMaintExit.setStatus(
        ""
    )

netopMaintProtect = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 171)
)
if mibBuilder.loadTexts:
    netopMaintProtect.setStatus(
        ""
    )

netopMaintPW = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 172)
)
if mibBuilder.loadTexts:
    netopMaintPW.setStatus(
        ""
    )

netopAccessAllowance = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 173)
)
if mibBuilder.loadTexts:
    netopAccessAllowance.setStatus(
        ""
    )

netopAccessMACIP = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 174)
)
if mibBuilder.loadTexts:
    netopAccessMACIP.setStatus(
        ""
    )

netopAccessFTrans = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 175)
)
if mibBuilder.loadTexts:
    netopAccessFTrans.setStatus(
        ""
    )

netopSSGroupIDChg = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 176)
)
if mibBuilder.loadTexts:
    netopSSGroupIDChg.setStatus(
        ""
    )

netopPWRejectLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 177)
)
if mibBuilder.loadTexts:
    netopPWRejectLimit.setStatus(
        ""
    )

netopNameServerStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 178)
)
if mibBuilder.loadTexts:
    netopNameServerStart.setStatus(
        ""
    )

netopNameServerStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 179)
)
if mibBuilder.loadTexts:
    netopNameServerStop.setStatus(
        ""
    )

netopSecurityServerStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 180)
)
if mibBuilder.loadTexts:
    netopSecurityServerStart.setStatus(
        ""
    )

netopSecurityServerStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 181)
)
if mibBuilder.loadTexts:
    netopSecurityServerStop.setStatus(
        ""
    )

netopGatewayStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 182)
)
if mibBuilder.loadTexts:
    netopGatewayStart.setStatus(
        ""
    )

netopGatwayStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 183)
)
if mibBuilder.loadTexts:
    netopGatwayStop.setStatus(
        ""
    )

netopOptLockHangUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 184)
)
if mibBuilder.loadTexts:
    netopOptLockHangUp.setStatus(
        ""
    )

netopOptNothingHangUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 185)
)
if mibBuilder.loadTexts:
    netopOptNothingHangUp.setStatus(
        ""
    )

netopOptUserName = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 186)
)
if mibBuilder.loadTexts:
    netopOptUserName.setStatus(
        ""
    )

netopFMStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 187)
)
if mibBuilder.loadTexts:
    netopFMStarted.setStatus(
        ""
    )

netopFMStopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 188)
)
if mibBuilder.loadTexts:
    netopFMStopped.setStatus(
        ""
    )

netopHChatStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 189)
)
if mibBuilder.loadTexts:
    netopHChatStarted.setStatus(
        ""
    )

netopHChatStopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 190)
)
if mibBuilder.loadTexts:
    netopHChatStopped.setStatus(
        ""
    )

netopHAudioStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 191)
)
if mibBuilder.loadTexts:
    netopHAudioStarted.setStatus(
        ""
    )

netopHAudioStopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 192)
)
if mibBuilder.loadTexts:
    netopHAudioStopped.setStatus(
        ""
    )

netopCommunicationStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 193)
)
if mibBuilder.loadTexts:
    netopCommunicationStarted.setStatus(
        ""
    )

netopCommunicationStopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 194)
)
if mibBuilder.loadTexts:
    netopCommunicationStopped.setStatus(
        ""
    )

netopRunScript = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 195)
)
if mibBuilder.loadTexts:
    netopRunScript.setStatus(
        ""
    )

netopRunProgram = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 196)
)
if mibBuilder.loadTexts:
    netopRunProgram.setStatus(
        ""
    )

netopExecuteCommand = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 197)
)
if mibBuilder.loadTexts:
    netopExecuteCommand.setStatus(
        ""
    )

netopGatewGrpDefined = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 198)
)
if mibBuilder.loadTexts:
    netopGatewGrpDefined.setStatus(
        ""
    )

netopGatewGrpDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 199)
)
if mibBuilder.loadTexts:
    netopGatewGrpDeleted.setStatus(
        ""
    )

netopGatewAccessAllowed = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 200)
)
if mibBuilder.loadTexts:
    netopGatewAccessAllowed.setStatus(
        ""
    )

netopGatewNNSGDIChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 201)
)
if mibBuilder.loadTexts:
    netopGatewNNSGDIChanged.setStatus(
        ""
    )

netopAccessServerPWChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 202)
)
if mibBuilder.loadTexts:
    netopAccessServerPWChanged.setStatus(
        ""
    )

netopInventoryReceived = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 203)
)
if mibBuilder.loadTexts:
    netopInventoryReceived.setStatus(
        ""
    )

netopMessageSent = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 204)
)
if mibBuilder.loadTexts:
    netopMessageSent.setStatus(
        ""
    )

netopInventorySent = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 205)
)
if mibBuilder.loadTexts:
    netopInventorySent.setStatus(
        ""
    )

netopMessageReceived = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 206)
)
if mibBuilder.loadTexts:
    netopMessageReceived.setStatus(
        ""
    )

netopTimeoutLimitExeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 207)
)
if mibBuilder.loadTexts:
    netopTimeoutLimitExeded.setStatus(
        ""
    )

netopAuthenticatedUser = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 208)
)
if mibBuilder.loadTexts:
    netopAuthenticatedUser.setStatus(
        ""
    )

netopGatewayPWRejected = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 209)
)
if mibBuilder.loadTexts:
    netopGatewayPWRejected.setStatus(
        ""
    )

netopWebUpdateCheck = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 210)
)
if mibBuilder.loadTexts:
    netopWebUpdateCheck.setStatus(
        ""
    )

netopWebUpdateDownload = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 211)
)
if mibBuilder.loadTexts:
    netopWebUpdateDownload.setStatus(
        ""
    )

netopWebUpdateInstall = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 212)
)
if mibBuilder.loadTexts:
    netopWebUpdateInstall.setStatus(
        ""
    )

netopWebUpdateSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 213)
)
if mibBuilder.loadTexts:
    netopWebUpdateSuccess.setStatus(
        ""
    )

netopWebUpdateFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 214)
)
if mibBuilder.loadTexts:
    netopWebUpdateFailed.setStatus(
        ""
    )

netopClassServerStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 215)
)
if mibBuilder.loadTexts:
    netopClassServerStart.setStatus(
        ""
    )

netopClassServerStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 216)
)
if mibBuilder.loadTexts:
    netopClassServerStop.setStatus(
        ""
    )

netopOptMultiGuest = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 217)
)
if mibBuilder.loadTexts:
    netopOptMultiGuest.setStatus(
        ""
    )

netopRemoteMgmStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 218)
)
if mibBuilder.loadTexts:
    netopRemoteMgmStarted.setStatus(
        ""
    )

netopRemoteMgmStopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 219)
)
if mibBuilder.loadTexts:
    netopRemoteMgmStopped.setStatus(
        ""
    )

netopRemoteMgmStarted2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 220)
)
if mibBuilder.loadTexts:
    netopRemoteMgmStarted2.setStatus(
        ""
    )

netopRemoteMgmStopped2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 8116, 2, 6, 0, 221)
)
if mibBuilder.loadTexts:
    netopRemoteMgmStopped2.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DANWARE-MIB",
    **{"danware": danware,
       "netop": netop,
       "netopManufacturer": netopManufacturer,
       "netopProducts": netopProducts,
       "netopVersionNumber": netopVersionNumber,
       "netopStatus": netopStatus,
       "netopEvent": netopEvent,
       "netopCallHost": netopCallHost,
       "netopHangupHost": netopHangupHost,
       "netopStartHelp": netopStartHelp,
       "netopStopHelp": netopStopHelp,
       "netopHelpDefined": netopHelpDefined,
       "netopHelpDeleted": netopHelpDeleted,
       "netopHelpReqReceived": netopHelpReqReceived,
       "netopHelpReqCancel": netopHelpReqCancel,
       "netopSesRecStarted": netopSesRecStarted,
       "netopSesRecStop": netopSesRecStop,
       "netopACLogin": netopACLogin,
       "netopACLogOff": netopACLogOff,
       "netopUnknown": netopUnknown,
       "netopHostStarted": netopHostStarted,
       "netopHostStopped": netopHostStopped,
       "netopStartRemoteCtrl": netopStartRemoteCtrl,
       "netopStopRemoteCtrl": netopStopRemoteCtrl,
       "netopStartCallback": netopStartCallback,
       "netopHelpReqSent": netopHelpReqSent,
       "netopHstHelpReqCancel": netopHstHelpReqCancel,
       "netopIndvSeqEnab": netopIndvSeqEnab,
       "netopIndvSeqDisab": netopIndvSeqDisab,
       "netopSecRoleAdded": netopSecRoleAdded,
       "netopSecRoleDeleted": netopSecRoleDeleted,
       "netopSecRoleChange": netopSecRoleChange,
       "netopGstGrpAdded": netopGstGrpAdded,
       "netopGstGrpDeleted": netopGstGrpDeleted,
       "netopGstGrpChange": netopGstGrpChange,
       "netopPWEnabled": netopPWEnabled,
       "netopPWDisabled": netopPWDisabled,
       "netopPWChange": netopPWChange,
       "netopCallBEnabled": netopCallBEnabled,
       "netopCallBDisabled": netopCallBDisabled,
       "netopCallBChange": netopCallBChange,
       "netopConfAccEnab": netopConfAccEnab,
       "netopConfAccDisab": netopConfAccDisab,
       "netopGatewCallb": netopGatewCallb,
       "netopGatewIndvDef": netopGatewIndvDef,
       "netopGatewIndvDEL": netopGatewIndvDEL,
       "netopGatewGstAdded": netopGatewGstAdded,
       "netopGatewGstDelete": netopGatewGstDelete,
       "netopGatewGstChange": netopGatewGstChange,
       "netopGatewPWEnab": netopGatewPWEnab,
       "netopGatewPWDisab": netopGatewPWDisab,
       "netopGatewPWChange": netopGatewPWChange,
       "netopGatewCallbEnab": netopGatewCallbEnab,
       "netopGatewCallbDisab": netopGatewCallbDisab,
       "netopGatewCallbChange": netopGatewCallbChange,
       "netopFileReceive": netopFileReceive,
       "netopFileSent": netopFileSent,
       "netopBooted": netopBooted,
       "netopConectionLost": netopConectionLost,
       "netopPassWordRejected": netopPassWordRejected,
       "netopConfAccessDenied": netopConfAccessDenied,
       "netopASPWRejected": netopASPWRejected,
       "netopASAdminChange": netopASAdminChange,
       "netopEventLoggingFailed": netopEventLoggingFailed,
       "netopSNMPLoggingFailed": netopSNMPLoggingFailed,
       "netopRCStarted": netopRCStarted,
       "netopRCStopped": netopRCStopped,
       "netopFileTrStarted": netopFileTrStarted,
       "netopFileTrStopped": netopFileTrStopped,
       "netopGChatStarted": netopGChatStarted,
       "netopGChatStopped": netopGChatStopped,
       "netopGAudioStarted": netopGAudioStarted,
       "netopGAudioStopped": netopGAudioStopped,
       "netopClipReceived": netopClipReceived,
       "netopClipSent": netopClipSent,
       "netopRrintReceived": netopRrintReceived,
       "netopPrintSent": netopPrintSent,
       "netopCommProfileStart": netopCommProfileStart,
       "netopCommProfileStop": netopCommProfileStop,
       "netopLogLocalOn": netopLogLocalOn,
       "netopLogLocalOff": netopLogLocalOff,
       "netopLogLocalChange": netopLogLocalChange,
       "netopLogServerOn": netopLogServerOn,
       "netopLogServerOff": netopLogServerOff,
       "netopIsLogServer": netopIsLogServer,
       "netopIsNotLogServer": netopIsNotLogServer,
       "netopLogEventlogOn": netopLogEventlogOn,
       "netopLogEventlogOff": netopLogEventlogOff,
       "netopLogSNMPOn": netopLogSNMPOn,
       "netopLogSNMPOff": netopLogSNMPOff,
       "netopKbdLock": netopKbdLock,
       "netopKbdUnlock": netopKbdUnlock,
       "netopScrBlank": netopScrBlank,
       "netopScrUnblank": netopScrUnblank,
       "netopLogoff": netopLogoff,
       "netopGWLogin": netopGWLogin,
       "netopOptWaitStart": netopOptWaitStart,
       "netopOptLoadStar": netopOptLoadStar,
       "netopOptMinStart": netopOptMinStart,
       "netopOptStealth": netopOptStealth,
       "netopOptMinConn": netopOptMinConn,
       "netopOptOnTop": netopOptOnTop,
       "netopOptShowFile": netopOptShowFile,
       "netopOptKeepAlive": netopOptKeepAlive,
       "netopOptBootHangUp": netopOptBootHangUp,
       "netopOptLogOffHangUp": netopOptLogOffHangUp,
       "netopOptNaming": netopOptNaming,
       "netopOptPublic": netopOptPublic,
       "netopOptNotification": netopOptNotification,
       "netopOptHlpDescr": netopOptHlpDescr,
       "netopOptHlpProvid": netopOptHlpProvid,
       "netopOptHlpComm": netopOptHlpComm,
       "netopOptHlpAdr": netopOptHlpAdr,
       "netopOptHlpIcon": netopOptHlpIcon,
       "netopOptAudDuplex": netopOptAudDuplex,
       "netopOptAudSilence": netopOptAudSilence,
       "netopOptAudLineHold": netopOptAudLineHold,
       "netopOptNNSChg": netopOptNNSChg,
       "netopMaintGuest": netopMaintGuest,
       "netopMaintGW": netopMaintGW,
       "netopMaintOther": netopMaintOther,
       "netopMaintExit": netopMaintExit,
       "netopMaintProtect": netopMaintProtect,
       "netopMaintPW": netopMaintPW,
       "netopAccessAllowance": netopAccessAllowance,
       "netopAccessMACIP": netopAccessMACIP,
       "netopAccessFTrans": netopAccessFTrans,
       "netopSSGroupIDChg": netopSSGroupIDChg,
       "netopPWRejectLimit": netopPWRejectLimit,
       "netopNameServerStart": netopNameServerStart,
       "netopNameServerStop": netopNameServerStop,
       "netopSecurityServerStart": netopSecurityServerStart,
       "netopSecurityServerStop": netopSecurityServerStop,
       "netopGatewayStart": netopGatewayStart,
       "netopGatwayStop": netopGatwayStop,
       "netopOptLockHangUp": netopOptLockHangUp,
       "netopOptNothingHangUp": netopOptNothingHangUp,
       "netopOptUserName": netopOptUserName,
       "netopFMStarted": netopFMStarted,
       "netopFMStopped": netopFMStopped,
       "netopHChatStarted": netopHChatStarted,
       "netopHChatStopped": netopHChatStopped,
       "netopHAudioStarted": netopHAudioStarted,
       "netopHAudioStopped": netopHAudioStopped,
       "netopCommunicationStarted": netopCommunicationStarted,
       "netopCommunicationStopped": netopCommunicationStopped,
       "netopRunScript": netopRunScript,
       "netopRunProgram": netopRunProgram,
       "netopExecuteCommand": netopExecuteCommand,
       "netopGatewGrpDefined": netopGatewGrpDefined,
       "netopGatewGrpDeleted": netopGatewGrpDeleted,
       "netopGatewAccessAllowed": netopGatewAccessAllowed,
       "netopGatewNNSGDIChanged": netopGatewNNSGDIChanged,
       "netopAccessServerPWChanged": netopAccessServerPWChanged,
       "netopInventoryReceived": netopInventoryReceived,
       "netopMessageSent": netopMessageSent,
       "netopInventorySent": netopInventorySent,
       "netopMessageReceived": netopMessageReceived,
       "netopTimeoutLimitExeded": netopTimeoutLimitExeded,
       "netopAuthenticatedUser": netopAuthenticatedUser,
       "netopGatewayPWRejected": netopGatewayPWRejected,
       "netopWebUpdateCheck": netopWebUpdateCheck,
       "netopWebUpdateDownload": netopWebUpdateDownload,
       "netopWebUpdateInstall": netopWebUpdateInstall,
       "netopWebUpdateSuccess": netopWebUpdateSuccess,
       "netopWebUpdateFailed": netopWebUpdateFailed,
       "netopClassServerStart": netopClassServerStart,
       "netopClassServerStop": netopClassServerStop,
       "netopOptMultiGuest": netopOptMultiGuest,
       "netopRemoteMgmStarted": netopRemoteMgmStarted,
       "netopRemoteMgmStopped": netopRemoteMgmStopped,
       "netopRemoteMgmStarted2": netopRemoteMgmStarted2,
       "netopRemoteMgmStopped2": netopRemoteMgmStopped2}
)
