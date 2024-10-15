# SNMP MIB module (HPN-ICF-EFM-COMMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-EFM-COMMON-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:00:03 2024
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

(hpnicfEpon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfEpon")

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

hpnicfEfmOamMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3)
)
hpnicfEfmOamMIB.setRevisions(
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

_HpnicfDot3OamMIB_ObjectIdentity = ObjectIdentity
hpnicfDot3OamMIB = _HpnicfDot3OamMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1)
)
_HpnicfDot3OamTable_Object = MibTable
hpnicfDot3OamTable = _HpnicfDot3OamTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfDot3OamTable.setStatus("current")
_HpnicfDot3OamEntry_Object = MibTableRow
hpnicfDot3OamEntry = _HpnicfDot3OamEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 1, 1)
)
hpnicfDot3OamEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfDot3OamEntry.setStatus("current")


class _HpnicfDot3OamAdminState_Type(Integer32):
    """Custom type hpnicfDot3OamAdminState based on Integer32"""
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


_HpnicfDot3OamAdminState_Type.__name__ = "Integer32"
_HpnicfDot3OamAdminState_Object = MibTableColumn
hpnicfDot3OamAdminState = _HpnicfDot3OamAdminState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 1, 1, 1),
    _HpnicfDot3OamAdminState_Type()
)
hpnicfDot3OamAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot3OamAdminState.setStatus("current")


class _HpnicfDot3OamOperStatus_Type(Integer32):
    """Custom type hpnicfDot3OamOperStatus based on Integer32"""
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


_HpnicfDot3OamOperStatus_Type.__name__ = "Integer32"
_HpnicfDot3OamOperStatus_Object = MibTableColumn
hpnicfDot3OamOperStatus = _HpnicfDot3OamOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 1, 1, 2),
    _HpnicfDot3OamOperStatus_Type()
)
hpnicfDot3OamOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot3OamOperStatus.setStatus("current")


class _HpnicfDot3OamMode_Type(Integer32):
    """Custom type hpnicfDot3OamMode based on Integer32"""
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


_HpnicfDot3OamMode_Type.__name__ = "Integer32"
_HpnicfDot3OamMode_Object = MibTableColumn
hpnicfDot3OamMode = _HpnicfDot3OamMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 1, 1, 3),
    _HpnicfDot3OamMode_Type()
)
hpnicfDot3OamMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot3OamMode.setStatus("current")


class _HpnicfDot3OamMaxOamPduSize_Type(Integer32):
    """Custom type hpnicfDot3OamMaxOamPduSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 1522),
    )


_HpnicfDot3OamMaxOamPduSize_Type.__name__ = "Integer32"
_HpnicfDot3OamMaxOamPduSize_Object = MibTableColumn
hpnicfDot3OamMaxOamPduSize = _HpnicfDot3OamMaxOamPduSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 1, 1, 4),
    _HpnicfDot3OamMaxOamPduSize_Type()
)
hpnicfDot3OamMaxOamPduSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot3OamMaxOamPduSize.setStatus("current")
_HpnicfDot3OamConfigRevision_Type = Unsigned32
_HpnicfDot3OamConfigRevision_Object = MibTableColumn
hpnicfDot3OamConfigRevision = _HpnicfDot3OamConfigRevision_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 1, 1, 5),
    _HpnicfDot3OamConfigRevision_Type()
)
hpnicfDot3OamConfigRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot3OamConfigRevision.setStatus("current")


class _HpnicfDot3OamFunctionsSupported_Type(Bits):
    """Custom type hpnicfDot3OamFunctionsSupported based on Bits"""
    namedValues = NamedValues(
        *(("eventSupport", 2),
          ("loopbackSupport", 1),
          ("unidirectionalSupport", 0),
          ("variableSupport", 3))
    )

_HpnicfDot3OamFunctionsSupported_Type.__name__ = "Bits"
_HpnicfDot3OamFunctionsSupported_Object = MibTableColumn
hpnicfDot3OamFunctionsSupported = _HpnicfDot3OamFunctionsSupported_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 1, 1, 6),
    _HpnicfDot3OamFunctionsSupported_Type()
)
hpnicfDot3OamFunctionsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot3OamFunctionsSupported.setStatus("current")
_HpnicfDot3OamPeerTable_Object = MibTable
hpnicfDot3OamPeerTable = _HpnicfDot3OamPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 2)
)
if mibBuilder.loadTexts:
    hpnicfDot3OamPeerTable.setStatus("current")
_HpnicfDot3OamPeerEntry_Object = MibTableRow
hpnicfDot3OamPeerEntry = _HpnicfDot3OamPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 2, 1)
)
hpnicfDot3OamPeerEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfDot3OamPeerEntry.setStatus("current")


class _HpnicfDot3OamPeerStatus_Type(Integer32):
    """Custom type hpnicfDot3OamPeerStatus based on Integer32"""
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


_HpnicfDot3OamPeerStatus_Type.__name__ = "Integer32"
_HpnicfDot3OamPeerStatus_Object = MibTableColumn
hpnicfDot3OamPeerStatus = _HpnicfDot3OamPeerStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 2, 1, 1),
    _HpnicfDot3OamPeerStatus_Type()
)
hpnicfDot3OamPeerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot3OamPeerStatus.setStatus("current")
_HpnicfDot3OamPeerMacAddress_Type = MacAddress
_HpnicfDot3OamPeerMacAddress_Object = MibTableColumn
hpnicfDot3OamPeerMacAddress = _HpnicfDot3OamPeerMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 2, 1, 2),
    _HpnicfDot3OamPeerMacAddress_Type()
)
hpnicfDot3OamPeerMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot3OamPeerMacAddress.setStatus("current")
_HpnicfDot3OamPeerVendorOui_Type = Dot3Oui
_HpnicfDot3OamPeerVendorOui_Object = MibTableColumn
hpnicfDot3OamPeerVendorOui = _HpnicfDot3OamPeerVendorOui_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 2, 1, 3),
    _HpnicfDot3OamPeerVendorOui_Type()
)
hpnicfDot3OamPeerVendorOui.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot3OamPeerVendorOui.setStatus("current")
_HpnicfDot3OamPeerVendorInfo_Type = Unsigned32
_HpnicfDot3OamPeerVendorInfo_Object = MibTableColumn
hpnicfDot3OamPeerVendorInfo = _HpnicfDot3OamPeerVendorInfo_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 2, 1, 4),
    _HpnicfDot3OamPeerVendorInfo_Type()
)
hpnicfDot3OamPeerVendorInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot3OamPeerVendorInfo.setStatus("current")


class _HpnicfDot3OamPeerMode_Type(Integer32):
    """Custom type hpnicfDot3OamPeerMode based on Integer32"""
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


_HpnicfDot3OamPeerMode_Type.__name__ = "Integer32"
_HpnicfDot3OamPeerMode_Object = MibTableColumn
hpnicfDot3OamPeerMode = _HpnicfDot3OamPeerMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 2, 1, 5),
    _HpnicfDot3OamPeerMode_Type()
)
hpnicfDot3OamPeerMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot3OamPeerMode.setStatus("current")


class _HpnicfDot3OamPeerMaxOamPduSize_Type(Integer32):
    """Custom type hpnicfDot3OamPeerMaxOamPduSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 1522),
    )


