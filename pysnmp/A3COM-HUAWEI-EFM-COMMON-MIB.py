# SNMP MIB module (A3COM-HUAWEI-EFM-COMMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-HUAWEI-EFM-COMMON-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:27:50 2024
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

(h3cEpon,) = mibBuilder.importSymbols(
    "A3COM-HUAWEI-OID-MIB",
    "h3cEpon")

(CounterBasedGauge64,) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "CounterBasedGauge64")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DateAndTime,
 DisplayString,
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY

h3cEfmOamMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 3)
)
h3cEfmOamMIB.setRevisions(
        ("2004-10-24 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Dot3Oui(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )



# MIB Managed Objects in the order of their OIDs

_H3cDot3OamMIB_ObjectIdentity = ObjectIdentity
h3cDot3OamMIB = _H3cDot3OamMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 3, 1)
)
_H3cDot3OamTable_Object = MibTable
h3cDot3OamTable = _H3cDot3OamTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 3, 1, 1)
)
if mibBuilder.loadTexts:
    h3cDot3OamTable.setStatus("current")
_H3cDot3OamEntry_Object = MibTableRow
h3cDot3OamEntry = _H3cDot3OamEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 3, 1, 1, 1)
)
h3cDot3OamEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cDot3OamEntry.setStatus("current")


class _H3cDot3OamAdminState_Type(Integer32):
    """Custom type h3cDot3OamAdminState based on Integer32"""
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


_H3cDot3OamAdminState_Type.__name__ = "Integer32"
_H3cDot3OamAdminState_Object = MibTableColumn
h3cDot3OamAdminState = _H3cDot3OamAdminState_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 3, 1, 1, 1, 1),
    _H3cDot3OamAdminState_Type()
)
h3cDot3OamAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot3OamAdminState.setStatus("current")


class _H3cDot3OamOperStatus_Type(Integer32):
    """Custom type h3cDot3OamOperStatus based on Integer32"""
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


_H3cDot3OamOperStatus_Type.__name__ = "Integer32"
_H3cDot3OamOperStatus_Object = MibTableColumn
h3cDot3OamOperStatus = _H3cDot3OamOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 3, 1, 1, 1, 2),
    _H3cDot3OamOperStatus_Type()
)
h3cDot3OamOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot3OamOperStatus.setStatus("current")


class _H3cDot3OamMode_Type(Integer32):
    """Custom type h3cDot3OamMode based on Integer32"""
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


_H3cDot3OamMode_Type.__name__ = "Integer32"
_H3cDot3OamMode_Object = MibTableColumn
h3cDot3OamMode = _H3cDot3OamMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 3, 1, 1, 1, 3),
    _H3cDot3OamMode_Type()
)
h3cDot3OamMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot3OamMode.setStatus("current")


class _H3cDot3OamMaxOamPduSize_Type(Integer32):
    """Custom type h3cDot3OamMaxOamPduSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 1522),
    )


_H3cDot3OamMaxOamPduSize_Type.__name__ = "Integer32"
_H3cDot3OamMaxOamPduSize_Object = MibTableColumn
h3cDot3OamMaxOamPduSize = _H3cDot3OamMaxOamPduSize_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 3, 1, 1, 1, 4),
    _H3cDot3OamMaxOamPduSize_Type()
)
h3cDot3OamMaxOamPduSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot3OamMaxOamPduSize.setStatus("current")
_H3cDot3OamConfigRevision_Type = Unsigned32
_H3cDot3OamConfigRevision_Object = MibTableColumn
h3cDot3OamConfigRevision = _H3cDot3OamConfigRevision_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 3, 1, 1, 1, 5),
    _H3cDot3OamConfigRevision_Type()
)
h3cDot3OamConfigRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot3OamConfigRevision.setStatus("current")


class _H3cDot3OamFunctionsSupported_Type(Bits):
    """Custom type h3cDot3OamFunctionsSupported based on Bits"""
    namedValues = NamedValues(
        *(("eventSupport", 2),
          ("loopbackSupport", 1),
          ("unidirectionalSupport", 0),
          ("variableSupport", 3))
    )

_H3cDot3OamFunctionsSupported_Type.__name__ = "Bits"
_H3cDot3OamFunctionsSupported_Object = MibTableColumn
h3cDot3OamFunctionsSupported = _H3cDot3OamFunctionsSupported_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 3, 1, 1, 1, 6),
    _H3cDot3OamFunctionsSupported_Type()
)
h3cDot3OamFunctionsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot3OamFunctionsSupported.setStatus("current")
_H3cDot3OamPeerTable_Object = MibTable
h3cDot3OamPeerTable = _H3cDot3OamPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 3, 1, 2)
)
if mibBuilder.loadTexts:
    h3cDot3OamPeerTable.setStatus("current")
_H3cDot3OamPeerEntry_Object = MibTableRow
h3cDot3OamPeerEntry = _H3cDot3OamPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 3, 1, 2, 1)
)
h3cDot3OamPeerEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cDot3OamPeerEntry.setStatus("current")


class _H3cDot3OamPeerStatus_Type(Integer32):
    """Custom type h3cDot3OamPeerStatus based on Integer32"""
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


_H3cDot3OamPeerStatus_Type.__name__ = "Integer32"
_H3cDot3OamPeerStatus_Object = MibTableColumn
h3cDot3OamPeerStatus = _H3cDot3OamPeerStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 3, 1, 2, 1, 1),
    _H3cDot3OamPeerStatus_Type()
)
h3cDot3OamPeerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot3OamPeerStatus.setStatus("current")
_H3cDot3OamPeerMacAddress_Type = MacAddress
_H3cDot3OamPeerMacAddress_Object = MibTableColumn
h3cDot3OamPeerMacAddress = _H3cDot3OamPeerMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 3, 1, 2, 1, 2),
    _H3cDot3OamPeerMacAddress_Type()
)
h3cDot3OamPeerMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot3OamPeerMacAddress.setStatus("current")
_H3cDot3OamPeerVendorOui_Type = Dot3Oui
_H3cDot3OamPeerVendorOui_Object = MibTableColumn
h3cDot3OamPeerVendorOui = _H3cDot3OamPeerVendorOui_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 3, 1, 2, 1, 3),
    _H3cDot3OamPeerVendorOui_Type()
)
h3cDot3OamPeerVendorOui.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot3OamPeerVendorOui.setStatus("current")
_H3cDot3OamPeerVendorInfo_Type = Unsigned32
_H3cDot3OamPeerVendorInfo_Object = MibTableColumn
h3cDot3OamPeerVendorInfo = _H3cDot3OamPeerVendorInfo_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 3, 1, 2, 1, 4),
    _H3cDot3OamPeerVendorInfo_Type()
)
h3cDot3OamPeerVendorInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot3OamPeerVendorInfo.setStatus("current")


class _H3cDot3OamPeerMode_Type(Integer32):
    """Custom type h3cDot3OamPeerMode based on Integer32"""
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


_H3cDot3OamPeerMode_Type.__name__ = "Integer32"
_H3cDot3OamPeerMode_Object = MibTableColumn
h3cDot3OamPeerMode = _H3cDot3OamPeerMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 3, 1, 2, 1, 5),
    _H3cDot3OamPeerMode_Type()
)
h3cDot3OamPeerMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot3OamPeerMode.setStatus("current")


class _H3cDot3OamPeerMaxOamPduSize_Type(Integer32):
    """Custom type h3cDot3OamPeerMaxOamPduSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 1522),
    )


