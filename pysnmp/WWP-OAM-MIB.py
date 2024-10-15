# SNMP MIB module (WWP-OAM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WWP-OAM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:15:18 2024
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
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp")

(wwpModules,) = mibBuilder.importSymbols(
    "WWP-SMI",
    "wwpModules")


# MODULE-IDENTITY

wwpOamMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 400)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WwpOamMIB_ObjectIdentity = ObjectIdentity
wwpOamMIB = _WwpOamMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 400, 1)
)
_WwpOamConf_ObjectIdentity = ObjectIdentity
wwpOamConf = _WwpOamConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 400, 1, 1)
)
_WwpOamGroups_ObjectIdentity = ObjectIdentity
wwpOamGroups = _WwpOamGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 400, 1, 1, 1)
)
_WwpOamCompls_ObjectIdentity = ObjectIdentity
wwpOamCompls = _WwpOamCompls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 400, 1, 1, 2)
)
_WwpOamObjs_ObjectIdentity = ObjectIdentity
wwpOamObjs = _WwpOamObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 400, 1, 2)
)
_WwpOamTable_Object = MibTable
wwpOamTable = _WwpOamTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 400, 1, 2, 1)
)
if mibBuilder.loadTexts:
    wwpOamTable.setStatus("current")
_WwpOamEntry_Object = MibTableRow
wwpOamEntry = _WwpOamEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 400, 1, 2, 1, 1)
)
wwpOamEntry.setIndexNames(
    (0, "WWP-OAM-MIB", "wwpOamPort"),
)
if mibBuilder.loadTexts:
    wwpOamEntry.setStatus("current")


class _WwpOamAdminState_Type(Integer32):
    """Custom type wwpOamAdminState based on Integer32"""
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


_WwpOamAdminState_Type.__name__ = "Integer32"
_WwpOamAdminState_Object = MibTableColumn
wwpOamAdminState = _WwpOamAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 400, 1, 2, 1, 1, 1),
    _WwpOamAdminState_Type()
)
wwpOamAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpOamAdminState.setStatus("current")


class _WwpOamOperStatus_Type(Integer32):
    """Custom type wwpOamOperStatus based on Integer32"""
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


_WwpOamOperStatus_Type.__name__ = "Integer32"
_WwpOamOperStatus_Object = MibTableColumn
wwpOamOperStatus = _WwpOamOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 400, 1, 2, 1, 1, 2),
    _WwpOamOperStatus_Type()
)
wwpOamOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpOamOperStatus.setStatus("current")


class _WwpOamMode_Type(Integer32):
    """Custom type wwpOamMode based on Integer32"""
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


_WwpOamMode_Type.__name__ = "Integer32"
_WwpOamMode_Object = MibTableColumn
wwpOamMode = _WwpOamMode_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 400, 1, 2, 1, 1, 3),
    _WwpOamMode_Type()
)
wwpOamMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpOamMode.setStatus("current")
_WwpMaxOamPduSize_Type = Integer32
_WwpMaxOamPduSize_Object = MibTableColumn
wwpMaxOamPduSize = _WwpMaxOamPduSize_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 400, 1, 2, 1, 1, 4),
    _WwpMaxOamPduSize_Type()
)
wwpMaxOamPduSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpMaxOamPduSize.setStatus("current")
if mibBuilder.loadTexts:
    wwpMaxOamPduSize.setUnits("bytes")
_WwpOamConfigRevision_Type = Unsigned32
_WwpOamConfigRevision_Object = MibTableColumn
wwpOamConfigRevision = _WwpOamConfigRevision_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 400, 1, 2, 1, 1, 5),
    _WwpOamConfigRevision_Type()
)
wwpOamConfigRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpOamConfigRevision.setStatus("current")


class _WwpOamFunctionsSupported_Type(Bits):
    """Custom type wwpOamFunctionsSupported based on Bits"""
    namedValues = NamedValues(
        *(("eventSupport", 2),
          ("loopbackSupport", 1),
          ("unidirectionalSupport", 0),
          ("variableSupport", 3))
    )

_WwpOamFunctionsSupported_Type.__name__ = "Bits"
_WwpOamFunctionsSupported_Object = MibTableColumn
wwpOamFunctionsSupported = _WwpOamFunctionsSupported_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 400, 1, 2, 1, 1, 6),
    _WwpOamFunctionsSupported_Type()
)
wwpOamFunctionsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpOamFunctionsSupported.setStatus("current")


class _WwpOamPort_Type(Integer32):
    """Custom type wwpOamPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_WwpOamPort_Type.__name__ = "Integer32"
_WwpOamPort_Object = MibTableColumn
wwpOamPort = _WwpOamPort_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 400, 1, 2, 1, 1, 7),
    _WwpOamPort_Type()
)
wwpOamPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpOamPort.setStatus("current")
_WwpOamPeerTable_Object = MibTable
wwpOamPeerTable = _WwpOamPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 400, 1, 2, 2)
)
if mibBuilder.loadTexts:
    wwpOamPeerTable.setStatus("current")
_WwpOamPeerEntry_Object = MibTableRow
wwpOamPeerEntry = _WwpOamPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 400, 1, 2, 2, 1)
)
wwpOamPeerEntry.setIndexNames(
    (0, "WWP-OAM-MIB", "wwpOamLocalPort"),
)
if mibBuilder.loadTexts:
    wwpOamPeerEntry.setStatus("current")


class _WwpOamPeerStatus_Type(Integer32):
    """Custom type wwpOamPeerStatus based on Integer32"""
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


_WwpOamPeerStatus_Type.__name__ = "Integer32"
_WwpOamPeerStatus_Object = MibTableColumn
wwpOamPeerStatus = _WwpOamPeerStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 400, 1, 2, 2, 1, 1),
    _WwpOamPeerStatus_Type()
)
wwpOamPeerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpOamPeerStatus.setStatus("current")


class _WwpOamPeerMacAddress_Type(OctetString):
    """Custom type wwpOamPeerMacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_WwpOamPeerMacAddress_Type.__name__ = "OctetString"
