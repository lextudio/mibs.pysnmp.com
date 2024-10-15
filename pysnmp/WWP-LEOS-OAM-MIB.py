# SNMP MIB module (WWP-LEOS-OAM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WWP-LEOS-OAM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:15:00 2024
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
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(wwpLeosEtherPortDesc,
 wwpLeosEtherPortOperStatus) = mibBuilder.importSymbols(
    "WWP-LEOS-PORT-MIB",
    "wwpLeosEtherPortDesc",
    "wwpLeosEtherPortOperStatus")

(wwpModulesLeos,) = mibBuilder.importSymbols(
    "WWP-SMI",
    "wwpModulesLeos")


# MODULE-IDENTITY

wwpLeosOamMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 400)
)
wwpLeosOamMibModule.setRevisions(
        ("2008-01-03 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WwpLeosOamMIB_ObjectIdentity = ObjectIdentity
wwpLeosOamMIB = _WwpLeosOamMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 400, 1)
)
_WwpLeosOamConf_ObjectIdentity = ObjectIdentity
wwpLeosOamConf = _WwpLeosOamConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 400, 1, 1)
)
_WwpLeosOamGroups_ObjectIdentity = ObjectIdentity
wwpLeosOamGroups = _WwpLeosOamGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 400, 1, 1, 1)
)
_WwpLeosOamCompls_ObjectIdentity = ObjectIdentity
wwpLeosOamCompls = _WwpLeosOamCompls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 400, 1, 1, 2)
)
_WwpLeosOamObjs_ObjectIdentity = ObjectIdentity
wwpLeosOamObjs = _WwpLeosOamObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 400, 1, 2)
)
_WwpLeosOamTable_Object = MibTable
wwpLeosOamTable = _WwpLeosOamTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 400, 1, 2, 1)
)
if mibBuilder.loadTexts:
    wwpLeosOamTable.setStatus("current")
_WwpLeosOamEntry_Object = MibTableRow
wwpLeosOamEntry = _WwpLeosOamEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 400, 1, 2, 1, 1)
)
wwpLeosOamEntry.setIndexNames(
    (0, "WWP-LEOS-OAM-MIB", "wwpLeosOamPort"),
)
if mibBuilder.loadTexts:
    wwpLeosOamEntry.setStatus("current")


class _WwpLeosOamAdminState_Type(Integer32):
    """Custom type wwpLeosOamAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_WwpLeosOamAdminState_Type.__name__ = "Integer32"
_WwpLeosOamAdminState_Object = MibTableColumn
wwpLeosOamAdminState = _WwpLeosOamAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 400, 1, 2, 1, 1, 1),
    _WwpLeosOamAdminState_Type()
)
wwpLeosOamAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosOamAdminState.setStatus("current")


class _WwpLeosOamOperStatus_Type(Integer32):
    """Custom type wwpLeosOamOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("activeSendLocal", 4),
          ("disabled", 1),
          ("linkfault", 2),
          ("oamPeeringLocallyRejected", 7),
          ("oamPeeringRemotelyRejected", 8),
          ("operational", 9),
          ("passiveWait", 3),
          ("sendLocalAndRemote", 5),
          ("sendLocalAndRemoteOk", 6))
    )


_WwpLeosOamOperStatus_Type.__name__ = "Integer32"
_WwpLeosOamOperStatus_Object = MibTableColumn
wwpLeosOamOperStatus = _WwpLeosOamOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 400, 1, 2, 1, 1, 2),
    _WwpLeosOamOperStatus_Type()
)
wwpLeosOamOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosOamOperStatus.setStatus("current")


class _WwpLeosOamMode_Type(Integer32):
    """Custom type wwpLeosOamMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("passive", 2))
    )


_WwpLeosOamMode_Type.__name__ = "Integer32"
_WwpLeosOamMode_Object = MibTableColumn
wwpLeosOamMode = _WwpLeosOamMode_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 400, 1, 2, 1, 1, 3),
    _WwpLeosOamMode_Type()
)
wwpLeosOamMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosOamMode.setStatus("current")
_WwpLeosMaxOamPduSize_Type = Integer32
_WwpLeosMaxOamPduSize_Object = MibTableColumn
wwpLeosMaxOamPduSize = _WwpLeosMaxOamPduSize_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 400, 1, 2, 1, 1, 4),
    _WwpLeosMaxOamPduSize_Type()
)
wwpLeosMaxOamPduSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosMaxOamPduSize.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosMaxOamPduSize.setUnits("bytes")
_WwpLeosOamConfigRevision_Type = Unsigned32
_WwpLeosOamConfigRevision_Object = MibTableColumn
wwpLeosOamConfigRevision = _WwpLeosOamConfigRevision_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 400, 1, 2, 1, 1, 5),
    _WwpLeosOamConfigRevision_Type()
)
wwpLeosOamConfigRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosOamConfigRevision.setStatus("current")


class _WwpLeosOamFunctionsSupported_Type(Bits):
    """Custom type wwpLeosOamFunctionsSupported based on Bits"""
    namedValues = NamedValues(
        *(("eventSupport", 2),
          ("loopbackSupport", 1),
          ("unidirectionalSupport", 0),
          ("variableSupport", 3))
    )

_WwpLeosOamFunctionsSupported_Type.__name__ = "Bits"
_WwpLeosOamFunctionsSupported_Object = MibTableColumn
wwpLeosOamFunctionsSupported = _WwpLeosOamFunctionsSupported_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 400, 1, 2, 1, 1, 6),
    _WwpLeosOamFunctionsSupported_Type()
)
wwpLeosOamFunctionsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosOamFunctionsSupported.setStatus("current")


class _WwpLeosOamPort_Type(Integer32):
    """Custom type wwpLeosOamPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_WwpLeosOamPort_Type.__name__ = "Integer32"
_WwpLeosOamPort_Object = MibTableColumn
wwpLeosOamPort = _WwpLeosOamPort_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 400, 1, 2, 1, 1, 7),
    _WwpLeosOamPort_Type()
)
wwpLeosOamPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosOamPort.setStatus("current")


class _WwpLeosOamPduTimer_Type(Integer32):
    """Custom type wwpLeosOamPduTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_WwpLeosOamPduTimer_Type.__name__ = "Integer32"
_WwpLeosOamPduTimer_Object = MibTableColumn
wwpLeosOamPduTimer = _WwpLeosOamPduTimer_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 400, 1, 2, 1, 1, 8),
    _WwpLeosOamPduTimer_Type()
)
wwpLeosOamPduTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosOamPduTimer.setStatus("current")


class _WwpLeosOamLinkLostTimer_Type(Integer32):
    """Custom type wwpLeosOamLinkLostTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 5000),
    )