_HpnicfDot3OamPeerMaxOamPduSize_Type.__name__ = "Integer32"
_HpnicfDot3OamPeerMaxOamPduSize_Object = MibTableColumn
hpnicfDot3OamPeerMaxOamPduSize = _HpnicfDot3OamPeerMaxOamPduSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 2, 1, 6),
    _HpnicfDot3OamPeerMaxOamPduSize_Type()
)
hpnicfDot3OamPeerMaxOamPduSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot3OamPeerMaxOamPduSize.setStatus("current")
_HpnicfDot3OamPeerConfigRevision_Type = Unsigned32
_HpnicfDot3OamPeerConfigRevision_Object = MibTableColumn
hpnicfDot3OamPeerConfigRevision = _HpnicfDot3OamPeerConfigRevision_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 2, 1, 7),
    _HpnicfDot3OamPeerConfigRevision_Type()
)
hpnicfDot3OamPeerConfigRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot3OamPeerConfigRevision.setStatus("current")


class _HpnicfDot3OamPeerFunctionsSupported_Type(Bits):
    """Custom type hpnicfDot3OamPeerFunctionsSupported based on Bits"""
    namedValues = NamedValues(
        *(("eventSupport", 2),
          ("loopbackSupport", 1),
          ("unidirectionalSupport", 0),
          ("variableSupport", 3))
    )

_HpnicfDot3OamPeerFunctionsSupported_Type.__name__ = "Bits"
_HpnicfDot3OamPeerFunctionsSupported_Object = MibTableColumn
hpnicfDot3OamPeerFunctionsSupported = _HpnicfDot3OamPeerFunctionsSupported_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 2, 1, 8),
    _HpnicfDot3OamPeerFunctionsSupported_Type()
)
hpnicfDot3OamPeerFunctionsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot3OamPeerFunctionsSupported.setStatus("current")
_HpnicfDot3OamLoopbackTable_Object = MibTable
hpnicfDot3OamLoopbackTable = _HpnicfDot3OamLoopbackTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 3)
)
if mibBuilder.loadTexts:
    hpnicfDot3OamLoopbackTable.setStatus("current")
_HpnicfDot3OamLoopbackEntry_Object = MibTableRow
hpnicfDot3OamLoopbackEntry = _HpnicfDot3OamLoopbackEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 3, 1)
)
hpnicfDot3OamLoopbackEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfDot3OamLoopbackEntry.setStatus("current")


class _HpnicfDot3OamLoopbackCommand_Type(Integer32):
    """Custom type hpnicfDot3OamLoopbackCommand based on Integer32"""
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


_HpnicfDot3OamLoopbackCommand_Type.__name__ = "Integer32"
_HpnicfDot3OamLoopbackCommand_Object = MibTableColumn
hpnicfDot3OamLoopbackCommand = _HpnicfDot3OamLoopbackCommand_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 3, 1, 1),
    _HpnicfDot3OamLoopbackCommand_Type()
)
hpnicfDot3OamLoopbackCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot3OamLoopbackCommand.setStatus("current")


class _HpnicfDot3OamLoopbackStatus_Type(Integer32):
    """Custom type hpnicfDot3OamLoopbackStatus based on Integer32"""
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


_HpnicfDot3OamLoopbackStatus_Type.__name__ = "Integer32"
_HpnicfDot3OamLoopbackStatus_Object = MibTableColumn
hpnicfDot3OamLoopbackStatus = _HpnicfDot3OamLoopbackStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 3, 1, 2),
    _HpnicfDot3OamLoopbackStatus_Type()
)
hpnicfDot3OamLoopbackStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot3OamLoopbackStatus.setStatus("current")


class _HpnicfDot3OamLoopbackIgnoreRx_Type(Integer32):
    """Custom type hpnicfDot3OamLoopbackIgnoreRx based on Integer32"""
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


_HpnicfDot3OamLoopbackIgnoreRx_Type.__name__ = "Integer32"
_HpnicfDot3OamLoopbackIgnoreRx_Object = MibTableColumn
hpnicfDot3OamLoopbackIgnoreRx = _HpnicfDot3OamLoopbackIgnoreRx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 3, 1, 3),
    _HpnicfDot3OamLoopbackIgnoreRx_Type()
)
hpnicfDot3OamLoopbackIgnoreRx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot3OamLoopbackIgnoreRx.setStatus("current")
_HpnicfDot3OamStatsTable_Object = MibTable
hpnicfDot3OamStatsTable = _HpnicfDot3OamStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 4)
)
if mibBuilder.loadTexts:
    hpnicfDot3OamStatsTable.setStatus("current")
