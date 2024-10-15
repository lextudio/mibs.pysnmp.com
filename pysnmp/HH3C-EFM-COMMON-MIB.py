# SNMP MIB module (HH3C-EFM-COMMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-EFM-COMMON-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:53:03 2024
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

(CounterBasedGauge64,) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "CounterBasedGauge64")

(hh3cEpon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cEpon")

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

hh3cEfmOamMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 3)
)
hh3cEfmOamMIB.setRevisions(
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

_Hh3cDot3OamMIB_ObjectIdentity = ObjectIdentity
hh3cDot3OamMIB = _Hh3cDot3OamMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 3, 1)
)
_Hh3cDot3OamTable_Object = MibTable
hh3cDot3OamTable = _Hh3cDot3OamTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cDot3OamTable.setStatus("current")
_Hh3cDot3OamEntry_Object = MibTableRow
hh3cDot3OamEntry = _Hh3cDot3OamEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 3, 1, 1, 1)
)
hh3cDot3OamEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cDot3OamEntry.setStatus("current")


class _Hh3cDot3OamAdminState_Type(Integer32):
    """Custom type hh3cDot3OamAdminState based on Integer32"""
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


_Hh3cDot3OamAdminState_Type.__name__ = "Integer32"
_Hh3cDot3OamAdminState_Object = MibTableColumn
hh3cDot3OamAdminState = _Hh3cDot3OamAdminState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 3, 1, 1, 1, 1),
    _Hh3cDot3OamAdminState_Type()
)
hh3cDot3OamAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot3OamAdminState.setStatus("current")


class _Hh3cDot3OamOperStatus_Type(Integer32):
    """Custom type hh3cDot3OamOperStatus based on Integer32"""
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


_Hh3cDot3OamOperStatus_Type.__name__ = "Integer32"
_Hh3cDot3OamOperStatus_Object = MibTableColumn
hh3cDot3OamOperStatus = _Hh3cDot3OamOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 3, 1, 1, 1, 2),
    _Hh3cDot3OamOperStatus_Type()
)
hh3cDot3OamOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot3OamOperStatus.setStatus("current")


class _Hh3cDot3OamMode_Type(Integer32):
    """Custom type hh3cDot3OamMode based on Integer32"""
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


_Hh3cDot3OamMode_Type.__name__ = "Integer32"
_Hh3cDot3OamMode_Object = MibTableColumn
hh3cDot3OamMode = _Hh3cDot3OamMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 3, 1, 1, 1, 3),
    _Hh3cDot3OamMode_Type()
)
hh3cDot3OamMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot3OamMode.setStatus("current")


class _Hh3cDot3OamMaxOamPduSize_Type(Integer32):
    """Custom type hh3cDot3OamMaxOamPduSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 1522),
    )


_Hh3cDot3OamMaxOamPduSize_Type.__name__ = "Integer32"
_Hh3cDot3OamMaxOamPduSize_Object = MibTableColumn
hh3cDot3OamMaxOamPduSize = _Hh3cDot3OamMaxOamPduSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 3, 1, 1, 1, 4),
    _Hh3cDot3OamMaxOamPduSize_Type()
)
hh3cDot3OamMaxOamPduSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot3OamMaxOamPduSize.setStatus("current")
_Hh3cDot3OamConfigRevision_Type = Unsigned32
_Hh3cDot3OamConfigRevision_Object = MibTableColumn
hh3cDot3OamConfigRevision = _Hh3cDot3OamConfigRevision_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 3, 1, 1, 1, 5),
    _Hh3cDot3OamConfigRevision_Type()
)
hh3cDot3OamConfigRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot3OamConfigRevision.setStatus("current")


class _Hh3cDot3OamFunctionsSupported_Type(Bits):
    """Custom type hh3cDot3OamFunctionsSupported based on Bits"""
    namedValues = NamedValues(
        *(("eventSupport", 2),
          ("loopbackSupport", 1),
          ("unidirectionalSupport", 0),
          ("variableSupport", 3))
    )

_Hh3cDot3OamFunctionsSupported_Type.__name__ = "Bits"
_Hh3cDot3OamFunctionsSupported_Object = MibTableColumn
hh3cDot3OamFunctionsSupported = _Hh3cDot3OamFunctionsSupported_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 3, 1, 1, 1, 6),
    _Hh3cDot3OamFunctionsSupported_Type()
)
hh3cDot3OamFunctionsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot3OamFunctionsSupported.setStatus("current")
_Hh3cDot3OamPeerTable_Object = MibTable
hh3cDot3OamPeerTable = _Hh3cDot3OamPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 3, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cDot3OamPeerTable.setStatus("current")
_Hh3cDot3OamPeerEntry_Object = MibTableRow
hh3cDot3OamPeerEntry = _Hh3cDot3OamPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 3, 1, 2, 1)
)
hh3cDot3OamPeerEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cDot3OamPeerEntry.setStatus("current")


class _Hh3cDot3OamPeerStatus_Type(Integer32):
    """Custom type hh3cDot3OamPeerStatus based on Integer32"""
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


_Hh3cDot3OamPeerStatus_Type.__name__ = "Integer32"
_Hh3cDot3OamPeerStatus_Object = MibTableColumn
hh3cDot3OamPeerStatus = _Hh3cDot3OamPeerStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 3, 1, 2, 1, 1),
    _Hh3cDot3OamPeerStatus_Type()
)
hh3cDot3OamPeerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot3OamPeerStatus.setStatus("current")
_Hh3cDot3OamPeerMacAddress_Type = MacAddress
_Hh3cDot3OamPeerMacAddress_Object = MibTableColumn
hh3cDot3OamPeerMacAddress = _Hh3cDot3OamPeerMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 3, 1, 2, 1, 2),
    _Hh3cDot3OamPeerMacAddress_Type()
)
hh3cDot3OamPeerMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot3OamPeerMacAddress.setStatus("current")
_Hh3cDot3OamPeerVendorOui_Type = Dot3Oui
_Hh3cDot3OamPeerVendorOui_Object = MibTableColumn
hh3cDot3OamPeerVendorOui = _Hh3cDot3OamPeerVendorOui_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 3, 1, 2, 1, 3),
    _Hh3cDot3OamPeerVendorOui_Type()
)
hh3cDot3OamPeerVendorOui.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot3OamPeerVendorOui.setStatus("current")
_Hh3cDot3OamPeerVendorInfo_Type = Unsigned32
_Hh3cDot3OamPeerVendorInfo_Object = MibTableColumn
hh3cDot3OamPeerVendorInfo = _Hh3cDot3OamPeerVendorInfo_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 3, 1, 2, 1, 4),
    _Hh3cDot3OamPeerVendorInfo_Type()
)
hh3cDot3OamPeerVendorInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot3OamPeerVendorInfo.setStatus("current")


class _Hh3cDot3OamPeerMode_Type(Integer32):
    """Custom type hh3cDot3OamPeerMode based on Integer32"""
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


_Hh3cDot3OamPeerMode_Type.__name__ = "Integer32"
_Hh3cDot3OamPeerMode_Object = MibTableColumn
hh3cDot3OamPeerMode = _Hh3cDot3OamPeerMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 3, 1, 2, 1, 5),
    _Hh3cDot3OamPeerMode_Type()
)
hh3cDot3OamPeerMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot3OamPeerMode.setStatus("current")


class _Hh3cDot3OamPeerMaxOamPduSize_Type(Integer32):
    """Custom type hh3cDot3OamPeerMaxOamPduSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 1522),
    )