_WwpOamPeerMacAddress_Object = MibTableColumn
wwpOamPeerMacAddress = _WwpOamPeerMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 400, 1, 2, 2, 1, 2),
    _WwpOamPeerMacAddress_Type()
)
wwpOamPeerMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpOamPeerMacAddress.setStatus("current")


class _WwpOamPeerVendorOui_Type(OctetString):
    """Custom type wwpOamPeerVendorOui based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_WwpOamPeerVendorOui_Type.__name__ = "OctetString"
_WwpOamPeerVendorOui_Object = MibTableColumn
wwpOamPeerVendorOui = _WwpOamPeerVendorOui_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 400, 1, 2, 2, 1, 3),
    _WwpOamPeerVendorOui_Type()
)
wwpOamPeerVendorOui.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpOamPeerVendorOui.setStatus("current")
_WwpOamPeerVendorInfo_Type = Unsigned32
_WwpOamPeerVendorInfo_Object = MibTableColumn
wwpOamPeerVendorInfo = _WwpOamPeerVendorInfo_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 400, 1, 2, 2, 1, 4),
    _WwpOamPeerVendorInfo_Type()
)
wwpOamPeerVendorInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpOamPeerVendorInfo.setStatus("current")


class _WwpOamPeerMode_Type(Integer32):
    """Custom type wwpOamPeerMode based on Integer32"""
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


_WwpOamPeerMode_Type.__name__ = "Integer32"
_WwpOamPeerMode_Object = MibTableColumn
wwpOamPeerMode = _WwpOamPeerMode_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 400, 1, 2, 2, 1, 5),
    _WwpOamPeerMode_Type()
)
wwpOamPeerMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpOamPeerMode.setStatus("current")
_WwpOamPeerMaxOamPduSize_Type = Integer32
_WwpOamPeerMaxOamPduSize_Object = MibTableColumn
wwpOamPeerMaxOamPduSize = _WwpOamPeerMaxOamPduSize_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 400, 1, 2, 2, 1, 6),
    _WwpOamPeerMaxOamPduSize_Type()
)
wwpOamPeerMaxOamPduSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpOamPeerMaxOamPduSize.setStatus("current")
if mibBuilder.loadTexts:
    wwpOamPeerMaxOamPduSize.setUnits("bytes")
_WwpOamPeerConfigRevision_Type = Unsigned32
_WwpOamPeerConfigRevision_Object = MibTableColumn
wwpOamPeerConfigRevision = _WwpOamPeerConfigRevision_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 400, 1, 2, 2, 1, 7),
    _WwpOamPeerConfigRevision_Type()
)
wwpOamPeerConfigRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpOamPeerConfigRevision.setStatus("current")


class _WwpOamPeerFunctionsSupported_Type(Bits):
    """Custom type wwpOamPeerFunctionsSupported based on Bits"""
    namedValues = NamedValues(
        *(("eventSupport", 2),
          ("loopbackSupport", 1),
          ("unidirectionalSupport", 0),
          ("variableSupport", 3))
    )

_WwpOamPeerFunctionsSupported_Type.__name__ = "Bits"
_WwpOamPeerFunctionsSupported_Object = MibTableColumn
wwpOamPeerFunctionsSupported = _WwpOamPeerFunctionsSupported_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 400, 1, 2, 2, 1, 8),
    _WwpOamPeerFunctionsSupported_Type()
)
wwpOamPeerFunctionsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpOamPeerFunctionsSupported.setStatus("current")


class _WwpOamLocalPort_Type(Integer32):
    """Custom type wwpOamLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_WwpOamLocalPort_Type.__name__ = "Integer32"
_WwpOamLocalPort_Object = MibTableColumn
wwpOamLocalPort = _WwpOamLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 400, 1, 2, 2, 1, 9),
    _WwpOamLocalPort_Type()
)
wwpOamLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpOamLocalPort.setStatus("current")
_WwpOamLoopbackTable_Object = MibTable
wwpOamLoopbackTable = _WwpOamLoopbackTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 400, 1, 2, 3)
)
if mibBuilder.loadTexts:
    wwpOamLoopbackTable.setStatus("current")
_WwpOamLoopbackEntry_Object = MibTableRow
wwpOamLoopbackEntry = _WwpOamLoopbackEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 400, 1, 2, 3, 1)
)
wwpOamLoopbackEntry.setIndexNames(
    (0, "WWP-OAM-MIB", "wwpOamLoopbackPort"),
)
if mibBuilder.loadTexts:
    wwpOamLoopbackEntry.setStatus("current")


class _WwpOamLoopbackCommand_Type(Integer32):
    """Custom type wwpOamLoopbackCommand based on Integer32"""
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