_H3cDot3OamPeerMaxOamPduSize_Type.__name__ = "Integer32"
_H3cDot3OamPeerMaxOamPduSize_Object = MibTableColumn
h3cDot3OamPeerMaxOamPduSize = _H3cDot3OamPeerMaxOamPduSize_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 3, 1, 2, 1, 6),
    _H3cDot3OamPeerMaxOamPduSize_Type()
)
h3cDot3OamPeerMaxOamPduSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot3OamPeerMaxOamPduSize.setStatus("current")
_H3cDot3OamPeerConfigRevision_Type = Unsigned32
_H3cDot3OamPeerConfigRevision_Object = MibTableColumn
h3cDot3OamPeerConfigRevision = _H3cDot3OamPeerConfigRevision_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 3, 1, 2, 1, 7),
    _H3cDot3OamPeerConfigRevision_Type()
)
h3cDot3OamPeerConfigRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot3OamPeerConfigRevision.setStatus("current")


class _H3cDot3OamPeerFunctionsSupported_Type(Bits):
    """Custom type h3cDot3OamPeerFunctionsSupported based on Bits"""
    namedValues = NamedValues(
        *(("eventSupport", 2),
          ("loopbackSupport", 1),
          ("unidirectionalSupport", 0),
          ("variableSupport", 3))
    )

_H3cDot3OamPeerFunctionsSupported_Type.__name__ = "Bits"
_H3cDot3OamPeerFunctionsSupported_Object = MibTableColumn
h3cDot3OamPeerFunctionsSupported = _H3cDot3OamPeerFunctionsSupported_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 3, 1, 2, 1, 8),
    _H3cDot3OamPeerFunctionsSupported_Type()
)
h3cDot3OamPeerFunctionsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot3OamPeerFunctionsSupported.setStatus("current")
_H3cDot3OamLoopbackTable_Object = MibTable
h3cDot3OamLoopbackTable = _H3cDot3OamLoopbackTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 3, 1, 3)
)
if mibBuilder.loadTexts:
    h3cDot3OamLoopbackTable.setStatus("current")
_H3cDot3OamLoopbackEntry_Object = MibTableRow
h3cDot3OamLoopbackEntry = _H3cDot3OamLoopbackEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 3, 1, 3, 1)
)
h3cDot3OamLoopbackEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cDot3OamLoopbackEntry.setStatus("current")


class _H3cDot3OamLoopbackCommand_Type(Integer32):
    """Custom type h3cDot3OamLoopbackCommand based on Integer32"""
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


_H3cDot3OamLoopbackCommand_Type.__name__ = "Integer32"
_H3cDot3OamLoopbackCommand_Object = MibTableColumn
h3cDot3OamLoopbackCommand = _H3cDot3OamLoopbackCommand_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 3, 1, 3, 1, 1),
    _H3cDot3OamLoopbackCommand_Type()
)
h3cDot3OamLoopbackCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot3OamLoopbackCommand.setStatus("current")


class _H3cDot3OamLoopbackStatus_Type(Integer32):
    """Custom type h3cDot3OamLoopbackStatus based on Integer32"""
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


_H3cDot3OamLoopbackStatus_Type.__name__ = "Integer32"
_H3cDot3OamLoopbackStatus_Object = MibTableColumn
h3cDot3OamLoopbackStatus = _H3cDot3OamLoopbackStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 3, 1, 3, 1, 2),
    _H3cDot3OamLoopbackStatus_Type()
)
h3cDot3OamLoopbackStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot3OamLoopbackStatus.setStatus("current")


class _H3cDot3OamLoopbackIgnoreRx_Type(Integer32):
    """Custom type h3cDot3OamLoopbackIgnoreRx based on Integer32"""
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


_H3cDot3OamLoopbackIgnoreRx_Type.__name__ = "Integer32"
_H3cDot3OamLoopbackIgnoreRx_Object = MibTableColumn
h3cDot3OamLoopbackIgnoreRx = _H3cDot3OamLoopbackIgnoreRx_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 3, 1, 3, 1, 3),
    _H3cDot3OamLoopbackIgnoreRx_Type()
)
h3cDot3OamLoopbackIgnoreRx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot3OamLoopbackIgnoreRx.setStatus("current")
_H3cDot3OamStatsTable_Object = MibTable
h3cDot3OamStatsTable = _H3cDot3OamStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 3, 1, 4)
)
if mibBuilder.loadTexts:
    h3cDot3OamStatsTable.setStatus("current")