_Hh3cDot3OamPeerMaxOamPduSize_Type.__name__ = "Integer32"
_Hh3cDot3OamPeerMaxOamPduSize_Object = MibTableColumn
hh3cDot3OamPeerMaxOamPduSize = _Hh3cDot3OamPeerMaxOamPduSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 3, 1, 2, 1, 6),
    _Hh3cDot3OamPeerMaxOamPduSize_Type()
)
hh3cDot3OamPeerMaxOamPduSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot3OamPeerMaxOamPduSize.setStatus("current")
_Hh3cDot3OamPeerConfigRevision_Type = Unsigned32
_Hh3cDot3OamPeerConfigRevision_Object = MibTableColumn
hh3cDot3OamPeerConfigRevision = _Hh3cDot3OamPeerConfigRevision_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 3, 1, 2, 1, 7),
    _Hh3cDot3OamPeerConfigRevision_Type()
)
hh3cDot3OamPeerConfigRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot3OamPeerConfigRevision.setStatus("current")


class _Hh3cDot3OamPeerFunctionsSupported_Type(Bits):
    """Custom type hh3cDot3OamPeerFunctionsSupported based on Bits"""
    namedValues = NamedValues(
        *(("eventSupport", 2),
          ("loopbackSupport", 1),
          ("unidirectionalSupport", 0),
          ("variableSupport", 3))
    )

_Hh3cDot3OamPeerFunctionsSupported_Type.__name__ = "Bits"
_Hh3cDot3OamPeerFunctionsSupported_Object = MibTableColumn
hh3cDot3OamPeerFunctionsSupported = _Hh3cDot3OamPeerFunctionsSupported_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 3, 1, 2, 1, 8),
    _Hh3cDot3OamPeerFunctionsSupported_Type()
)
hh3cDot3OamPeerFunctionsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot3OamPeerFunctionsSupported.setStatus("current")
_Hh3cDot3OamLoopbackTable_Object = MibTable
hh3cDot3OamLoopbackTable = _Hh3cDot3OamLoopbackTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 3, 1, 3)
)
if mibBuilder.loadTexts:
    hh3cDot3OamLoopbackTable.setStatus("current")
_Hh3cDot3OamLoopbackEntry_Object = MibTableRow
hh3cDot3OamLoopbackEntry = _Hh3cDot3OamLoopbackEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 3, 1, 3, 1)
)
hh3cDot3OamLoopbackEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cDot3OamLoopbackEntry.setStatus("current")


class _Hh3cDot3OamLoopbackCommand_Type(Integer32):
    """Custom type hh3cDot3OamLoopbackCommand based on Integer32"""
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


_Hh3cDot3OamLoopbackCommand_Type.__name__ = "Integer32"
_Hh3cDot3OamLoopbackCommand_Object = MibTableColumn
hh3cDot3OamLoopbackCommand = _Hh3cDot3OamLoopbackCommand_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 3, 1, 3, 1, 1),
    _Hh3cDot3OamLoopbackCommand_Type()
)
hh3cDot3OamLoopbackCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot3OamLoopbackCommand.setStatus("current")


class _Hh3cDot3OamLoopbackStatus_Type(Integer32):
    """Custom type hh3cDot3OamLoopbackStatus based on Integer32"""
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


_Hh3cDot3OamLoopbackStatus_Type.__name__ = "Integer32"
_Hh3cDot3OamLoopbackStatus_Object = MibTableColumn
hh3cDot3OamLoopbackStatus = _Hh3cDot3OamLoopbackStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 3, 1, 3, 1, 2),
    _Hh3cDot3OamLoopbackStatus_Type()
)
hh3cDot3OamLoopbackStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot3OamLoopbackStatus.setStatus("current")


class _Hh3cDot3OamLoopbackIgnoreRx_Type(Integer32):
    """Custom type hh3cDot3OamLoopbackIgnoreRx based on Integer32"""
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


_Hh3cDot3OamLoopbackIgnoreRx_Type.__name__ = "Integer32"
_Hh3cDot3OamLoopbackIgnoreRx_Object = MibTableColumn
hh3cDot3OamLoopbackIgnoreRx = _Hh3cDot3OamLoopbackIgnoreRx_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 3, 1, 3, 1, 3),
    _Hh3cDot3OamLoopbackIgnoreRx_Type()
)
hh3cDot3OamLoopbackIgnoreRx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot3OamLoopbackIgnoreRx.setStatus("current")
_Hh3cDot3OamStatsTable_Object = MibTable
hh3cDot3OamStatsTable = _Hh3cDot3OamStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 3, 1, 4)
)
if mibBuilder.loadTexts:
    hh3cDot3OamStatsTable.setStatus("current")