_HpnicfDot3OamStatsEntry_Object = MibTableRow
hpnicfDot3OamStatsEntry = _HpnicfDot3OamStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 4, 1)
)
hpnicfDot3OamStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfDot3OamStatsEntry.setStatus("current")
_HpnicfDot3OamInformationTx_Type = Counter32
_HpnicfDot3OamInformationTx_Object = MibTableColumn
hpnicfDot3OamInformationTx = _HpnicfDot3OamInformationTx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 4, 1, 1),
    _HpnicfDot3OamInformationTx_Type()
)
hpnicfDot3OamInformationTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot3OamInformationTx.setStatus("current")
_HpnicfDot3OamInformationRx_Type = Counter32
_HpnicfDot3OamInformationRx_Object = MibTableColumn
hpnicfDot3OamInformationRx = _HpnicfDot3OamInformationRx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 4, 1, 2),
    _HpnicfDot3OamInformationRx_Type()
)
hpnicfDot3OamInformationRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot3OamInformationRx.setStatus("current")
_HpnicfDot3OamUniqueEventNotificationTx_Type = Counter32
_HpnicfDot3OamUniqueEventNotificationTx_Object = MibTableColumn
hpnicfDot3OamUniqueEventNotificationTx = _HpnicfDot3OamUniqueEventNotificationTx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 4, 1, 3),
    _HpnicfDot3OamUniqueEventNotificationTx_Type()
)
hpnicfDot3OamUniqueEventNotificationTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot3OamUniqueEventNotificationTx.setStatus("current")
_HpnicfDot3OamUniqueEventNotificationRx_Type = Counter32
_HpnicfDot3OamUniqueEventNotificationRx_Object = MibTableColumn
hpnicfDot3OamUniqueEventNotificationRx = _HpnicfDot3OamUniqueEventNotificationRx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 4, 1, 4),
    _HpnicfDot3OamUniqueEventNotificationRx_Type()
)
hpnicfDot3OamUniqueEventNotificationRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot3OamUniqueEventNotificationRx.setStatus("current")
_HpnicfDot3OamDuplicateEventNotificationTx_Type = Counter32
_HpnicfDot3OamDuplicateEventNotificationTx_Object = MibTableColumn
hpnicfDot3OamDuplicateEventNotificationTx = _HpnicfDot3OamDuplicateEventNotificationTx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 4, 1, 5),
    _HpnicfDot3OamDuplicateEventNotificationTx_Type()
)
hpnicfDot3OamDuplicateEventNotificationTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot3OamDuplicateEventNotificationTx.setStatus("current")
_HpnicfDot3OamDuplicateEventNotificationRx_Type = Counter32
_HpnicfDot3OamDuplicateEventNotificationRx_Object = MibTableColumn
hpnicfDot3OamDuplicateEventNotificationRx = _HpnicfDot3OamDuplicateEventNotificationRx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 4, 1, 6),
    _HpnicfDot3OamDuplicateEventNotificationRx_Type()
)
hpnicfDot3OamDuplicateEventNotificationRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot3OamDuplicateEventNotificationRx.setStatus("current")
_HpnicfDot3OamLoopbackControlTx_Type = Counter32
_HpnicfDot3OamLoopbackControlTx_Object = MibTableColumn
hpnicfDot3OamLoopbackControlTx = _HpnicfDot3OamLoopbackControlTx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 4, 1, 7),
    _HpnicfDot3OamLoopbackControlTx_Type()
)
hpnicfDot3OamLoopbackControlTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot3OamLoopbackControlTx.setStatus("current")
_HpnicfDot3OamLoopbackControlRx_Type = Counter32
_HpnicfDot3OamLoopbackControlRx_Object = MibTableColumn
hpnicfDot3OamLoopbackControlRx = _HpnicfDot3OamLoopbackControlRx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 4, 1, 8),
    _HpnicfDot3OamLoopbackControlRx_Type()
)
hpnicfDot3OamLoopbackControlRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot3OamLoopbackControlRx.setStatus("current")
_HpnicfDot3OamVariableRequestTx_Type = Counter32
_HpnicfDot3OamVariableRequestTx_Object = MibTableColumn
hpnicfDot3OamVariableRequestTx = _HpnicfDot3OamVariableRequestTx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 4, 1, 9),
    _HpnicfDot3OamVariableRequestTx_Type()
)
hpnicfDot3OamVariableRequestTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot3OamVariableRequestTx.setStatus("current")
_HpnicfDot3OamVariableRequestRx_Type = Counter32
_HpnicfDot3OamVariableRequestRx_Object = MibTableColumn
hpnicfDot3OamVariableRequestRx = _HpnicfDot3OamVariableRequestRx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 4, 1, 10),
    _HpnicfDot3OamVariableRequestRx_Type()
)
hpnicfDot3OamVariableRequestRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot3OamVariableRequestRx.setStatus("current")
_HpnicfDot3OamVariableResponseTx_Type = Counter32
_HpnicfDot3OamVariableResponseTx_Object = MibTableColumn
hpnicfDot3OamVariableResponseTx = _HpnicfDot3OamVariableResponseTx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 4, 1, 11),
    _HpnicfDot3OamVariableResponseTx_Type()
)
hpnicfDot3OamVariableResponseTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot3OamVariableResponseTx.setStatus("current")
_HpnicfDot3OamVariableResponseRx_Type = Counter32
_HpnicfDot3OamVariableResponseRx_Object = MibTableColumn
hpnicfDot3OamVariableResponseRx = _HpnicfDot3OamVariableResponseRx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 4, 1, 12),
    _HpnicfDot3OamVariableResponseRx_Type()
)
hpnicfDot3OamVariableResponseRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot3OamVariableResponseRx.setStatus("current")
_HpnicfDot3OamOrgSpecificTx_Type = Counter32
_HpnicfDot3OamOrgSpecificTx_Object = MibTableColumn
hpnicfDot3OamOrgSpecificTx = _HpnicfDot3OamOrgSpecificTx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 4, 1, 13),
    _HpnicfDot3OamOrgSpecificTx_Type()
)
hpnicfDot3OamOrgSpecificTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot3OamOrgSpecificTx.setStatus("current")
_HpnicfDot3OamOrgSpecificRx_Type = Counter32
_HpnicfDot3OamOrgSpecificRx_Object = MibTableColumn
hpnicfDot3OamOrgSpecificRx = _HpnicfDot3OamOrgSpecificRx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 4, 1, 14),
    _HpnicfDot3OamOrgSpecificRx_Type()
)
hpnicfDot3OamOrgSpecificRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot3OamOrgSpecificRx.setStatus("current")
_HpnicfDot3OamUnsupportedCodesTx_Type = Counter32
_HpnicfDot3OamUnsupportedCodesTx_Object = MibTableColumn
hpnicfDot3OamUnsupportedCodesTx = _HpnicfDot3OamUnsupportedCodesTx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 4, 1, 15),
    _HpnicfDot3OamUnsupportedCodesTx_Type()
)
hpnicfDot3OamUnsupportedCodesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot3OamUnsupportedCodesTx.setStatus("current")
_HpnicfDot3OamUnsupportedCodesRx_Type = Counter32
_HpnicfDot3OamUnsupportedCodesRx_Object = MibTableColumn
hpnicfDot3OamUnsupportedCodesRx = _HpnicfDot3OamUnsupportedCodesRx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 4, 1, 16),
    _HpnicfDot3OamUnsupportedCodesRx_Type()
)
hpnicfDot3OamUnsupportedCodesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot3OamUnsupportedCodesRx.setStatus("current")
_HpnicfDot3OamFramesLostDueToOam_Type = Counter32
_HpnicfDot3OamFramesLostDueToOam_Object = MibTableColumn
hpnicfDot3OamFramesLostDueToOam = _HpnicfDot3OamFramesLostDueToOam_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 4, 1, 17),
    _HpnicfDot3OamFramesLostDueToOam_Type()
)
hpnicfDot3OamFramesLostDueToOam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot3OamFramesLostDueToOam.setStatus("current")
_HpnicfDot3OamEventConfigTable_Object = MibTable
hpnicfDot3OamEventConfigTable = _HpnicfDot3OamEventConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 5)
)
if mibBuilder.loadTexts:
    hpnicfDot3OamEventConfigTable.setStatus("current")