_WwpOamLoopbackCommand_Type.__name__ = "Integer32"
_WwpOamLoopbackCommand_Object = MibTableColumn
wwpOamLoopbackCommand = _WwpOamLoopbackCommand_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 400, 1, 2, 3, 1, 1),
    _WwpOamLoopbackCommand_Type()
)
wwpOamLoopbackCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpOamLoopbackCommand.setStatus("current")


class _WwpOamLoopbackStatus_Type(Integer32):
    """Custom type wwpOamLoopbackStatus based on Integer32"""
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


_WwpOamLoopbackStatus_Type.__name__ = "Integer32"
_WwpOamLoopbackStatus_Object = MibTableColumn
wwpOamLoopbackStatus = _WwpOamLoopbackStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 400, 1, 2, 3, 1, 2),
    _WwpOamLoopbackStatus_Type()
)
wwpOamLoopbackStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpOamLoopbackStatus.setStatus("current")


class _WwpOamLoopbackIgnoreRx_Type(Integer32):
    """Custom type wwpOamLoopbackIgnoreRx based on Integer32"""
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


_WwpOamLoopbackIgnoreRx_Type.__name__ = "Integer32"
_WwpOamLoopbackIgnoreRx_Object = MibTableColumn
wwpOamLoopbackIgnoreRx = _WwpOamLoopbackIgnoreRx_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 400, 1, 2, 3, 1, 3),
    _WwpOamLoopbackIgnoreRx_Type()
)
wwpOamLoopbackIgnoreRx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpOamLoopbackIgnoreRx.setStatus("current")