_Hh3cDot3OamStatsEntry_Object = MibTableRow
hh3cDot3OamStatsEntry = _Hh3cDot3OamStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 3, 1, 4, 1)
)
hh3cDot3OamStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cDot3OamStatsEntry.setStatus("current")
_Hh3cDot3OamInformationTx_Type = Counter32
_Hh3cDot3OamInformationTx_Object = MibTableColumn
hh3cDot3OamInformationTx = _Hh3cDot3OamInformationTx_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 3, 1, 4, 1, 1),
    _Hh3cDot3OamInformationTx_Type()
)
hh3cDot3OamInformationTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot3OamInformationTx.setStatus("current")
_Hh3cDot3OamInformationRx_Type = Counter32
_Hh3cDot3OamInformationRx_Object = MibTableColumn
hh3cDot3OamInformationRx = _Hh3cDot3OamInformationRx_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 3, 1, 4, 1, 2),
    _Hh3cDot3OamInformationRx_Type()
)
hh3cDot3OamInformationRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot3OamInformationRx.setStatus("current")
_Hh3cDot3OamUniqueEventNotificationTx_Type = Counter32
_Hh3cDot3OamUniqueEventNotificationTx_Object = MibTableColumn
hh3cDot3OamUniqueEventNotificationTx = _Hh3cDot3OamUniqueEventNotificationTx_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 3, 1, 4, 1, 3),
    _Hh3cDot3OamUniqueEventNotificationTx_Type()
)
hh3cDot3OamUniqueEventNotificationTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot3OamUniqueEventNotificationTx.setStatus("current")
_Hh3cDot3OamUniqueEventNotificationRx_Type = Counter32
_Hh3cDot3OamUniqueEventNotificationRx_Object = MibTableColumn
hh3cDot3OamUniqueEventNotificationRx = _Hh3cDot3OamUniqueEventNotificationRx_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 3, 1, 4, 1, 4),
    _Hh3cDot3OamUniqueEventNotificationRx_Type()
)
hh3cDot3OamUniqueEventNotificationRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot3OamUniqueEventNotificationRx.setStatus("current")
_Hh3cDot3OamDuplicateEventNotificationTx_Type = Counter32
_Hh3cDot3OamDuplicateEventNotificationTx_Object = MibTableColumn
hh3cDot3OamDuplicateEventNotificationTx = _Hh3cDot3OamDuplicateEventNotificationTx_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 3, 1, 4, 1, 5),
    _Hh3cDot3OamDuplicateEventNotificationTx_Type()
)
hh3cDot3OamDuplicateEventNotificationTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot3OamDuplicateEventNotificationTx.setStatus("current")
_Hh3cDot3OamDuplicateEventNotificationRx_Type = Counter32
_Hh3cDot3OamDuplicateEventNotificationRx_Object = MibTableColumn
hh3cDot3OamDuplicateEventNotificationRx = _Hh3cDot3OamDuplicateEventNotificationRx_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 3, 1, 4, 1, 6),
    _Hh3cDot3OamDuplicateEventNotificationRx_Type()
)
hh3cDot3OamDuplicateEventNotificationRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot3OamDuplicateEventNotificationRx.setStatus("current")
_Hh3cDot3OamLoopbackControlTx_Type = Counter32
_Hh3cDot3OamLoopbackControlTx_Object = MibTableColumn
hh3cDot3OamLoopbackControlTx = _Hh3cDot3OamLoopbackControlTx_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 3, 1, 4, 1, 7),
    _Hh3cDot3OamLoopbackControlTx_Type()
)
hh3cDot3OamLoopbackControlTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot3OamLoopbackControlTx.setStatus("current")
_Hh3cDot3OamLoopbackControlRx_Type = Counter32
_Hh3cDot3OamLoopbackControlRx_Object = MibTableColumn
hh3cDot3OamLoopbackControlRx = _Hh3cDot3OamLoopbackControlRx_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 3, 1, 4, 1, 8),
    _Hh3cDot3OamLoopbackControlRx_Type()
)
hh3cDot3OamLoopbackControlRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot3OamLoopbackControlRx.setStatus("current")
_Hh3cDot3OamVariableRequestTx_Type = Counter32
_Hh3cDot3OamVariableRequestTx_Object = MibTableColumn
hh3cDot3OamVariableRequestTx = _Hh3cDot3OamVariableRequestTx_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 3, 1, 4, 1, 9),
    _Hh3cDot3OamVariableRequestTx_Type()
)
hh3cDot3OamVariableRequestTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot3OamVariableRequestTx.setStatus("current")
_Hh3cDot3OamVariableRequestRx_Type = Counter32
_Hh3cDot3OamVariableRequestRx_Object = MibTableColumn
hh3cDot3OamVariableRequestRx = _Hh3cDot3OamVariableRequestRx_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 3, 1, 4, 1, 10),
    _Hh3cDot3OamVariableRequestRx_Type()
)
hh3cDot3OamVariableRequestRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot3OamVariableRequestRx.setStatus("current")
_Hh3cDot3OamVariableResponseTx_Type = Counter32
_Hh3cDot3OamVariableResponseTx_Object = MibTableColumn
hh3cDot3OamVariableResponseTx = _Hh3cDot3OamVariableResponseTx_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 3, 1, 4, 1, 11),
    _Hh3cDot3OamVariableResponseTx_Type()
)
hh3cDot3OamVariableResponseTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot3OamVariableResponseTx.setStatus("current")
_Hh3cDot3OamVariableResponseRx_Type = Counter32
_Hh3cDot3OamVariableResponseRx_Object = MibTableColumn
hh3cDot3OamVariableResponseRx = _Hh3cDot3OamVariableResponseRx_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 3, 1, 4, 1, 12),
    _Hh3cDot3OamVariableResponseRx_Type()
)
hh3cDot3OamVariableResponseRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot3OamVariableResponseRx.setStatus("current")
_Hh3cDot3OamOrgSpecificTx_Type = Counter32
_Hh3cDot3OamOrgSpecificTx_Object = MibTableColumn
hh3cDot3OamOrgSpecificTx = _Hh3cDot3OamOrgSpecificTx_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 3, 1, 4, 1, 13),
    _Hh3cDot3OamOrgSpecificTx_Type()
)
hh3cDot3OamOrgSpecificTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot3OamOrgSpecificTx.setStatus("current")
_Hh3cDot3OamOrgSpecificRx_Type = Counter32
_Hh3cDot3OamOrgSpecificRx_Object = MibTableColumn
hh3cDot3OamOrgSpecificRx = _Hh3cDot3OamOrgSpecificRx_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 3, 1, 4, 1, 14),
    _Hh3cDot3OamOrgSpecificRx_Type()
)
hh3cDot3OamOrgSpecificRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot3OamOrgSpecificRx.setStatus("current")
_Hh3cDot3OamUnsupportedCodesTx_Type = Counter32
_Hh3cDot3OamUnsupportedCodesTx_Object = MibTableColumn
hh3cDot3OamUnsupportedCodesTx = _Hh3cDot3OamUnsupportedCodesTx_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 3, 1, 4, 1, 15),
    _Hh3cDot3OamUnsupportedCodesTx_Type()
)
hh3cDot3OamUnsupportedCodesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot3OamUnsupportedCodesTx.setStatus("current")
_Hh3cDot3OamUnsupportedCodesRx_Type = Counter32
_Hh3cDot3OamUnsupportedCodesRx_Object = MibTableColumn
hh3cDot3OamUnsupportedCodesRx = _Hh3cDot3OamUnsupportedCodesRx_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 3, 1, 4, 1, 16),
    _Hh3cDot3OamUnsupportedCodesRx_Type()
)
hh3cDot3OamUnsupportedCodesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot3OamUnsupportedCodesRx.setStatus("current")
_Hh3cDot3OamFramesLostDueToOam_Type = Counter32
_Hh3cDot3OamFramesLostDueToOam_Object = MibTableColumn
hh3cDot3OamFramesLostDueToOam = _Hh3cDot3OamFramesLostDueToOam_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 3, 1, 4, 1, 17),
    _Hh3cDot3OamFramesLostDueToOam_Type()
)
hh3cDot3OamFramesLostDueToOam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot3OamFramesLostDueToOam.setStatus("current")
_Hh3cDot3OamEventConfigTable_Object = MibTable
hh3cDot3OamEventConfigTable = _Hh3cDot3OamEventConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 3, 1, 5)
)
if mibBuilder.loadTexts:
    hh3cDot3OamEventConfigTable.setStatus("current")