_WwpLeosOamLinkLostTimer_Type.__name__ = "Integer32"
_WwpLeosOamLinkLostTimer_Object = MibTableColumn
wwpLeosOamLinkLostTimer = _WwpLeosOamLinkLostTimer_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 400, 1, 2, 1, 1, 9),
    _WwpLeosOamLinkLostTimer_Type()
)
wwpLeosOamLinkLostTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosOamLinkLostTimer.setStatus("current")


class _WwpLeosOamPeerStatusNotifyState_Type(Integer32):
    """Custom type wwpLeosOamPeerStatusNotifyState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_WwpLeosOamPeerStatusNotifyState_Type.__name__ = "Integer32"
_WwpLeosOamPeerStatusNotifyState_Object = MibTableColumn
wwpLeosOamPeerStatusNotifyState = _WwpLeosOamPeerStatusNotifyState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 400, 1, 2, 1, 1, 10),
    _WwpLeosOamPeerStatusNotifyState_Type()
)
wwpLeosOamPeerStatusNotifyState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosOamPeerStatusNotifyState.setStatus("current")
_WwpLeosOamPeerTable_Object = MibTable
wwpLeosOamPeerTable = _WwpLeosOamPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 400, 1, 2, 2)
)
if mibBuilder.loadTexts:
    wwpLeosOamPeerTable.setStatus("current")
_WwpLeosOamPeerEntry_Object = MibTableRow
wwpLeosOamPeerEntry = _WwpLeosOamPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 400, 1, 2, 2, 1)
)
wwpLeosOamPeerEntry.setIndexNames(
    (0, "WWP-LEOS-OAM-MIB", "wwpLeosOamLocalPort"),
)
if mibBuilder.loadTexts:
    wwpLeosOamPeerEntry.setStatus("current")


class _WwpLeosOamPeerStatus_Type(Integer32):
    """Custom type wwpLeosOamPeerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_WwpLeosOamPeerStatus_Type.__name__ = "Integer32"
_WwpLeosOamPeerStatus_Object = MibTableColumn
wwpLeosOamPeerStatus = _WwpLeosOamPeerStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 400, 1, 2, 2, 1, 1),
    _WwpLeosOamPeerStatus_Type()
)
wwpLeosOamPeerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosOamPeerStatus.setStatus("current")


class _WwpLeosOamPeerMacAddress_Type(OctetString):
    """Custom type wwpLeosOamPeerMacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_WwpLeosOamPeerMacAddress_Type.__name__ = "OctetString"
_WwpLeosOamPeerMacAddress_Object = MibTableColumn
wwpLeosOamPeerMacAddress = _WwpLeosOamPeerMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 400, 1, 2, 2, 1, 2),
    _WwpLeosOamPeerMacAddress_Type()
)
wwpLeosOamPeerMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosOamPeerMacAddress.setStatus("current")


class _WwpLeosOamPeerVendorOui_Type(OctetString):
    """Custom type wwpLeosOamPeerVendorOui based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_WwpLeosOamPeerVendorOui_Type.__name__ = "OctetString"
_WwpLeosOamPeerVendorOui_Object = MibTableColumn
wwpLeosOamPeerVendorOui = _WwpLeosOamPeerVendorOui_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 400, 1, 2, 2, 1, 3),
    _WwpLeosOamPeerVendorOui_Type()
)
wwpLeosOamPeerVendorOui.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosOamPeerVendorOui.setStatus("current")
_WwpLeosOamPeerVendorInfo_Type = Unsigned32
_WwpLeosOamPeerVendorInfo_Object = MibTableColumn
wwpLeosOamPeerVendorInfo = _WwpLeosOamPeerVendorInfo_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 400, 1, 2, 2, 1, 4),
    _WwpLeosOamPeerVendorInfo_Type()
)
wwpLeosOamPeerVendorInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosOamPeerVendorInfo.setStatus("current")


class _WwpLeosOamPeerMode_Type(Integer32):
    """Custom type wwpLeosOamPeerMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("passive", 2),
          ("unknown", 3))
    )


_WwpLeosOamPeerMode_Type.__name__ = "Integer32"
_WwpLeosOamPeerMode_Object = MibTableColumn
wwpLeosOamPeerMode = _WwpLeosOamPeerMode_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 400, 1, 2, 2, 1, 5),
    _WwpLeosOamPeerMode_Type()
)
wwpLeosOamPeerMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosOamPeerMode.setStatus("current")
_WwpLeosOamPeerMaxOamPduSize_Type = Integer32
_WwpLeosOamPeerMaxOamPduSize_Object = MibTableColumn
wwpLeosOamPeerMaxOamPduSize = _WwpLeosOamPeerMaxOamPduSize_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 400, 1, 2, 2, 1, 6),
    _WwpLeosOamPeerMaxOamPduSize_Type()
)
wwpLeosOamPeerMaxOamPduSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosOamPeerMaxOamPduSize.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosOamPeerMaxOamPduSize.setUnits("bytes")
_WwpLeosOamPeerConfigRevision_Type = Unsigned32
_WwpLeosOamPeerConfigRevision_Object = MibTableColumn
wwpLeosOamPeerConfigRevision = _WwpLeosOamPeerConfigRevision_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 400, 1, 2, 2, 1, 7),
    _WwpLeosOamPeerConfigRevision_Type()
)
wwpLeosOamPeerConfigRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosOamPeerConfigRevision.setStatus("current")


class _WwpLeosOamPeerFunctionsSupported_Type(Bits):
    """Custom type wwpLeosOamPeerFunctionsSupported based on Bits"""
    namedValues = NamedValues(
        *(("eventSupport", 2),
          ("loopbackSupport", 1),
          ("unidirectionalSupport", 0),
          ("variableSupport", 3))
    )

_WwpLeosOamPeerFunctionsSupported_Type.__name__ = "Bits"
_WwpLeosOamPeerFunctionsSupported_Object = MibTableColumn
wwpLeosOamPeerFunctionsSupported = _WwpLeosOamPeerFunctionsSupported_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 400, 1, 2, 2, 1, 8),
    _WwpLeosOamPeerFunctionsSupported_Type()
)
wwpLeosOamPeerFunctionsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosOamPeerFunctionsSupported.setStatus("current")


class _WwpLeosOamLocalPort_Type(Integer32):
    """Custom type wwpLeosOamLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_WwpLeosOamLocalPort_Type.__name__ = "Integer32"
_WwpLeosOamLocalPort_Object = MibTableColumn
wwpLeosOamLocalPort = _WwpLeosOamLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 400, 1, 2, 2, 1, 9),
    _WwpLeosOamLocalPort_Type()
)
wwpLeosOamLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosOamLocalPort.setStatus("current")
_WwpLeosOamLoopbackTable_Object = MibTable
wwpLeosOamLoopbackTable = _WwpLeosOamLoopbackTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 400, 1, 2, 3)
)
if mibBuilder.loadTexts:
    wwpLeosOamLoopbackTable.setStatus("current")