class _WwpOamLoopbackPort_Type(Integer32):
    """Custom type wwpOamLoopbackPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_WwpOamLoopbackPort_Type.__name__ = "Integer32"
_WwpOamLoopbackPort_Object = MibTableColumn
wwpOamLoopbackPort = _WwpOamLoopbackPort_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 400, 1, 2, 3, 1, 4),
    _WwpOamLoopbackPort_Type()
)
wwpOamLoopbackPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpOamLoopbackPort.setStatus("current")
_WwpOamStatsTable_Object = MibTable
wwpOamStatsTable = _WwpOamStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 400, 1, 2, 4)
)
if mibBuilder.loadTexts:
    wwpOamStatsTable.setStatus("current")
_WwpOamStatsEntry_Object = MibTableRow
wwpOamStatsEntry = _WwpOamStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 400, 1, 2, 4, 1)
)
wwpOamStatsEntry.setIndexNames(
    (0, "WWP-OAM-MIB", "wwpOamStatsPort"),
)
if mibBuilder.loadTexts:
    wwpOamStatsEntry.setStatus("current")
_WwpOamInformationTx_Type = Counter32
_WwpOamInformationTx_Object = MibTableColumn
wwpOamInformationTx = _WwpOamInformationTx_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 400, 1, 2, 4, 1, 1),
    _WwpOamInformationTx_Type()
)
wwpOamInformationTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpOamInformationTx.setStatus("current")
if mibBuilder.loadTexts:
    wwpOamInformationTx.setUnits("frames")
_WwpOamInformationRx_Type = Counter32
_WwpOamInformationRx_Object = MibTableColumn
wwpOamInformationRx = _WwpOamInformationRx_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 400, 1, 2, 4, 1, 2),
    _WwpOamInformationRx_Type()
)
wwpOamInformationRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpOamInformationRx.setStatus("current")
if mibBuilder.loadTexts:
    wwpOamInformationRx.setUnits("frames")
_WwpOamUniqueEventNotificationTx_Type = Counter32
_WwpOamUniqueEventNotificationTx_Object = MibTableColumn
wwpOamUniqueEventNotificationTx = _WwpOamUniqueEventNotificationTx_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 400, 1, 2, 4, 1, 3),
    _WwpOamUniqueEventNotificationTx_Type()
)
wwpOamUniqueEventNotificationTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpOamUniqueEventNotificationTx.setStatus("current")
if mibBuilder.loadTexts:
    wwpOamUniqueEventNotificationTx.setUnits("frames")
_WwpOamUniqueEventNotificationRx_Type = Counter32
_WwpOamUniqueEventNotificationRx_Object = MibTableColumn
wwpOamUniqueEventNotificationRx = _WwpOamUniqueEventNotificationRx_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 400, 1, 2, 4, 1, 4),
    _WwpOamUniqueEventNotificationRx_Type()
)
wwpOamUniqueEventNotificationRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpOamUniqueEventNotificationRx.setStatus("current")
if mibBuilder.loadTexts:
    wwpOamUniqueEventNotificationRx.setUnits("frames")
_WwpOamLoopbackControlTx_Type = Counter32
_WwpOamLoopbackControlTx_Object = MibTableColumn
wwpOamLoopbackControlTx = _WwpOamLoopbackControlTx_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 400, 1, 2, 4, 1, 5),
    _WwpOamLoopbackControlTx_Type()
)
wwpOamLoopbackControlTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpOamLoopbackControlTx.setStatus("current")
if mibBuilder.loadTexts:
    wwpOamLoopbackControlTx.setUnits("frames")
_WwpOamLoopbackControlRx_Type = Counter32
_WwpOamLoopbackControlRx_Object = MibTableColumn
wwpOamLoopbackControlRx = _WwpOamLoopbackControlRx_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 400, 1, 2, 4, 1, 6),
    _WwpOamLoopbackControlRx_Type()
)
wwpOamLoopbackControlRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpOamLoopbackControlRx.setStatus("current")
if mibBuilder.loadTexts:
    wwpOamLoopbackControlRx.setUnits("frames")
_WwpOamVariableRequestTx_Type = Counter32
_WwpOamVariableRequestTx_Object = MibTableColumn
wwpOamVariableRequestTx = _WwpOamVariableRequestTx_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 400, 1, 2, 4, 1, 7),
    _WwpOamVariableRequestTx_Type()
)
wwpOamVariableRequestTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpOamVariableRequestTx.setStatus("current")
if mibBuilder.loadTexts:
    wwpOamVariableRequestTx.setUnits("frames")
_WwpOamVariableRequestRx_Type = Counter32
_WwpOamVariableRequestRx_Object = MibTableColumn
wwpOamVariableRequestRx = _WwpOamVariableRequestRx_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 400, 1, 2, 4, 1, 8),
    _WwpOamVariableRequestRx_Type()
)
wwpOamVariableRequestRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpOamVariableRequestRx.setStatus("current")
if mibBuilder.loadTexts:
    wwpOamVariableRequestRx.setUnits("frames")
_WwpOamVariableResponseTx_Type = Counter32
_WwpOamVariableResponseTx_Object = MibTableColumn
wwpOamVariableResponseTx = _WwpOamVariableResponseTx_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 400, 1, 2, 4, 1, 9),
    _WwpOamVariableResponseTx_Type()
)
wwpOamVariableResponseTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpOamVariableResponseTx.setStatus("current")
if mibBuilder.loadTexts:
    wwpOamVariableResponseTx.setUnits("frames")
_WwpOamVariableResponseRx_Type = Counter32
_WwpOamVariableResponseRx_Object = MibTableColumn
wwpOamVariableResponseRx = _WwpOamVariableResponseRx_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 400, 1, 2, 4, 1, 10),
    _WwpOamVariableResponseRx_Type()
)
wwpOamVariableResponseRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpOamVariableResponseRx.setStatus("current")
if mibBuilder.loadTexts:
    wwpOamVariableResponseRx.setUnits("frames")
_WwpOamOrgSpecificTx_Type = Counter32
_WwpOamOrgSpecificTx_Object = MibTableColumn
wwpOamOrgSpecificTx = _WwpOamOrgSpecificTx_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 400, 1, 2, 4, 1, 11),
    _WwpOamOrgSpecificTx_Type()
)
wwpOamOrgSpecificTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpOamOrgSpecificTx.setStatus("current")
if mibBuilder.loadTexts:
    wwpOamOrgSpecificTx.setUnits("frames")
_WwpOamOrgSpecificRx_Type = Counter32
_WwpOamOrgSpecificRx_Object = MibTableColumn
wwpOamOrgSpecificRx = _WwpOamOrgSpecificRx_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 400, 1, 2, 4, 1, 12),
    _WwpOamOrgSpecificRx_Type()
)
wwpOamOrgSpecificRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpOamOrgSpecificRx.setStatus("current")
if mibBuilder.loadTexts:
    wwpOamOrgSpecificRx.setUnits("frames")
_WwpOamUnsupportedCodesTx_Type = Counter32
_WwpOamUnsupportedCodesTx_Object = MibTableColumn
wwpOamUnsupportedCodesTx = _WwpOamUnsupportedCodesTx_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 400, 1, 2, 4, 1, 13),
    _WwpOamUnsupportedCodesTx_Type()
)
wwpOamUnsupportedCodesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpOamUnsupportedCodesTx.setStatus("current")
if mibBuilder.loadTexts:
    wwpOamUnsupportedCodesTx.setUnits("frames")
_WwpOamUnsupportedCodesRx_Type = Counter32
_WwpOamUnsupportedCodesRx_Object = MibTableColumn
wwpOamUnsupportedCodesRx = _WwpOamUnsupportedCodesRx_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 400, 1, 2, 4, 1, 14),
    _WwpOamUnsupportedCodesRx_Type()
)
wwpOamUnsupportedCodesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpOamUnsupportedCodesRx.setStatus("current")
if mibBuilder.loadTexts:
    wwpOamUnsupportedCodesRx.setUnits("frames")
_WwpOamframesLostDueToOam_Type = Counter32
_WwpOamframesLostDueToOam_Object = MibTableColumn
wwpOamframesLostDueToOam = _WwpOamframesLostDueToOam_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 400, 1, 2, 4, 1, 15),
    _WwpOamframesLostDueToOam_Type()
)
wwpOamframesLostDueToOam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpOamframesLostDueToOam.setStatus("current")
if mibBuilder.loadTexts:
    wwpOamframesLostDueToOam.setUnits("frames")


class _WwpOamStatsPort_Type(Integer32):
    """Custom type wwpOamStatsPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_WwpOamStatsPort_Type.__name__ = "Integer32"
_WwpOamStatsPort_Object = MibTableColumn
wwpOamStatsPort = _WwpOamStatsPort_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 400, 1, 2, 4, 1, 16),
    _WwpOamStatsPort_Type()
)
wwpOamStatsPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpOamStatsPort.setStatus("current")
_WwpOamDuplicateEventNotificationTx_Type = Counter32
_WwpOamDuplicateEventNotificationTx_Object = MibTableColumn
wwpOamDuplicateEventNotificationTx = _WwpOamDuplicateEventNotificationTx_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 400, 1, 2, 4, 1, 17),
    _WwpOamDuplicateEventNotificationTx_Type()
)
wwpOamDuplicateEventNotificationTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpOamDuplicateEventNotificationTx.setStatus("current")
if mibBuilder.loadTexts:
    wwpOamDuplicateEventNotificationTx.setUnits("frames")