_H3cDot3OamStatsEntry_Object = MibTableRow
h3cDot3OamStatsEntry = _H3cDot3OamStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 3, 1, 4, 1)
)
h3cDot3OamStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cDot3OamStatsEntry.setStatus("current")
_H3cDot3OamInformationTx_Type = Counter32
_H3cDot3OamInformationTx_Object = MibTableColumn
h3cDot3OamInformationTx = _H3cDot3OamInformationTx_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 3, 1, 4, 1, 1),
    _H3cDot3OamInformationTx_Type()
)
h3cDot3OamInformationTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot3OamInformationTx.setStatus("current")
_H3cDot3OamInformationRx_Type = Counter32
_H3cDot3OamInformationRx_Object = MibTableColumn
h3cDot3OamInformationRx = _H3cDot3OamInformationRx_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 3, 1, 4, 1, 2),
    _H3cDot3OamInformationRx_Type()
)
h3cDot3OamInformationRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot3OamInformationRx.setStatus("current")
_H3cDot3OamUniqueEventNotificationTx_Type = Counter32
_H3cDot3OamUniqueEventNotificationTx_Object = MibTableColumn
h3cDot3OamUniqueEventNotificationTx = _H3cDot3OamUniqueEventNotificationTx_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 3, 1, 4, 1, 3),
    _H3cDot3OamUniqueEventNotificationTx_Type()
)
h3cDot3OamUniqueEventNotificationTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot3OamUniqueEventNotificationTx.setStatus("current")
_H3cDot3OamUniqueEventNotificationRx_Type = Counter32
_H3cDot3OamUniqueEventNotificationRx_Object = MibTableColumn
h3cDot3OamUniqueEventNotificationRx = _H3cDot3OamUniqueEventNotificationRx_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 3, 1, 4, 1, 4),
    _H3cDot3OamUniqueEventNotificationRx_Type()
)
h3cDot3OamUniqueEventNotificationRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot3OamUniqueEventNotificationRx.setStatus("current")
_H3cDot3OamDuplicateEventNotificationTx_Type = Counter32
_H3cDot3OamDuplicateEventNotificationTx_Object = MibTableColumn
h3cDot3OamDuplicateEventNotificationTx = _H3cDot3OamDuplicateEventNotificationTx_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 3, 1, 4, 1, 5),
    _H3cDot3OamDuplicateEventNotificationTx_Type()
)
h3cDot3OamDuplicateEventNotificationTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot3OamDuplicateEventNotificationTx.setStatus("current")
_H3cDot3OamDuplicateEventNotificationRx_Type = Counter32
_H3cDot3OamDuplicateEventNotificationRx_Object = MibTableColumn
h3cDot3OamDuplicateEventNotificationRx = _H3cDot3OamDuplicateEventNotificationRx_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 3, 1, 4, 1, 6),
    _H3cDot3OamDuplicateEventNotificationRx_Type()
)
h3cDot3OamDuplicateEventNotificationRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot3OamDuplicateEventNotificationRx.setStatus("current")
_H3cDot3OamLoopbackControlTx_Type = Counter32
_H3cDot3OamLoopbackControlTx_Object = MibTableColumn
h3cDot3OamLoopbackControlTx = _H3cDot3OamLoopbackControlTx_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 3, 1, 4, 1, 7),
    _H3cDot3OamLoopbackControlTx_Type()
)
h3cDot3OamLoopbackControlTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot3OamLoopbackControlTx.setStatus("current")
_H3cDot3OamLoopbackControlRx_Type = Counter32
_H3cDot3OamLoopbackControlRx_Object = MibTableColumn
h3cDot3OamLoopbackControlRx = _H3cDot3OamLoopbackControlRx_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 3, 1, 4, 1, 8),
    _H3cDot3OamLoopbackControlRx_Type()
)
h3cDot3OamLoopbackControlRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot3OamLoopbackControlRx.setStatus("current")
_H3cDot3OamVariableRequestTx_Type = Counter32
_H3cDot3OamVariableRequestTx_Object = MibTableColumn
h3cDot3OamVariableRequestTx = _H3cDot3OamVariableRequestTx_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 3, 1, 4, 1, 9),
    _H3cDot3OamVariableRequestTx_Type()
)
h3cDot3OamVariableRequestTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot3OamVariableRequestTx.setStatus("current")
_H3cDot3OamVariableRequestRx_Type = Counter32
_H3cDot3OamVariableRequestRx_Object = MibTableColumn
h3cDot3OamVariableRequestRx = _H3cDot3OamVariableRequestRx_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 3, 1, 4, 1, 10),
    _H3cDot3OamVariableRequestRx_Type()
)
h3cDot3OamVariableRequestRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot3OamVariableRequestRx.setStatus("current")
_H3cDot3OamVariableResponseTx_Type = Counter32
_H3cDot3OamVariableResponseTx_Object = MibTableColumn
h3cDot3OamVariableResponseTx = _H3cDot3OamVariableResponseTx_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 3, 1, 4, 1, 11),
    _H3cDot3OamVariableResponseTx_Type()
)
h3cDot3OamVariableResponseTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot3OamVariableResponseTx.setStatus("current")
_H3cDot3OamVariableResponseRx_Type = Counter32
_H3cDot3OamVariableResponseRx_Object = MibTableColumn
h3cDot3OamVariableResponseRx = _H3cDot3OamVariableResponseRx_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 3, 1, 4, 1, 12),
    _H3cDot3OamVariableResponseRx_Type()
)
h3cDot3OamVariableResponseRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot3OamVariableResponseRx.setStatus("current")
_H3cDot3OamOrgSpecificTx_Type = Counter32
_H3cDot3OamOrgSpecificTx_Object = MibTableColumn
h3cDot3OamOrgSpecificTx = _H3cDot3OamOrgSpecificTx_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 3, 1, 4, 1, 13),
    _H3cDot3OamOrgSpecificTx_Type()
)
h3cDot3OamOrgSpecificTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot3OamOrgSpecificTx.setStatus("current")
_H3cDot3OamOrgSpecificRx_Type = Counter32
_H3cDot3OamOrgSpecificRx_Object = MibTableColumn
h3cDot3OamOrgSpecificRx = _H3cDot3OamOrgSpecificRx_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 3, 1, 4, 1, 14),
    _H3cDot3OamOrgSpecificRx_Type()
)
h3cDot3OamOrgSpecificRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot3OamOrgSpecificRx.setStatus("current")
_H3cDot3OamUnsupportedCodesTx_Type = Counter32
_H3cDot3OamUnsupportedCodesTx_Object = MibTableColumn
h3cDot3OamUnsupportedCodesTx = _H3cDot3OamUnsupportedCodesTx_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 3, 1, 4, 1, 15),
    _H3cDot3OamUnsupportedCodesTx_Type()
)
h3cDot3OamUnsupportedCodesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot3OamUnsupportedCodesTx.setStatus("current")
_H3cDot3OamUnsupportedCodesRx_Type = Counter32
_H3cDot3OamUnsupportedCodesRx_Object = MibTableColumn
h3cDot3OamUnsupportedCodesRx = _H3cDot3OamUnsupportedCodesRx_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 3, 1, 4, 1, 16),
    _H3cDot3OamUnsupportedCodesRx_Type()
)
h3cDot3OamUnsupportedCodesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot3OamUnsupportedCodesRx.setStatus("current")
_H3cDot3OamFramesLostDueToOam_Type = Counter32
_H3cDot3OamFramesLostDueToOam_Object = MibTableColumn
h3cDot3OamFramesLostDueToOam = _H3cDot3OamFramesLostDueToOam_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 3, 1, 4, 1, 17),
    _H3cDot3OamFramesLostDueToOam_Type()
)
h3cDot3OamFramesLostDueToOam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot3OamFramesLostDueToOam.setStatus("current")
_H3cDot3OamEventConfigTable_Object = MibTable
h3cDot3OamEventConfigTable = _H3cDot3OamEventConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 3, 1, 5)
)
if mibBuilder.loadTexts:
    h3cDot3OamEventConfigTable.setStatus("current")
_H3cDot3OamEventConfigEntry_Object = MibTableRow
h3cDot3OamEventConfigEntry = _H3cDot3OamEventConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 3, 1, 5, 1)
)
h3cDot3OamEventConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cDot3OamEventConfigEntry.setStatus("current")
_H3cDot3OamErrSymPeriodWindowHi_Type = Unsigned32
_H3cDot3OamErrSymPeriodWindowHi_Object = MibTableColumn
h3cDot3OamErrSymPeriodWindowHi = _H3cDot3OamErrSymPeriodWindowHi_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 3, 1, 5, 1, 1),
    _H3cDot3OamErrSymPeriodWindowHi_Type()
)
h3cDot3OamErrSymPeriodWindowHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot3OamErrSymPeriodWindowHi.setStatus("current")
_H3cDot3OamErrSymPeriodWindowLo_Type = Unsigned32
_H3cDot3OamErrSymPeriodWindowLo_Object = MibTableColumn
h3cDot3OamErrSymPeriodWindowLo = _H3cDot3OamErrSymPeriodWindowLo_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 3, 1, 5, 1, 2),
    _H3cDot3OamErrSymPeriodWindowLo_Type()
)
h3cDot3OamErrSymPeriodWindowLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot3OamErrSymPeriodWindowLo.setStatus("current")
_H3cDot3OamErrSymPeriodThresholdHi_Type = Unsigned32
_H3cDot3OamErrSymPeriodThresholdHi_Object = MibTableColumn
h3cDot3OamErrSymPeriodThresholdHi = _H3cDot3OamErrSymPeriodThresholdHi_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 3, 1, 5, 1, 3),
    _H3cDot3OamErrSymPeriodThresholdHi_Type()
)
h3cDot3OamErrSymPeriodThresholdHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot3OamErrSymPeriodThresholdHi.setStatus("current")
_H3cDot3OamErrSymPeriodThresholdLo_Type = Unsigned32
_H3cDot3OamErrSymPeriodThresholdLo_Object = MibTableColumn
h3cDot3OamErrSymPeriodThresholdLo = _H3cDot3OamErrSymPeriodThresholdLo_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 3, 1, 5, 1, 4),
    _H3cDot3OamErrSymPeriodThresholdLo_Type()
)
h3cDot3OamErrSymPeriodThresholdLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot3OamErrSymPeriodThresholdLo.setStatus("current")