_HpnicfDot3OamEventConfigEntry_Object = MibTableRow
hpnicfDot3OamEventConfigEntry = _HpnicfDot3OamEventConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 5, 1)
)
hpnicfDot3OamEventConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfDot3OamEventConfigEntry.setStatus("current")
_HpnicfDot3OamErrSymPeriodWindowHi_Type = Unsigned32
_HpnicfDot3OamErrSymPeriodWindowHi_Object = MibTableColumn
hpnicfDot3OamErrSymPeriodWindowHi = _HpnicfDot3OamErrSymPeriodWindowHi_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 5, 1, 1),
    _HpnicfDot3OamErrSymPeriodWindowHi_Type()
)
hpnicfDot3OamErrSymPeriodWindowHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot3OamErrSymPeriodWindowHi.setStatus("current")
_HpnicfDot3OamErrSymPeriodWindowLo_Type = Unsigned32
_HpnicfDot3OamErrSymPeriodWindowLo_Object = MibTableColumn
hpnicfDot3OamErrSymPeriodWindowLo = _HpnicfDot3OamErrSymPeriodWindowLo_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 5, 1, 2),
    _HpnicfDot3OamErrSymPeriodWindowLo_Type()
)
hpnicfDot3OamErrSymPeriodWindowLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot3OamErrSymPeriodWindowLo.setStatus("current")
_HpnicfDot3OamErrSymPeriodThresholdHi_Type = Unsigned32
_HpnicfDot3OamErrSymPeriodThresholdHi_Object = MibTableColumn
hpnicfDot3OamErrSymPeriodThresholdHi = _HpnicfDot3OamErrSymPeriodThresholdHi_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 5, 1, 3),
    _HpnicfDot3OamErrSymPeriodThresholdHi_Type()
)
hpnicfDot3OamErrSymPeriodThresholdHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot3OamErrSymPeriodThresholdHi.setStatus("current")
_HpnicfDot3OamErrSymPeriodThresholdLo_Type = Unsigned32
_HpnicfDot3OamErrSymPeriodThresholdLo_Object = MibTableColumn
hpnicfDot3OamErrSymPeriodThresholdLo = _HpnicfDot3OamErrSymPeriodThresholdLo_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 5, 1, 4),
    _HpnicfDot3OamErrSymPeriodThresholdLo_Type()
)
hpnicfDot3OamErrSymPeriodThresholdLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot3OamErrSymPeriodThresholdLo.setStatus("current")


class _HpnicfDot3OamErrSymPeriodEvNotifEnable_Type(Integer32):
    """Custom type hpnicfDot3OamErrSymPeriodEvNotifEnable based on Integer32"""
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


_HpnicfDot3OamErrSymPeriodEvNotifEnable_Type.__name__ = "Integer32"
_HpnicfDot3OamErrSymPeriodEvNotifEnable_Object = MibTableColumn
hpnicfDot3OamErrSymPeriodEvNotifEnable = _HpnicfDot3OamErrSymPeriodEvNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 5, 1, 5),
    _HpnicfDot3OamErrSymPeriodEvNotifEnable_Type()
)
hpnicfDot3OamErrSymPeriodEvNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot3OamErrSymPeriodEvNotifEnable.setStatus("current")
_HpnicfDot3OamErrFramePeriodWindow_Type = Unsigned32
_HpnicfDot3OamErrFramePeriodWindow_Object = MibTableColumn
hpnicfDot3OamErrFramePeriodWindow = _HpnicfDot3OamErrFramePeriodWindow_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 5, 1, 6),
    _HpnicfDot3OamErrFramePeriodWindow_Type()
)
hpnicfDot3OamErrFramePeriodWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot3OamErrFramePeriodWindow.setStatus("current")
_HpnicfDot3OamErrFramePeriodThreshold_Type = Unsigned32
_HpnicfDot3OamErrFramePeriodThreshold_Object = MibTableColumn
hpnicfDot3OamErrFramePeriodThreshold = _HpnicfDot3OamErrFramePeriodThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 5, 1, 7),
    _HpnicfDot3OamErrFramePeriodThreshold_Type()
)
hpnicfDot3OamErrFramePeriodThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot3OamErrFramePeriodThreshold.setStatus("current")


class _HpnicfDot3OamErrFramePeriodEvNotifEnable_Type(Integer32):
    """Custom type hpnicfDot3OamErrFramePeriodEvNotifEnable based on Integer32"""
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


_HpnicfDot3OamErrFramePeriodEvNotifEnable_Type.__name__ = "Integer32"
_HpnicfDot3OamErrFramePeriodEvNotifEnable_Object = MibTableColumn
hpnicfDot3OamErrFramePeriodEvNotifEnable = _HpnicfDot3OamErrFramePeriodEvNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 5, 1, 8),
    _HpnicfDot3OamErrFramePeriodEvNotifEnable_Type()
)
hpnicfDot3OamErrFramePeriodEvNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot3OamErrFramePeriodEvNotifEnable.setStatus("current")
_HpnicfDot3OamErrFrameWindow_Type = Unsigned32
_HpnicfDot3OamErrFrameWindow_Object = MibTableColumn
hpnicfDot3OamErrFrameWindow = _HpnicfDot3OamErrFrameWindow_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 5, 1, 9),
    _HpnicfDot3OamErrFrameWindow_Type()
)
hpnicfDot3OamErrFrameWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot3OamErrFrameWindow.setStatus("current")
_HpnicfDot3OamErrFrameThreshold_Type = Unsigned32
_HpnicfDot3OamErrFrameThreshold_Object = MibTableColumn
hpnicfDot3OamErrFrameThreshold = _HpnicfDot3OamErrFrameThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 5, 1, 10),
    _HpnicfDot3OamErrFrameThreshold_Type()
)
hpnicfDot3OamErrFrameThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot3OamErrFrameThreshold.setStatus("current")