_WwpOamDuplicateEventNotificationRx_Type = Counter32
_WwpOamDuplicateEventNotificationRx_Object = MibTableColumn
wwpOamDuplicateEventNotificationRx = _WwpOamDuplicateEventNotificationRx_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 400, 1, 2, 4, 1, 18),
    _WwpOamDuplicateEventNotificationRx_Type()
)
wwpOamDuplicateEventNotificationRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpOamDuplicateEventNotificationRx.setStatus("current")
if mibBuilder.loadTexts:
    wwpOamDuplicateEventNotificationRx.setUnits("frames")


class _WwpOamSystemEnableDisable_Type(Integer32):
    """Custom type wwpOamSystemEnableDisable based on Integer32"""
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


_WwpOamSystemEnableDisable_Type.__name__ = "Integer32"
_WwpOamSystemEnableDisable_Object = MibScalar
wwpOamSystemEnableDisable = _WwpOamSystemEnableDisable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 400, 1, 2, 5),
    _WwpOamSystemEnableDisable_Type()
)
wwpOamSystemEnableDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpOamSystemEnableDisable.setStatus("current")
_WwpOamEventConfigTable_Object = MibTable
wwpOamEventConfigTable = _WwpOamEventConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 400, 1, 2, 6)
)
if mibBuilder.loadTexts:
    wwpOamEventConfigTable.setStatus("current")
_WwpOamEventConfigEntry_Object = MibTableRow
wwpOamEventConfigEntry = _WwpOamEventConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 400, 1, 2, 6, 1)
)
wwpOamEventConfigEntry.setIndexNames(
    (0, "WWP-OAM-MIB", "wwpOamEventPort"),
)
if mibBuilder.loadTexts:
    wwpOamEventConfigEntry.setStatus("current")


class _WwpOamEventPort_Type(Integer32):
    """Custom type wwpOamEventPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_WwpOamEventPort_Type.__name__ = "Integer32"
_WwpOamEventPort_Object = MibTableColumn
wwpOamEventPort = _WwpOamEventPort_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 400, 1, 2, 6, 1, 1),
    _WwpOamEventPort_Type()
)
wwpOamEventPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpOamEventPort.setStatus("current")
_WwpOamErrFramePeriodWindow_Type = Unsigned32
_WwpOamErrFramePeriodWindow_Object = MibTableColumn
wwpOamErrFramePeriodWindow = _WwpOamErrFramePeriodWindow_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 400, 1, 2, 6, 1, 2),
    _WwpOamErrFramePeriodWindow_Type()
)
wwpOamErrFramePeriodWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpOamErrFramePeriodWindow.setStatus("current")
if mibBuilder.loadTexts:
    wwpOamErrFramePeriodWindow.setUnits("frames")
_WwpOamErrFramePeriodThreshold_Type = Unsigned32
_WwpOamErrFramePeriodThreshold_Object = MibTableColumn
wwpOamErrFramePeriodThreshold = _WwpOamErrFramePeriodThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 400, 1, 2, 6, 1, 3),
    _WwpOamErrFramePeriodThreshold_Type()
)
wwpOamErrFramePeriodThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpOamErrFramePeriodThreshold.setStatus("current")
if mibBuilder.loadTexts:
    wwpOamErrFramePeriodThreshold.setUnits("frames")


class _WwpOamErrFramePeriodEvNotifEnable_Type(Integer32):
    """Custom type wwpOamErrFramePeriodEvNotifEnable based on Integer32"""
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


_WwpOamErrFramePeriodEvNotifEnable_Type.__name__ = "Integer32"
_WwpOamErrFramePeriodEvNotifEnable_Object = MibTableColumn
wwpOamErrFramePeriodEvNotifEnable = _WwpOamErrFramePeriodEvNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 400, 1, 2, 6, 1, 4),
    _WwpOamErrFramePeriodEvNotifEnable_Type()
)
wwpOamErrFramePeriodEvNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpOamErrFramePeriodEvNotifEnable.setStatus("current")
_WwpOamErrFrameWindow_Type = Unsigned32
_WwpOamErrFrameWindow_Object = MibTableColumn
wwpOamErrFrameWindow = _WwpOamErrFrameWindow_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 400, 1, 2, 6, 1, 5),
    _WwpOamErrFrameWindow_Type()
)
wwpOamErrFrameWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpOamErrFrameWindow.setStatus("current")
if mibBuilder.loadTexts:
    wwpOamErrFrameWindow.setUnits("tenths of a second")
_WwpOamErrFrameThreshold_Type = Unsigned32
_WwpOamErrFrameThreshold_Object = MibTableColumn
wwpOamErrFrameThreshold = _WwpOamErrFrameThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 400, 1, 2, 6, 1, 6),
    _WwpOamErrFrameThreshold_Type()
)
wwpOamErrFrameThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpOamErrFrameThreshold.setStatus("current")
if mibBuilder.loadTexts:
    wwpOamErrFrameThreshold.setUnits("frames")


class _WwpOamErrFrameEvNotifEnable_Type(Integer32):
    """Custom type wwpOamErrFrameEvNotifEnable based on Integer32"""
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


_WwpOamErrFrameEvNotifEnable_Type.__name__ = "Integer32"
_WwpOamErrFrameEvNotifEnable_Object = MibTableColumn
wwpOamErrFrameEvNotifEnable = _WwpOamErrFrameEvNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 400, 1, 2, 6, 1, 7),
    _WwpOamErrFrameEvNotifEnable_Type()
)
wwpOamErrFrameEvNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpOamErrFrameEvNotifEnable.setStatus("current")


class _WwpOamErrFrameSecsSummaryWindow_Type(Integer32):
    """Custom type wwpOamErrFrameSecsSummaryWindow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 9000),
    )