class _H3cDot3OamErrSymPeriodEvNotifEnable_Type(Integer32):
    """Custom type h3cDot3OamErrSymPeriodEvNotifEnable based on Integer32"""
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


_H3cDot3OamErrSymPeriodEvNotifEnable_Type.__name__ = "Integer32"
_H3cDot3OamErrSymPeriodEvNotifEnable_Object = MibTableColumn
h3cDot3OamErrSymPeriodEvNotifEnable = _H3cDot3OamErrSymPeriodEvNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 3, 1, 5, 1, 5),
    _H3cDot3OamErrSymPeriodEvNotifEnable_Type()
)
h3cDot3OamErrSymPeriodEvNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot3OamErrSymPeriodEvNotifEnable.setStatus("current")
_H3cDot3OamErrFramePeriodWindow_Type = Unsigned32
_H3cDot3OamErrFramePeriodWindow_Object = MibTableColumn
h3cDot3OamErrFramePeriodWindow = _H3cDot3OamErrFramePeriodWindow_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 3, 1, 5, 1, 6),
    _H3cDot3OamErrFramePeriodWindow_Type()
)
h3cDot3OamErrFramePeriodWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot3OamErrFramePeriodWindow.setStatus("current")
_H3cDot3OamErrFramePeriodThreshold_Type = Unsigned32
_H3cDot3OamErrFramePeriodThreshold_Object = MibTableColumn
h3cDot3OamErrFramePeriodThreshold = _H3cDot3OamErrFramePeriodThreshold_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 3, 1, 5, 1, 7),
    _H3cDot3OamErrFramePeriodThreshold_Type()
)
h3cDot3OamErrFramePeriodThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot3OamErrFramePeriodThreshold.setStatus("current")


class _H3cDot3OamErrFramePeriodEvNotifEnable_Type(Integer32):
    """Custom type h3cDot3OamErrFramePeriodEvNotifEnable based on Integer32"""
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


_H3cDot3OamErrFramePeriodEvNotifEnable_Type.__name__ = "Integer32"
_H3cDot3OamErrFramePeriodEvNotifEnable_Object = MibTableColumn
h3cDot3OamErrFramePeriodEvNotifEnable = _H3cDot3OamErrFramePeriodEvNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 3, 1, 5, 1, 8),
    _H3cDot3OamErrFramePeriodEvNotifEnable_Type()
)
h3cDot3OamErrFramePeriodEvNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot3OamErrFramePeriodEvNotifEnable.setStatus("current")
_H3cDot3OamErrFrameWindow_Type = Unsigned32
_H3cDot3OamErrFrameWindow_Object = MibTableColumn
h3cDot3OamErrFrameWindow = _H3cDot3OamErrFrameWindow_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 3, 1, 5, 1, 9),
    _H3cDot3OamErrFrameWindow_Type()
)
h3cDot3OamErrFrameWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot3OamErrFrameWindow.setStatus("current")
_H3cDot3OamErrFrameThreshold_Type = Unsigned32
_H3cDot3OamErrFrameThreshold_Object = MibTableColumn
h3cDot3OamErrFrameThreshold = _H3cDot3OamErrFrameThreshold_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 3, 1, 5, 1, 10),
    _H3cDot3OamErrFrameThreshold_Type()
)
h3cDot3OamErrFrameThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot3OamErrFrameThreshold.setStatus("current")


class _H3cDot3OamErrFrameEvNotifEnable_Type(Integer32):
    """Custom type h3cDot3OamErrFrameEvNotifEnable based on Integer32"""
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


_H3cDot3OamErrFrameEvNotifEnable_Type.__name__ = "Integer32"
_H3cDot3OamErrFrameEvNotifEnable_Object = MibTableColumn
h3cDot3OamErrFrameEvNotifEnable = _H3cDot3OamErrFrameEvNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 3, 1, 5, 1, 11),
    _H3cDot3OamErrFrameEvNotifEnable_Type()
)
h3cDot3OamErrFrameEvNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot3OamErrFrameEvNotifEnable.setStatus("current")


class _H3cDot3OamErrFrameSecsSummaryWindow_Type(Integer32):
    """Custom type h3cDot3OamErrFrameSecsSummaryWindow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 9000),
    )


_H3cDot3OamErrFrameSecsSummaryWindow_Type.__name__ = "Integer32"
_H3cDot3OamErrFrameSecsSummaryWindow_Object = MibTableColumn
h3cDot3OamErrFrameSecsSummaryWindow = _H3cDot3OamErrFrameSecsSummaryWindow_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 3, 1, 5, 1, 12),
    _H3cDot3OamErrFrameSecsSummaryWindow_Type()
)
h3cDot3OamErrFrameSecsSummaryWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot3OamErrFrameSecsSummaryWindow.setStatus("current")


class _H3cDot3OamErrFrameSecsSummaryThreshold_Type(Integer32):
    """Custom type h3cDot3OamErrFrameSecsSummaryThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_H3cDot3OamErrFrameSecsSummaryThreshold_Type.__name__ = "Integer32"
_H3cDot3OamErrFrameSecsSummaryThreshold_Object = MibTableColumn
h3cDot3OamErrFrameSecsSummaryThreshold = _H3cDot3OamErrFrameSecsSummaryThreshold_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 3, 1, 5, 1, 13),
    _H3cDot3OamErrFrameSecsSummaryThreshold_Type()
)
h3cDot3OamErrFrameSecsSummaryThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot3OamErrFrameSecsSummaryThreshold.setStatus("current")


class _H3cDot3OamErrFrameSecsEvNotifEnable_Type(Integer32):
    """Custom type h3cDot3OamErrFrameSecsEvNotifEnable based on Integer32"""
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