class _HpnicfDot3OamErrFrameEvNotifEnable_Type(Integer32):
    """Custom type hpnicfDot3OamErrFrameEvNotifEnable based on Integer32"""
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


_HpnicfDot3OamErrFrameEvNotifEnable_Type.__name__ = "Integer32"
_HpnicfDot3OamErrFrameEvNotifEnable_Object = MibTableColumn
hpnicfDot3OamErrFrameEvNotifEnable = _HpnicfDot3OamErrFrameEvNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 5, 1, 11),
    _HpnicfDot3OamErrFrameEvNotifEnable_Type()
)
hpnicfDot3OamErrFrameEvNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot3OamErrFrameEvNotifEnable.setStatus("current")


class _HpnicfDot3OamErrFrameSecsSummaryWindow_Type(Integer32):
    """Custom type hpnicfDot3OamErrFrameSecsSummaryWindow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 9000),
    )


_HpnicfDot3OamErrFrameSecsSummaryWindow_Type.__name__ = "Integer32"
_HpnicfDot3OamErrFrameSecsSummaryWindow_Object = MibTableColumn
hpnicfDot3OamErrFrameSecsSummaryWindow = _HpnicfDot3OamErrFrameSecsSummaryWindow_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 5, 1, 12),
    _HpnicfDot3OamErrFrameSecsSummaryWindow_Type()
)
hpnicfDot3OamErrFrameSecsSummaryWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot3OamErrFrameSecsSummaryWindow.setStatus("current")


class _HpnicfDot3OamErrFrameSecsSummaryThreshold_Type(Integer32):
    """Custom type hpnicfDot3OamErrFrameSecsSummaryThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_HpnicfDot3OamErrFrameSecsSummaryThreshold_Type.__name__ = "Integer32"
_HpnicfDot3OamErrFrameSecsSummaryThreshold_Object = MibTableColumn
hpnicfDot3OamErrFrameSecsSummaryThreshold = _HpnicfDot3OamErrFrameSecsSummaryThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 5, 1, 13),
    _HpnicfDot3OamErrFrameSecsSummaryThreshold_Type()
)
hpnicfDot3OamErrFrameSecsSummaryThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot3OamErrFrameSecsSummaryThreshold.setStatus("current")


class _HpnicfDot3OamErrFrameSecsEvNotifEnable_Type(Integer32):
    """Custom type hpnicfDot3OamErrFrameSecsEvNotifEnable based on Integer32"""
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


_HpnicfDot3OamErrFrameSecsEvNotifEnable_Type.__name__ = "Integer32"
_HpnicfDot3OamErrFrameSecsEvNotifEnable_Object = MibTableColumn
hpnicfDot3OamErrFrameSecsEvNotifEnable = _HpnicfDot3OamErrFrameSecsEvNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 5, 1, 14),
    _HpnicfDot3OamErrFrameSecsEvNotifEnable_Type()
)
hpnicfDot3OamErrFrameSecsEvNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot3OamErrFrameSecsEvNotifEnable.setStatus("current")
_HpnicfDot3OamEventLogTable_Object = MibTable
hpnicfDot3OamEventLogTable = _HpnicfDot3OamEventLogTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 6)
)
if mibBuilder.loadTexts:
    hpnicfDot3OamEventLogTable.setStatus("current")
_HpnicfDot3OamEventLogEntry_Object = MibTableRow
hpnicfDot3OamEventLogEntry = _HpnicfDot3OamEventLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 6, 1)
)
hpnicfDot3OamEventLogEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamEventLogIndex"),
)
if mibBuilder.loadTexts:
    hpnicfDot3OamEventLogEntry.setStatus("current")
_HpnicfDot3OamEventLogIndex_Type = Unsigned32
_HpnicfDot3OamEventLogIndex_Object = MibTableColumn
hpnicfDot3OamEventLogIndex = _HpnicfDot3OamEventLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 6, 1, 1),
    _HpnicfDot3OamEventLogIndex_Type()
)
hpnicfDot3OamEventLogIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot3OamEventLogIndex.setStatus("current")
_HpnicfDot3OamEventLogTimestamp_Type = DateAndTime
_HpnicfDot3OamEventLogTimestamp_Object = MibTableColumn
hpnicfDot3OamEventLogTimestamp = _HpnicfDot3OamEventLogTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 6, 1, 2),
    _HpnicfDot3OamEventLogTimestamp_Type()
)
hpnicfDot3OamEventLogTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot3OamEventLogTimestamp.setStatus("current")
_HpnicfDot3OamEventLogOui_Type = Dot3Oui
_HpnicfDot3OamEventLogOui_Object = MibTableColumn
hpnicfDot3OamEventLogOui = _HpnicfDot3OamEventLogOui_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 6, 1, 3),
    _HpnicfDot3OamEventLogOui_Type()
)
hpnicfDot3OamEventLogOui.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot3OamEventLogOui.setStatus("current")
_HpnicfDot3OamEventLogType_Type = Unsigned32
_HpnicfDot3OamEventLogType_Object = MibTableColumn
hpnicfDot3OamEventLogType = _HpnicfDot3OamEventLogType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 6, 1, 4),
    _HpnicfDot3OamEventLogType_Type()
)
hpnicfDot3OamEventLogType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot3OamEventLogType.setStatus("current")


class _HpnicfDot3OamEventLogLocation_Type(Integer32):
    """Custom type hpnicfDot3OamEventLogLocation based on Integer32"""
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