_WwpLeosOamLoopbackEntry_Object = MibTableRow
wwpLeosOamLoopbackEntry = _WwpLeosOamLoopbackEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 400, 1, 2, 3, 1)
)
wwpLeosOamLoopbackEntry.setIndexNames(
    (0, "WWP-LEOS-OAM-MIB", "wwpLeosOamLoopbackPort"),
)
if mibBuilder.loadTexts:
    wwpLeosOamLoopbackEntry.setStatus("current")


class _WwpLeosOamLoopbackCommand_Type(Integer32):
    """Custom type wwpLeosOamLoopbackCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noLoopback", 1),
          ("startRemoteLoopback", 2),
          ("stopRemoteLoopback", 3))
    )


_WwpLeosOamLoopbackCommand_Type.__name__ = "Integer32"
_WwpLeosOamLoopbackCommand_Object = MibTableColumn
wwpLeosOamLoopbackCommand = _WwpLeosOamLoopbackCommand_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 400, 1, 2, 3, 1, 1),
    _WwpLeosOamLoopbackCommand_Type()
)
wwpLeosOamLoopbackCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosOamLoopbackCommand.setStatus("current")


class _WwpLeosOamLoopbackStatus_Type(Integer32):
    """Custom type wwpLeosOamLoopbackStatus based on Integer32"""
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
        *(("initiatingLoopback", 2),
          ("localLoopback", 5),
          ("noLoopback", 1),
          ("remoteLoopback", 3),
          ("terminatingLoopback", 4),
          ("unknown", 6))
    )


_WwpLeosOamLoopbackStatus_Type.__name__ = "Integer32"
_WwpLeosOamLoopbackStatus_Object = MibTableColumn
wwpLeosOamLoopbackStatus = _WwpLeosOamLoopbackStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 400, 1, 2, 3, 1, 2),
    _WwpLeosOamLoopbackStatus_Type()
)
wwpLeosOamLoopbackStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosOamLoopbackStatus.setStatus("current")


class _WwpLeosOamLoopbackIgnoreRx_Type(Integer32):
    """Custom type wwpLeosOamLoopbackIgnoreRx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 1),
          ("process", 2))
    )


_WwpLeosOamLoopbackIgnoreRx_Type.__name__ = "Integer32"
_WwpLeosOamLoopbackIgnoreRx_Object = MibTableColumn
wwpLeosOamLoopbackIgnoreRx = _WwpLeosOamLoopbackIgnoreRx_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 400, 1, 2, 3, 1, 3),
    _WwpLeosOamLoopbackIgnoreRx_Type()
)
wwpLeosOamLoopbackIgnoreRx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosOamLoopbackIgnoreRx.setStatus("current")