_Hh3cDot3OamEventConfigEntry_Object = MibTableRow
hh3cDot3OamEventConfigEntry = _Hh3cDot3OamEventConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 3, 1, 5, 1)
)
hh3cDot3OamEventConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cDot3OamEventConfigEntry.setStatus("current")
_Hh3cDot3OamErrSymPeriodWindowHi_Type = Unsigned32
_Hh3cDot3OamErrSymPeriodWindowHi_Object = MibTableColumn
hh3cDot3OamErrSymPeriodWindowHi = _Hh3cDot3OamErrSymPeriodWindowHi_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 3, 1, 5, 1, 1),
    _Hh3cDot3OamErrSymPeriodWindowHi_Type()
)
hh3cDot3OamErrSymPeriodWindowHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot3OamErrSymPeriodWindowHi.setStatus("current")
_Hh3cDot3OamErrSymPeriodWindowLo_Type = Unsigned32
_Hh3cDot3OamErrSymPeriodWindowLo_Object = MibTableColumn
hh3cDot3OamErrSymPeriodWindowLo = _Hh3cDot3OamErrSymPeriodWindowLo_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 3, 1, 5, 1, 2),
    _Hh3cDot3OamErrSymPeriodWindowLo_Type()
)
hh3cDot3OamErrSymPeriodWindowLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot3OamErrSymPeriodWindowLo.setStatus("current")
_Hh3cDot3OamErrSymPeriodThresholdHi_Type = Unsigned32
_Hh3cDot3OamErrSymPeriodThresholdHi_Object = MibTableColumn
hh3cDot3OamErrSymPeriodThresholdHi = _Hh3cDot3OamErrSymPeriodThresholdHi_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 3, 1, 5, 1, 3),
    _Hh3cDot3OamErrSymPeriodThresholdHi_Type()
)
hh3cDot3OamErrSymPeriodThresholdHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot3OamErrSymPeriodThresholdHi.setStatus("current")
_Hh3cDot3OamErrSymPeriodThresholdLo_Type = Unsigned32
_Hh3cDot3OamErrSymPeriodThresholdLo_Object = MibTableColumn
hh3cDot3OamErrSymPeriodThresholdLo = _Hh3cDot3OamErrSymPeriodThresholdLo_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 3, 1, 5, 1, 4),
    _Hh3cDot3OamErrSymPeriodThresholdLo_Type()
)
hh3cDot3OamErrSymPeriodThresholdLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot3OamErrSymPeriodThresholdLo.setStatus("current")


class _Hh3cDot3OamErrSymPeriodEvNotifEnable_Type(Integer32):
    """Custom type hh3cDot3OamErrSymPeriodEvNotifEnable based on Integer32"""
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


_Hh3cDot3OamErrSymPeriodEvNotifEnable_Type.__name__ = "Integer32"
_Hh3cDot3OamErrSymPeriodEvNotifEnable_Object = MibTableColumn
hh3cDot3OamErrSymPeriodEvNotifEnable = _Hh3cDot3OamErrSymPeriodEvNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 3, 1, 5, 1, 5),
    _Hh3cDot3OamErrSymPeriodEvNotifEnable_Type()
)
hh3cDot3OamErrSymPeriodEvNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot3OamErrSymPeriodEvNotifEnable.setStatus("current")
_Hh3cDot3OamErrFramePeriodWindow_Type = Unsigned32
_Hh3cDot3OamErrFramePeriodWindow_Object = MibTableColumn
hh3cDot3OamErrFramePeriodWindow = _Hh3cDot3OamErrFramePeriodWindow_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 3, 1, 5, 1, 6),
    _Hh3cDot3OamErrFramePeriodWindow_Type()
)
hh3cDot3OamErrFramePeriodWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot3OamErrFramePeriodWindow.setStatus("current")
_Hh3cDot3OamErrFramePeriodThreshold_Type = Unsigned32
_Hh3cDot3OamErrFramePeriodThreshold_Object = MibTableColumn
hh3cDot3OamErrFramePeriodThreshold = _Hh3cDot3OamErrFramePeriodThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 3, 1, 5, 1, 7),
    _Hh3cDot3OamErrFramePeriodThreshold_Type()
)
hh3cDot3OamErrFramePeriodThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot3OamErrFramePeriodThreshold.setStatus("current")


class _Hh3cDot3OamErrFramePeriodEvNotifEnable_Type(Integer32):
    """Custom type hh3cDot3OamErrFramePeriodEvNotifEnable based on Integer32"""
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


_Hh3cDot3OamErrFramePeriodEvNotifEnable_Type.__name__ = "Integer32"
_Hh3cDot3OamErrFramePeriodEvNotifEnable_Object = MibTableColumn
hh3cDot3OamErrFramePeriodEvNotifEnable = _Hh3cDot3OamErrFramePeriodEvNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 3, 1, 5, 1, 8),
    _Hh3cDot3OamErrFramePeriodEvNotifEnable_Type()
)
hh3cDot3OamErrFramePeriodEvNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot3OamErrFramePeriodEvNotifEnable.setStatus("current")
_Hh3cDot3OamErrFrameWindow_Type = Unsigned32
_Hh3cDot3OamErrFrameWindow_Object = MibTableColumn
hh3cDot3OamErrFrameWindow = _Hh3cDot3OamErrFrameWindow_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 3, 1, 5, 1, 9),
    _Hh3cDot3OamErrFrameWindow_Type()
)
hh3cDot3OamErrFrameWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot3OamErrFrameWindow.setStatus("current")
_Hh3cDot3OamErrFrameThreshold_Type = Unsigned32
_Hh3cDot3OamErrFrameThreshold_Object = MibTableColumn
hh3cDot3OamErrFrameThreshold = _Hh3cDot3OamErrFrameThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 3, 1, 5, 1, 10),
    _Hh3cDot3OamErrFrameThreshold_Type()
)
hh3cDot3OamErrFrameThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot3OamErrFrameThreshold.setStatus("current")


class _Hh3cDot3OamErrFrameEvNotifEnable_Type(Integer32):
    """Custom type hh3cDot3OamErrFrameEvNotifEnable based on Integer32"""
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


_Hh3cDot3OamErrFrameEvNotifEnable_Type.__name__ = "Integer32"
_Hh3cDot3OamErrFrameEvNotifEnable_Object = MibTableColumn
hh3cDot3OamErrFrameEvNotifEnable = _Hh3cDot3OamErrFrameEvNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 3, 1, 5, 1, 11),
    _Hh3cDot3OamErrFrameEvNotifEnable_Type()
)
hh3cDot3OamErrFrameEvNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot3OamErrFrameEvNotifEnable.setStatus("current")


class _Hh3cDot3OamErrFrameSecsSummaryWindow_Type(Integer32):
    """Custom type hh3cDot3OamErrFrameSecsSummaryWindow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 9000),
    )


_Hh3cDot3OamErrFrameSecsSummaryWindow_Type.__name__ = "Integer32"
_Hh3cDot3OamErrFrameSecsSummaryWindow_Object = MibTableColumn
hh3cDot3OamErrFrameSecsSummaryWindow = _Hh3cDot3OamErrFrameSecsSummaryWindow_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 3, 1, 5, 1, 12),
    _Hh3cDot3OamErrFrameSecsSummaryWindow_Type()
)
hh3cDot3OamErrFrameSecsSummaryWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot3OamErrFrameSecsSummaryWindow.setStatus("current")


class _Hh3cDot3OamErrFrameSecsSummaryThreshold_Type(Integer32):
    """Custom type hh3cDot3OamErrFrameSecsSummaryThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_Hh3cDot3OamErrFrameSecsSummaryThreshold_Type.__name__ = "Integer32"
_Hh3cDot3OamErrFrameSecsSummaryThreshold_Object = MibTableColumn
hh3cDot3OamErrFrameSecsSummaryThreshold = _Hh3cDot3OamErrFrameSecsSummaryThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 3, 1, 5, 1, 13),
    _Hh3cDot3OamErrFrameSecsSummaryThreshold_Type()
)
hh3cDot3OamErrFrameSecsSummaryThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot3OamErrFrameSecsSummaryThreshold.setStatus("current")