_WwpOamErrFrameSecsSummaryWindow_Type.__name__ = "Integer32"
_WwpOamErrFrameSecsSummaryWindow_Object = MibTableColumn
wwpOamErrFrameSecsSummaryWindow = _WwpOamErrFrameSecsSummaryWindow_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 400, 1, 2, 6, 1, 8),
    _WwpOamErrFrameSecsSummaryWindow_Type()
)
wwpOamErrFrameSecsSummaryWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpOamErrFrameSecsSummaryWindow.setStatus("current")
if mibBuilder.loadTexts:
    wwpOamErrFrameSecsSummaryWindow.setUnits("tenths of a second")
_WwpOamErrFrameSecsSummaryThreshold_Type = Integer32
_WwpOamErrFrameSecsSummaryThreshold_Object = MibTableColumn
wwpOamErrFrameSecsSummaryThreshold = _WwpOamErrFrameSecsSummaryThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 400, 1, 2, 6, 1, 9),
    _WwpOamErrFrameSecsSummaryThreshold_Type()
)
wwpOamErrFrameSecsSummaryThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpOamErrFrameSecsSummaryThreshold.setStatus("current")
if mibBuilder.loadTexts:
    wwpOamErrFrameSecsSummaryThreshold.setUnits("errored frame seconds")


class _WwpOamErrFrameSecsEvNotifEnable_Type(Integer32):
    """Custom type wwpOamErrFrameSecsEvNotifEnable based on Integer32"""
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


_WwpOamErrFrameSecsEvNotifEnable_Type.__name__ = "Integer32"
_WwpOamErrFrameSecsEvNotifEnable_Object = MibTableColumn
wwpOamErrFrameSecsEvNotifEnable = _WwpOamErrFrameSecsEvNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 400, 1, 2, 6, 1, 10),
    _WwpOamErrFrameSecsEvNotifEnable_Type()
)
wwpOamErrFrameSecsEvNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpOamErrFrameSecsEvNotifEnable.setStatus("current")


class _WwpOamDyingGaspEnable_Type(Integer32):
    """Custom type wwpOamDyingGaspEnable based on Integer32"""
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


_WwpOamDyingGaspEnable_Type.__name__ = "Integer32"
_WwpOamDyingGaspEnable_Object = MibTableColumn
wwpOamDyingGaspEnable = _WwpOamDyingGaspEnable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 400, 1, 2, 6, 1, 11),
    _WwpOamDyingGaspEnable_Type()
)
wwpOamDyingGaspEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpOamDyingGaspEnable.setStatus("current")


class _WwpOamCriticalEventEnable_Type(Integer32):
    """Custom type wwpOamCriticalEventEnable based on Integer32"""
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


_WwpOamCriticalEventEnable_Type.__name__ = "Integer32"
_WwpOamCriticalEventEnable_Object = MibTableColumn
wwpOamCriticalEventEnable = _WwpOamCriticalEventEnable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 400, 1, 2, 6, 1, 12),
    _WwpOamCriticalEventEnable_Type()
)
wwpOamCriticalEventEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpOamCriticalEventEnable.setStatus("current")
_WwpOamEventLogTable_Object = MibTable
wwpOamEventLogTable = _WwpOamEventLogTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 400, 1, 2, 7)
)
if mibBuilder.loadTexts:
    wwpOamEventLogTable.setStatus("current")
_WwpOamEventLogEntry_Object = MibTableRow
wwpOamEventLogEntry = _WwpOamEventLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 400, 1, 2, 7, 1)
)
wwpOamEventLogEntry.setIndexNames(
    (0, "WWP-OAM-MIB", "wwpOamEventLogPort"),
    (0, "WWP-OAM-MIB", "wwpOamEventLogIndex"),
)
if mibBuilder.loadTexts:
    wwpOamEventLogEntry.setStatus("current")


class _WwpOamEventLogPort_Type(Integer32):
    """Custom type wwpOamEventLogPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_WwpOamEventLogPort_Type.__name__ = "Integer32"
_WwpOamEventLogPort_Object = MibTableColumn
wwpOamEventLogPort = _WwpOamEventLogPort_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 400, 1, 2, 7, 1, 1),
    _WwpOamEventLogPort_Type()
)
wwpOamEventLogPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpOamEventLogPort.setStatus("current")
_WwpOamEventLogIndex_Type = Unsigned32
_WwpOamEventLogIndex_Object = MibTableColumn
wwpOamEventLogIndex = _WwpOamEventLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 400, 1, 2, 7, 1, 2),
    _WwpOamEventLogIndex_Type()
)
wwpOamEventLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpOamEventLogIndex.setStatus("current")
_WwpOamEventLogTimestamp_Type = TimeStamp
_WwpOamEventLogTimestamp_Object = MibTableColumn
wwpOamEventLogTimestamp = _WwpOamEventLogTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 400, 1, 2, 7, 1, 3),
    _WwpOamEventLogTimestamp_Type()
)
wwpOamEventLogTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpOamEventLogTimestamp.setStatus("current")


class _WwpOamEventLogOui_Type(OctetString):
    """Custom type wwpOamEventLogOui based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_WwpOamEventLogOui_Type.__name__ = "OctetString"