class _WwpLeosOamLoopbackPort_Type(Integer32):
    """Custom type wwpLeosOamLoopbackPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_WwpLeosOamLoopbackPort_Type.__name__ = "Integer32"
_WwpLeosOamLoopbackPort_Object = MibTableColumn
wwpLeosOamLoopbackPort = _WwpLeosOamLoopbackPort_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 400, 1, 2, 3, 1, 4),
    _WwpLeosOamLoopbackPort_Type()
)
wwpLeosOamLoopbackPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosOamLoopbackPort.setStatus("current")
_WwpLeosOamStatsTable_Object = MibTable
wwpLeosOamStatsTable = _WwpLeosOamStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 400, 1, 2, 4)
)
if mibBuilder.loadTexts:
    wwpLeosOamStatsTable.setStatus("current")
_WwpLeosOamStatsEntry_Object = MibTableRow
wwpLeosOamStatsEntry = _WwpLeosOamStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 400, 1, 2, 4, 1)
)
wwpLeosOamStatsEntry.setIndexNames(
    (0, "WWP-LEOS-OAM-MIB", "wwpLeosOamStatsPort"),
)
if mibBuilder.loadTexts:
    wwpLeosOamStatsEntry.setStatus("current")
_WwpLeosOamInformationTx_Type = Counter32
_WwpLeosOamInformationTx_Object = MibTableColumn
wwpLeosOamInformationTx = _WwpLeosOamInformationTx_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 400, 1, 2, 4, 1, 1),
    _WwpLeosOamInformationTx_Type()
)
wwpLeosOamInformationTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosOamInformationTx.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosOamInformationTx.setUnits("frames")
_WwpLeosOamInformationRx_Type = Counter32
_WwpLeosOamInformationRx_Object = MibTableColumn
wwpLeosOamInformationRx = _WwpLeosOamInformationRx_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 400, 1, 2, 4, 1, 2),
    _WwpLeosOamInformationRx_Type()
)
wwpLeosOamInformationRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosOamInformationRx.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosOamInformationRx.setUnits("frames")
_WwpLeosOamUniqueEventNotificationTx_Type = Counter32
_WwpLeosOamUniqueEventNotificationTx_Object = MibTableColumn
wwpLeosOamUniqueEventNotificationTx = _WwpLeosOamUniqueEventNotificationTx_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 400, 1, 2, 4, 1, 3),
    _WwpLeosOamUniqueEventNotificationTx_Type()
)
wwpLeosOamUniqueEventNotificationTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosOamUniqueEventNotificationTx.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosOamUniqueEventNotificationTx.setUnits("frames")
_WwpLeosOamUniqueEventNotificationRx_Type = Counter32
_WwpLeosOamUniqueEventNotificationRx_Object = MibTableColumn
wwpLeosOamUniqueEventNotificationRx = _WwpLeosOamUniqueEventNotificationRx_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 400, 1, 2, 4, 1, 4),
    _WwpLeosOamUniqueEventNotificationRx_Type()
)
wwpLeosOamUniqueEventNotificationRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosOamUniqueEventNotificationRx.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosOamUniqueEventNotificationRx.setUnits("frames")
_WwpLeosOamLoopbackControlTx_Type = Counter32
_WwpLeosOamLoopbackControlTx_Object = MibTableColumn
wwpLeosOamLoopbackControlTx = _WwpLeosOamLoopbackControlTx_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 400, 1, 2, 4, 1, 5),
    _WwpLeosOamLoopbackControlTx_Type()
)
wwpLeosOamLoopbackControlTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosOamLoopbackControlTx.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosOamLoopbackControlTx.setUnits("frames")
_WwpLeosOamLoopbackControlRx_Type = Counter32
_WwpLeosOamLoopbackControlRx_Object = MibTableColumn
wwpLeosOamLoopbackControlRx = _WwpLeosOamLoopbackControlRx_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 400, 1, 2, 4, 1, 6),
    _WwpLeosOamLoopbackControlRx_Type()
)
wwpLeosOamLoopbackControlRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosOamLoopbackControlRx.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosOamLoopbackControlRx.setUnits("frames")
_WwpLeosOamVariableRequestTx_Type = Counter32
_WwpLeosOamVariableRequestTx_Object = MibTableColumn
wwpLeosOamVariableRequestTx = _WwpLeosOamVariableRequestTx_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 400, 1, 2, 4, 1, 7),
    _WwpLeosOamVariableRequestTx_Type()
)
wwpLeosOamVariableRequestTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosOamVariableRequestTx.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosOamVariableRequestTx.setUnits("frames")
_WwpLeosOamVariableRequestRx_Type = Counter32
_WwpLeosOamVariableRequestRx_Object = MibTableColumn
wwpLeosOamVariableRequestRx = _WwpLeosOamVariableRequestRx_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 400, 1, 2, 4, 1, 8),
    _WwpLeosOamVariableRequestRx_Type()
)
wwpLeosOamVariableRequestRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosOamVariableRequestRx.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosOamVariableRequestRx.setUnits("frames")
_WwpLeosOamVariableResponseTx_Type = Counter32
_WwpLeosOamVariableResponseTx_Object = MibTableColumn
wwpLeosOamVariableResponseTx = _WwpLeosOamVariableResponseTx_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 400, 1, 2, 4, 1, 9),
    _WwpLeosOamVariableResponseTx_Type()
)
wwpLeosOamVariableResponseTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosOamVariableResponseTx.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosOamVariableResponseTx.setUnits("frames")
_WwpLeosOamVariableResponseRx_Type = Counter32
_WwpLeosOamVariableResponseRx_Object = MibTableColumn
wwpLeosOamVariableResponseRx = _WwpLeosOamVariableResponseRx_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 400, 1, 2, 4, 1, 10),
    _WwpLeosOamVariableResponseRx_Type()
)
wwpLeosOamVariableResponseRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosOamVariableResponseRx.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosOamVariableResponseRx.setUnits("frames")
_WwpLeosOamOrgSpecificTx_Type = Counter32
_WwpLeosOamOrgSpecificTx_Object = MibTableColumn
wwpLeosOamOrgSpecificTx = _WwpLeosOamOrgSpecificTx_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 400, 1, 2, 4, 1, 11),
    _WwpLeosOamOrgSpecificTx_Type()
)
wwpLeosOamOrgSpecificTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosOamOrgSpecificTx.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosOamOrgSpecificTx.setUnits("frames")
_WwpLeosOamOrgSpecificRx_Type = Counter32
_WwpLeosOamOrgSpecificRx_Object = MibTableColumn
wwpLeosOamOrgSpecificRx = _WwpLeosOamOrgSpecificRx_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 400, 1, 2, 4, 1, 12),
    _WwpLeosOamOrgSpecificRx_Type()
)
wwpLeosOamOrgSpecificRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosOamOrgSpecificRx.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosOamOrgSpecificRx.setUnits("frames")
_WwpLeosOamUnsupportedCodesTx_Type = Counter32
_WwpLeosOamUnsupportedCodesTx_Object = MibTableColumn
wwpLeosOamUnsupportedCodesTx = _WwpLeosOamUnsupportedCodesTx_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 400, 1, 2, 4, 1, 13),
    _WwpLeosOamUnsupportedCodesTx_Type()
)
wwpLeosOamUnsupportedCodesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosOamUnsupportedCodesTx.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosOamUnsupportedCodesTx.setUnits("frames")
_WwpLeosOamUnsupportedCodesRx_Type = Counter32
_WwpLeosOamUnsupportedCodesRx_Object = MibTableColumn
wwpLeosOamUnsupportedCodesRx = _WwpLeosOamUnsupportedCodesRx_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 400, 1, 2, 4, 1, 14),
    _WwpLeosOamUnsupportedCodesRx_Type()
)
wwpLeosOamUnsupportedCodesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosOamUnsupportedCodesRx.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosOamUnsupportedCodesRx.setUnits("frames")
_WwpLeosOamframesLostDueToOam_Type = Counter32
_WwpLeosOamframesLostDueToOam_Object = MibTableColumn
wwpLeosOamframesLostDueToOam = _WwpLeosOamframesLostDueToOam_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 400, 1, 2, 4, 1, 15),
    _WwpLeosOamframesLostDueToOam_Type()
)
wwpLeosOamframesLostDueToOam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosOamframesLostDueToOam.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosOamframesLostDueToOam.setUnits("frames")


class _WwpLeosOamStatsPort_Type(Integer32):
    """Custom type wwpLeosOamStatsPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_WwpLeosOamStatsPort_Type.__name__ = "Integer32"
_WwpLeosOamStatsPort_Object = MibTableColumn
wwpLeosOamStatsPort = _WwpLeosOamStatsPort_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 400, 1, 2, 4, 1, 16),
    _WwpLeosOamStatsPort_Type()
)
wwpLeosOamStatsPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosOamStatsPort.setStatus("current")
_WwpLeosOamDuplicateEventNotificationTx_Type = Counter32
_WwpLeosOamDuplicateEventNotificationTx_Object = MibTableColumn
wwpLeosOamDuplicateEventNotificationTx = _WwpLeosOamDuplicateEventNotificationTx_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 400, 1, 2, 4, 1, 17),
    _WwpLeosOamDuplicateEventNotificationTx_Type()
)
wwpLeosOamDuplicateEventNotificationTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosOamDuplicateEventNotificationTx.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosOamDuplicateEventNotificationTx.setUnits("frames")
_WwpLeosOamDuplicateEventNotificationRx_Type = Counter32
_WwpLeosOamDuplicateEventNotificationRx_Object = MibTableColumn
wwpLeosOamDuplicateEventNotificationRx = _WwpLeosOamDuplicateEventNotificationRx_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 400, 1, 2, 4, 1, 18),
    _WwpLeosOamDuplicateEventNotificationRx_Type()
)
wwpLeosOamDuplicateEventNotificationRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosOamDuplicateEventNotificationRx.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosOamDuplicateEventNotificationRx.setUnits("frames")


class _WwpLeosOamSystemEnableDisable_Type(Integer32):
    """Custom type wwpLeosOamSystemEnableDisable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_WwpLeosOamSystemEnableDisable_Type.__name__ = "Integer32"
_WwpLeosOamSystemEnableDisable_Object = MibScalar
wwpLeosOamSystemEnableDisable = _WwpLeosOamSystemEnableDisable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 400, 1, 2, 5),
    _WwpLeosOamSystemEnableDisable_Type()
)
wwpLeosOamSystemEnableDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosOamSystemEnableDisable.setStatus("current")
_WwpLeosOamEventConfigTable_Object = MibTable
wwpLeosOamEventConfigTable = _WwpLeosOamEventConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 400, 1, 2, 6)
)
if mibBuilder.loadTexts:
    wwpLeosOamEventConfigTable.setStatus("current")
_WwpLeosOamEventConfigEntry_Object = MibTableRow
wwpLeosOamEventConfigEntry = _WwpLeosOamEventConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 400, 1, 2, 6, 1)
)
wwpLeosOamEventConfigEntry.setIndexNames(
    (0, "WWP-LEOS-OAM-MIB", "wwpLeosOamEventPort"),
)
if mibBuilder.loadTexts:
    wwpLeosOamEventConfigEntry.setStatus("current")


class _WwpLeosOamEventPort_Type(Integer32):
    """Custom type wwpLeosOamEventPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_WwpLeosOamEventPort_Type.__name__ = "Integer32"