class _Hh3cDot3OamErrFrameSecsEvNotifEnable_Type(Integer32):
    """Custom type hh3cDot3OamErrFrameSecsEvNotifEnable based on Integer32"""
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


_Hh3cDot3OamErrFrameSecsEvNotifEnable_Type.__name__ = "Integer32"
_Hh3cDot3OamErrFrameSecsEvNotifEnable_Object = MibTableColumn
hh3cDot3OamErrFrameSecsEvNotifEnable = _Hh3cDot3OamErrFrameSecsEvNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 3, 1, 5, 1, 14),
    _Hh3cDot3OamErrFrameSecsEvNotifEnable_Type()
)
hh3cDot3OamErrFrameSecsEvNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot3OamErrFrameSecsEvNotifEnable.setStatus("current")
_Hh3cDot3OamEventLogTable_Object = MibTable
hh3cDot3OamEventLogTable = _Hh3cDot3OamEventLogTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 3, 1, 6)
)
if mibBuilder.loadTexts:
    hh3cDot3OamEventLogTable.setStatus("current")
_Hh3cDot3OamEventLogEntry_Object = MibTableRow
hh3cDot3OamEventLogEntry = _Hh3cDot3OamEventLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 3, 1, 6, 1)
)
hh3cDot3OamEventLogEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-EFM-COMMON-MIB", "hh3cDot3OamEventLogIndex"),
)
if mibBuilder.loadTexts:
    hh3cDot3OamEventLogEntry.setStatus("current")
_Hh3cDot3OamEventLogIndex_Type = Unsigned32
_Hh3cDot3OamEventLogIndex_Object = MibTableColumn
hh3cDot3OamEventLogIndex = _Hh3cDot3OamEventLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 3, 1, 6, 1, 1),
    _Hh3cDot3OamEventLogIndex_Type()
)
hh3cDot3OamEventLogIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot3OamEventLogIndex.setStatus("current")
_Hh3cDot3OamEventLogTimestamp_Type = DateAndTime
_Hh3cDot3OamEventLogTimestamp_Object = MibTableColumn
hh3cDot3OamEventLogTimestamp = _Hh3cDot3OamEventLogTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 3, 1, 6, 1, 2),
    _Hh3cDot3OamEventLogTimestamp_Type()
)
hh3cDot3OamEventLogTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot3OamEventLogTimestamp.setStatus("current")
_Hh3cDot3OamEventLogOui_Type = Dot3Oui
_Hh3cDot3OamEventLogOui_Object = MibTableColumn
hh3cDot3OamEventLogOui = _Hh3cDot3OamEventLogOui_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 3, 1, 6, 1, 3),
    _Hh3cDot3OamEventLogOui_Type()
)
hh3cDot3OamEventLogOui.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot3OamEventLogOui.setStatus("current")
_Hh3cDot3OamEventLogType_Type = Unsigned32
_Hh3cDot3OamEventLogType_Object = MibTableColumn
hh3cDot3OamEventLogType = _Hh3cDot3OamEventLogType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 3, 1, 6, 1, 4),
    _Hh3cDot3OamEventLogType_Type()
)
hh3cDot3OamEventLogType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot3OamEventLogType.setStatus("current")


class _Hh3cDot3OamEventLogLocation_Type(Integer32):
    """Custom type hh3cDot3OamEventLogLocation based on Integer32"""
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


_Hh3cDot3OamEventLogLocation_Type.__name__ = "Integer32"
_Hh3cDot3OamEventLogLocation_Object = MibTableColumn
hh3cDot3OamEventLogLocation = _Hh3cDot3OamEventLogLocation_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 3, 1, 6, 1, 5),
    _Hh3cDot3OamEventLogLocation_Type()
)
hh3cDot3OamEventLogLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot3OamEventLogLocation.setStatus("current")
_Hh3cDot3OamEventLogWindowHi_Type = Unsigned32
_Hh3cDot3OamEventLogWindowHi_Object = MibTableColumn
hh3cDot3OamEventLogWindowHi = _Hh3cDot3OamEventLogWindowHi_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 3, 1, 6, 1, 6),
    _Hh3cDot3OamEventLogWindowHi_Type()
)
hh3cDot3OamEventLogWindowHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot3OamEventLogWindowHi.setStatus("current")
_Hh3cDot3OamEventLogWindowLo_Type = Unsigned32
_Hh3cDot3OamEventLogWindowLo_Object = MibTableColumn
hh3cDot3OamEventLogWindowLo = _Hh3cDot3OamEventLogWindowLo_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 3, 1, 6, 1, 7),
    _Hh3cDot3OamEventLogWindowLo_Type()
)
hh3cDot3OamEventLogWindowLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot3OamEventLogWindowLo.setStatus("current")
_Hh3cDot3OamEventLogThresholdHi_Type = Unsigned32
_Hh3cDot3OamEventLogThresholdHi_Object = MibTableColumn
hh3cDot3OamEventLogThresholdHi = _Hh3cDot3OamEventLogThresholdHi_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 3, 1, 6, 1, 8),
    _Hh3cDot3OamEventLogThresholdHi_Type()
)
hh3cDot3OamEventLogThresholdHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot3OamEventLogThresholdHi.setStatus("current")
_Hh3cDot3OamEventLogThresholdLo_Type = Unsigned32
_Hh3cDot3OamEventLogThresholdLo_Object = MibTableColumn
hh3cDot3OamEventLogThresholdLo = _Hh3cDot3OamEventLogThresholdLo_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 3, 1, 6, 1, 9),
    _Hh3cDot3OamEventLogThresholdLo_Type()
)
hh3cDot3OamEventLogThresholdLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot3OamEventLogThresholdLo.setStatus("current")
_Hh3cDot3OamEventLogValue_Type = CounterBasedGauge64
_Hh3cDot3OamEventLogValue_Object = MibTableColumn
hh3cDot3OamEventLogValue = _Hh3cDot3OamEventLogValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 3, 1, 6, 1, 10),
    _Hh3cDot3OamEventLogValue_Type()
)
hh3cDot3OamEventLogValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot3OamEventLogValue.setStatus("current")
_Hh3cDot3OamEventLogRunningTotal_Type = CounterBasedGauge64
_Hh3cDot3OamEventLogRunningTotal_Object = MibTableColumn
hh3cDot3OamEventLogRunningTotal = _Hh3cDot3OamEventLogRunningTotal_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 3, 1, 6, 1, 11),
    _Hh3cDot3OamEventLogRunningTotal_Type()
)
hh3cDot3OamEventLogRunningTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot3OamEventLogRunningTotal.setStatus("current")
_Hh3cDot3OamEventLogEventTotal_Type = Unsigned32
_Hh3cDot3OamEventLogEventTotal_Object = MibTableColumn
hh3cDot3OamEventLogEventTotal = _Hh3cDot3OamEventLogEventTotal_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 3, 1, 6, 1, 12),
    _Hh3cDot3OamEventLogEventTotal_Type()
)
hh3cDot3OamEventLogEventTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot3OamEventLogEventTotal.setStatus("current")
_Hh3cDot3OamTraps_ObjectIdentity = ObjectIdentity
hh3cDot3OamTraps = _Hh3cDot3OamTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 3, 1, 7)
)
_Hh3cDot3OamTrapsPrefix_ObjectIdentity = ObjectIdentity
hh3cDot3OamTrapsPrefix = _Hh3cDot3OamTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 3, 1, 7, 0)
)
_Hh3cDot3OamConformance_ObjectIdentity = ObjectIdentity
hh3cDot3OamConformance = _Hh3cDot3OamConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 3, 2)
)
_Hh3cDot3OamGroups_ObjectIdentity = ObjectIdentity
hh3cDot3OamGroups = _Hh3cDot3OamGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 3, 2, 1)
)
_Hh3cDot3OamCompliances_ObjectIdentity = ObjectIdentity
hh3cDot3OamCompliances = _Hh3cDot3OamCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 3, 2, 2)
)