_WwpOamEventLogOui_Object = MibTableColumn
wwpOamEventLogOui = _WwpOamEventLogOui_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 400, 1, 2, 7, 1, 4),
    _WwpOamEventLogOui_Type()
)
wwpOamEventLogOui.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpOamEventLogOui.setStatus("current")
_WwpOamEventLogType_Type = Unsigned32
_WwpOamEventLogType_Object = MibTableColumn
wwpOamEventLogType = _WwpOamEventLogType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 400, 1, 2, 7, 1, 5),
    _WwpOamEventLogType_Type()
)
wwpOamEventLogType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpOamEventLogType.setStatus("current")


class _WwpOamEventLogLocation_Type(Integer32):
    """Custom type wwpOamEventLogLocation based on Integer32"""
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


_WwpOamEventLogLocation_Type.__name__ = "Integer32"
_WwpOamEventLogLocation_Object = MibTableColumn
wwpOamEventLogLocation = _WwpOamEventLogLocation_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 400, 1, 2, 7, 1, 6),
    _WwpOamEventLogLocation_Type()
)
wwpOamEventLogLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpOamEventLogLocation.setStatus("current")
_WwpOamEventLogWindowHi_Type = Unsigned32
_WwpOamEventLogWindowHi_Object = MibTableColumn
wwpOamEventLogWindowHi = _WwpOamEventLogWindowHi_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 400, 1, 2, 7, 1, 7),
    _WwpOamEventLogWindowHi_Type()
)
wwpOamEventLogWindowHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpOamEventLogWindowHi.setStatus("current")
_WwpOamEventLogWindowLo_Type = Unsigned32
_WwpOamEventLogWindowLo_Object = MibTableColumn
wwpOamEventLogWindowLo = _WwpOamEventLogWindowLo_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 400, 1, 2, 7, 1, 8),
    _WwpOamEventLogWindowLo_Type()
)
wwpOamEventLogWindowLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpOamEventLogWindowLo.setStatus("current")
_WwpOamEventLogThresholdHi_Type = Unsigned32
_WwpOamEventLogThresholdHi_Object = MibTableColumn
wwpOamEventLogThresholdHi = _WwpOamEventLogThresholdHi_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 400, 1, 2, 7, 1, 9),
    _WwpOamEventLogThresholdHi_Type()
)
wwpOamEventLogThresholdHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpOamEventLogThresholdHi.setStatus("current")
_WwpOamEventLogThresholdLo_Type = Unsigned32
_WwpOamEventLogThresholdLo_Object = MibTableColumn
wwpOamEventLogThresholdLo = _WwpOamEventLogThresholdLo_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 400, 1, 2, 7, 1, 10),
    _WwpOamEventLogThresholdLo_Type()
)
wwpOamEventLogThresholdLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpOamEventLogThresholdLo.setStatus("current")
_WwpOamEventLogValue_Type = Counter64
_WwpOamEventLogValue_Object = MibTableColumn
wwpOamEventLogValue = _WwpOamEventLogValue_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 400, 1, 2, 7, 1, 11),
    _WwpOamEventLogValue_Type()
)
wwpOamEventLogValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpOamEventLogValue.setStatus("current")
_WwpOamEventLogRunningTotal_Type = Counter64
_WwpOamEventLogRunningTotal_Object = MibTableColumn
wwpOamEventLogRunningTotal = _WwpOamEventLogRunningTotal_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 400, 1, 2, 7, 1, 12),
    _WwpOamEventLogRunningTotal_Type()
)
wwpOamEventLogRunningTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpOamEventLogRunningTotal.setStatus("current")
_WwpOamEventLogEventTotal_Type = Unsigned32
_WwpOamEventLogEventTotal_Object = MibTableColumn
wwpOamEventLogEventTotal = _WwpOamEventLogEventTotal_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 400, 1, 2, 7, 1, 13),
    _WwpOamEventLogEventTotal_Type()
)
wwpOamEventLogEventTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpOamEventLogEventTotal.setStatus("current")
_WwpOamEvents_ObjectIdentity = ObjectIdentity
wwpOamEvents = _WwpOamEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 400, 1, 3)
)
_WwpOamEventsV2_ObjectIdentity = ObjectIdentity
wwpOamEventsV2 = _WwpOamEventsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 400, 1, 3, 0)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WWP-OAM-MIB",
    **{"wwpOamMibModule": wwpOamMibModule,
       "wwpOamMIB": wwpOamMIB,
       "wwpOamConf": wwpOamConf,
       "wwpOamGroups": wwpOamGroups,
       "wwpOamCompls": wwpOamCompls,
       "wwpOamObjs": wwpOamObjs,
       "wwpOamTable": wwpOamTable,
       "wwpOamEntry": wwpOamEntry,
       "wwpOamAdminState": wwpOamAdminState,
       "wwpOamOperStatus": wwpOamOperStatus,
       "wwpOamMode": wwpOamMode,
       "wwpMaxOamPduSize": wwpMaxOamPduSize,
       "wwpOamConfigRevision": wwpOamConfigRevision,
       "wwpOamFunctionsSupported": wwpOamFunctionsSupported,
       "wwpOamPort": wwpOamPort,
       "wwpOamPeerTable": wwpOamPeerTable,
       "wwpOamPeerEntry": wwpOamPeerEntry,
       "wwpOamPeerStatus": wwpOamPeerStatus,
       "wwpOamPeerMacAddress": wwpOamPeerMacAddress,
       "wwpOamPeerVendorOui": wwpOamPeerVendorOui,
       "wwpOamPeerVendorInfo": wwpOamPeerVendorInfo,
       "wwpOamPeerMode": wwpOamPeerMode,
       "wwpOamPeerMaxOamPduSize": wwpOamPeerMaxOamPduSize,
       "wwpOamPeerConfigRevision": wwpOamPeerConfigRevision,
       "wwpOamPeerFunctionsSupported": wwpOamPeerFunctionsSupported,
       "wwpOamLocalPort": wwpOamLocalPort,
       "wwpOamLoopbackTable": wwpOamLoopbackTable,
       "wwpOamLoopbackEntry": wwpOamLoopbackEntry,
       "wwpOamLoopbackCommand": wwpOamLoopbackCommand,
       "wwpOamLoopbackStatus": wwpOamLoopbackStatus,
       "wwpOamLoopbackIgnoreRx": wwpOamLoopbackIgnoreRx,
       "wwpOamLoopbackPort": wwpOamLoopbackPort,
       "wwpOamStatsTable": wwpOamStatsTable,
       "wwpOamStatsEntry": wwpOamStatsEntry,
       "wwpOamInformationTx": wwpOamInformationTx,
       "wwpOamInformationRx": wwpOamInformationRx,
       "wwpOamUniqueEventNotificationTx": wwpOamUniqueEventNotificationTx,
       "wwpOamUniqueEventNotificationRx": wwpOamUniqueEventNotificationRx,
       "wwpOamLoopbackControlTx": wwpOamLoopbackControlTx,
       "wwpOamLoopbackControlRx": wwpOamLoopbackControlRx,
       "wwpOamVariableRequestTx": wwpOamVariableRequestTx,
       "wwpOamVariableRequestRx": wwpOamVariableRequestRx,
       "wwpOamVariableResponseTx": wwpOamVariableResponseTx,
       "wwpOamVariableResponseRx": wwpOamVariableResponseRx,
       "wwpOamOrgSpecificTx": wwpOamOrgSpecificTx,
       "wwpOamOrgSpecificRx": wwpOamOrgSpecificRx,
       "wwpOamUnsupportedCodesTx": wwpOamUnsupportedCodesTx,
       "wwpOamUnsupportedCodesRx": wwpOamUnsupportedCodesRx,
       "wwpOamframesLostDueToOam": wwpOamframesLostDueToOam,
       "wwpOamStatsPort": wwpOamStatsPort,
       "wwpOamDuplicateEventNotificationTx": wwpOamDuplicateEventNotificationTx,
       "wwpOamDuplicateEventNotificationRx": wwpOamDuplicateEventNotificationRx,
       "wwpOamSystemEnableDisable": wwpOamSystemEnableDisable,
       "wwpOamEventConfigTable": wwpOamEventConfigTable,
       "wwpOamEventConfigEntry": wwpOamEventConfigEntry,
       "wwpOamEventPort": wwpOamEventPort,
       "wwpOamErrFramePeriodWindow": wwpOamErrFramePeriodWindow,
       "wwpOamErrFramePeriodThreshold": wwpOamErrFramePeriodThreshold,
       "wwpOamErrFramePeriodEvNotifEnable": wwpOamErrFramePeriodEvNotifEnable,
       "wwpOamErrFrameWindow": wwpOamErrFrameWindow,
       "wwpOamErrFrameThreshold": wwpOamErrFrameThreshold,
       "wwpOamErrFrameEvNotifEnable": wwpOamErrFrameEvNotifEnable,
       "wwpOamErrFrameSecsSummaryWindow": wwpOamErrFrameSecsSummaryWindow,
       "wwpOamErrFrameSecsSummaryThreshold": wwpOamErrFrameSecsSummaryThreshold,
       "wwpOamErrFrameSecsEvNotifEnable": wwpOamErrFrameSecsEvNotifEnable,
       "wwpOamDyingGaspEnable": wwpOamDyingGaspEnable,
       "wwpOamCriticalEventEnable": wwpOamCriticalEventEnable,
       "wwpOamEventLogTable": wwpOamEventLogTable,
       "wwpOamEventLogEntry": wwpOamEventLogEntry,
       "wwpOamEventLogPort": wwpOamEventLogPort,
       "wwpOamEventLogIndex": wwpOamEventLogIndex,
       "wwpOamEventLogTimestamp": wwpOamEventLogTimestamp,
       "wwpOamEventLogOui": wwpOamEventLogOui,
       "wwpOamEventLogType": wwpOamEventLogType,
       "wwpOamEventLogLocation": wwpOamEventLogLocation,
       "wwpOamEventLogWindowHi": wwpOamEventLogWindowHi,
       "wwpOamEventLogWindowLo": wwpOamEventLogWindowLo,
       "wwpOamEventLogThresholdHi": wwpOamEventLogThresholdHi,
       "wwpOamEventLogThresholdLo": wwpOamEventLogThresholdLo,
       "wwpOamEventLogValue": wwpOamEventLogValue,
       "wwpOamEventLogRunningTotal": wwpOamEventLogRunningTotal,
       "wwpOamEventLogEventTotal": wwpOamEventLogEventTotal,
       "wwpOamEvents": wwpOamEvents,
       "wwpOamEventsV2": wwpOamEventsV2}
)