_H3cDot3OamErrFrameSecsEvNotifEnable_Type.__name__ = "Integer32"
_H3cDot3OamErrFrameSecsEvNotifEnable_Object = MibTableColumn
h3cDot3OamErrFrameSecsEvNotifEnable = _H3cDot3OamErrFrameSecsEvNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 3, 1, 5, 1, 14),
    _H3cDot3OamErrFrameSecsEvNotifEnable_Type()
)
h3cDot3OamErrFrameSecsEvNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot3OamErrFrameSecsEvNotifEnable.setStatus("current")
_H3cDot3OamEventLogTable_Object = MibTable
h3cDot3OamEventLogTable = _H3cDot3OamEventLogTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 3, 1, 6)
)
if mibBuilder.loadTexts:
    h3cDot3OamEventLogTable.setStatus("current")
_H3cDot3OamEventLogEntry_Object = MibTableRow
h3cDot3OamEventLogEntry = _H3cDot3OamEventLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 3, 1, 6, 1)
)
h3cDot3OamEventLogEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "A3COM-HUAWEI-EFM-COMMON-MIB", "h3cDot3OamEventLogIndex"),
)
if mibBuilder.loadTexts:
    h3cDot3OamEventLogEntry.setStatus("current")
_H3cDot3OamEventLogIndex_Type = Unsigned32
_H3cDot3OamEventLogIndex_Object = MibTableColumn
h3cDot3OamEventLogIndex = _H3cDot3OamEventLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 3, 1, 6, 1, 1),
    _H3cDot3OamEventLogIndex_Type()
)
h3cDot3OamEventLogIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot3OamEventLogIndex.setStatus("current")
_H3cDot3OamEventLogTimestamp_Type = DateAndTime
_H3cDot3OamEventLogTimestamp_Object = MibTableColumn
h3cDot3OamEventLogTimestamp = _H3cDot3OamEventLogTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 3, 1, 6, 1, 2),
    _H3cDot3OamEventLogTimestamp_Type()
)
h3cDot3OamEventLogTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot3OamEventLogTimestamp.setStatus("current")
_H3cDot3OamEventLogOui_Type = Dot3Oui
_H3cDot3OamEventLogOui_Object = MibTableColumn
h3cDot3OamEventLogOui = _H3cDot3OamEventLogOui_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 3, 1, 6, 1, 3),
    _H3cDot3OamEventLogOui_Type()
)
h3cDot3OamEventLogOui.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot3OamEventLogOui.setStatus("current")
_H3cDot3OamEventLogType_Type = Unsigned32
_H3cDot3OamEventLogType_Object = MibTableColumn
h3cDot3OamEventLogType = _H3cDot3OamEventLogType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 3, 1, 6, 1, 4),
    _H3cDot3OamEventLogType_Type()
)
h3cDot3OamEventLogType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot3OamEventLogType.setStatus("current")


class _H3cDot3OamEventLogLocation_Type(Integer32):
    """Custom type h3cDot3OamEventLogLocation based on Integer32"""
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


_H3cDot3OamEventLogLocation_Type.__name__ = "Integer32"
_H3cDot3OamEventLogLocation_Object = MibTableColumn
h3cDot3OamEventLogLocation = _H3cDot3OamEventLogLocation_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 3, 1, 6, 1, 5),
    _H3cDot3OamEventLogLocation_Type()
)
h3cDot3OamEventLogLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot3OamEventLogLocation.setStatus("current")
_H3cDot3OamEventLogWindowHi_Type = Unsigned32
_H3cDot3OamEventLogWindowHi_Object = MibTableColumn
h3cDot3OamEventLogWindowHi = _H3cDot3OamEventLogWindowHi_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 3, 1, 6, 1, 6),
    _H3cDot3OamEventLogWindowHi_Type()
)
h3cDot3OamEventLogWindowHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot3OamEventLogWindowHi.setStatus("current")
_H3cDot3OamEventLogWindowLo_Type = Unsigned32
_H3cDot3OamEventLogWindowLo_Object = MibTableColumn
h3cDot3OamEventLogWindowLo = _H3cDot3OamEventLogWindowLo_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 3, 1, 6, 1, 7),
    _H3cDot3OamEventLogWindowLo_Type()
)
h3cDot3OamEventLogWindowLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot3OamEventLogWindowLo.setStatus("current")
_H3cDot3OamEventLogThresholdHi_Type = Unsigned32
_H3cDot3OamEventLogThresholdHi_Object = MibTableColumn
h3cDot3OamEventLogThresholdHi = _H3cDot3OamEventLogThresholdHi_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 3, 1, 6, 1, 8),
    _H3cDot3OamEventLogThresholdHi_Type()
)
h3cDot3OamEventLogThresholdHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot3OamEventLogThresholdHi.setStatus("current")
_H3cDot3OamEventLogThresholdLo_Type = Unsigned32
_H3cDot3OamEventLogThresholdLo_Object = MibTableColumn
h3cDot3OamEventLogThresholdLo = _H3cDot3OamEventLogThresholdLo_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 3, 1, 6, 1, 9),
    _H3cDot3OamEventLogThresholdLo_Type()
)
h3cDot3OamEventLogThresholdLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot3OamEventLogThresholdLo.setStatus("current")
_H3cDot3OamEventLogValue_Type = CounterBasedGauge64
_H3cDot3OamEventLogValue_Object = MibTableColumn
h3cDot3OamEventLogValue = _H3cDot3OamEventLogValue_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 3, 1, 6, 1, 10),
    _H3cDot3OamEventLogValue_Type()
)
h3cDot3OamEventLogValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot3OamEventLogValue.setStatus("current")
_H3cDot3OamEventLogRunningTotal_Type = CounterBasedGauge64
_H3cDot3OamEventLogRunningTotal_Object = MibTableColumn
h3cDot3OamEventLogRunningTotal = _H3cDot3OamEventLogRunningTotal_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 3, 1, 6, 1, 11),
    _H3cDot3OamEventLogRunningTotal_Type()
)
h3cDot3OamEventLogRunningTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot3OamEventLogRunningTotal.setStatus("current")
_H3cDot3OamEventLogEventTotal_Type = Unsigned32
_H3cDot3OamEventLogEventTotal_Object = MibTableColumn
h3cDot3OamEventLogEventTotal = _H3cDot3OamEventLogEventTotal_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 3, 1, 6, 1, 12),
    _H3cDot3OamEventLogEventTotal_Type()
)
h3cDot3OamEventLogEventTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot3OamEventLogEventTotal.setStatus("current")
_H3cDot3OamTraps_ObjectIdentity = ObjectIdentity
h3cDot3OamTraps = _H3cDot3OamTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 3, 1, 7)
)
_H3cDot3OamTrapsPrefix_ObjectIdentity = ObjectIdentity
h3cDot3OamTrapsPrefix = _H3cDot3OamTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 3, 1, 7, 0)
)
_H3cDot3OamConformance_ObjectIdentity = ObjectIdentity
h3cDot3OamConformance = _H3cDot3OamConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 3, 2)
)
_H3cDot3OamGroups_ObjectIdentity = ObjectIdentity
h3cDot3OamGroups = _H3cDot3OamGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 3, 2, 1)
)
_H3cDot3OamCompliances_ObjectIdentity = ObjectIdentity
h3cDot3OamCompliances = _H3cDot3OamCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 3, 2, 2)
)

# Managed Objects groups