# Managed Objects groups

hh3cDot3OamControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 3, 2, 1, 1)
)
hh3cDot3OamControlGroup.setObjects(
      *(("HH3C-EFM-COMMON-MIB", "hh3cDot3OamAdminState"),
        ("HH3C-EFM-COMMON-MIB", "hh3cDot3OamOperStatus"),
        ("HH3C-EFM-COMMON-MIB", "hh3cDot3OamMode"),
        ("HH3C-EFM-COMMON-MIB", "hh3cDot3OamMaxOamPduSize"),
        ("HH3C-EFM-COMMON-MIB", "hh3cDot3OamConfigRevision"),
        ("HH3C-EFM-COMMON-MIB", "hh3cDot3OamFunctionsSupported"))
)
if mibBuilder.loadTexts:
    hh3cDot3OamControlGroup.setStatus("current")

hh3cDot3OamPeerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 3, 2, 1, 2)
)
hh3cDot3OamPeerGroup.setObjects(
      *(("HH3C-EFM-COMMON-MIB", "hh3cDot3OamPeerStatus"),
        ("HH3C-EFM-COMMON-MIB", "hh3cDot3OamPeerMacAddress"),
        ("HH3C-EFM-COMMON-MIB", "hh3cDot3OamPeerVendorOui"),
        ("HH3C-EFM-COMMON-MIB", "hh3cDot3OamPeerVendorInfo"),
        ("HH3C-EFM-COMMON-MIB", "hh3cDot3OamPeerMode"),
        ("HH3C-EFM-COMMON-MIB", "hh3cDot3OamPeerFunctionsSupported"),
        ("HH3C-EFM-COMMON-MIB", "hh3cDot3OamPeerMaxOamPduSize"),
        ("HH3C-EFM-COMMON-MIB", "hh3cDot3OamPeerConfigRevision"))
)
if mibBuilder.loadTexts:
    hh3cDot3OamPeerGroup.setStatus("current")

hh3cDot3OamStatsBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 3, 2, 1, 3)
)
hh3cDot3OamStatsBaseGroup.setObjects(
      *(("HH3C-EFM-COMMON-MIB", "hh3cDot3OamInformationTx"),
        ("HH3C-EFM-COMMON-MIB", "hh3cDot3OamInformationRx"),
        ("HH3C-EFM-COMMON-MIB", "hh3cDot3OamUniqueEventNotificationTx"),
        ("HH3C-EFM-COMMON-MIB", "hh3cDot3OamUniqueEventNotificationRx"),
        ("HH3C-EFM-COMMON-MIB", "hh3cDot3OamDuplicateEventNotificationTx"),
        ("HH3C-EFM-COMMON-MIB", "hh3cDot3OamDuplicateEventNotificationRx"),
        ("HH3C-EFM-COMMON-MIB", "hh3cDot3OamLoopbackControlTx"),
        ("HH3C-EFM-COMMON-MIB", "hh3cDot3OamLoopbackControlRx"),
        ("HH3C-EFM-COMMON-MIB", "hh3cDot3OamVariableRequestTx"),
        ("HH3C-EFM-COMMON-MIB", "hh3cDot3OamVariableRequestRx"),
        ("HH3C-EFM-COMMON-MIB", "hh3cDot3OamVariableResponseTx"),
        ("HH3C-EFM-COMMON-MIB", "hh3cDot3OamVariableResponseRx"),
        ("HH3C-EFM-COMMON-MIB", "hh3cDot3OamOrgSpecificTx"),
        ("HH3C-EFM-COMMON-MIB", "hh3cDot3OamOrgSpecificRx"),
        ("HH3C-EFM-COMMON-MIB", "hh3cDot3OamUnsupportedCodesTx"),
        ("HH3C-EFM-COMMON-MIB", "hh3cDot3OamUnsupportedCodesRx"),
        ("HH3C-EFM-COMMON-MIB", "hh3cDot3OamFramesLostDueToOam"))
)
if mibBuilder.loadTexts:
    hh3cDot3OamStatsBaseGroup.setStatus("current")

hh3cDot3OamLoopbackGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 3, 2, 1, 4)
)
hh3cDot3OamLoopbackGroup.setObjects(
      *(("HH3C-EFM-COMMON-MIB", "hh3cDot3OamLoopbackCommand"),
        ("HH3C-EFM-COMMON-MIB", "hh3cDot3OamLoopbackStatus"),
        ("HH3C-EFM-COMMON-MIB", "hh3cDot3OamLoopbackIgnoreRx"))
)
if mibBuilder.loadTexts:
    hh3cDot3OamLoopbackGroup.setStatus("current")

hh3cDot3OamErrSymbolPeriodEventGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 3, 2, 1, 5)
)
hh3cDot3OamErrSymbolPeriodEventGroup.setObjects(
      *(("HH3C-EFM-COMMON-MIB", "hh3cDot3OamErrSymPeriodWindowHi"),
        ("HH3C-EFM-COMMON-MIB", "hh3cDot3OamErrSymPeriodWindowLo"),
        ("HH3C-EFM-COMMON-MIB", "hh3cDot3OamErrSymPeriodThresholdHi"),
        ("HH3C-EFM-COMMON-MIB", "hh3cDot3OamErrSymPeriodThresholdLo"),
        ("HH3C-EFM-COMMON-MIB", "hh3cDot3OamErrSymPeriodEvNotifEnable"))
)
if mibBuilder.loadTexts:
    hh3cDot3OamErrSymbolPeriodEventGroup.setStatus("current")

hh3cDot3OamErrFramePeriodEventGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 3, 2, 1, 6)
)
hh3cDot3OamErrFramePeriodEventGroup.setObjects(
      *(("HH3C-EFM-COMMON-MIB", "hh3cDot3OamErrFramePeriodWindow"),
        ("HH3C-EFM-COMMON-MIB", "hh3cDot3OamErrFramePeriodThreshold"),
        ("HH3C-EFM-COMMON-MIB", "hh3cDot3OamErrFramePeriodEvNotifEnable"))
)
if mibBuilder.loadTexts:
    hh3cDot3OamErrFramePeriodEventGroup.setStatus("current")