_WwpLeosOamEventPort_Object = MibTableColumn
wwpLeosOamEventPort = _WwpLeosOamEventPort_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 400, 1, 2, 6, 1, 1),
    _WwpLeosOamEventPort_Type()
)
wwpLeosOamEventPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosOamEventPort.setStatus("current")


class _WwpLeosOamErrFramePeriodWindow_Type(Unsigned32):
    """Custom type wwpLeosOamErrFramePeriodWindow based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(14880, 8928000),
    )


_WwpLeosOamErrFramePeriodWindow_Type.__name__ = "Unsigned32"
_WwpLeosOamErrFramePeriodWindow_Object = MibTableColumn
wwpLeosOamErrFramePeriodWindow = _WwpLeosOamErrFramePeriodWindow_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 400, 1, 2, 6, 1, 2),
    _WwpLeosOamErrFramePeriodWindow_Type()
)
wwpLeosOamErrFramePeriodWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosOamErrFramePeriodWindow.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosOamErrFramePeriodWindow.setUnits("frames")


class _WwpLeosOamErrFramePeriodThreshold_Type(Unsigned32):
    """Custom type wwpLeosOamErrFramePeriodThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967293),
    )


_WwpLeosOamErrFramePeriodThreshold_Type.__name__ = "Unsigned32"
_WwpLeosOamErrFramePeriodThreshold_Object = MibTableColumn
wwpLeosOamErrFramePeriodThreshold = _WwpLeosOamErrFramePeriodThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 400, 1, 2, 6, 1, 3),
    _WwpLeosOamErrFramePeriodThreshold_Type()
)
wwpLeosOamErrFramePeriodThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosOamErrFramePeriodThreshold.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosOamErrFramePeriodThreshold.setUnits("frames")


class _WwpLeosOamErrFramePeriodEvNotifEnable_Type(Integer32):
    """Custom type wwpLeosOamErrFramePeriodEvNotifEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WwpLeosOamErrFramePeriodEvNotifEnable_Type.__name__ = "Integer32"
_WwpLeosOamErrFramePeriodEvNotifEnable_Object = MibTableColumn
wwpLeosOamErrFramePeriodEvNotifEnable = _WwpLeosOamErrFramePeriodEvNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 400, 1, 2, 6, 1, 4),
    _WwpLeosOamErrFramePeriodEvNotifEnable_Type()
)
wwpLeosOamErrFramePeriodEvNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosOamErrFramePeriodEvNotifEnable.setStatus("current")


class _WwpLeosOamErrFrameWindow_Type(Unsigned32):
    """Custom type wwpLeosOamErrFrameWindow based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 600),
    )


_WwpLeosOamErrFrameWindow_Type.__name__ = "Unsigned32"
_WwpLeosOamErrFrameWindow_Object = MibTableColumn
wwpLeosOamErrFrameWindow = _WwpLeosOamErrFrameWindow_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 400, 1, 2, 6, 1, 5),
    _WwpLeosOamErrFrameWindow_Type()
)
wwpLeosOamErrFrameWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosOamErrFrameWindow.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosOamErrFrameWindow.setUnits("tenths of a second")


class _WwpLeosOamErrFrameThreshold_Type(Unsigned32):
    """Custom type wwpLeosOamErrFrameThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967293),
    )


_WwpLeosOamErrFrameThreshold_Type.__name__ = "Unsigned32"
_WwpLeosOamErrFrameThreshold_Object = MibTableColumn
wwpLeosOamErrFrameThreshold = _WwpLeosOamErrFrameThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 400, 1, 2, 6, 1, 6),
    _WwpLeosOamErrFrameThreshold_Type()
)
wwpLeosOamErrFrameThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosOamErrFrameThreshold.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosOamErrFrameThreshold.setUnits("frames")


class _WwpLeosOamErrFrameEvNotifEnable_Type(Integer32):
    """Custom type wwpLeosOamErrFrameEvNotifEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WwpLeosOamErrFrameEvNotifEnable_Type.__name__ = "Integer32"
_WwpLeosOamErrFrameEvNotifEnable_Object = MibTableColumn
wwpLeosOamErrFrameEvNotifEnable = _WwpLeosOamErrFrameEvNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 400, 1, 2, 6, 1, 7),
    _WwpLeosOamErrFrameEvNotifEnable_Type()
)
wwpLeosOamErrFrameEvNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosOamErrFrameEvNotifEnable.setStatus("current")


class _WwpLeosOamErrFrameSecsSummaryWindow_Type(Integer32):
    """Custom type wwpLeosOamErrFrameSecsSummaryWindow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 9000),
    )


_WwpLeosOamErrFrameSecsSummaryWindow_Type.__name__ = "Integer32"
_WwpLeosOamErrFrameSecsSummaryWindow_Object = MibTableColumn
wwpLeosOamErrFrameSecsSummaryWindow = _WwpLeosOamErrFrameSecsSummaryWindow_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 400, 1, 2, 6, 1, 8),
    _WwpLeosOamErrFrameSecsSummaryWindow_Type()
)
wwpLeosOamErrFrameSecsSummaryWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosOamErrFrameSecsSummaryWindow.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosOamErrFrameSecsSummaryWindow.setUnits("tenths of a second")


class _WwpLeosOamErrFrameSecsSummaryThreshold_Type(Integer32):
    """Custom type wwpLeosOamErrFrameSecsSummaryThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WwpLeosOamErrFrameSecsSummaryThreshold_Type.__name__ = "Integer32"
_WwpLeosOamErrFrameSecsSummaryThreshold_Object = MibTableColumn
wwpLeosOamErrFrameSecsSummaryThreshold = _WwpLeosOamErrFrameSecsSummaryThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 400, 1, 2, 6, 1, 9),
    _WwpLeosOamErrFrameSecsSummaryThreshold_Type()
)
wwpLeosOamErrFrameSecsSummaryThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosOamErrFrameSecsSummaryThreshold.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosOamErrFrameSecsSummaryThreshold.setUnits("errored frame seconds")