h3cDot3OamControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 3, 2, 1, 1)
)
h3cDot3OamControlGroup.setObjects(
      *(("A3COM-HUAWEI-EFM-COMMON-MIB", "h3cDot3OamAdminState"),
        ("A3COM-HUAWEI-EFM-COMMON-MIB", "h3cDot3OamOperStatus"),
        ("A3COM-HUAWEI-EFM-COMMON-MIB", "h3cDot3OamMode"),
        ("A3COM-HUAWEI-EFM-COMMON-MIB", "h3cDot3OamMaxOamPduSize"),
        ("A3COM-HUAWEI-EFM-COMMON-MIB", "h3cDot3OamConfigRevision"),
        ("A3COM-HUAWEI-EFM-COMMON-MIB", "h3cDot3OamFunctionsSupported"))
)
if mibBuilder.loadTexts:
    h3cDot3OamControlGroup.setStatus("current")

h3cDot3OamPeerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 3, 2, 1, 2)
)
h3cDot3OamPeerGroup.setObjects(
      *(("A3COM-HUAWEI-EFM-COMMON-MIB", "h3cDot3OamPeerStatus"),
        ("A3COM-HUAWEI-EFM-COMMON-MIB", "h3cDot3OamPeerMacAddress"),
        ("A3COM-HUAWEI-EFM-COMMON-MIB", "h3cDot3OamPeerVendorOui"),
        ("A3COM-HUAWEI-EFM-COMMON-MIB", "h3cDot3OamPeerVendorInfo"),
        ("A3COM-HUAWEI-EFM-COMMON-MIB", "h3cDot3OamPeerMode"),
        ("A3COM-HUAWEI-EFM-COMMON-MIB", "h3cDot3OamPeerFunctionsSupported"),
        ("A3COM-HUAWEI-EFM-COMMON-MIB", "h3cDot3OamPeerMaxOamPduSize"),
        ("A3COM-HUAWEI-EFM-COMMON-MIB", "h3cDot3OamPeerConfigRevision"))
)
if mibBuilder.loadTexts:
    h3cDot3OamPeerGroup.setStatus("current")

h3cDot3OamStatsBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 3, 2, 1, 3)
)
h3cDot3OamStatsBaseGroup.setObjects(
      *(("A3COM-HUAWEI-EFM-COMMON-MIB", "h3cDot3OamInformationTx"),
        ("A3COM-HUAWEI-EFM-COMMON-MIB", "h3cDot3OamInformationRx"),
        ("A3COM-HUAWEI-EFM-COMMON-MIB", "h3cDot3OamUniqueEventNotificationTx"),
        ("A3COM-HUAWEI-EFM-COMMON-MIB", "h3cDot3OamUniqueEventNotificationRx"),
        ("A3COM-HUAWEI-EFM-COMMON-MIB", "h3cDot3OamDuplicateEventNotificationTx"),
        ("A3COM-HUAWEI-EFM-COMMON-MIB", "h3cDot3OamDuplicateEventNotificationRx"),
        ("A3COM-HUAWEI-EFM-COMMON-MIB", "h3cDot3OamLoopbackControlTx"),
        ("A3COM-HUAWEI-EFM-COMMON-MIB", "h3cDot3OamLoopbackControlRx"),
        ("A3COM-HUAWEI-EFM-COMMON-MIB", "h3cDot3OamVariableRequestTx"),
        ("A3COM-HUAWEI-EFM-COMMON-MIB", "h3cDot3OamVariableRequestRx"),
        ("A3COM-HUAWEI-EFM-COMMON-MIB", "h3cDot3OamVariableResponseTx"),
        ("A3COM-HUAWEI-EFM-COMMON-MIB", "h3cDot3OamVariableResponseRx"),
        ("A3COM-HUAWEI-EFM-COMMON-MIB", "h3cDot3OamOrgSpecificTx"),
        ("A3COM-HUAWEI-EFM-COMMON-MIB", "h3cDot3OamOrgSpecificRx"),
        ("A3COM-HUAWEI-EFM-COMMON-MIB", "h3cDot3OamUnsupportedCodesTx"),
        ("A3COM-HUAWEI-EFM-COMMON-MIB", "h3cDot3OamUnsupportedCodesRx"),
        ("A3COM-HUAWEI-EFM-COMMON-MIB", "h3cDot3OamFramesLostDueToOam"))
)
if mibBuilder.loadTexts:
    h3cDot3OamStatsBaseGroup.setStatus("current")

h3cDot3OamLoopbackGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 3, 2, 1, 4)
)
h3cDot3OamLoopbackGroup.setObjects(
      *(("A3COM-HUAWEI-EFM-COMMON-MIB", "h3cDot3OamLoopbackCommand"),
        ("A3COM-HUAWEI-EFM-COMMON-MIB", "h3cDot3OamLoopbackStatus"),
        ("A3COM-HUAWEI-EFM-COMMON-MIB", "h3cDot3OamLoopbackIgnoreRx"))
)
if mibBuilder.loadTexts:
    h3cDot3OamLoopbackGroup.setStatus("current")

h3cDot3OamErrSymbolPeriodEventGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 3, 2, 1, 5)
)
h3cDot3OamErrSymbolPeriodEventGroup.setObjects(
      *(("A3COM-HUAWEI-EFM-COMMON-MIB", "h3cDot3OamErrSymPeriodWindowHi"),
        ("A3COM-HUAWEI-EFM-COMMON-MIB", "h3cDot3OamErrSymPeriodWindowLo"),
        ("A3COM-HUAWEI-EFM-COMMON-MIB", "h3cDot3OamErrSymPeriodThresholdHi"),
        ("A3COM-HUAWEI-EFM-COMMON-MIB", "h3cDot3OamErrSymPeriodThresholdLo"),
        ("A3COM-HUAWEI-EFM-COMMON-MIB", "h3cDot3OamErrSymPeriodEvNotifEnable"))
)
if mibBuilder.loadTexts:
    h3cDot3OamErrSymbolPeriodEventGroup.setStatus("current")

h3cDot3OamErrFramePeriodEventGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 3, 2, 1, 6)
)
h3cDot3OamErrFramePeriodEventGroup.setObjects(
      *(("A3COM-HUAWEI-EFM-COMMON-MIB", "h3cDot3OamErrFramePeriodWindow"),
        ("A3COM-HUAWEI-EFM-COMMON-MIB", "h3cDot3OamErrFramePeriodThreshold"),
        ("A3COM-HUAWEI-EFM-COMMON-MIB", "h3cDot3OamErrFramePeriodEvNotifEnable"))
)
if mibBuilder.loadTexts:
    h3cDot3OamErrFramePeriodEventGroup.setStatus("current")

h3cDot3OamErrFrameEventGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 3, 2, 1, 7)
)
h3cDot3OamErrFrameEventGroup.setObjects(
      *(("A3COM-HUAWEI-EFM-COMMON-MIB", "h3cDot3OamErrFrameWindow"),
        ("A3COM-HUAWEI-EFM-COMMON-MIB", "h3cDot3OamErrFrameThreshold"),
        ("A3COM-HUAWEI-EFM-COMMON-MIB", "h3cDot3OamErrFrameEvNotifEnable"))
)
if mibBuilder.loadTexts:
    h3cDot3OamErrFrameEventGroup.setStatus("current")