_HpnicfDot3OamEventLogLocation_Type.__name__ = "Integer32"
_HpnicfDot3OamEventLogLocation_Object = MibTableColumn
hpnicfDot3OamEventLogLocation = _HpnicfDot3OamEventLogLocation_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 6, 1, 5),
    _HpnicfDot3OamEventLogLocation_Type()
)
hpnicfDot3OamEventLogLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot3OamEventLogLocation.setStatus("current")
_HpnicfDot3OamEventLogWindowHi_Type = Unsigned32
_HpnicfDot3OamEventLogWindowHi_Object = MibTableColumn
hpnicfDot3OamEventLogWindowHi = _HpnicfDot3OamEventLogWindowHi_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 6, 1, 6),
    _HpnicfDot3OamEventLogWindowHi_Type()
)
hpnicfDot3OamEventLogWindowHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot3OamEventLogWindowHi.setStatus("current")
_HpnicfDot3OamEventLogWindowLo_Type = Unsigned32
_HpnicfDot3OamEventLogWindowLo_Object = MibTableColumn
hpnicfDot3OamEventLogWindowLo = _HpnicfDot3OamEventLogWindowLo_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 6, 1, 7),
    _HpnicfDot3OamEventLogWindowLo_Type()
)
hpnicfDot3OamEventLogWindowLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot3OamEventLogWindowLo.setStatus("current")
_HpnicfDot3OamEventLogThresholdHi_Type = Unsigned32
_HpnicfDot3OamEventLogThresholdHi_Object = MibTableColumn
hpnicfDot3OamEventLogThresholdHi = _HpnicfDot3OamEventLogThresholdHi_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 6, 1, 8),
    _HpnicfDot3OamEventLogThresholdHi_Type()
)
hpnicfDot3OamEventLogThresholdHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot3OamEventLogThresholdHi.setStatus("current")
_HpnicfDot3OamEventLogThresholdLo_Type = Unsigned32
_HpnicfDot3OamEventLogThresholdLo_Object = MibTableColumn
hpnicfDot3OamEventLogThresholdLo = _HpnicfDot3OamEventLogThresholdLo_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 6, 1, 9),
    _HpnicfDot3OamEventLogThresholdLo_Type()
)
hpnicfDot3OamEventLogThresholdLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot3OamEventLogThresholdLo.setStatus("current")
_HpnicfDot3OamEventLogValue_Type = CounterBasedGauge64
_HpnicfDot3OamEventLogValue_Object = MibTableColumn
hpnicfDot3OamEventLogValue = _HpnicfDot3OamEventLogValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 6, 1, 10),
    _HpnicfDot3OamEventLogValue_Type()
)
hpnicfDot3OamEventLogValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot3OamEventLogValue.setStatus("current")
_HpnicfDot3OamEventLogRunningTotal_Type = CounterBasedGauge64
_HpnicfDot3OamEventLogRunningTotal_Object = MibTableColumn
hpnicfDot3OamEventLogRunningTotal = _HpnicfDot3OamEventLogRunningTotal_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 6, 1, 11),
    _HpnicfDot3OamEventLogRunningTotal_Type()
)
hpnicfDot3OamEventLogRunningTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot3OamEventLogRunningTotal.setStatus("current")
_HpnicfDot3OamEventLogEventTotal_Type = Unsigned32
_HpnicfDot3OamEventLogEventTotal_Object = MibTableColumn
hpnicfDot3OamEventLogEventTotal = _HpnicfDot3OamEventLogEventTotal_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 6, 1, 12),
    _HpnicfDot3OamEventLogEventTotal_Type()
)
hpnicfDot3OamEventLogEventTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot3OamEventLogEventTotal.setStatus("current")
_HpnicfDot3OamTraps_ObjectIdentity = ObjectIdentity
hpnicfDot3OamTraps = _HpnicfDot3OamTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 7)
)
_HpnicfDot3OamTrapsPrefix_ObjectIdentity = ObjectIdentity
hpnicfDot3OamTrapsPrefix = _HpnicfDot3OamTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 7, 0)
)
_HpnicfDot3OamConformance_ObjectIdentity = ObjectIdentity
hpnicfDot3OamConformance = _HpnicfDot3OamConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 2)
)
_HpnicfDot3OamGroups_ObjectIdentity = ObjectIdentity
hpnicfDot3OamGroups = _HpnicfDot3OamGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 2, 1)
)
_HpnicfDot3OamCompliances_ObjectIdentity = ObjectIdentity
hpnicfDot3OamCompliances = _HpnicfDot3OamCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 2, 2)
)

# Managed Objects groups

hpnicfDot3OamControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 2, 1, 1)
)
hpnicfDot3OamControlGroup.setObjects(
      *(("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamAdminState"),
        ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamOperStatus"),
        ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamMode"),
        ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamMaxOamPduSize"),
        ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamConfigRevision"),
        ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamFunctionsSupported"))
)
if mibBuilder.loadTexts:
    hpnicfDot3OamControlGroup.setStatus("current")

hpnicfDot3OamPeerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 2, 1, 2)
)
hpnicfDot3OamPeerGroup.setObjects(
      *(("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamPeerStatus"),
        ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamPeerMacAddress"),
        ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamPeerVendorOui"),
        ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamPeerVendorInfo"),
        ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamPeerMode"),
        ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamPeerFunctionsSupported"),
        ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamPeerMaxOamPduSize"),
        ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamPeerConfigRevision"))
)
if mibBuilder.loadTexts:
    hpnicfDot3OamPeerGroup.setStatus("current")

hpnicfDot3OamStatsBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 2, 1, 3)
)
hpnicfDot3OamStatsBaseGroup.setObjects(
      *(("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamInformationTx"),
        ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamInformationRx"),
        ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamUniqueEventNotificationTx"),
        ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamUniqueEventNotificationRx"),
        ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamDuplicateEventNotificationTx"),
        ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamDuplicateEventNotificationRx"),
        ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamLoopbackControlTx"),
        ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamLoopbackControlRx"),
        ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamVariableRequestTx"),
        ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamVariableRequestRx"),
        ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamVariableResponseTx"),
        ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamVariableResponseRx"),
        ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamOrgSpecificTx"),
        ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamOrgSpecificRx"),
        ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamUnsupportedCodesTx"),
        ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamUnsupportedCodesRx"),
        ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamFramesLostDueToOam"))
)
if mibBuilder.loadTexts:
    hpnicfDot3OamStatsBaseGroup.setStatus("current")

hpnicfDot3OamLoopbackGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 2, 1, 4)
)
hpnicfDot3OamLoopbackGroup.setObjects(
      *(("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamLoopbackCommand"),
        ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamLoopbackStatus"),
        ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamLoopbackIgnoreRx"))
)
if mibBuilder.loadTexts:
    hpnicfDot3OamLoopbackGroup.setStatus("current")

hpnicfDot3OamErrSymbolPeriodEventGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 2, 1, 5)
)
hpnicfDot3OamErrSymbolPeriodEventGroup.setObjects(
      *(("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamErrSymPeriodWindowHi"),
        ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamErrSymPeriodWindowLo"),
        ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamErrSymPeriodThresholdHi"),
        ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamErrSymPeriodThresholdLo"),
        ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamErrSymPeriodEvNotifEnable"))
)
if mibBuilder.loadTexts:
    hpnicfDot3OamErrSymbolPeriodEventGroup.setStatus("current")

hpnicfDot3OamErrFramePeriodEventGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 2, 1, 6)
)
hpnicfDot3OamErrFramePeriodEventGroup.setObjects(
      *(("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamErrFramePeriodWindow"),
        ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamErrFramePeriodThreshold"),
        ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamErrFramePeriodEvNotifEnable"))
)
if mibBuilder.loadTexts:
    hpnicfDot3OamErrFramePeriodEventGroup.setStatus("current")

hpnicfDot3OamErrFrameEventGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 2, 1, 7)
)
hpnicfDot3OamErrFrameEventGroup.setObjects(
      *(("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamErrFrameWindow"),
        ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamErrFrameThreshold"),
        ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamErrFrameEvNotifEnable"))
)
if mibBuilder.loadTexts:
    hpnicfDot3OamErrFrameEventGroup.setStatus("current")

hpnicfDot3OamErrFrameSecsSummaryEventGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 2, 1, 8)
)
hpnicfDot3OamErrFrameSecsSummaryEventGroup.setObjects(
      *(("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamErrFrameSecsSummaryWindow"),
        ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamErrFrameSecsSummaryThreshold"),
        ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamErrFrameSecsEvNotifEnable"))
)
if mibBuilder.loadTexts:
    hpnicfDot3OamErrFrameSecsSummaryEventGroup.setStatus("current")

hpnicfDot3OamEventLogGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 2, 1, 9)
)
hpnicfDot3OamEventLogGroup.setObjects(
      *(("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamEventLogTimestamp"),
        ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamEventLogOui"),
        ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamEventLogType"),
        ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamEventLogLocation"),
        ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamEventLogWindowHi"),
        ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamEventLogWindowLo"),
        ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamEventLogThresholdHi"),
        ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamEventLogThresholdLo"),
        ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamEventLogValue"),
        ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamEventLogRunningTotal"),
        ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamEventLogEventTotal"))
)
if mibBuilder.loadTexts:
    hpnicfDot3OamEventLogGroup.setStatus("current")


# Notification objects

hpnicfDot3OamThresholdEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 7, 0, 1)
)
hpnicfDot3OamThresholdEvent.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamEventLogTimestamp"),
        ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamEventLogOui"),
        ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamEventLogType"),
        ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamEventLogLocation"),
        ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamEventLogWindowHi"),
        ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamEventLogWindowLo"),
        ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamEventLogThresholdHi"),
        ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamEventLogThresholdLo"),
        ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamEventLogValue"),
        ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamEventLogRunningTotal"),
        ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamEventLogEventTotal"))
)
if mibBuilder.loadTexts:
    hpnicfDot3OamThresholdEvent.setStatus(
        "current"
    )