class _WwpLeosOamErrFrameSecsEvNotifEnable_Type(Integer32):
    """Custom type wwpLeosOamErrFrameSecsEvNotifEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WwpLeosOamErrFrameSecsEvNotifEnable_Type.__name__ = "Integer32"
_WwpLeosOamErrFrameSecsEvNotifEnable_Object = MibTableColumn
wwpLeosOamErrFrameSecsEvNotifEnable = _WwpLeosOamErrFrameSecsEvNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 400, 1, 2, 6, 1, 10),
    _WwpLeosOamErrFrameSecsEvNotifEnable_Type()
)
wwpLeosOamErrFrameSecsEvNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosOamErrFrameSecsEvNotifEnable.setStatus("current")


class _WwpLeosOamDyingGaspEnable_Type(Integer32):
    """Custom type wwpLeosOamDyingGaspEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WwpLeosOamDyingGaspEnable_Type.__name__ = "Integer32"
_WwpLeosOamDyingGaspEnable_Object = MibTableColumn
wwpLeosOamDyingGaspEnable = _WwpLeosOamDyingGaspEnable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 400, 1, 2, 6, 1, 11),
    _WwpLeosOamDyingGaspEnable_Type()
)
wwpLeosOamDyingGaspEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosOamDyingGaspEnable.setStatus("current")


class _WwpLeosOamCriticalEventEnable_Type(Integer32):
    """Custom type wwpLeosOamCriticalEventEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WwpLeosOamCriticalEventEnable_Type.__name__ = "Integer32"
_WwpLeosOamCriticalEventEnable_Object = MibTableColumn
wwpLeosOamCriticalEventEnable = _WwpLeosOamCriticalEventEnable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 400, 1, 2, 6, 1, 12),
    _WwpLeosOamCriticalEventEnable_Type()
)
wwpLeosOamCriticalEventEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosOamCriticalEventEnable.setStatus("current")
_WwpLeosOamEventLogTable_Object = MibTable
wwpLeosOamEventLogTable = _WwpLeosOamEventLogTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 400, 1, 2, 7)
)
if mibBuilder.loadTexts:
    wwpLeosOamEventLogTable.setStatus("current")
_WwpLeosOamEventLogEntry_Object = MibTableRow
wwpLeosOamEventLogEntry = _WwpLeosOamEventLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 400, 1, 2, 7, 1)
)
wwpLeosOamEventLogEntry.setIndexNames(
    (0, "WWP-LEOS-OAM-MIB", "wwpLeosOamEventLogPort"),
    (0, "WWP-LEOS-OAM-MIB", "wwpLeosOamEventLogIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosOamEventLogEntry.setStatus("current")


class _WwpLeosOamEventLogPort_Type(Integer32):
    """Custom type wwpLeosOamEventLogPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_WwpLeosOamEventLogPort_Type.__name__ = "Integer32"
_WwpLeosOamEventLogPort_Object = MibTableColumn
wwpLeosOamEventLogPort = _WwpLeosOamEventLogPort_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 400, 1, 2, 7, 1, 1),
    _WwpLeosOamEventLogPort_Type()
)
wwpLeosOamEventLogPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosOamEventLogPort.setStatus("current")
_WwpLeosOamEventLogIndex_Type = Unsigned32
_WwpLeosOamEventLogIndex_Object = MibTableColumn
wwpLeosOamEventLogIndex = _WwpLeosOamEventLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 400, 1, 2, 7, 1, 2),
    _WwpLeosOamEventLogIndex_Type()
)
wwpLeosOamEventLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosOamEventLogIndex.setStatus("current")
_WwpLeosOamEventLogTimestamp_Type = TimeStamp
_WwpLeosOamEventLogTimestamp_Object = MibTableColumn
wwpLeosOamEventLogTimestamp = _WwpLeosOamEventLogTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 400, 1, 2, 7, 1, 3),
    _WwpLeosOamEventLogTimestamp_Type()
)
wwpLeosOamEventLogTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosOamEventLogTimestamp.setStatus("current")


class _WwpLeosOamEventLogOui_Type(OctetString):
    """Custom type wwpLeosOamEventLogOui based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_WwpLeosOamEventLogOui_Type.__name__ = "OctetString"
_WwpLeosOamEventLogOui_Object = MibTableColumn
wwpLeosOamEventLogOui = _WwpLeosOamEventLogOui_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 400, 1, 2, 7, 1, 4),
    _WwpLeosOamEventLogOui_Type()
)
wwpLeosOamEventLogOui.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosOamEventLogOui.setStatus("current")
_WwpLeosOamEventLogType_Type = Unsigned32
_WwpLeosOamEventLogType_Object = MibTableColumn
wwpLeosOamEventLogType = _WwpLeosOamEventLogType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 400, 1, 2, 7, 1, 5),
    _WwpLeosOamEventLogType_Type()
)
wwpLeosOamEventLogType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosOamEventLogType.setStatus("current")


class _WwpLeosOamEventLogLocation_Type(Integer32):
    """Custom type wwpLeosOamEventLogLocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("remote", 2))
    )