h3cDot3OamErrFrameSecsSummaryEventGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 3, 2, 1, 8)
)
h3cDot3OamErrFrameSecsSummaryEventGroup.setObjects(
      *(("A3COM-HUAWEI-EFM-COMMON-MIB", "h3cDot3OamErrFrameSecsSummaryWindow"),
        ("A3COM-HUAWEI-EFM-COMMON-MIB", "h3cDot3OamErrFrameSecsSummaryThreshold"),
        ("A3COM-HUAWEI-EFM-COMMON-MIB", "h3cDot3OamErrFrameSecsEvNotifEnable"))
)
if mibBuilder.loadTexts:
    h3cDot3OamErrFrameSecsSummaryEventGroup.setStatus("current")

h3cDot3OamEventLogGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 3, 2, 1, 9)
)
h3cDot3OamEventLogGroup.setObjects(
      *(("A3COM-HUAWEI-EFM-COMMON-MIB", "h3cDot3OamEventLogTimestamp"),
        ("A3COM-HUAWEI-EFM-COMMON-MIB", "h3cDot3OamEventLogOui"),
        ("A3COM-HUAWEI-EFM-COMMON-MIB", "h3cDot3OamEventLogType"),
        ("A3COM-HUAWEI-EFM-COMMON-MIB", "h3cDot3OamEventLogLocation"),
        ("A3COM-HUAWEI-EFM-COMMON-MIB", "h3cDot3OamEventLogWindowHi"),
        ("A3COM-HUAWEI-EFM-COMMON-MIB", "h3cDot3OamEventLogWindowLo"),
        ("A3COM-HUAWEI-EFM-COMMON-MIB", "h3cDot3OamEventLogThresholdHi"),
        ("A3COM-HUAWEI-EFM-COMMON-MIB", "h3cDot3OamEventLogThresholdLo"),
        ("A3COM-HUAWEI-EFM-COMMON-MIB", "h3cDot3OamEventLogValue"),
        ("A3COM-HUAWEI-EFM-COMMON-MIB", "h3cDot3OamEventLogRunningTotal"),
        ("A3COM-HUAWEI-EFM-COMMON-MIB", "h3cDot3OamEventLogEventTotal"))
)
if mibBuilder.loadTexts:
    h3cDot3OamEventLogGroup.setStatus("current")


# Notification objects

h3cDot3OamThresholdEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 3, 1, 7, 0, 1)
)
h3cDot3OamThresholdEvent.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("A3COM-HUAWEI-EFM-COMMON-MIB", "h3cDot3OamEventLogTimestamp"),
        ("A3COM-HUAWEI-EFM-COMMON-MIB", "h3cDot3OamEventLogOui"),
        ("A3COM-HUAWEI-EFM-COMMON-MIB", "h3cDot3OamEventLogType"),
        ("A3COM-HUAWEI-EFM-COMMON-MIB", "h3cDot3OamEventLogLocation"),
        ("A3COM-HUAWEI-EFM-COMMON-MIB", "h3cDot3OamEventLogWindowHi"),
        ("A3COM-HUAWEI-EFM-COMMON-MIB", "h3cDot3OamEventLogWindowLo"),
        ("A3COM-HUAWEI-EFM-COMMON-MIB", "h3cDot3OamEventLogThresholdHi"),
        ("A3COM-HUAWEI-EFM-COMMON-MIB", "h3cDot3OamEventLogThresholdLo"),
        ("A3COM-HUAWEI-EFM-COMMON-MIB", "h3cDot3OamEventLogValue"),
        ("A3COM-HUAWEI-EFM-COMMON-MIB", "h3cDot3OamEventLogRunningTotal"),
        ("A3COM-HUAWEI-EFM-COMMON-MIB", "h3cDot3OamEventLogEventTotal"))
)
if mibBuilder.loadTexts:
    h3cDot3OamThresholdEvent.setStatus(
        "current"
    )

h3cDot3OamNonThresholdEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 3, 1, 7, 0, 2)
)
h3cDot3OamNonThresholdEvent.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("A3COM-HUAWEI-EFM-COMMON-MIB", "h3cDot3OamEventLogTimestamp"),
        ("A3COM-HUAWEI-EFM-COMMON-MIB", "h3cDot3OamEventLogOui"),
        ("A3COM-HUAWEI-EFM-COMMON-MIB", "h3cDot3OamEventLogType"),
        ("A3COM-HUAWEI-EFM-COMMON-MIB", "h3cDot3OamEventLogLocation"),
        ("A3COM-HUAWEI-EFM-COMMON-MIB", "h3cDot3OamEventLogEventTotal"))
)
if mibBuilder.loadTexts:
    h3cDot3OamNonThresholdEvent.setStatus(
        "current"
    )


# Notifications groups

h3cDot3OamNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 3, 2, 1, 10)
)
h3cDot3OamNotificationGroup.setObjects(
      *(("A3COM-HUAWEI-EFM-COMMON-MIB", "h3cDot3OamThresholdEvent"),
        ("A3COM-HUAWEI-EFM-COMMON-MIB", "h3cDot3OamNonThresholdEvent"))
)
if mibBuilder.loadTexts:
    h3cDot3OamNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