hpnicfDot3OamNonThresholdEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 7, 0, 2)
)
hpnicfDot3OamNonThresholdEvent.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamEventLogTimestamp"),
        ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamEventLogOui"),
        ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamEventLogType"),
        ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamEventLogLocation"),
        ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamEventLogEventTotal"))
)
if mibBuilder.loadTexts:
    hpnicfDot3OamNonThresholdEvent.setStatus(
        "current"
    )


# Notifications groups

hpnicfDot3OamNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 2, 1, 10)
)
hpnicfDot3OamNotificationGroup.setObjects(
      *(("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamThresholdEvent"),
        ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamNonThresholdEvent"))
)
if mibBuilder.loadTexts:
    hpnicfDot3OamNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hpnicfDot3OamCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 2, 2, 1)
)
if mibBuilder.loadTexts:
    hpnicfDot3OamCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-EFM-COMMON-MIB",
    **{"Dot3Oui": Dot3Oui,
       "hpnicfEfmOamMIB": hpnicfEfmOamMIB,
       "hpnicfDot3OamMIB": hpnicfDot3OamMIB,
       "hpnicfDot3OamTable": hpnicfDot3OamTable,
       "hpnicfDot3OamEntry": hpnicfDot3OamEntry,
       "hpnicfDot3OamAdminState": hpnicfDot3OamAdminState,
       "hpnicfDot3OamOperStatus": hpnicfDot3OamOperStatus,
       "hpnicfDot3OamMode": hpnicfDot3OamMode,
       "hpnicfDot3OamMaxOamPduSize": hpnicfDot3OamMaxOamPduSize,
       "hpnicfDot3OamConfigRevision": hpnicfDot3OamConfigRevision,
       "hpnicfDot3OamFunctionsSupported": hpnicfDot3OamFunctionsSupported,
       "hpnicfDot3OamPeerTable": hpnicfDot3OamPeerTable,
       "hpnicfDot3OamPeerEntry": hpnicfDot3OamPeerEntry,
       "hpnicfDot3OamPeerStatus": hpnicfDot3OamPeerStatus,
       "hpnicfDot3OamPeerMacAddress": hpnicfDot3OamPeerMacAddress,
       "hpnicfDot3OamPeerVendorOui": hpnicfDot3OamPeerVendorOui,
       "hpnicfDot3OamPeerVendorInfo": hpnicfDot3OamPeerVendorInfo,
       "hpnicfDot3OamPeerMode": hpnicfDot3OamPeerMode,
       "hpnicfDot3OamPeerMaxOamPduSize": hpnicfDot3OamPeerMaxOamPduSize,
       "hpnicfDot3OamPeerConfigRevision": hpnicfDot3OamPeerConfigRevision,
       "hpnicfDot3OamPeerFunctionsSupported": hpnicfDot3OamPeerFunctionsSupported,
       "hpnicfDot3OamLoopbackTable": hpnicfDot3OamLoopbackTable,
       "hpnicfDot3OamLoopbackEntry": hpnicfDot3OamLoopbackEntry,
       "hpnicfDot3OamLoopbackCommand": hpnicfDot3OamLoopbackCommand,
       "hpnicfDot3OamLoopbackStatus": hpnicfDot3OamLoopbackStatus,
       "hpnicfDot3OamLoopbackIgnoreRx": hpnicfDot3OamLoopbackIgnoreRx,
       "hpnicfDot3OamStatsTable": hpnicfDot3OamStatsTable,
       "hpnicfDot3OamStatsEntry": hpnicfDot3OamStatsEntry,
       "hpnicfDot3OamInformationTx": hpnicfDot3OamInformationTx,
       "hpnicfDot3OamInformationRx": hpnicfDot3OamInformationRx,
       "hpnicfDot3OamUniqueEventNotificationTx": hpnicfDot3OamUniqueEventNotificationTx,
       "hpnicfDot3OamUniqueEventNotificationRx": hpnicfDot3OamUniqueEventNotificationRx,
       "hpnicfDot3OamDuplicateEventNotificationTx": hpnicfDot3OamDuplicateEventNotificationTx,
       "hpnicfDot3OamDuplicateEventNotificationRx": hpnicfDot3OamDuplicateEventNotificationRx,
       "hpnicfDot3OamLoopbackControlTx": hpnicfDot3OamLoopbackControlTx,
       "hpnicfDot3OamLoopbackControlRx": hpnicfDot3OamLoopbackControlRx,
       "hpnicfDot3OamVariableRequestTx": hpnicfDot3OamVariableRequestTx,
       "hpnicfDot3OamVariableRequestRx": hpnicfDot3OamVariableRequestRx,
       "hpnicfDot3OamVariableResponseTx": hpnicfDot3OamVariableResponseTx,
       "hpnicfDot3OamVariableResponseRx": hpnicfDot3OamVariableResponseRx,
       "hpnicfDot3OamOrgSpecificTx": hpnicfDot3OamOrgSpecificTx,
       "hpnicfDot3OamOrgSpecificRx": hpnicfDot3OamOrgSpecificRx,
       "hpnicfDot3OamUnsupportedCodesTx": hpnicfDot3OamUnsupportedCodesTx,
       "hpnicfDot3OamUnsupportedCodesRx": hpnicfDot3OamUnsupportedCodesRx,
       "hpnicfDot3OamFramesLostDueToOam": hpnicfDot3OamFramesLostDueToOam,
       "hpnicfDot3OamEventConfigTable": hpnicfDot3OamEventConfigTable,
       "hpnicfDot3OamEventConfigEntry": hpnicfDot3OamEventConfigEntry,
       "hpnicfDot3OamErrSymPeriodWindowHi": hpnicfDot3OamErrSymPeriodWindowHi,
       "hpnicfDot3OamErrSymPeriodWindowLo": hpnicfDot3OamErrSymPeriodWindowLo,
       "hpnicfDot3OamErrSymPeriodThresholdHi": hpnicfDot3OamErrSymPeriodThresholdHi,
       "hpnicfDot3OamErrSymPeriodThresholdLo": hpnicfDot3OamErrSymPeriodThresholdLo,
       "hpnicfDot3OamErrSymPeriodEvNotifEnable": hpnicfDot3OamErrSymPeriodEvNotifEnable,
       "hpnicfDot3OamErrFramePeriodWindow": hpnicfDot3OamErrFramePeriodWindow,
       "hpnicfDot3OamErrFramePeriodThreshold": hpnicfDot3OamErrFramePeriodThreshold,
       "hpnicfDot3OamErrFramePeriodEvNotifEnable": hpnicfDot3OamErrFramePeriodEvNotifEnable,
       "hpnicfDot3OamErrFrameWindow": hpnicfDot3OamErrFrameWindow,
       "hpnicfDot3OamErrFrameThreshold": hpnicfDot3OamErrFrameThreshold,
       "hpnicfDot3OamErrFrameEvNotifEnable": hpnicfDot3OamErrFrameEvNotifEnable,
       "hpnicfDot3OamErrFrameSecsSummaryWindow": hpnicfDot3OamErrFrameSecsSummaryWindow,
       "hpnicfDot3OamErrFrameSecsSummaryThreshold": hpnicfDot3OamErrFrameSecsSummaryThreshold,
       "hpnicfDot3OamErrFrameSecsEvNotifEnable": hpnicfDot3OamErrFrameSecsEvNotifEnable,
       "hpnicfDot3OamEventLogTable": hpnicfDot3OamEventLogTable,
       "hpnicfDot3OamEventLogEntry": hpnicfDot3OamEventLogEntry,
       "hpnicfDot3OamEventLogIndex": hpnicfDot3OamEventLogIndex,
       "hpnicfDot3OamEventLogTimestamp": hpnicfDot3OamEventLogTimestamp,
       "hpnicfDot3OamEventLogOui": hpnicfDot3OamEventLogOui,
       "hpnicfDot3OamEventLogType": hpnicfDot3OamEventLogType,
       "hpnicfDot3OamEventLogLocation": hpnicfDot3OamEventLogLocation,
       "hpnicfDot3OamEventLogWindowHi": hpnicfDot3OamEventLogWindowHi,
       "hpnicfDot3OamEventLogWindowLo": hpnicfDot3OamEventLogWindowLo,
       "hpnicfDot3OamEventLogThresholdHi": hpnicfDot3OamEventLogThresholdHi,
       "hpnicfDot3OamEventLogThresholdLo": hpnicfDot3OamEventLogThresholdLo,
       "hpnicfDot3OamEventLogValue": hpnicfDot3OamEventLogValue,
       "hpnicfDot3OamEventLogRunningTotal": hpnicfDot3OamEventLogRunningTotal,
       "hpnicfDot3OamEventLogEventTotal": hpnicfDot3OamEventLogEventTotal,
       "hpnicfDot3OamTraps": hpnicfDot3OamTraps,
       "hpnicfDot3OamTrapsPrefix": hpnicfDot3OamTrapsPrefix,
       "hpnicfDot3OamThresholdEvent": hpnicfDot3OamThresholdEvent,
       "hpnicfDot3OamNonThresholdEvent": hpnicfDot3OamNonThresholdEvent,
       "hpnicfDot3OamConformance": hpnicfDot3OamConformance,
       "hpnicfDot3OamGroups": hpnicfDot3OamGroups,
       "hpnicfDot3OamControlGroup": hpnicfDot3OamControlGroup,
       "hpnicfDot3OamPeerGroup": hpnicfDot3OamPeerGroup,
       "hpnicfDot3OamStatsBaseGroup": hpnicfDot3OamStatsBaseGroup,
       "hpnicfDot3OamLoopbackGroup": hpnicfDot3OamLoopbackGroup,
       "hpnicfDot3OamErrSymbolPeriodEventGroup": hpnicfDot3OamErrSymbolPeriodEventGroup,
       "hpnicfDot3OamErrFramePeriodEventGroup": hpnicfDot3OamErrFramePeriodEventGroup,
       "hpnicfDot3OamErrFrameEventGroup": hpnicfDot3OamErrFrameEventGroup,
       "hpnicfDot3OamErrFrameSecsSummaryEventGroup": hpnicfDot3OamErrFrameSecsSummaryEventGroup,
       "hpnicfDot3OamEventLogGroup": hpnicfDot3OamEventLogGroup,
       "hpnicfDot3OamNotificationGroup": hpnicfDot3OamNotificationGroup,
       "hpnicfDot3OamCompliances": hpnicfDot3OamCompliances,
       "hpnicfDot3OamCompliance": hpnicfDot3OamCompliance}
)