_WwpLeosOamEventLogLocation_Type.__name__ = "Integer32"
_WwpLeosOamEventLogLocation_Object = MibTableColumn
wwpLeosOamEventLogLocation = _WwpLeosOamEventLogLocation_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 400, 1, 2, 7, 1, 6),
    _WwpLeosOamEventLogLocation_Type()
)
wwpLeosOamEventLogLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosOamEventLogLocation.setStatus("current")
_WwpLeosOamEventLogWindowHi_Type = Unsigned32
_WwpLeosOamEventLogWindowHi_Object = MibTableColumn
wwpLeosOamEventLogWindowHi = _WwpLeosOamEventLogWindowHi_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 400, 1, 2, 7, 1, 7),
    _WwpLeosOamEventLogWindowHi_Type()
)
wwpLeosOamEventLogWindowHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosOamEventLogWindowHi.setStatus("current")
_WwpLeosOamEventLogWindowLo_Type = Unsigned32
_WwpLeosOamEventLogWindowLo_Object = MibTableColumn
wwpLeosOamEventLogWindowLo = _WwpLeosOamEventLogWindowLo_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 400, 1, 2, 7, 1, 8),
    _WwpLeosOamEventLogWindowLo_Type()
)
wwpLeosOamEventLogWindowLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosOamEventLogWindowLo.setStatus("current")
_WwpLeosOamEventLogThresholdHi_Type = Unsigned32
_WwpLeosOamEventLogThresholdHi_Object = MibTableColumn
wwpLeosOamEventLogThresholdHi = _WwpLeosOamEventLogThresholdHi_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 400, 1, 2, 7, 1, 9),
    _WwpLeosOamEventLogThresholdHi_Type()
)
wwpLeosOamEventLogThresholdHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosOamEventLogThresholdHi.setStatus("current")
_WwpLeosOamEventLogThresholdLo_Type = Unsigned32
_WwpLeosOamEventLogThresholdLo_Object = MibTableColumn
wwpLeosOamEventLogThresholdLo = _WwpLeosOamEventLogThresholdLo_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 400, 1, 2, 7, 1, 10),
    _WwpLeosOamEventLogThresholdLo_Type()
)
wwpLeosOamEventLogThresholdLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosOamEventLogThresholdLo.setStatus("current")
_WwpLeosOamEventLogValue_Type = Counter64
_WwpLeosOamEventLogValue_Object = MibTableColumn
wwpLeosOamEventLogValue = _WwpLeosOamEventLogValue_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 400, 1, 2, 7, 1, 11),
    _WwpLeosOamEventLogValue_Type()
)
wwpLeosOamEventLogValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosOamEventLogValue.setStatus("current")
_WwpLeosOamEventLogRunningTotal_Type = Counter64
_WwpLeosOamEventLogRunningTotal_Object = MibTableColumn
wwpLeosOamEventLogRunningTotal = _WwpLeosOamEventLogRunningTotal_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 400, 1, 2, 7, 1, 12),
    _WwpLeosOamEventLogRunningTotal_Type()
)
wwpLeosOamEventLogRunningTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosOamEventLogRunningTotal.setStatus("current")
_WwpLeosOamEventLogEventTotal_Type = Unsigned32
_WwpLeosOamEventLogEventTotal_Object = MibTableColumn
wwpLeosOamEventLogEventTotal = _WwpLeosOamEventLogEventTotal_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 400, 1, 2, 7, 1, 13),
    _WwpLeosOamEventLogEventTotal_Type()
)
wwpLeosOamEventLogEventTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosOamEventLogEventTotal.setStatus("current")
_WwpLeosOamGlobal_ObjectIdentity = ObjectIdentity
wwpLeosOamGlobal = _WwpLeosOamGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 400, 1, 2, 8)
)
_WwpLeosOamStatsClear_Type = TruthValue
_WwpLeosOamStatsClear_Object = MibScalar
wwpLeosOamStatsClear = _WwpLeosOamStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 400, 1, 2, 8, 1),
    _WwpLeosOamStatsClear_Type()
)
wwpLeosOamStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosOamStatsClear.setStatus("current")
_WwpLeosOamNotifMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
wwpLeosOamNotifMIBNotificationPrefix = _WwpLeosOamNotifMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 400, 1, 3)
)
_WwpLeosOamNotifMIBNotification_ObjectIdentity = ObjectIdentity
wwpLeosOamNotifMIBNotification = _WwpLeosOamNotifMIBNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 400, 1, 3, 0)
)

# Managed Objects groups


# Notification objects

wwpLeosOamLinkEventTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 400, 1, 3, 0, 1)
)
wwpLeosOamLinkEventTrap.setObjects(
      *(("WWP-LEOS-OAM-MIB", "wwpLeosOamEventLogPort"),
        ("WWP-LEOS-OAM-MIB", "wwpLeosOamEventLogType"),
        ("WWP-LEOS-OAM-MIB", "wwpLeosOamEventLogLocation"))
)
if mibBuilder.loadTexts:
    wwpLeosOamLinkEventTrap.setStatus(
        "current"
    )

wwpLeosOamLinkLostTimerActiveTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 400, 1, 3, 0, 2)
)
wwpLeosOamLinkLostTimerActiveTrap.setObjects(
      *(("WWP-LEOS-OAM-MIB", "wwpLeosOamPort"),
        ("WWP-LEOS-PORT-MIB", "wwpLeosEtherPortDesc"),
        ("WWP-LEOS-PORT-MIB", "wwpLeosEtherPortOperStatus"),
        ("WWP-LEOS-OAM-MIB", "wwpLeosOamOperStatus"),
        ("WWP-LEOS-OAM-MIB", "wwpLeosOamPeerStatus"),
        ("WWP-LEOS-OAM-MIB", "wwpLeosOamPeerMacAddress"))
)
if mibBuilder.loadTexts:
    wwpLeosOamLinkLostTimerActiveTrap.setStatus(
        "current"
    )

wwpLeosOamLinkLostTimerExpiredTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 400, 1, 3, 0, 3)
)
wwpLeosOamLinkLostTimerExpiredTrap.setObjects(
      *(("WWP-LEOS-OAM-MIB", "wwpLeosOamPort"),
        ("WWP-LEOS-PORT-MIB", "wwpLeosEtherPortDesc"),
        ("WWP-LEOS-PORT-MIB", "wwpLeosEtherPortOperStatus"),
        ("WWP-LEOS-OAM-MIB", "wwpLeosOamOperStatus"),
        ("WWP-LEOS-OAM-MIB", "wwpLeosOamPeerStatus"),
        ("WWP-LEOS-OAM-MIB", "wwpLeosOamPeerMacAddress"))
)
if mibBuilder.loadTexts:
    wwpLeosOamLinkLostTimerExpiredTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WWP-LEOS-OAM-MIB",
    **{"wwpLeosOamMibModule": wwpLeosOamMibModule,
       "wwpLeosOamMIB": wwpLeosOamMIB,
       "wwpLeosOamConf": wwpLeosOamConf,
       "wwpLeosOamGroups": wwpLeosOamGroups,
       "wwpLeosOamCompls": wwpLeosOamCompls,
       "wwpLeosOamObjs": wwpLeosOamObjs,
       "wwpLeosOamTable": wwpLeosOamTable,
       "wwpLeosOamEntry": wwpLeosOamEntry,
       "wwpLeosOamAdminState": wwpLeosOamAdminState,
       "wwpLeosOamOperStatus": wwpLeosOamOperStatus,
       "wwpLeosOamMode": wwpLeosOamMode,
       "wwpLeosMaxOamPduSize": wwpLeosMaxOamPduSize,
       "wwpLeosOamConfigRevision": wwpLeosOamConfigRevision,
       "wwpLeosOamFunctionsSupported": wwpLeosOamFunctionsSupported,
       "wwpLeosOamPort": wwpLeosOamPort,
       "wwpLeosOamPduTimer": wwpLeosOamPduTimer,
       "wwpLeosOamLinkLostTimer": wwpLeosOamLinkLostTimer,
       "wwpLeosOamPeerStatusNotifyState": wwpLeosOamPeerStatusNotifyState,
       "wwpLeosOamPeerTable": wwpLeosOamPeerTable,
       "wwpLeosOamPeerEntry": wwpLeosOamPeerEntry,
       "wwpLeosOamPeerStatus": wwpLeosOamPeerStatus,
       "wwpLeosOamPeerMacAddress": wwpLeosOamPeerMacAddress,
       "wwpLeosOamPeerVendorOui": wwpLeosOamPeerVendorOui,
       "wwpLeosOamPeerVendorInfo": wwpLeosOamPeerVendorInfo,
       "wwpLeosOamPeerMode": wwpLeosOamPeerMode,
       "wwpLeosOamPeerMaxOamPduSize": wwpLeosOamPeerMaxOamPduSize,
       "wwpLeosOamPeerConfigRevision": wwpLeosOamPeerConfigRevision,
       "wwpLeosOamPeerFunctionsSupported": wwpLeosOamPeerFunctionsSupported,
       "wwpLeosOamLocalPort": wwpLeosOamLocalPort,
       "wwpLeosOamLoopbackTable": wwpLeosOamLoopbackTable,
       "wwpLeosOamLoopbackEntry": wwpLeosOamLoopbackEntry,
       "wwpLeosOamLoopbackCommand": wwpLeosOamLoopbackCommand,
       "wwpLeosOamLoopbackStatus": wwpLeosOamLoopbackStatus,
       "wwpLeosOamLoopbackIgnoreRx": wwpLeosOamLoopbackIgnoreRx,
       "wwpLeosOamLoopbackPort": wwpLeosOamLoopbackPort,
       "wwpLeosOamStatsTable": wwpLeosOamStatsTable,
       "wwpLeosOamStatsEntry": wwpLeosOamStatsEntry,
       "wwpLeosOamInformationTx": wwpLeosOamInformationTx,
       "wwpLeosOamInformationRx": wwpLeosOamInformationRx,
       "wwpLeosOamUniqueEventNotificationTx": wwpLeosOamUniqueEventNotificationTx,
       "wwpLeosOamUniqueEventNotificationRx": wwpLeosOamUniqueEventNotificationRx,
       "wwpLeosOamLoopbackControlTx": wwpLeosOamLoopbackControlTx,
       "wwpLeosOamLoopbackControlRx": wwpLeosOamLoopbackControlRx,
       "wwpLeosOamVariableRequestTx": wwpLeosOamVariableRequestTx,
       "wwpLeosOamVariableRequestRx": wwpLeosOamVariableRequestRx,
       "wwpLeosOamVariableResponseTx": wwpLeosOamVariableResponseTx,
       "wwpLeosOamVariableResponseRx": wwpLeosOamVariableResponseRx,
       "wwpLeosOamOrgSpecificTx": wwpLeosOamOrgSpecificTx,
       "wwpLeosOamOrgSpecificRx": wwpLeosOamOrgSpecificRx,
       "wwpLeosOamUnsupportedCodesTx": wwpLeosOamUnsupportedCodesTx,
       "wwpLeosOamUnsupportedCodesRx": wwpLeosOamUnsupportedCodesRx,
       "wwpLeosOamframesLostDueToOam": wwpLeosOamframesLostDueToOam,
       "wwpLeosOamStatsPort": wwpLeosOamStatsPort,
       "wwpLeosOamDuplicateEventNotificationTx": wwpLeosOamDuplicateEventNotificationTx,
       "wwpLeosOamDuplicateEventNotificationRx": wwpLeosOamDuplicateEventNotificationRx,
       "wwpLeosOamSystemEnableDisable": wwpLeosOamSystemEnableDisable,
       "wwpLeosOamEventConfigTable": wwpLeosOamEventConfigTable,
       "wwpLeosOamEventConfigEntry": wwpLeosOamEventConfigEntry,
       "wwpLeosOamEventPort": wwpLeosOamEventPort,
       "wwpLeosOamErrFramePeriodWindow": wwpLeosOamErrFramePeriodWindow,
       "wwpLeosOamErrFramePeriodThreshold": wwpLeosOamErrFramePeriodThreshold,
       "wwpLeosOamErrFramePeriodEvNotifEnable": wwpLeosOamErrFramePeriodEvNotifEnable,
       "wwpLeosOamErrFrameWindow": wwpLeosOamErrFrameWindow,
       "wwpLeosOamErrFrameThreshold": wwpLeosOamErrFrameThreshold,
       "wwpLeosOamErrFrameEvNotifEnable": wwpLeosOamErrFrameEvNotifEnable,
       "wwpLeosOamErrFrameSecsSummaryWindow": wwpLeosOamErrFrameSecsSummaryWindow,
       "wwpLeosOamErrFrameSecsSummaryThreshold": wwpLeosOamErrFrameSecsSummaryThreshold,
       "wwpLeosOamErrFrameSecsEvNotifEnable": wwpLeosOamErrFrameSecsEvNotifEnable,
       "wwpLeosOamDyingGaspEnable": wwpLeosOamDyingGaspEnable,
       "wwpLeosOamCriticalEventEnable": wwpLeosOamCriticalEventEnable,
       "wwpLeosOamEventLogTable": wwpLeosOamEventLogTable,
       "wwpLeosOamEventLogEntry": wwpLeosOamEventLogEntry,
       "wwpLeosOamEventLogPort": wwpLeosOamEventLogPort,
       "wwpLeosOamEventLogIndex": wwpLeosOamEventLogIndex,
       "wwpLeosOamEventLogTimestamp": wwpLeosOamEventLogTimestamp,
       "wwpLeosOamEventLogOui": wwpLeosOamEventLogOui,
       "wwpLeosOamEventLogType": wwpLeosOamEventLogType,
       "wwpLeosOamEventLogLocation": wwpLeosOamEventLogLocation,
       "wwpLeosOamEventLogWindowHi": wwpLeosOamEventLogWindowHi,
       "wwpLeosOamEventLogWindowLo": wwpLeosOamEventLogWindowLo,
       "wwpLeosOamEventLogThresholdHi": wwpLeosOamEventLogThresholdHi,
       "wwpLeosOamEventLogThresholdLo": wwpLeosOamEventLogThresholdLo,
       "wwpLeosOamEventLogValue": wwpLeosOamEventLogValue,
       "wwpLeosOamEventLogRunningTotal": wwpLeosOamEventLogRunningTotal,
       "wwpLeosOamEventLogEventTotal": wwpLeosOamEventLogEventTotal,
       "wwpLeosOamGlobal": wwpLeosOamGlobal,
       "wwpLeosOamStatsClear": wwpLeosOamStatsClear,
       "wwpLeosOamNotifMIBNotificationPrefix": wwpLeosOamNotifMIBNotificationPrefix,
       "wwpLeosOamNotifMIBNotification": wwpLeosOamNotifMIBNotification,
       "wwpLeosOamLinkEventTrap": wwpLeosOamLinkEventTrap,
       "wwpLeosOamLinkLostTimerActiveTrap": wwpLeosOamLinkLostTimerActiveTrap,
       "wwpLeosOamLinkLostTimerExpiredTrap": wwpLeosOamLinkLostTimerExpiredTrap}
)