h3cDot3OamCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 3, 2, 2, 1)
)
if mibBuilder.loadTexts:
    h3cDot3OamCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-EFM-COMMON-MIB",
    **{"Dot3Oui": Dot3Oui,
       "h3cEfmOamMIB": h3cEfmOamMIB,
       "h3cDot3OamMIB": h3cDot3OamMIB,
       "h3cDot3OamTable": h3cDot3OamTable,
       "h3cDot3OamEntry": h3cDot3OamEntry,
       "h3cDot3OamAdminState": h3cDot3OamAdminState,
       "h3cDot3OamOperStatus": h3cDot3OamOperStatus,
       "h3cDot3OamMode": h3cDot3OamMode,
       "h3cDot3OamMaxOamPduSize": h3cDot3OamMaxOamPduSize,
       "h3cDot3OamConfigRevision": h3cDot3OamConfigRevision,
       "h3cDot3OamFunctionsSupported": h3cDot3OamFunctionsSupported,
       "h3cDot3OamPeerTable": h3cDot3OamPeerTable,
       "h3cDot3OamPeerEntry": h3cDot3OamPeerEntry,
       "h3cDot3OamPeerStatus": h3cDot3OamPeerStatus,
       "h3cDot3OamPeerMacAddress": h3cDot3OamPeerMacAddress,
       "h3cDot3OamPeerVendorOui": h3cDot3OamPeerVendorOui,
       "h3cDot3OamPeerVendorInfo": h3cDot3OamPeerVendorInfo,
       "h3cDot3OamPeerMode": h3cDot3OamPeerMode,
       "h3cDot3OamPeerMaxOamPduSize": h3cDot3OamPeerMaxOamPduSize,
       "h3cDot3OamPeerConfigRevision": h3cDot3OamPeerConfigRevision,
       "h3cDot3OamPeerFunctionsSupported": h3cDot3OamPeerFunctionsSupported,
       "h3cDot3OamLoopbackTable": h3cDot3OamLoopbackTable,
       "h3cDot3OamLoopbackEntry": h3cDot3OamLoopbackEntry,
       "h3cDot3OamLoopbackCommand": h3cDot3OamLoopbackCommand,
       "h3cDot3OamLoopbackStatus": h3cDot3OamLoopbackStatus,
       "h3cDot3OamLoopbackIgnoreRx": h3cDot3OamLoopbackIgnoreRx,
       "h3cDot3OamStatsTable": h3cDot3OamStatsTable,
       "h3cDot3OamStatsEntry": h3cDot3OamStatsEntry,
       "h3cDot3OamInformationTx": h3cDot3OamInformationTx,
       "h3cDot3OamInformationRx": h3cDot3OamInformationRx,
       "h3cDot3OamUniqueEventNotificationTx": h3cDot3OamUniqueEventNotificationTx,
       "h3cDot3OamUniqueEventNotificationRx": h3cDot3OamUniqueEventNotificationRx,
       "h3cDot3OamDuplicateEventNotificationTx": h3cDot3OamDuplicateEventNotificationTx,
       "h3cDot3OamDuplicateEventNotificationRx": h3cDot3OamDuplicateEventNotificationRx,
       "h3cDot3OamLoopbackControlTx": h3cDot3OamLoopbackControlTx,
       "h3cDot3OamLoopbackControlRx": h3cDot3OamLoopbackControlRx,
       "h3cDot3OamVariableRequestTx": h3cDot3OamVariableRequestTx,
       "h3cDot3OamVariableRequestRx": h3cDot3OamVariableRequestRx,
       "h3cDot3OamVariableResponseTx": h3cDot3OamVariableResponseTx,
       "h3cDot3OamVariableResponseRx": h3cDot3OamVariableResponseRx,
       "h3cDot3OamOrgSpecificTx": h3cDot3OamOrgSpecificTx,
       "h3cDot3OamOrgSpecificRx": h3cDot3OamOrgSpecificRx,
       "h3cDot3OamUnsupportedCodesTx": h3cDot3OamUnsupportedCodesTx,
       "h3cDot3OamUnsupportedCodesRx": h3cDot3OamUnsupportedCodesRx,
       "h3cDot3OamFramesLostDueToOam": h3cDot3OamFramesLostDueToOam,
       "h3cDot3OamEventConfigTable": h3cDot3OamEventConfigTable,
       "h3cDot3OamEventConfigEntry": h3cDot3OamEventConfigEntry,
       "h3cDot3OamErrSymPeriodWindowHi": h3cDot3OamErrSymPeriodWindowHi,
       "h3cDot3OamErrSymPeriodWindowLo": h3cDot3OamErrSymPeriodWindowLo,
       "h3cDot3OamErrSymPeriodThresholdHi": h3cDot3OamErrSymPeriodThresholdHi,
       "h3cDot3OamErrSymPeriodThresholdLo": h3cDot3OamErrSymPeriodThresholdLo,
       "h3cDot3OamErrSymPeriodEvNotifEnable": h3cDot3OamErrSymPeriodEvNotifEnable,
       "h3cDot3OamErrFramePeriodWindow": h3cDot3OamErrFramePeriodWindow,
       "h3cDot3OamErrFramePeriodThreshold": h3cDot3OamErrFramePeriodThreshold,
       "h3cDot3OamErrFramePeriodEvNotifEnable": h3cDot3OamErrFramePeriodEvNotifEnable,
       "h3cDot3OamErrFrameWindow": h3cDot3OamErrFrameWindow,
       "h3cDot3OamErrFrameThreshold": h3cDot3OamErrFrameThreshold,
       "h3cDot3OamErrFrameEvNotifEnable": h3cDot3OamErrFrameEvNotifEnable,
       "h3cDot3OamErrFrameSecsSummaryWindow": h3cDot3OamErrFrameSecsSummaryWindow,
       "h3cDot3OamErrFrameSecsSummaryThreshold": h3cDot3OamErrFrameSecsSummaryThreshold,
       "h3cDot3OamErrFrameSecsEvNotifEnable": h3cDot3OamErrFrameSecsEvNotifEnable,
       "h3cDot3OamEventLogTable": h3cDot3OamEventLogTable,
       "h3cDot3OamEventLogEntry": h3cDot3OamEventLogEntry,
       "h3cDot3OamEventLogIndex": h3cDot3OamEventLogIndex,
       "h3cDot3OamEventLogTimestamp": h3cDot3OamEventLogTimestamp,
       "h3cDot3OamEventLogOui": h3cDot3OamEventLogOui,
       "h3cDot3OamEventLogType": h3cDot3OamEventLogType,
       "h3cDot3OamEventLogLocation": h3cDot3OamEventLogLocation,
       "h3cDot3OamEventLogWindowHi": h3cDot3OamEventLogWindowHi,
       "h3cDot3OamEventLogWindowLo": h3cDot3OamEventLogWindowLo,
       "h3cDot3OamEventLogThresholdHi": h3cDot3OamEventLogThresholdHi,
       "h3cDot3OamEventLogThresholdLo": h3cDot3OamEventLogThresholdLo,
       "h3cDot3OamEventLogValue": h3cDot3OamEventLogValue,
       "h3cDot3OamEventLogRunningTotal": h3cDot3OamEventLogRunningTotal,
       "h3cDot3OamEventLogEventTotal": h3cDot3OamEventLogEventTotal,
       "h3cDot3OamTraps": h3cDot3OamTraps,
       "h3cDot3OamTrapsPrefix": h3cDot3OamTrapsPrefix,
       "h3cDot3OamThresholdEvent": h3cDot3OamThresholdEvent,
       "h3cDot3OamNonThresholdEvent": h3cDot3OamNonThresholdEvent,
       "h3cDot3OamConformance": h3cDot3OamConformance,
       "h3cDot3OamGroups": h3cDot3OamGroups,
       "h3cDot3OamControlGroup": h3cDot3OamControlGroup,
       "h3cDot3OamPeerGroup": h3cDot3OamPeerGroup,
       "h3cDot3OamStatsBaseGroup": h3cDot3OamStatsBaseGroup,
       "h3cDot3OamLoopbackGroup": h3cDot3OamLoopbackGroup,
       "h3cDot3OamErrSymbolPeriodEventGroup": h3cDot3OamErrSymbolPeriodEventGroup,
       "h3cDot3OamErrFramePeriodEventGroup": h3cDot3OamErrFramePeriodEventGroup,
       "h3cDot3OamErrFrameEventGroup": h3cDot3OamErrFrameEventGroup,
       "h3cDot3OamErrFrameSecsSummaryEventGroup": h3cDot3OamErrFrameSecsSummaryEventGroup,
       "h3cDot3OamEventLogGroup": h3cDot3OamEventLogGroup,
       "h3cDot3OamNotificationGroup": h3cDot3OamNotificationGroup,
       "h3cDot3OamCompliances": h3cDot3OamCompliances,
       "h3cDot3OamCompliance": h3cDot3OamCompliance}
)