hh3cDot3OamErrFrameEventGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 3, 2, 1, 7)
)
hh3cDot3OamErrFrameEventGroup.setObjects(
      *(("HH3C-EFM-COMMON-MIB", "hh3cDot3OamErrFrameWindow"),
        ("HH3C-EFM-COMMON-MIB", "hh3cDot3OamErrFrameThreshold"),
        ("HH3C-EFM-COMMON-MIB", "hh3cDot3OamErrFrameEvNotifEnable"))
)
if mibBuilder.loadTexts:
    hh3cDot3OamErrFrameEventGroup.setStatus("current")

hh3cDot3OamErrFrameSecsSummaryEventGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 3, 2, 1, 8)
)
hh3cDot3OamErrFrameSecsSummaryEventGroup.setObjects(
      *(("HH3C-EFM-COMMON-MIB", "hh3cDot3OamErrFrameSecsSummaryWindow"),
        ("HH3C-EFM-COMMON-MIB", "hh3cDot3OamErrFrameSecsSummaryThreshold"),
        ("HH3C-EFM-COMMON-MIB", "hh3cDot3OamErrFrameSecsEvNotifEnable"))
)
if mibBuilder.loadTexts:
    hh3cDot3OamErrFrameSecsSummaryEventGroup.setStatus("current")

hh3cDot3OamEventLogGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 3, 2, 1, 9)
)
hh3cDot3OamEventLogGroup.setObjects(
      *(("HH3C-EFM-COMMON-MIB", "hh3cDot3OamEventLogTimestamp"),
        ("HH3C-EFM-COMMON-MIB", "hh3cDot3OamEventLogOui"),
        ("HH3C-EFM-COMMON-MIB", "hh3cDot3OamEventLogType"),
        ("HH3C-EFM-COMMON-MIB", "hh3cDot3OamEventLogLocation"),
        ("HH3C-EFM-COMMON-MIB", "hh3cDot3OamEventLogWindowHi"),
        ("HH3C-EFM-COMMON-MIB", "hh3cDot3OamEventLogWindowLo"),
        ("HH3C-EFM-COMMON-MIB", "hh3cDot3OamEventLogThresholdHi"),
        ("HH3C-EFM-COMMON-MIB", "hh3cDot3OamEventLogThresholdLo"),
        ("HH3C-EFM-COMMON-MIB", "hh3cDot3OamEventLogValue"),
        ("HH3C-EFM-COMMON-MIB", "hh3cDot3OamEventLogRunningTotal"),
        ("HH3C-EFM-COMMON-MIB", "hh3cDot3OamEventLogEventTotal"))
)
if mibBuilder.loadTexts:
    hh3cDot3OamEventLogGroup.setStatus("current")


# Notification objects

hh3cDot3OamThresholdEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 3, 1, 7, 0, 1)
)
hh3cDot3OamThresholdEvent.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("HH3C-EFM-COMMON-MIB", "hh3cDot3OamEventLogTimestamp"),
        ("HH3C-EFM-COMMON-MIB", "hh3cDot3OamEventLogOui"),
        ("HH3C-EFM-COMMON-MIB", "hh3cDot3OamEventLogType"),
        ("HH3C-EFM-COMMON-MIB", "hh3cDot3OamEventLogLocation"),
        ("HH3C-EFM-COMMON-MIB", "hh3cDot3OamEventLogWindowHi"),
        ("HH3C-EFM-COMMON-MIB", "hh3cDot3OamEventLogWindowLo"),
        ("HH3C-EFM-COMMON-MIB", "hh3cDot3OamEventLogThresholdHi"),
        ("HH3C-EFM-COMMON-MIB", "hh3cDot3OamEventLogThresholdLo"),
        ("HH3C-EFM-COMMON-MIB", "hh3cDot3OamEventLogValue"),
        ("HH3C-EFM-COMMON-MIB", "hh3cDot3OamEventLogRunningTotal"),
        ("HH3C-EFM-COMMON-MIB", "hh3cDot3OamEventLogEventTotal"))
)
if mibBuilder.loadTexts:
    hh3cDot3OamThresholdEvent.setStatus(
        "current"
    )

hh3cDot3OamNonThresholdEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 3, 1, 7, 0, 2)
)
hh3cDot3OamNonThresholdEvent.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("HH3C-EFM-COMMON-MIB", "hh3cDot3OamEventLogTimestamp"),
        ("HH3C-EFM-COMMON-MIB", "hh3cDot3OamEventLogOui"),
        ("HH3C-EFM-COMMON-MIB", "hh3cDot3OamEventLogType"),
        ("HH3C-EFM-COMMON-MIB", "hh3cDot3OamEventLogLocation"),
        ("HH3C-EFM-COMMON-MIB", "hh3cDot3OamEventLogEventTotal"))
)
if mibBuilder.loadTexts:
    hh3cDot3OamNonThresholdEvent.setStatus(
        "current"
    )


# Notifications groups

hh3cDot3OamNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 3, 2, 1, 10)
)
hh3cDot3OamNotificationGroup.setObjects(
      *(("HH3C-EFM-COMMON-MIB", "hh3cDot3OamThresholdEvent"),
        ("HH3C-EFM-COMMON-MIB", "hh3cDot3OamNonThresholdEvent"))
)
if mibBuilder.loadTexts:
    hh3cDot3OamNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hh3cDot3OamCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 3, 2, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cDot3OamCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-EFM-COMMON-MIB",
    **{"Dot3Oui": Dot3Oui,
       "hh3cEfmOamMIB": hh3cEfmOamMIB,
       "hh3cDot3OamMIB": hh3cDot3OamMIB,
       "hh3cDot3OamTable": hh3cDot3OamTable,
       "hh3cDot3OamEntry": hh3cDot3OamEntry,
       "hh3cDot3OamAdminState": hh3cDot3OamAdminState,
       "hh3cDot3OamOperStatus": hh3cDot3OamOperStatus,
       "hh3cDot3OamMode": hh3cDot3OamMode,
       "hh3cDot3OamMaxOamPduSize": hh3cDot3OamMaxOamPduSize,
       "hh3cDot3OamConfigRevision": hh3cDot3OamConfigRevision,
       "hh3cDot3OamFunctionsSupported": hh3cDot3OamFunctionsSupported,
       "hh3cDot3OamPeerTable": hh3cDot3OamPeerTable,
       "hh3cDot3OamPeerEntry": hh3cDot3OamPeerEntry,
       "hh3cDot3OamPeerStatus": hh3cDot3OamPeerStatus,
       "hh3cDot3OamPeerMacAddress": hh3cDot3OamPeerMacAddress,
       "hh3cDot3OamPeerVendorOui": hh3cDot3OamPeerVendorOui,
       "hh3cDot3OamPeerVendorInfo": hh3cDot3OamPeerVendorInfo,
       "hh3cDot3OamPeerMode": hh3cDot3OamPeerMode,
       "hh3cDot3OamPeerMaxOamPduSize": hh3cDot3OamPeerMaxOamPduSize,
       "hh3cDot3OamPeerConfigRevision": hh3cDot3OamPeerConfigRevision,
       "hh3cDot3OamPeerFunctionsSupported": hh3cDot3OamPeerFunctionsSupported,
       "hh3cDot3OamLoopbackTable": hh3cDot3OamLoopbackTable,
       "hh3cDot3OamLoopbackEntry": hh3cDot3OamLoopbackEntry,
       "hh3cDot3OamLoopbackCommand": hh3cDot3OamLoopbackCommand,
       "hh3cDot3OamLoopbackStatus": hh3cDot3OamLoopbackStatus,
       "hh3cDot3OamLoopbackIgnoreRx": hh3cDot3OamLoopbackIgnoreRx,
       "hh3cDot3OamStatsTable": hh3cDot3OamStatsTable,
       "hh3cDot3OamStatsEntry": hh3cDot3OamStatsEntry,
       "hh3cDot3OamInformationTx": hh3cDot3OamInformationTx,
       "hh3cDot3OamInformationRx": hh3cDot3OamInformationRx,
       "hh3cDot3OamUniqueEventNotificationTx": hh3cDot3OamUniqueEventNotificationTx,
       "hh3cDot3OamUniqueEventNotificationRx": hh3cDot3OamUniqueEventNotificationRx,
       "hh3cDot3OamDuplicateEventNotificationTx": hh3cDot3OamDuplicateEventNotificationTx,
       "hh3cDot3OamDuplicateEventNotificationRx": hh3cDot3OamDuplicateEventNotificationRx,
       "hh3cDot3OamLoopbackControlTx": hh3cDot3OamLoopbackControlTx,
       "hh3cDot3OamLoopbackControlRx": hh3cDot3OamLoopbackControlRx,
       "hh3cDot3OamVariableRequestTx": hh3cDot3OamVariableRequestTx,
       "hh3cDot3OamVariableRequestRx": hh3cDot3OamVariableRequestRx,
       "hh3cDot3OamVariableResponseTx": hh3cDot3OamVariableResponseTx,
       "hh3cDot3OamVariableResponseRx": hh3cDot3OamVariableResponseRx,
       "hh3cDot3OamOrgSpecificTx": hh3cDot3OamOrgSpecificTx,
       "hh3cDot3OamOrgSpecificRx": hh3cDot3OamOrgSpecificRx,
       "hh3cDot3OamUnsupportedCodesTx": hh3cDot3OamUnsupportedCodesTx,
       "hh3cDot3OamUnsupportedCodesRx": hh3cDot3OamUnsupportedCodesRx,
       "hh3cDot3OamFramesLostDueToOam": hh3cDot3OamFramesLostDueToOam,
       "hh3cDot3OamEventConfigTable": hh3cDot3OamEventConfigTable,
       "hh3cDot3OamEventConfigEntry": hh3cDot3OamEventConfigEntry,
       "hh3cDot3OamErrSymPeriodWindowHi": hh3cDot3OamErrSymPeriodWindowHi,
       "hh3cDot3OamErrSymPeriodWindowLo": hh3cDot3OamErrSymPeriodWindowLo,
       "hh3cDot3OamErrSymPeriodThresholdHi": hh3cDot3OamErrSymPeriodThresholdHi,
       "hh3cDot3OamErrSymPeriodThresholdLo": hh3cDot3OamErrSymPeriodThresholdLo,
       "hh3cDot3OamErrSymPeriodEvNotifEnable": hh3cDot3OamErrSymPeriodEvNotifEnable,
       "hh3cDot3OamErrFramePeriodWindow": hh3cDot3OamErrFramePeriodWindow,
       "hh3cDot3OamErrFramePeriodThreshold": hh3cDot3OamErrFramePeriodThreshold,
       "hh3cDot3OamErrFramePeriodEvNotifEnable": hh3cDot3OamErrFramePeriodEvNotifEnable,
       "hh3cDot3OamErrFrameWindow": hh3cDot3OamErrFrameWindow,
       "hh3cDot3OamErrFrameThreshold": hh3cDot3OamErrFrameThreshold,
       "hh3cDot3OamErrFrameEvNotifEnable": hh3cDot3OamErrFrameEvNotifEnable,
       "hh3cDot3OamErrFrameSecsSummaryWindow": hh3cDot3OamErrFrameSecsSummaryWindow,
       "hh3cDot3OamErrFrameSecsSummaryThreshold": hh3cDot3OamErrFrameSecsSummaryThreshold,
       "hh3cDot3OamErrFrameSecsEvNotifEnable": hh3cDot3OamErrFrameSecsEvNotifEnable,
       "hh3cDot3OamEventLogTable": hh3cDot3OamEventLogTable,
       "hh3cDot3OamEventLogEntry": hh3cDot3OamEventLogEntry,
       "hh3cDot3OamEventLogIndex": hh3cDot3OamEventLogIndex,
       "hh3cDot3OamEventLogTimestamp": hh3cDot3OamEventLogTimestamp,
       "hh3cDot3OamEventLogOui": hh3cDot3OamEventLogOui,
       "hh3cDot3OamEventLogType": hh3cDot3OamEventLogType,
       "hh3cDot3OamEventLogLocation": hh3cDot3OamEventLogLocation,
       "hh3cDot3OamEventLogWindowHi": hh3cDot3OamEventLogWindowHi,
       "hh3cDot3OamEventLogWindowLo": hh3cDot3OamEventLogWindowLo,
       "hh3cDot3OamEventLogThresholdHi": hh3cDot3OamEventLogThresholdHi,
       "hh3cDot3OamEventLogThresholdLo": hh3cDot3OamEventLogThresholdLo,
       "hh3cDot3OamEventLogValue": hh3cDot3OamEventLogValue,
       "hh3cDot3OamEventLogRunningTotal": hh3cDot3OamEventLogRunningTotal,
       "hh3cDot3OamEventLogEventTotal": hh3cDot3OamEventLogEventTotal,
       "hh3cDot3OamTraps": hh3cDot3OamTraps,
       "hh3cDot3OamTrapsPrefix": hh3cDot3OamTrapsPrefix,
       "hh3cDot3OamThresholdEvent": hh3cDot3OamThresholdEvent,
       "hh3cDot3OamNonThresholdEvent": hh3cDot3OamNonThresholdEvent,
       "hh3cDot3OamConformance": hh3cDot3OamConformance,
       "hh3cDot3OamGroups": hh3cDot3OamGroups,
       "hh3cDot3OamControlGroup": hh3cDot3OamControlGroup,
       "hh3cDot3OamPeerGroup": hh3cDot3OamPeerGroup,
       "hh3cDot3OamStatsBaseGroup": hh3cDot3OamStatsBaseGroup,
       "hh3cDot3OamLoopbackGroup": hh3cDot3OamLoopbackGroup,
       "hh3cDot3OamErrSymbolPeriodEventGroup": hh3cDot3OamErrSymbolPeriodEventGroup,
       "hh3cDot3OamErrFramePeriodEventGroup": hh3cDot3OamErrFramePeriodEventGroup,
       "hh3cDot3OamErrFrameEventGroup": hh3cDot3OamErrFrameEventGroup,
       "hh3cDot3OamErrFrameSecsSummaryEventGroup": hh3cDot3OamErrFrameSecsSummaryEventGroup,
       "hh3cDot3OamEventLogGroup": hh3cDot3OamEventLogGroup,
       "hh3cDot3OamNotificationGroup": hh3cDot3OamNotificationGroup,
       "hh3cDot3OamCompliances": hh3cDot3OamCompliances,
       "hh3cDot3OamCompliance": hh3cDot3OamCompliance}
)
