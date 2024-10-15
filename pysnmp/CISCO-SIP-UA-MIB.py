# SNMP MIB module (CISCO-SIP-UA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-SIP-UA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:08:18 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 StorageType,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "StorageType",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoSipUaMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 152)
)
ciscoSipUaMIB.setRevisions(
        ("2004-02-19 00:00",
         "2002-05-08 00:00",
         "2001-10-05 00:00",
         "2001-09-07 00:00",
         "2001-08-21 00:00",
         "2001-08-02 00:00",
         "2001-06-07 00:00",
         "2001-03-02 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CSipStatusCode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class CSipMethodStr(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoSipUaMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoSipUaMIBNotifs = _CiscoSipUaMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 0)
)
_CiscoSipUaMIBObjects_ObjectIdentity = ObjectIdentity
ciscoSipUaMIBObjects = _CiscoSipUaMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1)
)
_CSipCfg_ObjectIdentity = ObjectIdentity
cSipCfg = _CSipCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 1)
)
_CSipCfgBase_ObjectIdentity = ObjectIdentity
cSipCfgBase = _CSipCfgBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 1, 1)
)
_CSipCfgVersion_Type = SnmpAdminString
_CSipCfgVersion_Object = MibScalar
cSipCfgVersion = _CSipCfgVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 1, 1, 1),
    _CSipCfgVersion_Type()
)
cSipCfgVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipCfgVersion.setStatus("current")


class _CSipCfgTransport_Type(Integer32):
    """Custom type cSipCfgTransport based on Integer32"""
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
        *(("disabled", 4),
          ("tcp", 2),
          ("udp", 1),
          ("udpAndTcp", 3))
    )


_CSipCfgTransport_Type.__name__ = "Integer32"
_CSipCfgTransport_Object = MibScalar
cSipCfgTransport = _CSipCfgTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 1, 1, 2),
    _CSipCfgTransport_Type()
)
cSipCfgTransport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cSipCfgTransport.setStatus("current")
_CSipCfgUserLocationServerAddr_Type = SnmpAdminString
_CSipCfgUserLocationServerAddr_Object = MibScalar
cSipCfgUserLocationServerAddr = _CSipCfgUserLocationServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 1, 1, 3),
    _CSipCfgUserLocationServerAddr_Type()
)
cSipCfgUserLocationServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cSipCfgUserLocationServerAddr.setStatus("current")


class _CSipCfgMaxForwards_Type(Integer32):
    """Custom type cSipCfgMaxForwards based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_CSipCfgMaxForwards_Type.__name__ = "Integer32"
_CSipCfgMaxForwards_Object = MibScalar
cSipCfgMaxForwards = _CSipCfgMaxForwards_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 1, 1, 4),
    _CSipCfgMaxForwards_Type()
)
cSipCfgMaxForwards.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cSipCfgMaxForwards.setStatus("deprecated")


class _CSipCfgBindSrcAddrInterface_Type(InterfaceIndexOrZero):
    """Custom type cSipCfgBindSrcAddrInterface based on InterfaceIndexOrZero"""
    defaultValue = 0


_CSipCfgBindSrcAddrInterface_Object = MibScalar
cSipCfgBindSrcAddrInterface = _CSipCfgBindSrcAddrInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 1, 1, 5),
    _CSipCfgBindSrcAddrInterface_Type()
)
cSipCfgBindSrcAddrInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cSipCfgBindSrcAddrInterface.setStatus("deprecated")


class _CSipCfgBindSrcAddrScope_Type(Integer32):
    """Custom type cSipCfgBindSrcAddrScope based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("control", 2))
    )


_CSipCfgBindSrcAddrScope_Type.__name__ = "Integer32"
_CSipCfgBindSrcAddrScope_Object = MibScalar
cSipCfgBindSrcAddrScope = _CSipCfgBindSrcAddrScope_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 1, 1, 6),
    _CSipCfgBindSrcAddrScope_Type()
)
cSipCfgBindSrcAddrScope.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cSipCfgBindSrcAddrScope.setStatus("deprecated")


class _CSipCfgDnsSrvQueryStringFormat_Type(Integer32):
    """Custom type cSipCfgDnsSrvQueryStringFormat based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("v1", 1),
          ("v2", 2))
    )


_CSipCfgDnsSrvQueryStringFormat_Type.__name__ = "Integer32"
_CSipCfgDnsSrvQueryStringFormat_Object = MibScalar
cSipCfgDnsSrvQueryStringFormat = _CSipCfgDnsSrvQueryStringFormat_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 1, 1, 7),
    _CSipCfgDnsSrvQueryStringFormat_Type()
)
cSipCfgDnsSrvQueryStringFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cSipCfgDnsSrvQueryStringFormat.setStatus("current")


class _CSipCfgRedirectionDisabled_Type(TruthValue):
    """Custom type cSipCfgRedirectionDisabled based on TruthValue"""


_CSipCfgRedirectionDisabled_Object = MibScalar
cSipCfgRedirectionDisabled = _CSipCfgRedirectionDisabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 1, 1, 8),
    _CSipCfgRedirectionDisabled_Type()
)
cSipCfgRedirectionDisabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cSipCfgRedirectionDisabled.setStatus("current")
_CSipCfgEarlyMediaTable_Object = MibTable
cSipCfgEarlyMediaTable = _CSipCfgEarlyMediaTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 1, 1, 9)
)
if mibBuilder.loadTexts:
    cSipCfgEarlyMediaTable.setStatus("current")
_CSipCfgEarlyMediaEntry_Object = MibTableRow
cSipCfgEarlyMediaEntry = _CSipCfgEarlyMediaEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 1, 1, 9, 1)
)
cSipCfgEarlyMediaEntry.setIndexNames(
    (0, "CISCO-SIP-UA-MIB", "cSipCfgEarlyMediaStatusCodeIndex"),
)
if mibBuilder.loadTexts:
    cSipCfgEarlyMediaEntry.setStatus("current")
_CSipCfgEarlyMediaStatusCodeIndex_Type = CSipStatusCode
_CSipCfgEarlyMediaStatusCodeIndex_Object = MibTableColumn
cSipCfgEarlyMediaStatusCodeIndex = _CSipCfgEarlyMediaStatusCodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 1, 1, 9, 1, 1),
    _CSipCfgEarlyMediaStatusCodeIndex_Type()
)
cSipCfgEarlyMediaStatusCodeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cSipCfgEarlyMediaStatusCodeIndex.setStatus("current")


class _CSipCfgEarlyMediaCutThruDisabled_Type(TruthValue):
    """Custom type cSipCfgEarlyMediaCutThruDisabled based on TruthValue"""


_CSipCfgEarlyMediaCutThruDisabled_Object = MibTableColumn
cSipCfgEarlyMediaCutThruDisabled = _CSipCfgEarlyMediaCutThruDisabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 1, 1, 9, 1, 2),
    _CSipCfgEarlyMediaCutThruDisabled_Type()
)
cSipCfgEarlyMediaCutThruDisabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cSipCfgEarlyMediaCutThruDisabled.setStatus("current")


class _CSipCfgSymNatEnabled_Type(TruthValue):
    """Custom type cSipCfgSymNatEnabled based on TruthValue"""


_CSipCfgSymNatEnabled_Object = MibScalar
cSipCfgSymNatEnabled = _CSipCfgSymNatEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 1, 1, 10),
    _CSipCfgSymNatEnabled_Type()
)
cSipCfgSymNatEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cSipCfgSymNatEnabled.setStatus("current")


class _CSipCfgSymNatDirectionRole_Type(Integer32):
    """Custom type cSipCfgSymNatDirectionRole based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 3),
          ("none", 1),
          ("passive", 2))
    )


_CSipCfgSymNatDirectionRole_Type.__name__ = "Integer32"
_CSipCfgSymNatDirectionRole_Object = MibScalar
cSipCfgSymNatDirectionRole = _CSipCfgSymNatDirectionRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 1, 1, 11),
    _CSipCfgSymNatDirectionRole_Type()
)
cSipCfgSymNatDirectionRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cSipCfgSymNatDirectionRole.setStatus("current")
_CSipCfgBindSourceAddrTable_Object = MibTable
cSipCfgBindSourceAddrTable = _CSipCfgBindSourceAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 1, 1, 12)
)
if mibBuilder.loadTexts:
    cSipCfgBindSourceAddrTable.setStatus("current")
_CSipCfgBindSourceAddrEntry_Object = MibTableRow
cSipCfgBindSourceAddrEntry = _CSipCfgBindSourceAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 1, 1, 12, 1)
)
cSipCfgBindSourceAddrEntry.setIndexNames(
    (0, "CISCO-SIP-UA-MIB", "cSipCfgBindSourceAddrScope"),
)
if mibBuilder.loadTexts:
    cSipCfgBindSourceAddrEntry.setStatus("current")


class _CSipCfgBindSourceAddrScope_Type(Integer32):
    """Custom type cSipCfgBindSourceAddrScope based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("control", 2),
          ("media", 1))
    )


_CSipCfgBindSourceAddrScope_Type.__name__ = "Integer32"
_CSipCfgBindSourceAddrScope_Object = MibTableColumn
cSipCfgBindSourceAddrScope = _CSipCfgBindSourceAddrScope_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 1, 1, 12, 1, 1),
    _CSipCfgBindSourceAddrScope_Type()
)
cSipCfgBindSourceAddrScope.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cSipCfgBindSourceAddrScope.setStatus("current")


class _CSipCfgBindSourceAddrInterface_Type(InterfaceIndexOrZero):
    """Custom type cSipCfgBindSourceAddrInterface based on InterfaceIndexOrZero"""
    defaultValue = 0


_CSipCfgBindSourceAddrInterface_Object = MibTableColumn
cSipCfgBindSourceAddrInterface = _CSipCfgBindSourceAddrInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 1, 1, 12, 1, 2),
    _CSipCfgBindSourceAddrInterface_Type()
)
cSipCfgBindSourceAddrInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cSipCfgBindSourceAddrInterface.setStatus("current")


class _CSipCfgSuspendResumeEnabled_Type(TruthValue):
    """Custom type cSipCfgSuspendResumeEnabled based on TruthValue"""


_CSipCfgSuspendResumeEnabled_Object = MibScalar
cSipCfgSuspendResumeEnabled = _CSipCfgSuspendResumeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 1, 1, 13),
    _CSipCfgSuspendResumeEnabled_Type()
)
cSipCfgSuspendResumeEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cSipCfgSuspendResumeEnabled.setStatus("current")


class _CSipCfgOfferCallHold_Type(Integer32):
    """Custom type cSipCfgOfferCallHold based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connAddr", 2),
          ("directionAttr", 1))
    )


_CSipCfgOfferCallHold_Type.__name__ = "Integer32"
_CSipCfgOfferCallHold_Object = MibScalar
cSipCfgOfferCallHold = _CSipCfgOfferCallHold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 1, 1, 14),
    _CSipCfgOfferCallHold_Type()
)
cSipCfgOfferCallHold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cSipCfgOfferCallHold.setStatus("current")


class _CSipCfgReasonHeaderOveride_Type(TruthValue):
    """Custom type cSipCfgReasonHeaderOveride based on TruthValue"""


_CSipCfgReasonHeaderOveride_Object = MibScalar
cSipCfgReasonHeaderOveride = _CSipCfgReasonHeaderOveride_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 1, 1, 15),
    _CSipCfgReasonHeaderOveride_Type()
)
cSipCfgReasonHeaderOveride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cSipCfgReasonHeaderOveride.setStatus("current")


class _CSipCfgMaximumForwards_Type(Integer32):
    """Custom type cSipCfgMaximumForwards based on Integer32"""
    defaultValue = 70

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 70),
    )


_CSipCfgMaximumForwards_Type.__name__ = "Integer32"
_CSipCfgMaximumForwards_Object = MibScalar
cSipCfgMaximumForwards = _CSipCfgMaximumForwards_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 1, 1, 16),
    _CSipCfgMaximumForwards_Type()
)
cSipCfgMaximumForwards.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cSipCfgMaximumForwards.setStatus("current")
_CSipCfgTimer_ObjectIdentity = ObjectIdentity
cSipCfgTimer = _CSipCfgTimer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 1, 2)
)


class _CSipCfgTimerTrying_Type(Integer32):
    """Custom type cSipCfgTimerTrying based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_CSipCfgTimerTrying_Type.__name__ = "Integer32"
_CSipCfgTimerTrying_Object = MibScalar
cSipCfgTimerTrying = _CSipCfgTimerTrying_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 1, 2, 1),
    _CSipCfgTimerTrying_Type()
)
cSipCfgTimerTrying.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cSipCfgTimerTrying.setStatus("current")
if mibBuilder.loadTexts:
    cSipCfgTimerTrying.setUnits("milliseconds")


class _CSipCfgTimerExpires_Type(Integer32):
    """Custom type cSipCfgTimerExpires based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60000, 300000),
    )


_CSipCfgTimerExpires_Type.__name__ = "Integer32"
_CSipCfgTimerExpires_Object = MibScalar
cSipCfgTimerExpires = _CSipCfgTimerExpires_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 1, 2, 2),
    _CSipCfgTimerExpires_Type()
)
cSipCfgTimerExpires.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cSipCfgTimerExpires.setStatus("current")
if mibBuilder.loadTexts:
    cSipCfgTimerExpires.setUnits("milliseconds")


class _CSipCfgTimerConnect_Type(Integer32):
    """Custom type cSipCfgTimerConnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_CSipCfgTimerConnect_Type.__name__ = "Integer32"
_CSipCfgTimerConnect_Object = MibScalar
cSipCfgTimerConnect = _CSipCfgTimerConnect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 1, 2, 3),
    _CSipCfgTimerConnect_Type()
)
cSipCfgTimerConnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cSipCfgTimerConnect.setStatus("current")
if mibBuilder.loadTexts:
    cSipCfgTimerConnect.setUnits("milliseconds")


class _CSipCfgTimerDisconnect_Type(Integer32):
    """Custom type cSipCfgTimerDisconnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_CSipCfgTimerDisconnect_Type.__name__ = "Integer32"
_CSipCfgTimerDisconnect_Object = MibScalar
cSipCfgTimerDisconnect = _CSipCfgTimerDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 1, 2, 4),
    _CSipCfgTimerDisconnect_Type()
)
cSipCfgTimerDisconnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cSipCfgTimerDisconnect.setStatus("current")
if mibBuilder.loadTexts:
    cSipCfgTimerDisconnect.setUnits("milliseconds")


class _CSipCfgTimerPrack_Type(Integer32):
    """Custom type cSipCfgTimerPrack based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_CSipCfgTimerPrack_Type.__name__ = "Integer32"
_CSipCfgTimerPrack_Object = MibScalar
cSipCfgTimerPrack = _CSipCfgTimerPrack_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 1, 2, 5),
    _CSipCfgTimerPrack_Type()
)
cSipCfgTimerPrack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cSipCfgTimerPrack.setStatus("current")
if mibBuilder.loadTexts:
    cSipCfgTimerPrack.setUnits("milliseconds")


class _CSipCfgTimerComet_Type(Integer32):
    """Custom type cSipCfgTimerComet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_CSipCfgTimerComet_Type.__name__ = "Integer32"
_CSipCfgTimerComet_Object = MibScalar
cSipCfgTimerComet = _CSipCfgTimerComet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 1, 2, 6),
    _CSipCfgTimerComet_Type()
)
cSipCfgTimerComet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cSipCfgTimerComet.setStatus("current")
if mibBuilder.loadTexts:
    cSipCfgTimerComet.setUnits("milliseconds")


class _CSipCfgTimerReliableRsp_Type(Integer32):
    """Custom type cSipCfgTimerReliableRsp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_CSipCfgTimerReliableRsp_Type.__name__ = "Integer32"
_CSipCfgTimerReliableRsp_Object = MibScalar
cSipCfgTimerReliableRsp = _CSipCfgTimerReliableRsp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 1, 2, 7),
    _CSipCfgTimerReliableRsp_Type()
)
cSipCfgTimerReliableRsp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cSipCfgTimerReliableRsp.setStatus("current")
if mibBuilder.loadTexts:
    cSipCfgTimerReliableRsp.setUnits("milliseconds")


class _CSipCfgTimerNotify_Type(Integer32):
    """Custom type cSipCfgTimerNotify based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_CSipCfgTimerNotify_Type.__name__ = "Integer32"
_CSipCfgTimerNotify_Object = MibScalar
cSipCfgTimerNotify = _CSipCfgTimerNotify_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 1, 2, 8),
    _CSipCfgTimerNotify_Type()
)
cSipCfgTimerNotify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cSipCfgTimerNotify.setStatus("current")
if mibBuilder.loadTexts:
    cSipCfgTimerNotify.setUnits("milliseconds")


class _CSipCfgTimerRefer_Type(Integer32):
    """Custom type cSipCfgTimerRefer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_CSipCfgTimerRefer_Type.__name__ = "Integer32"
_CSipCfgTimerRefer_Object = MibScalar
cSipCfgTimerRefer = _CSipCfgTimerRefer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 1, 2, 9),
    _CSipCfgTimerRefer_Type()
)
cSipCfgTimerRefer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cSipCfgTimerRefer.setStatus("current")
if mibBuilder.loadTexts:
    cSipCfgTimerRefer.setUnits("milliseconds")


class _CSipCfgTimerSessionTimer_Type(Integer32):
    """Custom type cSipCfgTimerSessionTimer based on Integer32"""
    defaultValue = 1800

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 86400),
    )


_CSipCfgTimerSessionTimer_Type.__name__ = "Integer32"
_CSipCfgTimerSessionTimer_Object = MibScalar
cSipCfgTimerSessionTimer = _CSipCfgTimerSessionTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 1, 2, 10),
    _CSipCfgTimerSessionTimer_Type()
)
cSipCfgTimerSessionTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cSipCfgTimerSessionTimer.setStatus("current")
if mibBuilder.loadTexts:
    cSipCfgTimerSessionTimer.setUnits("seconds")


class _CSipCfgTimerHold_Type(Integer32):
    """Custom type cSipCfgTimerHold based on Integer32"""
    defaultValue = 2880

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(15, 2880),
    )


_CSipCfgTimerHold_Type.__name__ = "Integer32"
_CSipCfgTimerHold_Object = MibScalar
cSipCfgTimerHold = _CSipCfgTimerHold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 1, 2, 11),
    _CSipCfgTimerHold_Type()
)
cSipCfgTimerHold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cSipCfgTimerHold.setStatus("current")
if mibBuilder.loadTexts:
    cSipCfgTimerHold.setUnits("minutes")


class _CSipCfgTimerInfo_Type(Integer32):
    """Custom type cSipCfgTimerInfo based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_CSipCfgTimerInfo_Type.__name__ = "Integer32"
_CSipCfgTimerInfo_Object = MibScalar
cSipCfgTimerInfo = _CSipCfgTimerInfo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 1, 2, 12),
    _CSipCfgTimerInfo_Type()
)
cSipCfgTimerInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cSipCfgTimerInfo.setStatus("current")
if mibBuilder.loadTexts:
    cSipCfgTimerInfo.setUnits("milliseconds")


class _CSipCfgTimerConnectionAging_Type(Integer32):
    """Custom type cSipCfgTimerConnectionAging based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_CSipCfgTimerConnectionAging_Type.__name__ = "Integer32"
_CSipCfgTimerConnectionAging_Object = MibScalar
cSipCfgTimerConnectionAging = _CSipCfgTimerConnectionAging_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 1, 2, 13),
    _CSipCfgTimerConnectionAging_Type()
)
cSipCfgTimerConnectionAging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cSipCfgTimerConnectionAging.setStatus("current")
if mibBuilder.loadTexts:
    cSipCfgTimerConnectionAging.setUnits("minutes")


class _CSipCfgTimerBufferInvite_Type(Integer32):
    """Custom type cSipCfgTimerBufferInvite based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(50, 5000),
    )


_CSipCfgTimerBufferInvite_Type.__name__ = "Integer32"
_CSipCfgTimerBufferInvite_Object = MibScalar
cSipCfgTimerBufferInvite = _CSipCfgTimerBufferInvite_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 1, 2, 14),
    _CSipCfgTimerBufferInvite_Type()
)
cSipCfgTimerBufferInvite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cSipCfgTimerBufferInvite.setStatus("current")
if mibBuilder.loadTexts:
    cSipCfgTimerBufferInvite.setUnits("milliseconds")
_CSipCfgRetry_ObjectIdentity = ObjectIdentity
cSipCfgRetry = _CSipCfgRetry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 1, 3)
)


class _CSipCfgRetryInvite_Type(Integer32):
    """Custom type cSipCfgRetryInvite based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_CSipCfgRetryInvite_Type.__name__ = "Integer32"
_CSipCfgRetryInvite_Object = MibScalar
cSipCfgRetryInvite = _CSipCfgRetryInvite_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 1, 3, 1),
    _CSipCfgRetryInvite_Type()
)
cSipCfgRetryInvite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cSipCfgRetryInvite.setStatus("current")


class _CSipCfgRetryBye_Type(Integer32):
    """Custom type cSipCfgRetryBye based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_CSipCfgRetryBye_Type.__name__ = "Integer32"
_CSipCfgRetryBye_Object = MibScalar
cSipCfgRetryBye = _CSipCfgRetryBye_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 1, 3, 2),
    _CSipCfgRetryBye_Type()
)
cSipCfgRetryBye.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cSipCfgRetryBye.setStatus("current")


class _CSipCfgRetryCancel_Type(Integer32):
    """Custom type cSipCfgRetryCancel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_CSipCfgRetryCancel_Type.__name__ = "Integer32"
_CSipCfgRetryCancel_Object = MibScalar
cSipCfgRetryCancel = _CSipCfgRetryCancel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 1, 3, 3),
    _CSipCfgRetryCancel_Type()
)
cSipCfgRetryCancel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cSipCfgRetryCancel.setStatus("current")


class _CSipCfgRetryRegister_Type(Integer32):
    """Custom type cSipCfgRetryRegister based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_CSipCfgRetryRegister_Type.__name__ = "Integer32"
_CSipCfgRetryRegister_Object = MibScalar
cSipCfgRetryRegister = _CSipCfgRetryRegister_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 1, 3, 4),
    _CSipCfgRetryRegister_Type()
)
cSipCfgRetryRegister.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cSipCfgRetryRegister.setStatus("current")


class _CSipCfgRetryResponse_Type(Integer32):
    """Custom type cSipCfgRetryResponse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_CSipCfgRetryResponse_Type.__name__ = "Integer32"
_CSipCfgRetryResponse_Object = MibScalar
cSipCfgRetryResponse = _CSipCfgRetryResponse_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 1, 3, 5),
    _CSipCfgRetryResponse_Type()
)
cSipCfgRetryResponse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cSipCfgRetryResponse.setStatus("current")


class _CSipCfgRetryPrack_Type(Integer32):
    """Custom type cSipCfgRetryPrack based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_CSipCfgRetryPrack_Type.__name__ = "Integer32"
_CSipCfgRetryPrack_Object = MibScalar
cSipCfgRetryPrack = _CSipCfgRetryPrack_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 1, 3, 6),
    _CSipCfgRetryPrack_Type()
)
cSipCfgRetryPrack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cSipCfgRetryPrack.setStatus("current")


class _CSipCfgRetryComet_Type(Integer32):
    """Custom type cSipCfgRetryComet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_CSipCfgRetryComet_Type.__name__ = "Integer32"
_CSipCfgRetryComet_Object = MibScalar
cSipCfgRetryComet = _CSipCfgRetryComet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 1, 3, 7),
    _CSipCfgRetryComet_Type()
)
cSipCfgRetryComet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cSipCfgRetryComet.setStatus("current")


class _CSipCfgRetryReliableRsp_Type(Integer32):
    """Custom type cSipCfgRetryReliableRsp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_CSipCfgRetryReliableRsp_Type.__name__ = "Integer32"
_CSipCfgRetryReliableRsp_Object = MibScalar
cSipCfgRetryReliableRsp = _CSipCfgRetryReliableRsp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 1, 3, 8),
    _CSipCfgRetryReliableRsp_Type()
)
cSipCfgRetryReliableRsp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cSipCfgRetryReliableRsp.setStatus("current")


class _CSipCfgRetryNotify_Type(Integer32):
    """Custom type cSipCfgRetryNotify based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_CSipCfgRetryNotify_Type.__name__ = "Integer32"
_CSipCfgRetryNotify_Object = MibScalar
cSipCfgRetryNotify = _CSipCfgRetryNotify_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 1, 3, 9),
    _CSipCfgRetryNotify_Type()
)
cSipCfgRetryNotify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cSipCfgRetryNotify.setStatus("current")


class _CSipCfgRetryRefer_Type(Integer32):
    """Custom type cSipCfgRetryRefer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_CSipCfgRetryRefer_Type.__name__ = "Integer32"
_CSipCfgRetryRefer_Object = MibScalar
cSipCfgRetryRefer = _CSipCfgRetryRefer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 1, 3, 10),
    _CSipCfgRetryRefer_Type()
)
cSipCfgRetryRefer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cSipCfgRetryRefer.setStatus("current")


class _CSipCfgRetryInfo_Type(Integer32):
    """Custom type cSipCfgRetryInfo based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_CSipCfgRetryInfo_Type.__name__ = "Integer32"
_CSipCfgRetryInfo_Object = MibScalar
cSipCfgRetryInfo = _CSipCfgRetryInfo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 1, 3, 11),
    _CSipCfgRetryInfo_Type()
)
cSipCfgRetryInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cSipCfgRetryInfo.setStatus("current")


class _CSipCfgRetrySubscribe_Type(Integer32):
    """Custom type cSipCfgRetrySubscribe based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_CSipCfgRetrySubscribe_Type.__name__ = "Integer32"
_CSipCfgRetrySubscribe_Object = MibScalar
cSipCfgRetrySubscribe = _CSipCfgRetrySubscribe_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 1, 3, 12),
    _CSipCfgRetrySubscribe_Type()
)
cSipCfgRetrySubscribe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cSipCfgRetrySubscribe.setStatus("current")
_CSipCfgPeer_ObjectIdentity = ObjectIdentity
cSipCfgPeer = _CSipCfgPeer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 1, 4)
)
_CSipCfgPeerTable_Object = MibTable
cSipCfgPeerTable = _CSipCfgPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cSipCfgPeerTable.setStatus("current")
_CSipCfgPeerEntry_Object = MibTableRow
cSipCfgPeerEntry = _CSipCfgPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 1, 4, 1, 1)
)
cSipCfgPeerEntry.setIndexNames(
    (0, "CISCO-SIP-UA-MIB", "cSipCfgPeerIndex"),
)
if mibBuilder.loadTexts:
    cSipCfgPeerEntry.setStatus("current")


class _CSipCfgPeerIndex_Type(Integer32):
    """Custom type cSipCfgPeerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CSipCfgPeerIndex_Type.__name__ = "Integer32"
_CSipCfgPeerIndex_Object = MibTableColumn
cSipCfgPeerIndex = _CSipCfgPeerIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 1, 4, 1, 1, 1),
    _CSipCfgPeerIndex_Type()
)
cSipCfgPeerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cSipCfgPeerIndex.setStatus("current")


class _CSipCfgPeerOutSessionTransport_Type(Integer32):
    """Custom type cSipCfgPeerOutSessionTransport based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("system", 1),
          ("tcp", 3),
          ("udp", 2))
    )


_CSipCfgPeerOutSessionTransport_Type.__name__ = "Integer32"
_CSipCfgPeerOutSessionTransport_Object = MibTableColumn
cSipCfgPeerOutSessionTransport = _CSipCfgPeerOutSessionTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 1, 4, 1, 1, 2),
    _CSipCfgPeerOutSessionTransport_Type()
)
cSipCfgPeerOutSessionTransport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cSipCfgPeerOutSessionTransport.setStatus("current")


class _CSipCfgPeerReliable1xxRspStr_Type(SnmpAdminString):
    """Custom type cSipCfgPeerReliable1xxRspStr based on SnmpAdminString"""
    defaultValue = OctetString("100rel")


_CSipCfgPeerReliable1xxRspStr_Object = MibTableColumn
cSipCfgPeerReliable1xxRspStr = _CSipCfgPeerReliable1xxRspStr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 1, 4, 1, 1, 3),
    _CSipCfgPeerReliable1xxRspStr_Type()
)
cSipCfgPeerReliable1xxRspStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cSipCfgPeerReliable1xxRspStr.setStatus("current")


class _CSipCfgPeerReliable1xxRspHdr_Type(Integer32):
    """Custom type cSipCfgPeerReliable1xxRspHdr based on Integer32"""
    defaultValue = 1

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
        *(("disabled", 4),
          ("require", 3),
          ("supported", 2),
          ("system", 1))
    )


_CSipCfgPeerReliable1xxRspHdr_Type.__name__ = "Integer32"
_CSipCfgPeerReliable1xxRspHdr_Object = MibTableColumn
cSipCfgPeerReliable1xxRspHdr = _CSipCfgPeerReliable1xxRspHdr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 1, 4, 1, 1, 4),
    _CSipCfgPeerReliable1xxRspHdr_Type()
)
cSipCfgPeerReliable1xxRspHdr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cSipCfgPeerReliable1xxRspHdr.setStatus("current")


class _CSipCfgPeerUrlType_Type(Integer32):
    """Custom type cSipCfgPeerUrlType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("sip", 2),
          ("system", 1),
          ("tel", 3))
    )


_CSipCfgPeerUrlType_Type.__name__ = "Integer32"
_CSipCfgPeerUrlType_Object = MibTableColumn
cSipCfgPeerUrlType = _CSipCfgPeerUrlType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 1, 4, 1, 1, 5),
    _CSipCfgPeerUrlType_Type()
)
cSipCfgPeerUrlType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cSipCfgPeerUrlType.setStatus("current")


class _CSipCfgPeerSwitchTransEnabled_Type(TruthValue):
    """Custom type cSipCfgPeerSwitchTransEnabled based on TruthValue"""


_CSipCfgPeerSwitchTransEnabled_Object = MibTableColumn
cSipCfgPeerSwitchTransEnabled = _CSipCfgPeerSwitchTransEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 1, 4, 1, 1, 6),
    _CSipCfgPeerSwitchTransEnabled_Type()
)
cSipCfgPeerSwitchTransEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cSipCfgPeerSwitchTransEnabled.setStatus("current")


class _CSipCfgOutSessionTransport_Type(Integer32):
    """Custom type cSipCfgOutSessionTransport based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 2),
          ("udp", 1))
    )


_CSipCfgOutSessionTransport_Type.__name__ = "Integer32"
_CSipCfgOutSessionTransport_Object = MibScalar
cSipCfgOutSessionTransport = _CSipCfgOutSessionTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 1, 4, 2),
    _CSipCfgOutSessionTransport_Type()
)
cSipCfgOutSessionTransport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cSipCfgOutSessionTransport.setStatus("current")


class _CSipCfgReliable1xxRspStr_Type(SnmpAdminString):
    """Custom type cSipCfgReliable1xxRspStr based on SnmpAdminString"""
    defaultValue = OctetString("100rel")


_CSipCfgReliable1xxRspStr_Object = MibScalar
cSipCfgReliable1xxRspStr = _CSipCfgReliable1xxRspStr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 1, 4, 3),
    _CSipCfgReliable1xxRspStr_Type()
)
cSipCfgReliable1xxRspStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cSipCfgReliable1xxRspStr.setStatus("current")


class _CSipCfgReliable1xxRspHdr_Type(Integer32):
    """Custom type cSipCfgReliable1xxRspHdr based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("require", 2),
          ("supported", 1))
    )


_CSipCfgReliable1xxRspHdr_Type.__name__ = "Integer32"
_CSipCfgReliable1xxRspHdr_Object = MibScalar
cSipCfgReliable1xxRspHdr = _CSipCfgReliable1xxRspHdr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 1, 4, 4),
    _CSipCfgReliable1xxRspHdr_Type()
)
cSipCfgReliable1xxRspHdr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cSipCfgReliable1xxRspHdr.setStatus("current")


class _CSipCfgUrlType_Type(Integer32):
    """Custom type cSipCfgUrlType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sip", 1),
          ("tel", 2))
    )


_CSipCfgUrlType_Type.__name__ = "Integer32"
_CSipCfgUrlType_Object = MibScalar
cSipCfgUrlType = _CSipCfgUrlType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 1, 4, 5),
    _CSipCfgUrlType_Type()
)
cSipCfgUrlType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cSipCfgUrlType.setStatus("current")
_CSipCfgStatusCauseMap_ObjectIdentity = ObjectIdentity
cSipCfgStatusCauseMap = _CSipCfgStatusCauseMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 1, 5)
)
_CSipCfgStatusCauseTable_Object = MibTable
cSipCfgStatusCauseTable = _CSipCfgStatusCauseTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    cSipCfgStatusCauseTable.setStatus("current")
_CSipCfgStatusCauseEntry_Object = MibTableRow
cSipCfgStatusCauseEntry = _CSipCfgStatusCauseEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 1, 5, 1, 1)
)
cSipCfgStatusCauseEntry.setIndexNames(
    (0, "CISCO-SIP-UA-MIB", "cSipCfgStatusCodeIndex"),
)
if mibBuilder.loadTexts:
    cSipCfgStatusCauseEntry.setStatus("current")
_CSipCfgStatusCodeIndex_Type = CSipStatusCode
_CSipCfgStatusCodeIndex_Object = MibTableColumn
cSipCfgStatusCodeIndex = _CSipCfgStatusCodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 1, 5, 1, 1, 1),
    _CSipCfgStatusCodeIndex_Type()
)
cSipCfgStatusCodeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cSipCfgStatusCodeIndex.setStatus("current")


class _CSipCfgPstnCause_Type(Integer32):
    """Custom type cSipCfgPstnCause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CSipCfgPstnCause_Type.__name__ = "Integer32"
_CSipCfgPstnCause_Object = MibTableColumn
cSipCfgPstnCause = _CSipCfgPstnCause_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 1, 5, 1, 1, 2),
    _CSipCfgPstnCause_Type()
)
cSipCfgPstnCause.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cSipCfgPstnCause.setStatus("current")
_CSipCfgStatusCauseStoreStatus_Type = StorageType
_CSipCfgStatusCauseStoreStatus_Object = MibTableColumn
cSipCfgStatusCauseStoreStatus = _CSipCfgStatusCauseStoreStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 1, 5, 1, 1, 3),
    _CSipCfgStatusCauseStoreStatus_Type()
)
cSipCfgStatusCauseStoreStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipCfgStatusCauseStoreStatus.setStatus("current")
_CSipCfgCauseStatusTable_Object = MibTable
cSipCfgCauseStatusTable = _CSipCfgCauseStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 1, 5, 2)
)
if mibBuilder.loadTexts:
    cSipCfgCauseStatusTable.setStatus("current")
_CSipCfgCauseStatusEntry_Object = MibTableRow
cSipCfgCauseStatusEntry = _CSipCfgCauseStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 1, 5, 2, 1)
)
cSipCfgCauseStatusEntry.setIndexNames(
    (0, "CISCO-SIP-UA-MIB", "cSipCfgPstnCauseIndex"),
)
if mibBuilder.loadTexts:
    cSipCfgCauseStatusEntry.setStatus("current")


class _CSipCfgPstnCauseIndex_Type(Integer32):
    """Custom type cSipCfgPstnCauseIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CSipCfgPstnCauseIndex_Type.__name__ = "Integer32"
_CSipCfgPstnCauseIndex_Object = MibTableColumn
cSipCfgPstnCauseIndex = _CSipCfgPstnCauseIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 1, 5, 2, 1, 1),
    _CSipCfgPstnCauseIndex_Type()
)
cSipCfgPstnCauseIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cSipCfgPstnCauseIndex.setStatus("current")
_CSipCfgStatusCode_Type = CSipStatusCode
_CSipCfgStatusCode_Object = MibTableColumn
cSipCfgStatusCode = _CSipCfgStatusCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 1, 5, 2, 1, 2),
    _CSipCfgStatusCode_Type()
)
cSipCfgStatusCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cSipCfgStatusCode.setStatus("current")
_CSipCfgCauseStatusStoreStatus_Type = StorageType
_CSipCfgCauseStatusStoreStatus_Object = MibTableColumn
cSipCfgCauseStatusStoreStatus = _CSipCfgCauseStatusStoreStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 1, 5, 2, 1, 3),
    _CSipCfgCauseStatusStoreStatus_Type()
)
cSipCfgCauseStatusStoreStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipCfgCauseStatusStoreStatus.setStatus("current")
_CSipCfgAaa_ObjectIdentity = ObjectIdentity
cSipCfgAaa = _CSipCfgAaa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 1, 6)
)


class _CSipCfgAaaUsername_Type(Integer32):
    """Custom type cSipCfgAaaUsername based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("callingNumber", 1),
          ("proxyAuth", 2))
    )


_CSipCfgAaaUsername_Type.__name__ = "Integer32"
_CSipCfgAaaUsername_Object = MibScalar
cSipCfgAaaUsername = _CSipCfgAaaUsername_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 1, 6, 1),
    _CSipCfgAaaUsername_Type()
)
cSipCfgAaaUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cSipCfgAaaUsername.setStatus("current")
_CSipCfgVoiceServiceVoip_ObjectIdentity = ObjectIdentity
cSipCfgVoiceServiceVoip = _CSipCfgVoiceServiceVoip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 1, 7)
)


class _CSipCfgHeaderPassingEnabled_Type(TruthValue):
    """Custom type cSipCfgHeaderPassingEnabled based on TruthValue"""


_CSipCfgHeaderPassingEnabled_Object = MibScalar
cSipCfgHeaderPassingEnabled = _CSipCfgHeaderPassingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 1, 7, 1),
    _CSipCfgHeaderPassingEnabled_Type()
)
cSipCfgHeaderPassingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cSipCfgHeaderPassingEnabled.setStatus("current")


class _CSipCfgMaxSubscriptionAccept_Type(Unsigned32):
    """Custom type cSipCfgMaxSubscriptionAccept based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CSipCfgMaxSubscriptionAccept_Type.__name__ = "Unsigned32"
_CSipCfgMaxSubscriptionAccept_Object = MibScalar
cSipCfgMaxSubscriptionAccept = _CSipCfgMaxSubscriptionAccept_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 1, 7, 2),
    _CSipCfgMaxSubscriptionAccept_Type()
)
cSipCfgMaxSubscriptionAccept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cSipCfgMaxSubscriptionAccept.setStatus("current")


class _CSipCfgMaxSubscriptionOriginate_Type(Unsigned32):
    """Custom type cSipCfgMaxSubscriptionOriginate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CSipCfgMaxSubscriptionOriginate_Type.__name__ = "Unsigned32"
_CSipCfgMaxSubscriptionOriginate_Object = MibScalar
cSipCfgMaxSubscriptionOriginate = _CSipCfgMaxSubscriptionOriginate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 1, 7, 3),
    _CSipCfgMaxSubscriptionOriginate_Type()
)
cSipCfgMaxSubscriptionOriginate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cSipCfgMaxSubscriptionOriginate.setStatus("current")


class _CSipCfgSwitchTransportEnabled_Type(TruthValue):
    """Custom type cSipCfgSwitchTransportEnabled based on TruthValue"""


_CSipCfgSwitchTransportEnabled_Object = MibScalar
cSipCfgSwitchTransportEnabled = _CSipCfgSwitchTransportEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 1, 7, 4),
    _CSipCfgSwitchTransportEnabled_Type()
)
cSipCfgSwitchTransportEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cSipCfgSwitchTransportEnabled.setStatus("current")
_CSipStats_ObjectIdentity = ObjectIdentity
cSipStats = _CSipStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2)
)
_CSipStatsInfo_ObjectIdentity = ObjectIdentity
cSipStatsInfo = _CSipStatsInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 1)
)
_CSipStatsInfoTryingIns_Type = Counter32
_CSipStatsInfoTryingIns_Object = MibScalar
cSipStatsInfoTryingIns = _CSipStatsInfoTryingIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 1, 1),
    _CSipStatsInfoTryingIns_Type()
)
cSipStatsInfoTryingIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsInfoTryingIns.setStatus("current")
_CSipStatsInfoTryingOuts_Type = Counter32
_CSipStatsInfoTryingOuts_Object = MibScalar
cSipStatsInfoTryingOuts = _CSipStatsInfoTryingOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 1, 2),
    _CSipStatsInfoTryingOuts_Type()
)
cSipStatsInfoTryingOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsInfoTryingOuts.setStatus("current")
_CSipStatsInfoRingingIns_Type = Counter32
_CSipStatsInfoRingingIns_Object = MibScalar
cSipStatsInfoRingingIns = _CSipStatsInfoRingingIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 1, 3),
    _CSipStatsInfoRingingIns_Type()
)
cSipStatsInfoRingingIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsInfoRingingIns.setStatus("current")
_CSipStatsInfoRingingOuts_Type = Counter32
_CSipStatsInfoRingingOuts_Object = MibScalar
cSipStatsInfoRingingOuts = _CSipStatsInfoRingingOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 1, 4),
    _CSipStatsInfoRingingOuts_Type()
)
cSipStatsInfoRingingOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsInfoRingingOuts.setStatus("current")
_CSipStatsInfoForwardedIns_Type = Counter32
_CSipStatsInfoForwardedIns_Object = MibScalar
cSipStatsInfoForwardedIns = _CSipStatsInfoForwardedIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 1, 5),
    _CSipStatsInfoForwardedIns_Type()
)
cSipStatsInfoForwardedIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsInfoForwardedIns.setStatus("current")
_CSipStatsInfoForwardedOuts_Type = Counter32
_CSipStatsInfoForwardedOuts_Object = MibScalar
cSipStatsInfoForwardedOuts = _CSipStatsInfoForwardedOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 1, 6),
    _CSipStatsInfoForwardedOuts_Type()
)
cSipStatsInfoForwardedOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsInfoForwardedOuts.setStatus("current")
_CSipStatsInfoQueuedIns_Type = Counter32
_CSipStatsInfoQueuedIns_Object = MibScalar
cSipStatsInfoQueuedIns = _CSipStatsInfoQueuedIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 1, 7),
    _CSipStatsInfoQueuedIns_Type()
)
cSipStatsInfoQueuedIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsInfoQueuedIns.setStatus("current")
_CSipStatsInfoQueuedOuts_Type = Counter32
_CSipStatsInfoQueuedOuts_Object = MibScalar
cSipStatsInfoQueuedOuts = _CSipStatsInfoQueuedOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 1, 8),
    _CSipStatsInfoQueuedOuts_Type()
)
cSipStatsInfoQueuedOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsInfoQueuedOuts.setStatus("current")
_CSipStatsInfoSessionProgIns_Type = Counter32
_CSipStatsInfoSessionProgIns_Object = MibScalar
cSipStatsInfoSessionProgIns = _CSipStatsInfoSessionProgIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 1, 9),
    _CSipStatsInfoSessionProgIns_Type()
)
cSipStatsInfoSessionProgIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsInfoSessionProgIns.setStatus("current")
_CSipStatsInfoSessionProgOuts_Type = Counter32
_CSipStatsInfoSessionProgOuts_Object = MibScalar
cSipStatsInfoSessionProgOuts = _CSipStatsInfoSessionProgOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 1, 10),
    _CSipStatsInfoSessionProgOuts_Type()
)
cSipStatsInfoSessionProgOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsInfoSessionProgOuts.setStatus("current")
_CSipStatsSuccess_ObjectIdentity = ObjectIdentity
cSipStatsSuccess = _CSipStatsSuccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 2)
)
_CSipStatsSuccessOkIns_Type = Counter32
_CSipStatsSuccessOkIns_Object = MibScalar
cSipStatsSuccessOkIns = _CSipStatsSuccessOkIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 2, 1),
    _CSipStatsSuccessOkIns_Type()
)
cSipStatsSuccessOkIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsSuccessOkIns.setStatus("deprecated")
_CSipStatsSuccessOkOuts_Type = Counter32
_CSipStatsSuccessOkOuts_Object = MibScalar
cSipStatsSuccessOkOuts = _CSipStatsSuccessOkOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 2, 2),
    _CSipStatsSuccessOkOuts_Type()
)
cSipStatsSuccessOkOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsSuccessOkOuts.setStatus("deprecated")
_CSipStatsSuccessAcceptedIns_Type = Counter32
_CSipStatsSuccessAcceptedIns_Object = MibScalar
cSipStatsSuccessAcceptedIns = _CSipStatsSuccessAcceptedIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 2, 3),
    _CSipStatsSuccessAcceptedIns_Type()
)
cSipStatsSuccessAcceptedIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsSuccessAcceptedIns.setStatus("current")
_CSipStatsSuccessAcceptedOuts_Type = Counter32
_CSipStatsSuccessAcceptedOuts_Object = MibScalar
cSipStatsSuccessAcceptedOuts = _CSipStatsSuccessAcceptedOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 2, 4),
    _CSipStatsSuccessAcceptedOuts_Type()
)
cSipStatsSuccessAcceptedOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsSuccessAcceptedOuts.setStatus("current")
_CSipStatsSuccessOkTable_Object = MibTable
cSipStatsSuccessOkTable = _CSipStatsSuccessOkTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 2, 5)
)
if mibBuilder.loadTexts:
    cSipStatsSuccessOkTable.setStatus("current")
_CSipStatsSuccessOkEntry_Object = MibTableRow
cSipStatsSuccessOkEntry = _CSipStatsSuccessOkEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 2, 5, 1)
)
cSipStatsSuccessOkEntry.setIndexNames(
    (0, "CISCO-SIP-UA-MIB", "cSipStatsSuccessOkMethod"),
)
if mibBuilder.loadTexts:
    cSipStatsSuccessOkEntry.setStatus("current")
_CSipStatsSuccessOkMethod_Type = CSipMethodStr
_CSipStatsSuccessOkMethod_Object = MibTableColumn
cSipStatsSuccessOkMethod = _CSipStatsSuccessOkMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 2, 5, 1, 1),
    _CSipStatsSuccessOkMethod_Type()
)
cSipStatsSuccessOkMethod.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cSipStatsSuccessOkMethod.setStatus("current")
_CSipStatsSuccessOkInbounds_Type = Counter32
_CSipStatsSuccessOkInbounds_Object = MibTableColumn
cSipStatsSuccessOkInbounds = _CSipStatsSuccessOkInbounds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 2, 5, 1, 2),
    _CSipStatsSuccessOkInbounds_Type()
)
cSipStatsSuccessOkInbounds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsSuccessOkInbounds.setStatus("current")
_CSipStatsSuccessOkOutbounds_Type = Counter32
_CSipStatsSuccessOkOutbounds_Object = MibTableColumn
cSipStatsSuccessOkOutbounds = _CSipStatsSuccessOkOutbounds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 2, 5, 1, 3),
    _CSipStatsSuccessOkOutbounds_Type()
)
cSipStatsSuccessOkOutbounds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsSuccessOkOutbounds.setStatus("current")
_CSipStatsRedirect_ObjectIdentity = ObjectIdentity
cSipStatsRedirect = _CSipStatsRedirect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 3)
)
_CSipStatsRedirMultipleChoices_Type = Counter32
_CSipStatsRedirMultipleChoices_Object = MibScalar
cSipStatsRedirMultipleChoices = _CSipStatsRedirMultipleChoices_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 3, 1),
    _CSipStatsRedirMultipleChoices_Type()
)
cSipStatsRedirMultipleChoices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsRedirMultipleChoices.setStatus("current")
_CSipStatsRedirMovedPerms_Type = Counter32
_CSipStatsRedirMovedPerms_Object = MibScalar
cSipStatsRedirMovedPerms = _CSipStatsRedirMovedPerms_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 3, 2),
    _CSipStatsRedirMovedPerms_Type()
)
cSipStatsRedirMovedPerms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsRedirMovedPerms.setStatus("current")
_CSipStatsRedirMovedTemps_Type = Counter32
_CSipStatsRedirMovedTemps_Object = MibScalar
cSipStatsRedirMovedTemps = _CSipStatsRedirMovedTemps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 3, 3),
    _CSipStatsRedirMovedTemps_Type()
)
cSipStatsRedirMovedTemps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsRedirMovedTemps.setStatus("deprecated")
_CSipStatsRedirSeeOthers_Type = Counter32
_CSipStatsRedirSeeOthers_Object = MibScalar
cSipStatsRedirSeeOthers = _CSipStatsRedirSeeOthers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 3, 4),
    _CSipStatsRedirSeeOthers_Type()
)
cSipStatsRedirSeeOthers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsRedirSeeOthers.setStatus("obsolete")
_CSipStatsRedirUseProxys_Type = Counter32
_CSipStatsRedirUseProxys_Object = MibScalar
cSipStatsRedirUseProxys = _CSipStatsRedirUseProxys_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 3, 5),
    _CSipStatsRedirUseProxys_Type()
)
cSipStatsRedirUseProxys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsRedirUseProxys.setStatus("current")
_CSipStatsRedirAltServices_Type = Counter32
_CSipStatsRedirAltServices_Object = MibScalar
cSipStatsRedirAltServices = _CSipStatsRedirAltServices_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 3, 6),
    _CSipStatsRedirAltServices_Type()
)
cSipStatsRedirAltServices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsRedirAltServices.setStatus("current")
_CSipStatsRedirMovedTempsIns_Type = Counter32
_CSipStatsRedirMovedTempsIns_Object = MibScalar
cSipStatsRedirMovedTempsIns = _CSipStatsRedirMovedTempsIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 3, 7),
    _CSipStatsRedirMovedTempsIns_Type()
)
cSipStatsRedirMovedTempsIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsRedirMovedTempsIns.setStatus("current")
_CSipStatsRedirMovedTempsOuts_Type = Counter32
_CSipStatsRedirMovedTempsOuts_Object = MibScalar
cSipStatsRedirMovedTempsOuts = _CSipStatsRedirMovedTempsOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 3, 8),
    _CSipStatsRedirMovedTempsOuts_Type()
)
cSipStatsRedirMovedTempsOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsRedirMovedTempsOuts.setStatus("current")
_CSipStatsErrClient_ObjectIdentity = ObjectIdentity
cSipStatsErrClient = _CSipStatsErrClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 4)
)
_CSipStatsClientBadRequestIns_Type = Counter32
_CSipStatsClientBadRequestIns_Object = MibScalar
cSipStatsClientBadRequestIns = _CSipStatsClientBadRequestIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 4, 1),
    _CSipStatsClientBadRequestIns_Type()
)
cSipStatsClientBadRequestIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsClientBadRequestIns.setStatus("current")
_CSipStatsClientBadRequestOuts_Type = Counter32
_CSipStatsClientBadRequestOuts_Object = MibScalar
cSipStatsClientBadRequestOuts = _CSipStatsClientBadRequestOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 4, 2),
    _CSipStatsClientBadRequestOuts_Type()
)
cSipStatsClientBadRequestOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsClientBadRequestOuts.setStatus("current")
_CSipStatsClientUnauthorizedIns_Type = Counter32
_CSipStatsClientUnauthorizedIns_Object = MibScalar
cSipStatsClientUnauthorizedIns = _CSipStatsClientUnauthorizedIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 4, 3),
    _CSipStatsClientUnauthorizedIns_Type()
)
cSipStatsClientUnauthorizedIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsClientUnauthorizedIns.setStatus("current")
_CSipStatsClientUnauthorizedOuts_Type = Counter32
_CSipStatsClientUnauthorizedOuts_Object = MibScalar
cSipStatsClientUnauthorizedOuts = _CSipStatsClientUnauthorizedOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 4, 4),
    _CSipStatsClientUnauthorizedOuts_Type()
)
cSipStatsClientUnauthorizedOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsClientUnauthorizedOuts.setStatus("current")
_CSipStatsClientPaymentReqdIns_Type = Counter32
_CSipStatsClientPaymentReqdIns_Object = MibScalar
cSipStatsClientPaymentReqdIns = _CSipStatsClientPaymentReqdIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 4, 5),
    _CSipStatsClientPaymentReqdIns_Type()
)
cSipStatsClientPaymentReqdIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsClientPaymentReqdIns.setStatus("current")
_CSipStatsClientPaymentReqdOuts_Type = Counter32
_CSipStatsClientPaymentReqdOuts_Object = MibScalar
cSipStatsClientPaymentReqdOuts = _CSipStatsClientPaymentReqdOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 4, 6),
    _CSipStatsClientPaymentReqdOuts_Type()
)
cSipStatsClientPaymentReqdOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsClientPaymentReqdOuts.setStatus("current")
_CSipStatsClientForbiddenIns_Type = Counter32
_CSipStatsClientForbiddenIns_Object = MibScalar
cSipStatsClientForbiddenIns = _CSipStatsClientForbiddenIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 4, 7),
    _CSipStatsClientForbiddenIns_Type()
)
cSipStatsClientForbiddenIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsClientForbiddenIns.setStatus("current")
_CSipStatsClientForbiddenOuts_Type = Counter32
_CSipStatsClientForbiddenOuts_Object = MibScalar
cSipStatsClientForbiddenOuts = _CSipStatsClientForbiddenOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 4, 8),
    _CSipStatsClientForbiddenOuts_Type()
)
cSipStatsClientForbiddenOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsClientForbiddenOuts.setStatus("current")
_CSipStatsClientNotFoundIns_Type = Counter32
_CSipStatsClientNotFoundIns_Object = MibScalar
cSipStatsClientNotFoundIns = _CSipStatsClientNotFoundIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 4, 9),
    _CSipStatsClientNotFoundIns_Type()
)
cSipStatsClientNotFoundIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsClientNotFoundIns.setStatus("current")
_CSipStatsClientNotFoundOuts_Type = Counter32
_CSipStatsClientNotFoundOuts_Object = MibScalar
cSipStatsClientNotFoundOuts = _CSipStatsClientNotFoundOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 4, 10),
    _CSipStatsClientNotFoundOuts_Type()
)
cSipStatsClientNotFoundOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsClientNotFoundOuts.setStatus("current")
_CSipStatsClientMethNotAllowedIns_Type = Counter32
_CSipStatsClientMethNotAllowedIns_Object = MibScalar
cSipStatsClientMethNotAllowedIns = _CSipStatsClientMethNotAllowedIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 4, 11),
    _CSipStatsClientMethNotAllowedIns_Type()
)
cSipStatsClientMethNotAllowedIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsClientMethNotAllowedIns.setStatus("current")
_CSipStatsClientMethNotAllowedOuts_Type = Counter32
_CSipStatsClientMethNotAllowedOuts_Object = MibScalar
cSipStatsClientMethNotAllowedOuts = _CSipStatsClientMethNotAllowedOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 4, 12),
    _CSipStatsClientMethNotAllowedOuts_Type()
)
cSipStatsClientMethNotAllowedOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsClientMethNotAllowedOuts.setStatus("current")
_CSipStatsClientNotAcceptableIns_Type = Counter32
_CSipStatsClientNotAcceptableIns_Object = MibScalar
cSipStatsClientNotAcceptableIns = _CSipStatsClientNotAcceptableIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 4, 13),
    _CSipStatsClientNotAcceptableIns_Type()
)
cSipStatsClientNotAcceptableIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsClientNotAcceptableIns.setStatus("current")
_CSipStatsClientNotAcceptableOuts_Type = Counter32
_CSipStatsClientNotAcceptableOuts_Object = MibScalar
cSipStatsClientNotAcceptableOuts = _CSipStatsClientNotAcceptableOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 4, 14),
    _CSipStatsClientNotAcceptableOuts_Type()
)
cSipStatsClientNotAcceptableOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsClientNotAcceptableOuts.setStatus("current")
_CSipStatsClientProxyAuthReqdIns_Type = Counter32
_CSipStatsClientProxyAuthReqdIns_Object = MibScalar
cSipStatsClientProxyAuthReqdIns = _CSipStatsClientProxyAuthReqdIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 4, 15),
    _CSipStatsClientProxyAuthReqdIns_Type()
)
cSipStatsClientProxyAuthReqdIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsClientProxyAuthReqdIns.setStatus("current")
_CSipStatsClientProxyAuthReqdOuts_Type = Counter32
_CSipStatsClientProxyAuthReqdOuts_Object = MibScalar
cSipStatsClientProxyAuthReqdOuts = _CSipStatsClientProxyAuthReqdOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 4, 16),
    _CSipStatsClientProxyAuthReqdOuts_Type()
)
cSipStatsClientProxyAuthReqdOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsClientProxyAuthReqdOuts.setStatus("current")
_CSipStatsClientReqTimeoutIns_Type = Counter32
_CSipStatsClientReqTimeoutIns_Object = MibScalar
cSipStatsClientReqTimeoutIns = _CSipStatsClientReqTimeoutIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 4, 17),
    _CSipStatsClientReqTimeoutIns_Type()
)
cSipStatsClientReqTimeoutIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsClientReqTimeoutIns.setStatus("current")
_CSipStatsClientReqTimeoutOuts_Type = Counter32
_CSipStatsClientReqTimeoutOuts_Object = MibScalar
cSipStatsClientReqTimeoutOuts = _CSipStatsClientReqTimeoutOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 4, 18),
    _CSipStatsClientReqTimeoutOuts_Type()
)
cSipStatsClientReqTimeoutOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsClientReqTimeoutOuts.setStatus("current")
_CSipStatsClientConflictIns_Type = Counter32
_CSipStatsClientConflictIns_Object = MibScalar
cSipStatsClientConflictIns = _CSipStatsClientConflictIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 4, 19),
    _CSipStatsClientConflictIns_Type()
)
cSipStatsClientConflictIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsClientConflictIns.setStatus("current")
_CSipStatsClientConflictOuts_Type = Counter32
_CSipStatsClientConflictOuts_Object = MibScalar
cSipStatsClientConflictOuts = _CSipStatsClientConflictOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 4, 20),
    _CSipStatsClientConflictOuts_Type()
)
cSipStatsClientConflictOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsClientConflictOuts.setStatus("current")
_CSipStatsClientGoneIns_Type = Counter32
_CSipStatsClientGoneIns_Object = MibScalar
cSipStatsClientGoneIns = _CSipStatsClientGoneIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 4, 21),
    _CSipStatsClientGoneIns_Type()
)
cSipStatsClientGoneIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsClientGoneIns.setStatus("current")
_CSipStatsClientGoneOuts_Type = Counter32
_CSipStatsClientGoneOuts_Object = MibScalar
cSipStatsClientGoneOuts = _CSipStatsClientGoneOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 4, 22),
    _CSipStatsClientGoneOuts_Type()
)
cSipStatsClientGoneOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsClientGoneOuts.setStatus("current")
_CSipStatsClientLengthRequiredIns_Type = Counter32
_CSipStatsClientLengthRequiredIns_Object = MibScalar
cSipStatsClientLengthRequiredIns = _CSipStatsClientLengthRequiredIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 4, 23),
    _CSipStatsClientLengthRequiredIns_Type()
)
cSipStatsClientLengthRequiredIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsClientLengthRequiredIns.setStatus("obsolete")
_CSipStatsClientLengthRequiredOuts_Type = Counter32
_CSipStatsClientLengthRequiredOuts_Object = MibScalar
cSipStatsClientLengthRequiredOuts = _CSipStatsClientLengthRequiredOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 4, 24),
    _CSipStatsClientLengthRequiredOuts_Type()
)
cSipStatsClientLengthRequiredOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsClientLengthRequiredOuts.setStatus("obsolete")
_CSipStatsClientReqEntTooLargeIns_Type = Counter32
_CSipStatsClientReqEntTooLargeIns_Object = MibScalar
cSipStatsClientReqEntTooLargeIns = _CSipStatsClientReqEntTooLargeIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 4, 25),
    _CSipStatsClientReqEntTooLargeIns_Type()
)
cSipStatsClientReqEntTooLargeIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsClientReqEntTooLargeIns.setStatus("current")
_CSipStatsClientReqEntTooLargeOuts_Type = Counter32
_CSipStatsClientReqEntTooLargeOuts_Object = MibScalar
cSipStatsClientReqEntTooLargeOuts = _CSipStatsClientReqEntTooLargeOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 4, 26),
    _CSipStatsClientReqEntTooLargeOuts_Type()
)
cSipStatsClientReqEntTooLargeOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsClientReqEntTooLargeOuts.setStatus("current")
_CSipStatsClientReqURITooLargeIns_Type = Counter32
_CSipStatsClientReqURITooLargeIns_Object = MibScalar
cSipStatsClientReqURITooLargeIns = _CSipStatsClientReqURITooLargeIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 4, 27),
    _CSipStatsClientReqURITooLargeIns_Type()
)
cSipStatsClientReqURITooLargeIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsClientReqURITooLargeIns.setStatus("current")
_CSipStatsClientReqURITooLargeOuts_Type = Counter32
_CSipStatsClientReqURITooLargeOuts_Object = MibScalar
cSipStatsClientReqURITooLargeOuts = _CSipStatsClientReqURITooLargeOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 4, 28),
    _CSipStatsClientReqURITooLargeOuts_Type()
)
cSipStatsClientReqURITooLargeOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsClientReqURITooLargeOuts.setStatus("current")
_CSipStatsClientNoSupMediaTypeIns_Type = Counter32
_CSipStatsClientNoSupMediaTypeIns_Object = MibScalar
cSipStatsClientNoSupMediaTypeIns = _CSipStatsClientNoSupMediaTypeIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 4, 29),
    _CSipStatsClientNoSupMediaTypeIns_Type()
)
cSipStatsClientNoSupMediaTypeIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsClientNoSupMediaTypeIns.setStatus("current")
_CSipStatsClientNoSupMediaTypeOuts_Type = Counter32
_CSipStatsClientNoSupMediaTypeOuts_Object = MibScalar
cSipStatsClientNoSupMediaTypeOuts = _CSipStatsClientNoSupMediaTypeOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 4, 30),
    _CSipStatsClientNoSupMediaTypeOuts_Type()
)
cSipStatsClientNoSupMediaTypeOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsClientNoSupMediaTypeOuts.setStatus("current")
_CSipStatsClientBadExtensionIns_Type = Counter32
_CSipStatsClientBadExtensionIns_Object = MibScalar
cSipStatsClientBadExtensionIns = _CSipStatsClientBadExtensionIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 4, 31),
    _CSipStatsClientBadExtensionIns_Type()
)
cSipStatsClientBadExtensionIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsClientBadExtensionIns.setStatus("current")
_CSipStatsClientBadExtensionOuts_Type = Counter32
_CSipStatsClientBadExtensionOuts_Object = MibScalar
cSipStatsClientBadExtensionOuts = _CSipStatsClientBadExtensionOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 4, 32),
    _CSipStatsClientBadExtensionOuts_Type()
)
cSipStatsClientBadExtensionOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsClientBadExtensionOuts.setStatus("current")
_CSipStatsClientTempNotAvailIns_Type = Counter32
_CSipStatsClientTempNotAvailIns_Object = MibScalar
cSipStatsClientTempNotAvailIns = _CSipStatsClientTempNotAvailIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 4, 33),
    _CSipStatsClientTempNotAvailIns_Type()
)
cSipStatsClientTempNotAvailIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsClientTempNotAvailIns.setStatus("current")
_CSipStatsClientTempNotAvailOuts_Type = Counter32
_CSipStatsClientTempNotAvailOuts_Object = MibScalar
cSipStatsClientTempNotAvailOuts = _CSipStatsClientTempNotAvailOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 4, 34),
    _CSipStatsClientTempNotAvailOuts_Type()
)
cSipStatsClientTempNotAvailOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsClientTempNotAvailOuts.setStatus("current")
_CSipStatsClientCallLegNoExistIns_Type = Counter32
_CSipStatsClientCallLegNoExistIns_Object = MibScalar
cSipStatsClientCallLegNoExistIns = _CSipStatsClientCallLegNoExistIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 4, 35),
    _CSipStatsClientCallLegNoExistIns_Type()
)
cSipStatsClientCallLegNoExistIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsClientCallLegNoExistIns.setStatus("current")
_CSipStatsClientCallLegNoExistOuts_Type = Counter32
_CSipStatsClientCallLegNoExistOuts_Object = MibScalar
cSipStatsClientCallLegNoExistOuts = _CSipStatsClientCallLegNoExistOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 4, 36),
    _CSipStatsClientCallLegNoExistOuts_Type()
)
cSipStatsClientCallLegNoExistOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsClientCallLegNoExistOuts.setStatus("current")
_CSipStatsClientLoopDetectedIns_Type = Counter32
_CSipStatsClientLoopDetectedIns_Object = MibScalar
cSipStatsClientLoopDetectedIns = _CSipStatsClientLoopDetectedIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 4, 37),
    _CSipStatsClientLoopDetectedIns_Type()
)
cSipStatsClientLoopDetectedIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsClientLoopDetectedIns.setStatus("current")
_CSipStatsClientLoopDetectedOuts_Type = Counter32
_CSipStatsClientLoopDetectedOuts_Object = MibScalar
cSipStatsClientLoopDetectedOuts = _CSipStatsClientLoopDetectedOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 4, 38),
    _CSipStatsClientLoopDetectedOuts_Type()
)
cSipStatsClientLoopDetectedOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsClientLoopDetectedOuts.setStatus("current")
_CSipStatsClientTooManyHopsIns_Type = Counter32
_CSipStatsClientTooManyHopsIns_Object = MibScalar
cSipStatsClientTooManyHopsIns = _CSipStatsClientTooManyHopsIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 4, 39),
    _CSipStatsClientTooManyHopsIns_Type()
)
cSipStatsClientTooManyHopsIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsClientTooManyHopsIns.setStatus("current")
_CSipStatsClientTooManyHopsOuts_Type = Counter32
_CSipStatsClientTooManyHopsOuts_Object = MibScalar
cSipStatsClientTooManyHopsOuts = _CSipStatsClientTooManyHopsOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 4, 40),
    _CSipStatsClientTooManyHopsOuts_Type()
)
cSipStatsClientTooManyHopsOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsClientTooManyHopsOuts.setStatus("current")
_CSipStatsClientAddrIncompleteIns_Type = Counter32
_CSipStatsClientAddrIncompleteIns_Object = MibScalar
cSipStatsClientAddrIncompleteIns = _CSipStatsClientAddrIncompleteIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 4, 41),
    _CSipStatsClientAddrIncompleteIns_Type()
)
cSipStatsClientAddrIncompleteIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsClientAddrIncompleteIns.setStatus("current")
_CSipStatsClientAddrIncompleteOuts_Type = Counter32
_CSipStatsClientAddrIncompleteOuts_Object = MibScalar
cSipStatsClientAddrIncompleteOuts = _CSipStatsClientAddrIncompleteOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 4, 42),
    _CSipStatsClientAddrIncompleteOuts_Type()
)
cSipStatsClientAddrIncompleteOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsClientAddrIncompleteOuts.setStatus("current")
_CSipStatsClientAmbiguousIns_Type = Counter32
_CSipStatsClientAmbiguousIns_Object = MibScalar
cSipStatsClientAmbiguousIns = _CSipStatsClientAmbiguousIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 4, 43),
    _CSipStatsClientAmbiguousIns_Type()
)
cSipStatsClientAmbiguousIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsClientAmbiguousIns.setStatus("current")
_CSipStatsClientAmbiguousOuts_Type = Counter32
_CSipStatsClientAmbiguousOuts_Object = MibScalar
cSipStatsClientAmbiguousOuts = _CSipStatsClientAmbiguousOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 4, 44),
    _CSipStatsClientAmbiguousOuts_Type()
)
cSipStatsClientAmbiguousOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsClientAmbiguousOuts.setStatus("current")
_CSipStatsClientBusyHereIns_Type = Counter32
_CSipStatsClientBusyHereIns_Object = MibScalar
cSipStatsClientBusyHereIns = _CSipStatsClientBusyHereIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 4, 45),
    _CSipStatsClientBusyHereIns_Type()
)
cSipStatsClientBusyHereIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsClientBusyHereIns.setStatus("current")
_CSipStatsClientBusyHereOuts_Type = Counter32
_CSipStatsClientBusyHereOuts_Object = MibScalar
cSipStatsClientBusyHereOuts = _CSipStatsClientBusyHereOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 4, 46),
    _CSipStatsClientBusyHereOuts_Type()
)
cSipStatsClientBusyHereOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsClientBusyHereOuts.setStatus("current")
_CSipStatsClientReqTermIns_Type = Counter32
_CSipStatsClientReqTermIns_Object = MibScalar
cSipStatsClientReqTermIns = _CSipStatsClientReqTermIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 4, 47),
    _CSipStatsClientReqTermIns_Type()
)
cSipStatsClientReqTermIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsClientReqTermIns.setStatus("current")
_CSipStatsClientReqTermOuts_Type = Counter32
_CSipStatsClientReqTermOuts_Object = MibScalar
cSipStatsClientReqTermOuts = _CSipStatsClientReqTermOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 4, 48),
    _CSipStatsClientReqTermOuts_Type()
)
cSipStatsClientReqTermOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsClientReqTermOuts.setStatus("current")
_CSipStatsClientNoAcceptHereIns_Type = Counter32
_CSipStatsClientNoAcceptHereIns_Object = MibScalar
cSipStatsClientNoAcceptHereIns = _CSipStatsClientNoAcceptHereIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 4, 49),
    _CSipStatsClientNoAcceptHereIns_Type()
)
cSipStatsClientNoAcceptHereIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsClientNoAcceptHereIns.setStatus("current")
_CSipStatsClientNoAcceptHereOuts_Type = Counter32
_CSipStatsClientNoAcceptHereOuts_Object = MibScalar
cSipStatsClientNoAcceptHereOuts = _CSipStatsClientNoAcceptHereOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 4, 50),
    _CSipStatsClientNoAcceptHereOuts_Type()
)
cSipStatsClientNoAcceptHereOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsClientNoAcceptHereOuts.setStatus("current")
_CSipStatsClientBadEventIns_Type = Counter32
_CSipStatsClientBadEventIns_Object = MibScalar
cSipStatsClientBadEventIns = _CSipStatsClientBadEventIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 4, 51),
    _CSipStatsClientBadEventIns_Type()
)
cSipStatsClientBadEventIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsClientBadEventIns.setStatus("current")
_CSipStatsClientBadEventOuts_Type = Counter32
_CSipStatsClientBadEventOuts_Object = MibScalar
cSipStatsClientBadEventOuts = _CSipStatsClientBadEventOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 4, 52),
    _CSipStatsClientBadEventOuts_Type()
)
cSipStatsClientBadEventOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsClientBadEventOuts.setStatus("current")
_CSipStatsClientSTTooSmallIns_Type = Counter32
_CSipStatsClientSTTooSmallIns_Object = MibScalar
cSipStatsClientSTTooSmallIns = _CSipStatsClientSTTooSmallIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 4, 53),
    _CSipStatsClientSTTooSmallIns_Type()
)
cSipStatsClientSTTooSmallIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsClientSTTooSmallIns.setStatus("current")
_CSipStatsClientSTTooSmallOuts_Type = Counter32
_CSipStatsClientSTTooSmallOuts_Object = MibScalar
cSipStatsClientSTTooSmallOuts = _CSipStatsClientSTTooSmallOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 4, 54),
    _CSipStatsClientSTTooSmallOuts_Type()
)
cSipStatsClientSTTooSmallOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsClientSTTooSmallOuts.setStatus("current")
_CSipStatsClientReqPendingIns_Type = Counter32
_CSipStatsClientReqPendingIns_Object = MibScalar
cSipStatsClientReqPendingIns = _CSipStatsClientReqPendingIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 4, 55),
    _CSipStatsClientReqPendingIns_Type()
)
cSipStatsClientReqPendingIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsClientReqPendingIns.setStatus("current")
_CSipStatsClientReqPendingOuts_Type = Counter32
_CSipStatsClientReqPendingOuts_Object = MibScalar
cSipStatsClientReqPendingOuts = _CSipStatsClientReqPendingOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 4, 56),
    _CSipStatsClientReqPendingOuts_Type()
)
cSipStatsClientReqPendingOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsClientReqPendingOuts.setStatus("current")
_CSipStatsErrServer_ObjectIdentity = ObjectIdentity
cSipStatsErrServer = _CSipStatsErrServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 5)
)
_CSipStatsServerIntErrorIns_Type = Counter32
_CSipStatsServerIntErrorIns_Object = MibScalar
cSipStatsServerIntErrorIns = _CSipStatsServerIntErrorIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 5, 1),
    _CSipStatsServerIntErrorIns_Type()
)
cSipStatsServerIntErrorIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsServerIntErrorIns.setStatus("current")
_CSipStatsServerIntErrorOuts_Type = Counter32
_CSipStatsServerIntErrorOuts_Object = MibScalar
cSipStatsServerIntErrorOuts = _CSipStatsServerIntErrorOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 5, 2),
    _CSipStatsServerIntErrorOuts_Type()
)
cSipStatsServerIntErrorOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsServerIntErrorOuts.setStatus("current")
_CSipStatsServerNotImplementedIns_Type = Counter32
_CSipStatsServerNotImplementedIns_Object = MibScalar
cSipStatsServerNotImplementedIns = _CSipStatsServerNotImplementedIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 5, 3),
    _CSipStatsServerNotImplementedIns_Type()
)
cSipStatsServerNotImplementedIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsServerNotImplementedIns.setStatus("current")
_CSipStatsServerNotImplementedOuts_Type = Counter32
_CSipStatsServerNotImplementedOuts_Object = MibScalar
cSipStatsServerNotImplementedOuts = _CSipStatsServerNotImplementedOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 5, 4),
    _CSipStatsServerNotImplementedOuts_Type()
)
cSipStatsServerNotImplementedOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsServerNotImplementedOuts.setStatus("current")
_CSipStatsServerBadGatewayIns_Type = Counter32
_CSipStatsServerBadGatewayIns_Object = MibScalar
cSipStatsServerBadGatewayIns = _CSipStatsServerBadGatewayIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 5, 5),
    _CSipStatsServerBadGatewayIns_Type()
)
cSipStatsServerBadGatewayIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsServerBadGatewayIns.setStatus("current")
_CSipStatsServerBadGatewayOuts_Type = Counter32
_CSipStatsServerBadGatewayOuts_Object = MibScalar
cSipStatsServerBadGatewayOuts = _CSipStatsServerBadGatewayOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 5, 6),
    _CSipStatsServerBadGatewayOuts_Type()
)
cSipStatsServerBadGatewayOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsServerBadGatewayOuts.setStatus("current")
_CSipStatsServerServiceUnavailIns_Type = Counter32
_CSipStatsServerServiceUnavailIns_Object = MibScalar
cSipStatsServerServiceUnavailIns = _CSipStatsServerServiceUnavailIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 5, 7),
    _CSipStatsServerServiceUnavailIns_Type()
)
cSipStatsServerServiceUnavailIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsServerServiceUnavailIns.setStatus("current")
_CSipStatsServerServiceUnavailOuts_Type = Counter32
_CSipStatsServerServiceUnavailOuts_Object = MibScalar
cSipStatsServerServiceUnavailOuts = _CSipStatsServerServiceUnavailOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 5, 8),
    _CSipStatsServerServiceUnavailOuts_Type()
)
cSipStatsServerServiceUnavailOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsServerServiceUnavailOuts.setStatus("current")
_CSipStatsServerGatewayTimeoutIns_Type = Counter32
_CSipStatsServerGatewayTimeoutIns_Object = MibScalar
cSipStatsServerGatewayTimeoutIns = _CSipStatsServerGatewayTimeoutIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 5, 9),
    _CSipStatsServerGatewayTimeoutIns_Type()
)
cSipStatsServerGatewayTimeoutIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsServerGatewayTimeoutIns.setStatus("current")
_CSipStatsServerGatewayTimeoutOuts_Type = Counter32
_CSipStatsServerGatewayTimeoutOuts_Object = MibScalar
cSipStatsServerGatewayTimeoutOuts = _CSipStatsServerGatewayTimeoutOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 5, 10),
    _CSipStatsServerGatewayTimeoutOuts_Type()
)
cSipStatsServerGatewayTimeoutOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsServerGatewayTimeoutOuts.setStatus("current")
_CSipStatsServerBadSipVersionIns_Type = Counter32
_CSipStatsServerBadSipVersionIns_Object = MibScalar
cSipStatsServerBadSipVersionIns = _CSipStatsServerBadSipVersionIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 5, 11),
    _CSipStatsServerBadSipVersionIns_Type()
)
cSipStatsServerBadSipVersionIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsServerBadSipVersionIns.setStatus("current")
_CSipStatsServerBadSipVersionOuts_Type = Counter32
_CSipStatsServerBadSipVersionOuts_Object = MibScalar
cSipStatsServerBadSipVersionOuts = _CSipStatsServerBadSipVersionOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 5, 12),
    _CSipStatsServerBadSipVersionOuts_Type()
)
cSipStatsServerBadSipVersionOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsServerBadSipVersionOuts.setStatus("current")
_CSipStatsServerPrecondFailureIns_Type = Counter32
_CSipStatsServerPrecondFailureIns_Object = MibScalar
cSipStatsServerPrecondFailureIns = _CSipStatsServerPrecondFailureIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 5, 13),
    _CSipStatsServerPrecondFailureIns_Type()
)
cSipStatsServerPrecondFailureIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsServerPrecondFailureIns.setStatus("current")
_CSipStatsServerPrecondFailureOuts_Type = Counter32
_CSipStatsServerPrecondFailureOuts_Object = MibScalar
cSipStatsServerPrecondFailureOuts = _CSipStatsServerPrecondFailureOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 5, 14),
    _CSipStatsServerPrecondFailureOuts_Type()
)
cSipStatsServerPrecondFailureOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsServerPrecondFailureOuts.setStatus("current")
_CSipStatsGlobalFail_ObjectIdentity = ObjectIdentity
cSipStatsGlobalFail = _CSipStatsGlobalFail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 6)
)
_CSipStatsGlobalBusyEverywhereIns_Type = Counter32
_CSipStatsGlobalBusyEverywhereIns_Object = MibScalar
cSipStatsGlobalBusyEverywhereIns = _CSipStatsGlobalBusyEverywhereIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 6, 1),
    _CSipStatsGlobalBusyEverywhereIns_Type()
)
cSipStatsGlobalBusyEverywhereIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsGlobalBusyEverywhereIns.setStatus("current")
_CSipStatsGlobalBusyEverywhereOuts_Type = Counter32
_CSipStatsGlobalBusyEverywhereOuts_Object = MibScalar
cSipStatsGlobalBusyEverywhereOuts = _CSipStatsGlobalBusyEverywhereOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 6, 2),
    _CSipStatsGlobalBusyEverywhereOuts_Type()
)
cSipStatsGlobalBusyEverywhereOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsGlobalBusyEverywhereOuts.setStatus("current")
_CSipStatsGlobalDeclineIns_Type = Counter32
_CSipStatsGlobalDeclineIns_Object = MibScalar
cSipStatsGlobalDeclineIns = _CSipStatsGlobalDeclineIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 6, 3),
    _CSipStatsGlobalDeclineIns_Type()
)
cSipStatsGlobalDeclineIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsGlobalDeclineIns.setStatus("current")
_CSipStatsGlobalDeclineOuts_Type = Counter32
_CSipStatsGlobalDeclineOuts_Object = MibScalar
cSipStatsGlobalDeclineOuts = _CSipStatsGlobalDeclineOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 6, 4),
    _CSipStatsGlobalDeclineOuts_Type()
)
cSipStatsGlobalDeclineOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsGlobalDeclineOuts.setStatus("current")
_CSipStatsGlobalNotAnywhereIns_Type = Counter32
_CSipStatsGlobalNotAnywhereIns_Object = MibScalar
cSipStatsGlobalNotAnywhereIns = _CSipStatsGlobalNotAnywhereIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 6, 5),
    _CSipStatsGlobalNotAnywhereIns_Type()
)
cSipStatsGlobalNotAnywhereIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsGlobalNotAnywhereIns.setStatus("current")
_CSipStatsGlobalNotAnywhereOuts_Type = Counter32
_CSipStatsGlobalNotAnywhereOuts_Object = MibScalar
cSipStatsGlobalNotAnywhereOuts = _CSipStatsGlobalNotAnywhereOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 6, 6),
    _CSipStatsGlobalNotAnywhereOuts_Type()
)
cSipStatsGlobalNotAnywhereOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsGlobalNotAnywhereOuts.setStatus("current")
_CSipStatsGlobalNotAcceptableIns_Type = Counter32
_CSipStatsGlobalNotAcceptableIns_Object = MibScalar
cSipStatsGlobalNotAcceptableIns = _CSipStatsGlobalNotAcceptableIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 6, 7),
    _CSipStatsGlobalNotAcceptableIns_Type()
)
cSipStatsGlobalNotAcceptableIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsGlobalNotAcceptableIns.setStatus("current")
_CSipStatsGlobalNotAcceptableOuts_Type = Counter32
_CSipStatsGlobalNotAcceptableOuts_Object = MibScalar
cSipStatsGlobalNotAcceptableOuts = _CSipStatsGlobalNotAcceptableOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 6, 8),
    _CSipStatsGlobalNotAcceptableOuts_Type()
)
cSipStatsGlobalNotAcceptableOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsGlobalNotAcceptableOuts.setStatus("current")
_CSipStatsTraffic_ObjectIdentity = ObjectIdentity
cSipStatsTraffic = _CSipStatsTraffic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 7)
)
_CSipStatsTrafficInviteIns_Type = Counter32
_CSipStatsTrafficInviteIns_Object = MibScalar
cSipStatsTrafficInviteIns = _CSipStatsTrafficInviteIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 7, 1),
    _CSipStatsTrafficInviteIns_Type()
)
cSipStatsTrafficInviteIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsTrafficInviteIns.setStatus("current")
_CSipStatsTrafficInviteOuts_Type = Counter32
_CSipStatsTrafficInviteOuts_Object = MibScalar
cSipStatsTrafficInviteOuts = _CSipStatsTrafficInviteOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 7, 2),
    _CSipStatsTrafficInviteOuts_Type()
)
cSipStatsTrafficInviteOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsTrafficInviteOuts.setStatus("current")
_CSipStatsTrafficAckIns_Type = Counter32
_CSipStatsTrafficAckIns_Object = MibScalar
cSipStatsTrafficAckIns = _CSipStatsTrafficAckIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 7, 3),
    _CSipStatsTrafficAckIns_Type()
)
cSipStatsTrafficAckIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsTrafficAckIns.setStatus("current")
_CSipStatsTrafficAckOuts_Type = Counter32
_CSipStatsTrafficAckOuts_Object = MibScalar
cSipStatsTrafficAckOuts = _CSipStatsTrafficAckOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 7, 4),
    _CSipStatsTrafficAckOuts_Type()
)
cSipStatsTrafficAckOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsTrafficAckOuts.setStatus("current")
_CSipStatsTrafficByeIns_Type = Counter32
_CSipStatsTrafficByeIns_Object = MibScalar
cSipStatsTrafficByeIns = _CSipStatsTrafficByeIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 7, 5),
    _CSipStatsTrafficByeIns_Type()
)
cSipStatsTrafficByeIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsTrafficByeIns.setStatus("current")
_CSipStatsTrafficByeOuts_Type = Counter32
_CSipStatsTrafficByeOuts_Object = MibScalar
cSipStatsTrafficByeOuts = _CSipStatsTrafficByeOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 7, 6),
    _CSipStatsTrafficByeOuts_Type()
)
cSipStatsTrafficByeOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsTrafficByeOuts.setStatus("current")
_CSipStatsTrafficCancelIns_Type = Counter32
_CSipStatsTrafficCancelIns_Object = MibScalar
cSipStatsTrafficCancelIns = _CSipStatsTrafficCancelIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 7, 7),
    _CSipStatsTrafficCancelIns_Type()
)
cSipStatsTrafficCancelIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsTrafficCancelIns.setStatus("current")
_CSipStatsTrafficCancelOuts_Type = Counter32
_CSipStatsTrafficCancelOuts_Object = MibScalar
cSipStatsTrafficCancelOuts = _CSipStatsTrafficCancelOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 7, 8),
    _CSipStatsTrafficCancelOuts_Type()
)
cSipStatsTrafficCancelOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsTrafficCancelOuts.setStatus("current")
_CSipStatsTrafficOptionsIns_Type = Counter32
_CSipStatsTrafficOptionsIns_Object = MibScalar
cSipStatsTrafficOptionsIns = _CSipStatsTrafficOptionsIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 7, 9),
    _CSipStatsTrafficOptionsIns_Type()
)
cSipStatsTrafficOptionsIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsTrafficOptionsIns.setStatus("current")
_CSipStatsTrafficOptionsOuts_Type = Counter32
_CSipStatsTrafficOptionsOuts_Object = MibScalar
cSipStatsTrafficOptionsOuts = _CSipStatsTrafficOptionsOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 7, 10),
    _CSipStatsTrafficOptionsOuts_Type()
)
cSipStatsTrafficOptionsOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsTrafficOptionsOuts.setStatus("current")
_CSipStatsTrafficRegisterIns_Type = Counter32
_CSipStatsTrafficRegisterIns_Object = MibScalar
cSipStatsTrafficRegisterIns = _CSipStatsTrafficRegisterIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 7, 11),
    _CSipStatsTrafficRegisterIns_Type()
)
cSipStatsTrafficRegisterIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsTrafficRegisterIns.setStatus("current")
_CSipStatsTrafficRegisterOuts_Type = Counter32
_CSipStatsTrafficRegisterOuts_Object = MibScalar
cSipStatsTrafficRegisterOuts = _CSipStatsTrafficRegisterOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 7, 12),
    _CSipStatsTrafficRegisterOuts_Type()
)
cSipStatsTrafficRegisterOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsTrafficRegisterOuts.setStatus("current")
_CSipStatsTrafficCometIns_Type = Counter32
_CSipStatsTrafficCometIns_Object = MibScalar
cSipStatsTrafficCometIns = _CSipStatsTrafficCometIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 7, 13),
    _CSipStatsTrafficCometIns_Type()
)
cSipStatsTrafficCometIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsTrafficCometIns.setStatus("current")
_CSipStatsTrafficCometOuts_Type = Counter32
_CSipStatsTrafficCometOuts_Object = MibScalar
cSipStatsTrafficCometOuts = _CSipStatsTrafficCometOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 7, 14),
    _CSipStatsTrafficCometOuts_Type()
)
cSipStatsTrafficCometOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsTrafficCometOuts.setStatus("current")
_CSipStatsTrafficPrackIns_Type = Counter32
_CSipStatsTrafficPrackIns_Object = MibScalar
cSipStatsTrafficPrackIns = _CSipStatsTrafficPrackIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 7, 15),
    _CSipStatsTrafficPrackIns_Type()
)
cSipStatsTrafficPrackIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsTrafficPrackIns.setStatus("current")
_CSipStatsTrafficPrackOuts_Type = Counter32
_CSipStatsTrafficPrackOuts_Object = MibScalar
cSipStatsTrafficPrackOuts = _CSipStatsTrafficPrackOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 7, 16),
    _CSipStatsTrafficPrackOuts_Type()
)
cSipStatsTrafficPrackOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsTrafficPrackOuts.setStatus("current")
_CSipStatsTrafficReferIns_Type = Counter32
_CSipStatsTrafficReferIns_Object = MibScalar
cSipStatsTrafficReferIns = _CSipStatsTrafficReferIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 7, 17),
    _CSipStatsTrafficReferIns_Type()
)
cSipStatsTrafficReferIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsTrafficReferIns.setStatus("current")
_CSipStatsTrafficReferOuts_Type = Counter32
_CSipStatsTrafficReferOuts_Object = MibScalar
cSipStatsTrafficReferOuts = _CSipStatsTrafficReferOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 7, 18),
    _CSipStatsTrafficReferOuts_Type()
)
cSipStatsTrafficReferOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsTrafficReferOuts.setStatus("current")
_CSipStatsTrafficNotifyIns_Type = Counter32
_CSipStatsTrafficNotifyIns_Object = MibScalar
cSipStatsTrafficNotifyIns = _CSipStatsTrafficNotifyIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 7, 19),
    _CSipStatsTrafficNotifyIns_Type()
)
cSipStatsTrafficNotifyIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsTrafficNotifyIns.setStatus("current")
_CSipStatsTrafficNotifyOuts_Type = Counter32
_CSipStatsTrafficNotifyOuts_Object = MibScalar
cSipStatsTrafficNotifyOuts = _CSipStatsTrafficNotifyOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 7, 20),
    _CSipStatsTrafficNotifyOuts_Type()
)
cSipStatsTrafficNotifyOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsTrafficNotifyOuts.setStatus("current")
_CSipStatsTrafficInfoIns_Type = Counter32
_CSipStatsTrafficInfoIns_Object = MibScalar
cSipStatsTrafficInfoIns = _CSipStatsTrafficInfoIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 7, 21),
    _CSipStatsTrafficInfoIns_Type()
)
cSipStatsTrafficInfoIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsTrafficInfoIns.setStatus("current")
_CSipStatsTrafficInfoOuts_Type = Counter32
_CSipStatsTrafficInfoOuts_Object = MibScalar
cSipStatsTrafficInfoOuts = _CSipStatsTrafficInfoOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 7, 22),
    _CSipStatsTrafficInfoOuts_Type()
)
cSipStatsTrafficInfoOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsTrafficInfoOuts.setStatus("current")
_CSipStatsTrafficSubscribeIns_Type = Counter32
_CSipStatsTrafficSubscribeIns_Object = MibScalar
cSipStatsTrafficSubscribeIns = _CSipStatsTrafficSubscribeIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 7, 23),
    _CSipStatsTrafficSubscribeIns_Type()
)
cSipStatsTrafficSubscribeIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsTrafficSubscribeIns.setStatus("current")
_CSipStatsTrafficSubscribeOuts_Type = Counter32
_CSipStatsTrafficSubscribeOuts_Object = MibScalar
cSipStatsTrafficSubscribeOuts = _CSipStatsTrafficSubscribeOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 7, 24),
    _CSipStatsTrafficSubscribeOuts_Type()
)
cSipStatsTrafficSubscribeOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsTrafficSubscribeOuts.setStatus("current")
_CSipStatsTrafficUpdateIns_Type = Counter32
_CSipStatsTrafficUpdateIns_Object = MibScalar
cSipStatsTrafficUpdateIns = _CSipStatsTrafficUpdateIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 7, 25),
    _CSipStatsTrafficUpdateIns_Type()
)
cSipStatsTrafficUpdateIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsTrafficUpdateIns.setStatus("current")
_CSipStatsTrafficUpdateOuts_Type = Counter32
_CSipStatsTrafficUpdateOuts_Object = MibScalar
cSipStatsTrafficUpdateOuts = _CSipStatsTrafficUpdateOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 7, 26),
    _CSipStatsTrafficUpdateOuts_Type()
)
cSipStatsTrafficUpdateOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsTrafficUpdateOuts.setStatus("current")
_CSipStatsRetry_ObjectIdentity = ObjectIdentity
cSipStatsRetry = _CSipStatsRetry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 8)
)
_CSipStatsRetryInvites_Type = Counter32
_CSipStatsRetryInvites_Object = MibScalar
cSipStatsRetryInvites = _CSipStatsRetryInvites_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 8, 1),
    _CSipStatsRetryInvites_Type()
)
cSipStatsRetryInvites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsRetryInvites.setStatus("current")
_CSipStatsRetryByes_Type = Counter32
_CSipStatsRetryByes_Object = MibScalar
cSipStatsRetryByes = _CSipStatsRetryByes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 8, 2),
    _CSipStatsRetryByes_Type()
)
cSipStatsRetryByes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsRetryByes.setStatus("current")
_CSipStatsRetryCancels_Type = Counter32
_CSipStatsRetryCancels_Object = MibScalar
cSipStatsRetryCancels = _CSipStatsRetryCancels_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 8, 3),
    _CSipStatsRetryCancels_Type()
)
cSipStatsRetryCancels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsRetryCancels.setStatus("current")
_CSipStatsRetryRegisters_Type = Counter32
_CSipStatsRetryRegisters_Object = MibScalar
cSipStatsRetryRegisters = _CSipStatsRetryRegisters_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 8, 4),
    _CSipStatsRetryRegisters_Type()
)
cSipStatsRetryRegisters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsRetryRegisters.setStatus("current")
_CSipStatsRetryResponses_Type = Counter32
_CSipStatsRetryResponses_Object = MibScalar
cSipStatsRetryResponses = _CSipStatsRetryResponses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 8, 5),
    _CSipStatsRetryResponses_Type()
)
cSipStatsRetryResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsRetryResponses.setStatus("current")
_CSipStatsRetryPracks_Type = Counter32
_CSipStatsRetryPracks_Object = MibScalar
cSipStatsRetryPracks = _CSipStatsRetryPracks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 8, 6),
    _CSipStatsRetryPracks_Type()
)
cSipStatsRetryPracks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsRetryPracks.setStatus("current")
_CSipStatsRetryComets_Type = Counter32
_CSipStatsRetryComets_Object = MibScalar
cSipStatsRetryComets = _CSipStatsRetryComets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 8, 7),
    _CSipStatsRetryComets_Type()
)
cSipStatsRetryComets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsRetryComets.setStatus("current")
_CSipStatsRetryReliable1xxRsps_Type = Counter32
_CSipStatsRetryReliable1xxRsps_Object = MibScalar
cSipStatsRetryReliable1xxRsps = _CSipStatsRetryReliable1xxRsps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 8, 8),
    _CSipStatsRetryReliable1xxRsps_Type()
)
cSipStatsRetryReliable1xxRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsRetryReliable1xxRsps.setStatus("current")
_CSipStatsRetryNotifys_Type = Counter32
_CSipStatsRetryNotifys_Object = MibScalar
cSipStatsRetryNotifys = _CSipStatsRetryNotifys_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 8, 9),
    _CSipStatsRetryNotifys_Type()
)
cSipStatsRetryNotifys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsRetryNotifys.setStatus("current")
_CSipStatsRetryRefers_Type = Counter32
_CSipStatsRetryRefers_Object = MibScalar
cSipStatsRetryRefers = _CSipStatsRetryRefers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 8, 10),
    _CSipStatsRetryRefers_Type()
)
cSipStatsRetryRefers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsRetryRefers.setStatus("current")
_CSipStatsRetryInfo_Type = Counter32
_CSipStatsRetryInfo_Object = MibScalar
cSipStatsRetryInfo = _CSipStatsRetryInfo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 8, 11),
    _CSipStatsRetryInfo_Type()
)
cSipStatsRetryInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsRetryInfo.setStatus("current")
_CSipStatsRetrySubscribe_Type = Counter32
_CSipStatsRetrySubscribe_Object = MibScalar
cSipStatsRetrySubscribe = _CSipStatsRetrySubscribe_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 8, 12),
    _CSipStatsRetrySubscribe_Type()
)
cSipStatsRetrySubscribe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsRetrySubscribe.setStatus("current")
_CSipStatsMisc_ObjectIdentity = ObjectIdentity
cSipStatsMisc = _CSipStatsMisc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 9)
)
_CSipStatsMisc3xxMappedTo4xxRsps_Type = Counter32
_CSipStatsMisc3xxMappedTo4xxRsps_Object = MibScalar
cSipStatsMisc3xxMappedTo4xxRsps = _CSipStatsMisc3xxMappedTo4xxRsps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 9, 1),
    _CSipStatsMisc3xxMappedTo4xxRsps_Type()
)
cSipStatsMisc3xxMappedTo4xxRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsMisc3xxMappedTo4xxRsps.setStatus("current")
_CSipStatsConnection_ObjectIdentity = ObjectIdentity
cSipStatsConnection = _CSipStatsConnection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 10)
)
_CSipStatsConnTCPSendFailures_Type = Counter32
_CSipStatsConnTCPSendFailures_Object = MibScalar
cSipStatsConnTCPSendFailures = _CSipStatsConnTCPSendFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 10, 1),
    _CSipStatsConnTCPSendFailures_Type()
)
cSipStatsConnTCPSendFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsConnTCPSendFailures.setStatus("current")
_CSipStatsConnUDPSendFailures_Type = Counter32
_CSipStatsConnUDPSendFailures_Object = MibScalar
cSipStatsConnUDPSendFailures = _CSipStatsConnUDPSendFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 10, 2),
    _CSipStatsConnUDPSendFailures_Type()
)
cSipStatsConnUDPSendFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsConnUDPSendFailures.setStatus("current")
_CSipStatsConnTCPRemoteClosures_Type = Counter32
_CSipStatsConnTCPRemoteClosures_Object = MibScalar
cSipStatsConnTCPRemoteClosures = _CSipStatsConnTCPRemoteClosures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 10, 3),
    _CSipStatsConnTCPRemoteClosures_Type()
)
cSipStatsConnTCPRemoteClosures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsConnTCPRemoteClosures.setStatus("current")
_CSipStatsConnUDPCreateFailures_Type = Counter32
_CSipStatsConnUDPCreateFailures_Object = MibScalar
cSipStatsConnUDPCreateFailures = _CSipStatsConnUDPCreateFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 10, 4),
    _CSipStatsConnUDPCreateFailures_Type()
)
cSipStatsConnUDPCreateFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsConnUDPCreateFailures.setStatus("current")
_CSipStatsConnTCPCreateFailures_Type = Counter32
_CSipStatsConnTCPCreateFailures_Object = MibScalar
cSipStatsConnTCPCreateFailures = _CSipStatsConnTCPCreateFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 10, 5),
    _CSipStatsConnTCPCreateFailures_Type()
)
cSipStatsConnTCPCreateFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsConnTCPCreateFailures.setStatus("current")
_CSipStatsConnUDPInactiveTimeouts_Type = Counter32
_CSipStatsConnUDPInactiveTimeouts_Object = MibScalar
cSipStatsConnUDPInactiveTimeouts = _CSipStatsConnUDPInactiveTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 10, 6),
    _CSipStatsConnUDPInactiveTimeouts_Type()
)
cSipStatsConnUDPInactiveTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsConnUDPInactiveTimeouts.setStatus("current")
_CSipStatsConnTCPInactiveTimeouts_Type = Counter32
_CSipStatsConnTCPInactiveTimeouts_Object = MibScalar
cSipStatsConnTCPInactiveTimeouts = _CSipStatsConnTCPInactiveTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 10, 7),
    _CSipStatsConnTCPInactiveTimeouts_Type()
)
cSipStatsConnTCPInactiveTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsConnTCPInactiveTimeouts.setStatus("current")
_CSipStatsActiveUDPConnections_Type = Gauge32
_CSipStatsActiveUDPConnections_Object = MibScalar
cSipStatsActiveUDPConnections = _CSipStatsActiveUDPConnections_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 10, 8),
    _CSipStatsActiveUDPConnections_Type()
)
cSipStatsActiveUDPConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsActiveUDPConnections.setStatus("current")
_CSipStatsActiveTCPConnections_Type = Gauge32
_CSipStatsActiveTCPConnections_Object = MibScalar
cSipStatsActiveTCPConnections = _CSipStatsActiveTCPConnections_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 1, 2, 10, 9),
    _CSipStatsActiveTCPConnections_Type()
)
cSipStatsActiveTCPConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipStatsActiveTCPConnections.setStatus("current")
_CiscoSipUaMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
ciscoSipUaMIBNotificationPrefix = _CiscoSipUaMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 2)
)
if mibBuilder.loadTexts:
    ciscoSipUaMIBNotificationPrefix.setStatus("deprecated")
_CiscoSipUaMIBNotifications_ObjectIdentity = ObjectIdentity
ciscoSipUaMIBNotifications = _CiscoSipUaMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 2, 0)
)
if mibBuilder.loadTexts:
    ciscoSipUaMIBNotifications.setStatus("deprecated")
_CiscoSipUaMIBConformance_ObjectIdentity = ObjectIdentity
ciscoSipUaMIBConformance = _CiscoSipUaMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 3)
)
_CiscoSipUaMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoSipUaMIBCompliances = _CiscoSipUaMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 3, 1)
)
_CiscoSipUaMIBGroups_ObjectIdentity = ObjectIdentity
ciscoSipUaMIBGroups = _CiscoSipUaMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 3, 2)
)

# Managed Objects groups

ciscoSipBaseConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 3, 2, 1)
)
ciscoSipBaseConfigGroup.setObjects(
      *(("CISCO-SIP-UA-MIB", "cSipCfgUserLocationServerAddr"),
        ("CISCO-SIP-UA-MIB", "cSipCfgTransport"),
        ("CISCO-SIP-UA-MIB", "cSipCfgVersion"))
)
if mibBuilder.loadTexts:
    ciscoSipBaseConfigGroup.setStatus("deprecated")

ciscoSipTimerConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 3, 2, 2)
)
ciscoSipTimerConfigGroup.setObjects(
      *(("CISCO-SIP-UA-MIB", "cSipCfgTimerTrying"),
        ("CISCO-SIP-UA-MIB", "cSipCfgTimerExpires"),
        ("CISCO-SIP-UA-MIB", "cSipCfgTimerConnect"),
        ("CISCO-SIP-UA-MIB", "cSipCfgTimerDisconnect"))
)
if mibBuilder.loadTexts:
    ciscoSipTimerConfigGroup.setStatus("deprecated")

ciscoSipRetryConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 3, 2, 3)
)
ciscoSipRetryConfigGroup.setObjects(
      *(("CISCO-SIP-UA-MIB", "cSipCfgRetryInvite"),
        ("CISCO-SIP-UA-MIB", "cSipCfgRetryBye"),
        ("CISCO-SIP-UA-MIB", "cSipCfgRetryCancel"),
        ("CISCO-SIP-UA-MIB", "cSipCfgRetryRegister"),
        ("CISCO-SIP-UA-MIB", "cSipCfgRetryResponse"))
)
if mibBuilder.loadTexts:
    ciscoSipRetryConfigGroup.setStatus("deprecated")

ciscoSipStatsInfoStatusCodesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 3, 2, 4)
)
ciscoSipStatsInfoStatusCodesGroup.setObjects(
      *(("CISCO-SIP-UA-MIB", "cSipStatsInfoTryingIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsInfoTryingOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsInfoRingingIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsInfoRingingOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsInfoForwardedIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsInfoForwardedOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsInfoQueuedIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsInfoQueuedOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsInfoSessionProgIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsInfoSessionProgOuts"))
)
if mibBuilder.loadTexts:
    ciscoSipStatsInfoStatusCodesGroup.setStatus("current")

ciscoSipStatsSuccessStatusCodesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 3, 2, 5)
)
ciscoSipStatsSuccessStatusCodesGroup.setObjects(
      *(("CISCO-SIP-UA-MIB", "cSipStatsSuccessOkIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsSuccessOkOuts"))
)
if mibBuilder.loadTexts:
    ciscoSipStatsSuccessStatusCodesGroup.setStatus("deprecated")

ciscoSipStatsRedirStatusCodesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 3, 2, 6)
)
ciscoSipStatsRedirStatusCodesGroup.setObjects(
      *(("CISCO-SIP-UA-MIB", "cSipStatsRedirMultipleChoices"),
        ("CISCO-SIP-UA-MIB", "cSipStatsRedirMovedPerms"),
        ("CISCO-SIP-UA-MIB", "cSipStatsRedirMovedTemps"),
        ("CISCO-SIP-UA-MIB", "cSipStatsRedirSeeOthers"),
        ("CISCO-SIP-UA-MIB", "cSipStatsRedirUseProxys"),
        ("CISCO-SIP-UA-MIB", "cSipStatsRedirAltServices"))
)
if mibBuilder.loadTexts:
    ciscoSipStatsRedirStatusCodesGroup.setStatus("obsolete")

ciscoSipStatsClientStatusCodesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 3, 2, 7)
)
ciscoSipStatsClientStatusCodesGroup.setObjects(
      *(("CISCO-SIP-UA-MIB", "cSipStatsClientBadRequestIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientBadRequestOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientUnauthorizedIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientUnauthorizedOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientPaymentReqdIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientPaymentReqdOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientForbiddenIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientForbiddenOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientNotFoundIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientNotFoundOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientMethNotAllowedIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientMethNotAllowedOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientNotAcceptableIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientNotAcceptableOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientProxyAuthReqdIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientProxyAuthReqdOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientReqTimeoutIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientReqTimeoutOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientConflictIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientConflictOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientGoneIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientGoneOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientLengthRequiredIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientLengthRequiredOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientReqEntTooLargeIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientReqEntTooLargeOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientReqURITooLargeIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientReqURITooLargeOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientNoSupMediaTypeIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientNoSupMediaTypeOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientBadExtensionIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientBadExtensionOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientTempNotAvailIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientTempNotAvailOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientCallLegNoExistIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientCallLegNoExistOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientLoopDetectedIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientLoopDetectedOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientTooManyHopsIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientTooManyHopsOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientAddrIncompleteIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientAddrIncompleteOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientAmbiguousIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientAmbiguousOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientBusyHereIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientBusyHereOuts"))
)
if mibBuilder.loadTexts:
    ciscoSipStatsClientStatusCodesGroup.setStatus("obsolete")

ciscoSipStatsServerStatusCodesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 3, 2, 8)
)
ciscoSipStatsServerStatusCodesGroup.setObjects(
      *(("CISCO-SIP-UA-MIB", "cSipStatsServerIntErrorIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsServerIntErrorOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsServerNotImplementedIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsServerNotImplementedOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsServerBadGatewayIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsServerBadGatewayOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsServerServiceUnavailIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsServerServiceUnavailOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsServerGatewayTimeoutIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsServerGatewayTimeoutOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsServerBadSipVersionIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsServerBadSipVersionOuts"))
)
if mibBuilder.loadTexts:
    ciscoSipStatsServerStatusCodesGroup.setStatus("deprecated")

ciscoSipStatsGlobalStatusCodesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 3, 2, 9)
)
ciscoSipStatsGlobalStatusCodesGroup.setObjects(
      *(("CISCO-SIP-UA-MIB", "cSipStatsGlobalBusyEverywhereIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsGlobalBusyEverywhereOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsGlobalDeclineIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsGlobalDeclineOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsGlobalNotAnywhereIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsGlobalNotAnywhereOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsGlobalNotAcceptableIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsGlobalNotAcceptableOuts"))
)
if mibBuilder.loadTexts:
    ciscoSipStatsGlobalStatusCodesGroup.setStatus("current")

ciscoSipTrafficStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 3, 2, 10)
)
ciscoSipTrafficStatsGroup.setObjects(
      *(("CISCO-SIP-UA-MIB", "cSipStatsTrafficInviteIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsTrafficInviteOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsTrafficAckIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsTrafficAckOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsTrafficByeIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsTrafficByeOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsTrafficCancelIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsTrafficCancelOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsTrafficOptionsIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsTrafficOptionsOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsTrafficRegisterIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsTrafficRegisterOuts"))
)
if mibBuilder.loadTexts:
    ciscoSipTrafficStatsGroup.setStatus("deprecated")

ciscoSipRetryStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 3, 2, 11)
)
ciscoSipRetryStatsGroup.setObjects(
      *(("CISCO-SIP-UA-MIB", "cSipStatsRetryInvites"),
        ("CISCO-SIP-UA-MIB", "cSipStatsRetryByes"),
        ("CISCO-SIP-UA-MIB", "cSipStatsRetryCancels"),
        ("CISCO-SIP-UA-MIB", "cSipStatsRetryRegisters"),
        ("CISCO-SIP-UA-MIB", "cSipStatsRetryResponses"))
)
if mibBuilder.loadTexts:
    ciscoSipRetryStatsGroup.setStatus("deprecated")

ciscoSipBaseConfigGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 3, 2, 12)
)
ciscoSipBaseConfigGroupRev1.setObjects(
      *(("CISCO-SIP-UA-MIB", "cSipCfgUserLocationServerAddr"),
        ("CISCO-SIP-UA-MIB", "cSipCfgTransport"),
        ("CISCO-SIP-UA-MIB", "cSipCfgVersion"),
        ("CISCO-SIP-UA-MIB", "cSipCfgMaxForwards"))
)
if mibBuilder.loadTexts:
    ciscoSipBaseConfigGroupRev1.setStatus("deprecated")

ciscoSipTimerConfigGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 3, 2, 13)
)
ciscoSipTimerConfigGroupRev1.setObjects(
      *(("CISCO-SIP-UA-MIB", "cSipCfgTimerTrying"),
        ("CISCO-SIP-UA-MIB", "cSipCfgTimerExpires"),
        ("CISCO-SIP-UA-MIB", "cSipCfgTimerConnect"),
        ("CISCO-SIP-UA-MIB", "cSipCfgTimerDisconnect"),
        ("CISCO-SIP-UA-MIB", "cSipCfgTimerPrack"),
        ("CISCO-SIP-UA-MIB", "cSipCfgTimerComet"),
        ("CISCO-SIP-UA-MIB", "cSipCfgTimerReliableRsp"))
)
if mibBuilder.loadTexts:
    ciscoSipTimerConfigGroupRev1.setStatus("deprecated")

ciscoSipRetryConfigGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 3, 2, 14)
)
ciscoSipRetryConfigGroupRev1.setObjects(
      *(("CISCO-SIP-UA-MIB", "cSipCfgRetryInvite"),
        ("CISCO-SIP-UA-MIB", "cSipCfgRetryBye"),
        ("CISCO-SIP-UA-MIB", "cSipCfgRetryCancel"),
        ("CISCO-SIP-UA-MIB", "cSipCfgRetryRegister"),
        ("CISCO-SIP-UA-MIB", "cSipCfgRetryResponse"),
        ("CISCO-SIP-UA-MIB", "cSipCfgRetryPrack"),
        ("CISCO-SIP-UA-MIB", "cSipCfgRetryComet"),
        ("CISCO-SIP-UA-MIB", "cSipCfgRetryReliableRsp"))
)
if mibBuilder.loadTexts:
    ciscoSipRetryConfigGroupRev1.setStatus("deprecated")

ciscoSipTrafficStatsGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 3, 2, 15)
)
ciscoSipTrafficStatsGroupRev1.setObjects(
      *(("CISCO-SIP-UA-MIB", "cSipStatsTrafficInviteIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsTrafficInviteOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsTrafficAckIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsTrafficAckOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsTrafficByeIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsTrafficByeOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsTrafficCancelIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsTrafficCancelOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsTrafficOptionsIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsTrafficOptionsOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsTrafficRegisterIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsTrafficRegisterOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsTrafficCometIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsTrafficCometOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsTrafficPrackIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsTrafficPrackOuts"))
)
if mibBuilder.loadTexts:
    ciscoSipTrafficStatsGroupRev1.setStatus("deprecated")

ciscoSipStatsServerStatusCodesGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 3, 2, 16)
)
ciscoSipStatsServerStatusCodesGroupRev1.setObjects(
      *(("CISCO-SIP-UA-MIB", "cSipStatsServerIntErrorIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsServerIntErrorOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsServerNotImplementedIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsServerNotImplementedOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsServerBadGatewayIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsServerBadGatewayOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsServerServiceUnavailIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsServerServiceUnavailOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsServerGatewayTimeoutIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsServerGatewayTimeoutOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsServerBadSipVersionIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsServerBadSipVersionOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsServerPrecondFailureIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsServerPrecondFailureOuts"))
)
if mibBuilder.loadTexts:
    ciscoSipStatsServerStatusCodesGroupRev1.setStatus("current")

ciscoSipRetryStatsGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 3, 2, 17)
)
ciscoSipRetryStatsGroupRev1.setObjects(
      *(("CISCO-SIP-UA-MIB", "cSipStatsRetryInvites"),
        ("CISCO-SIP-UA-MIB", "cSipStatsRetryByes"),
        ("CISCO-SIP-UA-MIB", "cSipStatsRetryCancels"),
        ("CISCO-SIP-UA-MIB", "cSipStatsRetryRegisters"),
        ("CISCO-SIP-UA-MIB", "cSipStatsRetryResponses"),
        ("CISCO-SIP-UA-MIB", "cSipStatsRetryPracks"),
        ("CISCO-SIP-UA-MIB", "cSipStatsRetryComets"),
        ("CISCO-SIP-UA-MIB", "cSipStatsRetryReliable1xxRsps"))
)
if mibBuilder.loadTexts:
    ciscoSipRetryStatsGroupRev1.setStatus("deprecated")

ciscoSipStatsClientStatusCodesGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 3, 2, 18)
)
ciscoSipStatsClientStatusCodesGroupRev1.setObjects(
      *(("CISCO-SIP-UA-MIB", "cSipStatsClientBadRequestIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientBadRequestOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientUnauthorizedIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientUnauthorizedOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientPaymentReqdIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientPaymentReqdOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientForbiddenIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientForbiddenOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientNotFoundIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientNotFoundOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientMethNotAllowedIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientMethNotAllowedOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientNotAcceptableIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientNotAcceptableOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientProxyAuthReqdIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientProxyAuthReqdOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientReqTimeoutIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientReqTimeoutOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientConflictIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientConflictOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientGoneIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientGoneOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientLengthRequiredIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientLengthRequiredOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientReqEntTooLargeIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientReqEntTooLargeOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientReqURITooLargeIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientReqURITooLargeOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientNoSupMediaTypeIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientNoSupMediaTypeOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientBadExtensionIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientBadExtensionOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientTempNotAvailIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientTempNotAvailOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientCallLegNoExistIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientCallLegNoExistOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientLoopDetectedIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientLoopDetectedOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientTooManyHopsIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientTooManyHopsOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientAddrIncompleteIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientAddrIncompleteOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientAmbiguousIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientAmbiguousOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientBusyHereIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientBusyHereOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientReqTermIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientReqTermOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientNoAcceptHereIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientNoAcceptHereOuts"))
)
if mibBuilder.loadTexts:
    ciscoSipStatsClientStatusCodesGroupRev1.setStatus("obsolete")

ciscoSipCfgPeerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 3, 2, 19)
)
ciscoSipCfgPeerGroup.setObjects(
      *(("CISCO-SIP-UA-MIB", "cSipCfgPeerOutSessionTransport"),
        ("CISCO-SIP-UA-MIB", "cSipCfgPeerReliable1xxRspStr"),
        ("CISCO-SIP-UA-MIB", "cSipCfgPeerReliable1xxRspHdr"),
        ("CISCO-SIP-UA-MIB", "cSipCfgPeerUrlType"),
        ("CISCO-SIP-UA-MIB", "cSipCfgOutSessionTransport"),
        ("CISCO-SIP-UA-MIB", "cSipCfgReliable1xxRspStr"),
        ("CISCO-SIP-UA-MIB", "cSipCfgReliable1xxRspHdr"),
        ("CISCO-SIP-UA-MIB", "cSipCfgUrlType"))
)
if mibBuilder.loadTexts:
    ciscoSipCfgPeerGroup.setStatus("deprecated")

ciscoSipBaseConfigGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 3, 2, 20)
)
ciscoSipBaseConfigGroupRev2.setObjects(
      *(("CISCO-SIP-UA-MIB", "cSipCfgUserLocationServerAddr"),
        ("CISCO-SIP-UA-MIB", "cSipCfgTransport"),
        ("CISCO-SIP-UA-MIB", "cSipCfgVersion"),
        ("CISCO-SIP-UA-MIB", "cSipCfgMaxForwards"),
        ("CISCO-SIP-UA-MIB", "cSipCfgBindSrcAddrInterface"),
        ("CISCO-SIP-UA-MIB", "cSipCfgBindSrcAddrScope"),
        ("CISCO-SIP-UA-MIB", "cSipCfgDnsSrvQueryStringFormat"))
)
if mibBuilder.loadTexts:
    ciscoSipBaseConfigGroupRev2.setStatus("deprecated")

ciscoSipStatusCauseMapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 3, 2, 21)
)
ciscoSipStatusCauseMapGroup.setObjects(
      *(("CISCO-SIP-UA-MIB", "cSipCfgPstnCause"),
        ("CISCO-SIP-UA-MIB", "cSipCfgStatusCauseStoreStatus"),
        ("CISCO-SIP-UA-MIB", "cSipCfgStatusCode"),
        ("CISCO-SIP-UA-MIB", "cSipCfgCauseStatusStoreStatus"))
)
if mibBuilder.loadTexts:
    ciscoSipStatusCauseMapGroup.setStatus("current")

ciscoSipTrafficStatsGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 3, 2, 22)
)
ciscoSipTrafficStatsGroupRev2.setObjects(
      *(("CISCO-SIP-UA-MIB", "cSipStatsTrafficInviteIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsTrafficInviteOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsTrafficAckIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsTrafficAckOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsTrafficByeIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsTrafficByeOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsTrafficCancelIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsTrafficCancelOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsTrafficOptionsIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsTrafficOptionsOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsTrafficRegisterIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsTrafficRegisterOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsTrafficCometIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsTrafficCometOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsTrafficPrackIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsTrafficPrackOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsTrafficReferIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsTrafficReferOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsTrafficNotifyIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsTrafficNotifyOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsTrafficInfoIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsTrafficInfoOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsTrafficSubscribeIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsTrafficSubscribeOuts"))
)
if mibBuilder.loadTexts:
    ciscoSipTrafficStatsGroupRev2.setStatus("deprecated")

ciscoSipStatsSuccessStatusCodesGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 3, 2, 23)
)
ciscoSipStatsSuccessStatusCodesGroupRev1.setObjects(
      *(("CISCO-SIP-UA-MIB", "cSipStatsSuccessOkIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsSuccessOkOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsSuccessAcceptedIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsSuccessAcceptedOuts"))
)
if mibBuilder.loadTexts:
    ciscoSipStatsSuccessStatusCodesGroupRev1.setStatus("deprecated")

ciscoSipTimerConfigGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 3, 2, 24)
)
ciscoSipTimerConfigGroupRev2.setObjects(
      *(("CISCO-SIP-UA-MIB", "cSipCfgTimerTrying"),
        ("CISCO-SIP-UA-MIB", "cSipCfgTimerExpires"),
        ("CISCO-SIP-UA-MIB", "cSipCfgTimerConnect"),
        ("CISCO-SIP-UA-MIB", "cSipCfgTimerDisconnect"),
        ("CISCO-SIP-UA-MIB", "cSipCfgTimerPrack"),
        ("CISCO-SIP-UA-MIB", "cSipCfgTimerComet"),
        ("CISCO-SIP-UA-MIB", "cSipCfgTimerReliableRsp"),
        ("CISCO-SIP-UA-MIB", "cSipCfgTimerNotify"))
)
if mibBuilder.loadTexts:
    ciscoSipTimerConfigGroupRev2.setStatus("deprecated")

ciscoSipRetryConfigGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 3, 2, 25)
)
ciscoSipRetryConfigGroupRev2.setObjects(
      *(("CISCO-SIP-UA-MIB", "cSipCfgRetryInvite"),
        ("CISCO-SIP-UA-MIB", "cSipCfgRetryBye"),
        ("CISCO-SIP-UA-MIB", "cSipCfgRetryCancel"),
        ("CISCO-SIP-UA-MIB", "cSipCfgRetryRegister"),
        ("CISCO-SIP-UA-MIB", "cSipCfgRetryResponse"),
        ("CISCO-SIP-UA-MIB", "cSipCfgRetryPrack"),
        ("CISCO-SIP-UA-MIB", "cSipCfgRetryComet"),
        ("CISCO-SIP-UA-MIB", "cSipCfgRetryReliableRsp"),
        ("CISCO-SIP-UA-MIB", "cSipCfgRetryNotify"))
)
if mibBuilder.loadTexts:
    ciscoSipRetryConfigGroupRev2.setStatus("deprecated")

ciscoSipRetryStatsGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 3, 2, 26)
)
ciscoSipRetryStatsGroupRev2.setObjects(
      *(("CISCO-SIP-UA-MIB", "cSipStatsRetryInvites"),
        ("CISCO-SIP-UA-MIB", "cSipStatsRetryByes"),
        ("CISCO-SIP-UA-MIB", "cSipStatsRetryCancels"),
        ("CISCO-SIP-UA-MIB", "cSipStatsRetryRegisters"),
        ("CISCO-SIP-UA-MIB", "cSipStatsRetryResponses"),
        ("CISCO-SIP-UA-MIB", "cSipStatsRetryPracks"),
        ("CISCO-SIP-UA-MIB", "cSipStatsRetryComets"),
        ("CISCO-SIP-UA-MIB", "cSipStatsRetryReliable1xxRsps"),
        ("CISCO-SIP-UA-MIB", "cSipStatsRetryNotifys"))
)
if mibBuilder.loadTexts:
    ciscoSipRetryStatsGroupRev2.setStatus("deprecated")

ciscoSipCfgAaaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 3, 2, 27)
)
ciscoSipCfgAaaGroup.setObjects(
    ("CISCO-SIP-UA-MIB", "cSipCfgAaaUsername")
)
if mibBuilder.loadTexts:
    ciscoSipCfgAaaGroup.setStatus("current")

ciscoSipStatsClientStatusCodesGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 3, 2, 28)
)
ciscoSipStatsClientStatusCodesGroupRev2.setObjects(
      *(("CISCO-SIP-UA-MIB", "cSipStatsClientBadRequestIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientBadRequestOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientUnauthorizedIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientUnauthorizedOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientPaymentReqdIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientPaymentReqdOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientForbiddenIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientForbiddenOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientNotFoundIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientNotFoundOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientMethNotAllowedIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientMethNotAllowedOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientNotAcceptableIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientNotAcceptableOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientProxyAuthReqdIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientProxyAuthReqdOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientReqTimeoutIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientReqTimeoutOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientConflictIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientConflictOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientGoneIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientGoneOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientReqEntTooLargeIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientReqEntTooLargeOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientReqURITooLargeIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientReqURITooLargeOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientNoSupMediaTypeIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientNoSupMediaTypeOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientBadExtensionIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientBadExtensionOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientTempNotAvailIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientTempNotAvailOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientCallLegNoExistIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientCallLegNoExistOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientLoopDetectedIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientLoopDetectedOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientTooManyHopsIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientTooManyHopsOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientAddrIncompleteIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientAddrIncompleteOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientAmbiguousIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientAmbiguousOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientBusyHereIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientBusyHereOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientReqTermIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientReqTermOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientNoAcceptHereIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientNoAcceptHereOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientBadEventIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientBadEventOuts"))
)
if mibBuilder.loadTexts:
    ciscoSipStatsClientStatusCodesGroupRev2.setStatus("deprecated")

ciscoSipStatsRedirStatusCodesGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 3, 2, 29)
)
ciscoSipStatsRedirStatusCodesGroupRev1.setObjects(
      *(("CISCO-SIP-UA-MIB", "cSipStatsRedirMultipleChoices"),
        ("CISCO-SIP-UA-MIB", "cSipStatsRedirMovedPerms"),
        ("CISCO-SIP-UA-MIB", "cSipStatsRedirMovedTemps"),
        ("CISCO-SIP-UA-MIB", "cSipStatsRedirUseProxys"),
        ("CISCO-SIP-UA-MIB", "cSipStatsRedirAltServices"))
)
if mibBuilder.loadTexts:
    ciscoSipStatsRedirStatusCodesGroupRev1.setStatus("deprecated")

ciscoSipTimerConfigGroupRev3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 3, 2, 30)
)
ciscoSipTimerConfigGroupRev3.setObjects(
      *(("CISCO-SIP-UA-MIB", "cSipCfgTimerTrying"),
        ("CISCO-SIP-UA-MIB", "cSipCfgTimerExpires"),
        ("CISCO-SIP-UA-MIB", "cSipCfgTimerConnect"),
        ("CISCO-SIP-UA-MIB", "cSipCfgTimerDisconnect"),
        ("CISCO-SIP-UA-MIB", "cSipCfgTimerPrack"),
        ("CISCO-SIP-UA-MIB", "cSipCfgTimerComet"),
        ("CISCO-SIP-UA-MIB", "cSipCfgTimerReliableRsp"),
        ("CISCO-SIP-UA-MIB", "cSipCfgTimerNotify"),
        ("CISCO-SIP-UA-MIB", "cSipCfgTimerRefer"))
)
if mibBuilder.loadTexts:
    ciscoSipTimerConfigGroupRev3.setStatus("deprecated")

ciscoSipRetryConfigGroupRev3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 3, 2, 31)
)
ciscoSipRetryConfigGroupRev3.setObjects(
      *(("CISCO-SIP-UA-MIB", "cSipCfgRetryInvite"),
        ("CISCO-SIP-UA-MIB", "cSipCfgRetryBye"),
        ("CISCO-SIP-UA-MIB", "cSipCfgRetryCancel"),
        ("CISCO-SIP-UA-MIB", "cSipCfgRetryRegister"),
        ("CISCO-SIP-UA-MIB", "cSipCfgRetryResponse"),
        ("CISCO-SIP-UA-MIB", "cSipCfgRetryPrack"),
        ("CISCO-SIP-UA-MIB", "cSipCfgRetryComet"),
        ("CISCO-SIP-UA-MIB", "cSipCfgRetryReliableRsp"),
        ("CISCO-SIP-UA-MIB", "cSipCfgRetryNotify"),
        ("CISCO-SIP-UA-MIB", "cSipCfgRetryRefer"))
)
if mibBuilder.loadTexts:
    ciscoSipRetryConfigGroupRev3.setStatus("deprecated")

ciscoSipRetryStatsGroupRev3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 3, 2, 32)
)
ciscoSipRetryStatsGroupRev3.setObjects(
      *(("CISCO-SIP-UA-MIB", "cSipStatsRetryInvites"),
        ("CISCO-SIP-UA-MIB", "cSipStatsRetryByes"),
        ("CISCO-SIP-UA-MIB", "cSipStatsRetryCancels"),
        ("CISCO-SIP-UA-MIB", "cSipStatsRetryRegisters"),
        ("CISCO-SIP-UA-MIB", "cSipStatsRetryResponses"),
        ("CISCO-SIP-UA-MIB", "cSipStatsRetryPracks"),
        ("CISCO-SIP-UA-MIB", "cSipStatsRetryComets"),
        ("CISCO-SIP-UA-MIB", "cSipStatsRetryReliable1xxRsps"),
        ("CISCO-SIP-UA-MIB", "cSipStatsRetryNotifys"),
        ("CISCO-SIP-UA-MIB", "cSipStatsRetryRefers"))
)
if mibBuilder.loadTexts:
    ciscoSipRetryStatsGroupRev3.setStatus("deprecated")

ciscoSipStatsSuccessStatusCodesGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 3, 2, 33)
)
ciscoSipStatsSuccessStatusCodesGroupRev2.setObjects(
      *(("CISCO-SIP-UA-MIB", "cSipStatsSuccessAcceptedIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsSuccessAcceptedOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsSuccessOkInbounds"),
        ("CISCO-SIP-UA-MIB", "cSipStatsSuccessOkOutbounds"))
)
if mibBuilder.loadTexts:
    ciscoSipStatsSuccessStatusCodesGroupRev2.setStatus("current")

ciscoSipBaseConfigGroupRev3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 3, 2, 34)
)
ciscoSipBaseConfigGroupRev3.setObjects(
      *(("CISCO-SIP-UA-MIB", "cSipCfgUserLocationServerAddr"),
        ("CISCO-SIP-UA-MIB", "cSipCfgTransport"),
        ("CISCO-SIP-UA-MIB", "cSipCfgVersion"))
)
if mibBuilder.loadTexts:
    ciscoSipBaseConfigGroupRev3.setStatus("current")

ciscoSipStatsClientStatusCodesGroupRev3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 3, 2, 35)
)
ciscoSipStatsClientStatusCodesGroupRev3.setObjects(
      *(("CISCO-SIP-UA-MIB", "cSipStatsClientBadRequestIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientBadRequestOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientUnauthorizedIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientUnauthorizedOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientPaymentReqdIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientPaymentReqdOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientForbiddenIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientForbiddenOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientNotFoundIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientNotFoundOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientMethNotAllowedIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientMethNotAllowedOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientNotAcceptableIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientNotAcceptableOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientProxyAuthReqdIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientProxyAuthReqdOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientReqTimeoutIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientReqTimeoutOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientConflictIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientConflictOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientGoneIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientGoneOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientReqEntTooLargeIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientReqEntTooLargeOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientReqURITooLargeIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientReqURITooLargeOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientNoSupMediaTypeIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientNoSupMediaTypeOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientBadExtensionIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientBadExtensionOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientTempNotAvailIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientTempNotAvailOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientCallLegNoExistIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientCallLegNoExistOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientLoopDetectedIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientLoopDetectedOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientTooManyHopsIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientTooManyHopsOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientAddrIncompleteIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientAddrIncompleteOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientAmbiguousIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientAmbiguousOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientBusyHereIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientBusyHereOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientReqTermIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientReqTermOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientNoAcceptHereIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientNoAcceptHereOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientBadEventIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientBadEventOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientSTTooSmallIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientSTTooSmallOuts"))
)
if mibBuilder.loadTexts:
    ciscoSipStatsClientStatusCodesGroupRev3.setStatus("deprecated")

ciscoSipStatsMiscGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 3, 2, 36)
)
ciscoSipStatsMiscGroup.setObjects(
    ("CISCO-SIP-UA-MIB", "cSipStatsMisc3xxMappedTo4xxRsps")
)
if mibBuilder.loadTexts:
    ciscoSipStatsMiscGroup.setStatus("current")

ciscoSipBaseIOSConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 3, 2, 37)
)
ciscoSipBaseIOSConfigGroup.setObjects(
      *(("CISCO-SIP-UA-MIB", "cSipCfgMaxForwards"),
        ("CISCO-SIP-UA-MIB", "cSipCfgBindSrcAddrInterface"),
        ("CISCO-SIP-UA-MIB", "cSipCfgBindSrcAddrScope"),
        ("CISCO-SIP-UA-MIB", "cSipCfgDnsSrvQueryStringFormat"),
        ("CISCO-SIP-UA-MIB", "cSipCfgRedirectionDisabled"),
        ("CISCO-SIP-UA-MIB", "cSipCfgTimerSessionTimer"),
        ("CISCO-SIP-UA-MIB", "cSipCfgEarlyMediaCutThruDisabled"),
        ("CISCO-SIP-UA-MIB", "cSipCfgSymNatEnabled"),
        ("CISCO-SIP-UA-MIB", "cSipCfgSymNatDirectionRole"))
)
if mibBuilder.loadTexts:
    ciscoSipBaseIOSConfigGroup.setStatus("deprecated")

ciscoSipTrafficStatsGroupRev3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 3, 2, 38)
)
ciscoSipTrafficStatsGroupRev3.setObjects(
      *(("CISCO-SIP-UA-MIB", "cSipStatsTrafficInviteIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsTrafficInviteOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsTrafficAckIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsTrafficAckOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsTrafficByeIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsTrafficByeOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsTrafficCancelIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsTrafficCancelOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsTrafficOptionsIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsTrafficOptionsOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsTrafficRegisterIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsTrafficRegisterOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsTrafficCometIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsTrafficCometOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsTrafficPrackIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsTrafficPrackOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsTrafficReferIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsTrafficReferOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsTrafficNotifyIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsTrafficNotifyOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsTrafficInfoIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsTrafficInfoOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsTrafficSubscribeIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsTrafficSubscribeOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsTrafficUpdateIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsTrafficUpdateOuts"))
)
if mibBuilder.loadTexts:
    ciscoSipTrafficStatsGroupRev3.setStatus("current")

ciscoSipStatsRedirStatusCodesGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 3, 2, 39)
)
ciscoSipStatsRedirStatusCodesGroupRev2.setObjects(
      *(("CISCO-SIP-UA-MIB", "cSipStatsRedirMultipleChoices"),
        ("CISCO-SIP-UA-MIB", "cSipStatsRedirMovedPerms"),
        ("CISCO-SIP-UA-MIB", "cSipStatsRedirUseProxys"),
        ("CISCO-SIP-UA-MIB", "cSipStatsRedirAltServices"),
        ("CISCO-SIP-UA-MIB", "cSipStatsRedirMovedTempsIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsRedirMovedTempsOuts"))
)
if mibBuilder.loadTexts:
    ciscoSipStatsRedirStatusCodesGroupRev2.setStatus("current")

ciscoSipTimerConfigGroupRev4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 3, 2, 40)
)
ciscoSipTimerConfigGroupRev4.setObjects(
      *(("CISCO-SIP-UA-MIB", "cSipCfgTimerTrying"),
        ("CISCO-SIP-UA-MIB", "cSipCfgTimerExpires"),
        ("CISCO-SIP-UA-MIB", "cSipCfgTimerConnect"),
        ("CISCO-SIP-UA-MIB", "cSipCfgTimerDisconnect"),
        ("CISCO-SIP-UA-MIB", "cSipCfgTimerPrack"),
        ("CISCO-SIP-UA-MIB", "cSipCfgTimerComet"),
        ("CISCO-SIP-UA-MIB", "cSipCfgTimerReliableRsp"),
        ("CISCO-SIP-UA-MIB", "cSipCfgTimerNotify"),
        ("CISCO-SIP-UA-MIB", "cSipCfgTimerRefer"),
        ("CISCO-SIP-UA-MIB", "cSipCfgTimerHold"),
        ("CISCO-SIP-UA-MIB", "cSipCfgTimerInfo"),
        ("CISCO-SIP-UA-MIB", "cSipCfgTimerConnectionAging"),
        ("CISCO-SIP-UA-MIB", "cSipCfgTimerBufferInvite"))
)
if mibBuilder.loadTexts:
    ciscoSipTimerConfigGroupRev4.setStatus("current")

ciscoSipRetryStatsGroupRev4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 3, 2, 41)
)
ciscoSipRetryStatsGroupRev4.setObjects(
      *(("CISCO-SIP-UA-MIB", "cSipStatsRetryInvites"),
        ("CISCO-SIP-UA-MIB", "cSipStatsRetryByes"),
        ("CISCO-SIP-UA-MIB", "cSipStatsRetryCancels"),
        ("CISCO-SIP-UA-MIB", "cSipStatsRetryRegisters"),
        ("CISCO-SIP-UA-MIB", "cSipStatsRetryResponses"),
        ("CISCO-SIP-UA-MIB", "cSipStatsRetryPracks"),
        ("CISCO-SIP-UA-MIB", "cSipStatsRetryComets"),
        ("CISCO-SIP-UA-MIB", "cSipStatsRetryReliable1xxRsps"),
        ("CISCO-SIP-UA-MIB", "cSipStatsRetryNotifys"),
        ("CISCO-SIP-UA-MIB", "cSipStatsRetryRefers"),
        ("CISCO-SIP-UA-MIB", "cSipStatsRetryInfo"),
        ("CISCO-SIP-UA-MIB", "cSipStatsRetrySubscribe"))
)
if mibBuilder.loadTexts:
    ciscoSipRetryStatsGroupRev4.setStatus("current")

ciscoSipBaseIOSConfigGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 3, 2, 42)
)
ciscoSipBaseIOSConfigGroupRev1.setObjects(
      *(("CISCO-SIP-UA-MIB", "cSipCfgMaximumForwards"),
        ("CISCO-SIP-UA-MIB", "cSipCfgDnsSrvQueryStringFormat"),
        ("CISCO-SIP-UA-MIB", "cSipCfgRedirectionDisabled"),
        ("CISCO-SIP-UA-MIB", "cSipCfgTimerSessionTimer"),
        ("CISCO-SIP-UA-MIB", "cSipCfgEarlyMediaCutThruDisabled"),
        ("CISCO-SIP-UA-MIB", "cSipCfgSymNatEnabled"),
        ("CISCO-SIP-UA-MIB", "cSipCfgSymNatDirectionRole"),
        ("CISCO-SIP-UA-MIB", "cSipCfgBindSourceAddrInterface"),
        ("CISCO-SIP-UA-MIB", "cSipCfgSuspendResumeEnabled"),
        ("CISCO-SIP-UA-MIB", "cSipCfgOfferCallHold"),
        ("CISCO-SIP-UA-MIB", "cSipCfgReasonHeaderOveride"))
)
if mibBuilder.loadTexts:
    ciscoSipBaseIOSConfigGroupRev1.setStatus("current")

ciscoSipStatsClientStatusCodesGroupRev4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 3, 2, 43)
)
ciscoSipStatsClientStatusCodesGroupRev4.setObjects(
      *(("CISCO-SIP-UA-MIB", "cSipStatsClientBadRequestIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientBadRequestOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientUnauthorizedIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientUnauthorizedOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientPaymentReqdIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientPaymentReqdOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientForbiddenIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientForbiddenOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientNotFoundIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientNotFoundOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientMethNotAllowedIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientMethNotAllowedOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientNotAcceptableIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientNotAcceptableOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientProxyAuthReqdIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientProxyAuthReqdOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientReqTimeoutIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientReqTimeoutOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientConflictIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientConflictOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientGoneIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientGoneOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientReqEntTooLargeIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientReqEntTooLargeOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientReqURITooLargeIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientReqURITooLargeOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientNoSupMediaTypeIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientNoSupMediaTypeOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientBadExtensionIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientBadExtensionOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientTempNotAvailIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientTempNotAvailOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientCallLegNoExistIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientCallLegNoExistOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientLoopDetectedIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientLoopDetectedOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientTooManyHopsIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientTooManyHopsOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientAddrIncompleteIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientAddrIncompleteOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientAmbiguousIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientAmbiguousOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientBusyHereIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientBusyHereOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientReqTermIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientReqTermOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientNoAcceptHereIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientNoAcceptHereOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientBadEventIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientBadEventOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientSTTooSmallIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientSTTooSmallOuts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientReqPendingIns"),
        ("CISCO-SIP-UA-MIB", "cSipStatsClientReqPendingOuts"))
)
if mibBuilder.loadTexts:
    ciscoSipStatsClientStatusCodesGroupRev4.setStatus("current")

ciscoSipRetryConfigGroupRev4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 3, 2, 44)
)
ciscoSipRetryConfigGroupRev4.setObjects(
      *(("CISCO-SIP-UA-MIB", "cSipCfgRetryInvite"),
        ("CISCO-SIP-UA-MIB", "cSipCfgRetryBye"),
        ("CISCO-SIP-UA-MIB", "cSipCfgRetryCancel"),
        ("CISCO-SIP-UA-MIB", "cSipCfgRetryRegister"),
        ("CISCO-SIP-UA-MIB", "cSipCfgRetryResponse"),
        ("CISCO-SIP-UA-MIB", "cSipCfgRetryPrack"),
        ("CISCO-SIP-UA-MIB", "cSipCfgRetryComet"),
        ("CISCO-SIP-UA-MIB", "cSipCfgRetryReliableRsp"),
        ("CISCO-SIP-UA-MIB", "cSipCfgRetryNotify"),
        ("CISCO-SIP-UA-MIB", "cSipCfgRetryRefer"),
        ("CISCO-SIP-UA-MIB", "cSipCfgRetryInfo"),
        ("CISCO-SIP-UA-MIB", "cSipCfgRetrySubscribe"))
)
if mibBuilder.loadTexts:
    ciscoSipRetryConfigGroupRev4.setStatus("current")

ciscoSipCfgPeerGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 3, 2, 45)
)
ciscoSipCfgPeerGroupRev1.setObjects(
      *(("CISCO-SIP-UA-MIB", "cSipCfgPeerOutSessionTransport"),
        ("CISCO-SIP-UA-MIB", "cSipCfgPeerReliable1xxRspStr"),
        ("CISCO-SIP-UA-MIB", "cSipCfgPeerReliable1xxRspHdr"),
        ("CISCO-SIP-UA-MIB", "cSipCfgPeerUrlType"),
        ("CISCO-SIP-UA-MIB", "cSipCfgOutSessionTransport"),
        ("CISCO-SIP-UA-MIB", "cSipCfgReliable1xxRspStr"),
        ("CISCO-SIP-UA-MIB", "cSipCfgReliable1xxRspHdr"),
        ("CISCO-SIP-UA-MIB", "cSipCfgUrlType"),
        ("CISCO-SIP-UA-MIB", "cSipCfgPeerSwitchTransEnabled"))
)
if mibBuilder.loadTexts:
    ciscoSipCfgPeerGroupRev1.setStatus("current")

ciscoSipCfgVoiceServiceVoipGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 3, 2, 46)
)
ciscoSipCfgVoiceServiceVoipGroup.setObjects(
      *(("CISCO-SIP-UA-MIB", "cSipCfgHeaderPassingEnabled"),
        ("CISCO-SIP-UA-MIB", "cSipCfgMaxSubscriptionAccept"),
        ("CISCO-SIP-UA-MIB", "cSipCfgMaxSubscriptionOriginate"),
        ("CISCO-SIP-UA-MIB", "cSipCfgSwitchTransportEnabled"))
)
if mibBuilder.loadTexts:
    ciscoSipCfgVoiceServiceVoipGroup.setStatus("current")

ciscoSipStatsConnectionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 3, 2, 47)
)
ciscoSipStatsConnectionGroup.setObjects(
      *(("CISCO-SIP-UA-MIB", "cSipStatsConnTCPSendFailures"),
        ("CISCO-SIP-UA-MIB", "cSipStatsConnUDPSendFailures"),
        ("CISCO-SIP-UA-MIB", "cSipStatsConnTCPRemoteClosures"),
        ("CISCO-SIP-UA-MIB", "cSipStatsConnUDPCreateFailures"),
        ("CISCO-SIP-UA-MIB", "cSipStatsConnTCPCreateFailures"),
        ("CISCO-SIP-UA-MIB", "cSipStatsConnUDPInactiveTimeouts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsConnTCPInactiveTimeouts"),
        ("CISCO-SIP-UA-MIB", "cSipStatsActiveUDPConnections"),
        ("CISCO-SIP-UA-MIB", "cSipStatsActiveTCPConnections"))
)
if mibBuilder.loadTexts:
    ciscoSipStatsConnectionGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoSipCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoSipCompliance.setStatus(
        "obsolete"
    )

ciscoSipComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 3, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoSipComplianceRev1.setStatus(
        "obsolete"
    )

ciscoSipComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 3, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoSipComplianceRev2.setStatus(
        "deprecated"
    )

ciscoSipComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 3, 1, 4)
)
if mibBuilder.loadTexts:
    ciscoSipComplianceRev3.setStatus(
        "deprecated"
    )

ciscoSipComplianceRev4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 3, 1, 5)
)
if mibBuilder.loadTexts:
    ciscoSipComplianceRev4.setStatus(
        "deprecated"
    )

ciscoSipComplianceRev5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 152, 3, 1, 6)
)
if mibBuilder.loadTexts:
    ciscoSipComplianceRev5.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SIP-UA-MIB",
    **{"CSipStatusCode": CSipStatusCode,
       "CSipMethodStr": CSipMethodStr,
       "ciscoSipUaMIB": ciscoSipUaMIB,
       "ciscoSipUaMIBNotifs": ciscoSipUaMIBNotifs,
       "ciscoSipUaMIBObjects": ciscoSipUaMIBObjects,
       "cSipCfg": cSipCfg,
       "cSipCfgBase": cSipCfgBase,
       "cSipCfgVersion": cSipCfgVersion,
       "cSipCfgTransport": cSipCfgTransport,
       "cSipCfgUserLocationServerAddr": cSipCfgUserLocationServerAddr,
       "cSipCfgMaxForwards": cSipCfgMaxForwards,
       "cSipCfgBindSrcAddrInterface": cSipCfgBindSrcAddrInterface,
       "cSipCfgBindSrcAddrScope": cSipCfgBindSrcAddrScope,
       "cSipCfgDnsSrvQueryStringFormat": cSipCfgDnsSrvQueryStringFormat,
       "cSipCfgRedirectionDisabled": cSipCfgRedirectionDisabled,
       "cSipCfgEarlyMediaTable": cSipCfgEarlyMediaTable,
       "cSipCfgEarlyMediaEntry": cSipCfgEarlyMediaEntry,
       "cSipCfgEarlyMediaStatusCodeIndex": cSipCfgEarlyMediaStatusCodeIndex,
       "cSipCfgEarlyMediaCutThruDisabled": cSipCfgEarlyMediaCutThruDisabled,
       "cSipCfgSymNatEnabled": cSipCfgSymNatEnabled,
       "cSipCfgSymNatDirectionRole": cSipCfgSymNatDirectionRole,
       "cSipCfgBindSourceAddrTable": cSipCfgBindSourceAddrTable,
       "cSipCfgBindSourceAddrEntry": cSipCfgBindSourceAddrEntry,
       "cSipCfgBindSourceAddrScope": cSipCfgBindSourceAddrScope,
       "cSipCfgBindSourceAddrInterface": cSipCfgBindSourceAddrInterface,
       "cSipCfgSuspendResumeEnabled": cSipCfgSuspendResumeEnabled,
       "cSipCfgOfferCallHold": cSipCfgOfferCallHold,
       "cSipCfgReasonHeaderOveride": cSipCfgReasonHeaderOveride,
       "cSipCfgMaximumForwards": cSipCfgMaximumForwards,
       "cSipCfgTimer": cSipCfgTimer,
       "cSipCfgTimerTrying": cSipCfgTimerTrying,
       "cSipCfgTimerExpires": cSipCfgTimerExpires,
       "cSipCfgTimerConnect": cSipCfgTimerConnect,
       "cSipCfgTimerDisconnect": cSipCfgTimerDisconnect,
       "cSipCfgTimerPrack": cSipCfgTimerPrack,
       "cSipCfgTimerComet": cSipCfgTimerComet,
       "cSipCfgTimerReliableRsp": cSipCfgTimerReliableRsp,
       "cSipCfgTimerNotify": cSipCfgTimerNotify,
       "cSipCfgTimerRefer": cSipCfgTimerRefer,
       "cSipCfgTimerSessionTimer": cSipCfgTimerSessionTimer,
       "cSipCfgTimerHold": cSipCfgTimerHold,
       "cSipCfgTimerInfo": cSipCfgTimerInfo,
       "cSipCfgTimerConnectionAging": cSipCfgTimerConnectionAging,
       "cSipCfgTimerBufferInvite": cSipCfgTimerBufferInvite,
       "cSipCfgRetry": cSipCfgRetry,
       "cSipCfgRetryInvite": cSipCfgRetryInvite,
       "cSipCfgRetryBye": cSipCfgRetryBye,
       "cSipCfgRetryCancel": cSipCfgRetryCancel,
       "cSipCfgRetryRegister": cSipCfgRetryRegister,
       "cSipCfgRetryResponse": cSipCfgRetryResponse,
       "cSipCfgRetryPrack": cSipCfgRetryPrack,
       "cSipCfgRetryComet": cSipCfgRetryComet,
       "cSipCfgRetryReliableRsp": cSipCfgRetryReliableRsp,
       "cSipCfgRetryNotify": cSipCfgRetryNotify,
       "cSipCfgRetryRefer": cSipCfgRetryRefer,
       "cSipCfgRetryInfo": cSipCfgRetryInfo,
       "cSipCfgRetrySubscribe": cSipCfgRetrySubscribe,
       "cSipCfgPeer": cSipCfgPeer,
       "cSipCfgPeerTable": cSipCfgPeerTable,
       "cSipCfgPeerEntry": cSipCfgPeerEntry,
       "cSipCfgPeerIndex": cSipCfgPeerIndex,
       "cSipCfgPeerOutSessionTransport": cSipCfgPeerOutSessionTransport,
       "cSipCfgPeerReliable1xxRspStr": cSipCfgPeerReliable1xxRspStr,
       "cSipCfgPeerReliable1xxRspHdr": cSipCfgPeerReliable1xxRspHdr,
       "cSipCfgPeerUrlType": cSipCfgPeerUrlType,
       "cSipCfgPeerSwitchTransEnabled": cSipCfgPeerSwitchTransEnabled,
       "cSipCfgOutSessionTransport": cSipCfgOutSessionTransport,
       "cSipCfgReliable1xxRspStr": cSipCfgReliable1xxRspStr,
       "cSipCfgReliable1xxRspHdr": cSipCfgReliable1xxRspHdr,
       "cSipCfgUrlType": cSipCfgUrlType,
       "cSipCfgStatusCauseMap": cSipCfgStatusCauseMap,
       "cSipCfgStatusCauseTable": cSipCfgStatusCauseTable,
       "cSipCfgStatusCauseEntry": cSipCfgStatusCauseEntry,
       "cSipCfgStatusCodeIndex": cSipCfgStatusCodeIndex,
       "cSipCfgPstnCause": cSipCfgPstnCause,
       "cSipCfgStatusCauseStoreStatus": cSipCfgStatusCauseStoreStatus,
       "cSipCfgCauseStatusTable": cSipCfgCauseStatusTable,
       "cSipCfgCauseStatusEntry": cSipCfgCauseStatusEntry,
       "cSipCfgPstnCauseIndex": cSipCfgPstnCauseIndex,
       "cSipCfgStatusCode": cSipCfgStatusCode,
       "cSipCfgCauseStatusStoreStatus": cSipCfgCauseStatusStoreStatus,
       "cSipCfgAaa": cSipCfgAaa,
       "cSipCfgAaaUsername": cSipCfgAaaUsername,
       "cSipCfgVoiceServiceVoip": cSipCfgVoiceServiceVoip,
       "cSipCfgHeaderPassingEnabled": cSipCfgHeaderPassingEnabled,
       "cSipCfgMaxSubscriptionAccept": cSipCfgMaxSubscriptionAccept,
       "cSipCfgMaxSubscriptionOriginate": cSipCfgMaxSubscriptionOriginate,
       "cSipCfgSwitchTransportEnabled": cSipCfgSwitchTransportEnabled,
       "cSipStats": cSipStats,
       "cSipStatsInfo": cSipStatsInfo,
       "cSipStatsInfoTryingIns": cSipStatsInfoTryingIns,
       "cSipStatsInfoTryingOuts": cSipStatsInfoTryingOuts,
       "cSipStatsInfoRingingIns": cSipStatsInfoRingingIns,
       "cSipStatsInfoRingingOuts": cSipStatsInfoRingingOuts,
       "cSipStatsInfoForwardedIns": cSipStatsInfoForwardedIns,
       "cSipStatsInfoForwardedOuts": cSipStatsInfoForwardedOuts,
       "cSipStatsInfoQueuedIns": cSipStatsInfoQueuedIns,
       "cSipStatsInfoQueuedOuts": cSipStatsInfoQueuedOuts,
       "cSipStatsInfoSessionProgIns": cSipStatsInfoSessionProgIns,
       "cSipStatsInfoSessionProgOuts": cSipStatsInfoSessionProgOuts,
       "cSipStatsSuccess": cSipStatsSuccess,
       "cSipStatsSuccessOkIns": cSipStatsSuccessOkIns,
       "cSipStatsSuccessOkOuts": cSipStatsSuccessOkOuts,
       "cSipStatsSuccessAcceptedIns": cSipStatsSuccessAcceptedIns,
       "cSipStatsSuccessAcceptedOuts": cSipStatsSuccessAcceptedOuts,
       "cSipStatsSuccessOkTable": cSipStatsSuccessOkTable,
       "cSipStatsSuccessOkEntry": cSipStatsSuccessOkEntry,
       "cSipStatsSuccessOkMethod": cSipStatsSuccessOkMethod,
       "cSipStatsSuccessOkInbounds": cSipStatsSuccessOkInbounds,
       "cSipStatsSuccessOkOutbounds": cSipStatsSuccessOkOutbounds,
       "cSipStatsRedirect": cSipStatsRedirect,
       "cSipStatsRedirMultipleChoices": cSipStatsRedirMultipleChoices,
       "cSipStatsRedirMovedPerms": cSipStatsRedirMovedPerms,
       "cSipStatsRedirMovedTemps": cSipStatsRedirMovedTemps,
       "cSipStatsRedirSeeOthers": cSipStatsRedirSeeOthers,
       "cSipStatsRedirUseProxys": cSipStatsRedirUseProxys,
       "cSipStatsRedirAltServices": cSipStatsRedirAltServices,
       "cSipStatsRedirMovedTempsIns": cSipStatsRedirMovedTempsIns,
       "cSipStatsRedirMovedTempsOuts": cSipStatsRedirMovedTempsOuts,
       "cSipStatsErrClient": cSipStatsErrClient,
       "cSipStatsClientBadRequestIns": cSipStatsClientBadRequestIns,
       "cSipStatsClientBadRequestOuts": cSipStatsClientBadRequestOuts,
       "cSipStatsClientUnauthorizedIns": cSipStatsClientUnauthorizedIns,
       "cSipStatsClientUnauthorizedOuts": cSipStatsClientUnauthorizedOuts,
       "cSipStatsClientPaymentReqdIns": cSipStatsClientPaymentReqdIns,
       "cSipStatsClientPaymentReqdOuts": cSipStatsClientPaymentReqdOuts,
       "cSipStatsClientForbiddenIns": cSipStatsClientForbiddenIns,
       "cSipStatsClientForbiddenOuts": cSipStatsClientForbiddenOuts,
       "cSipStatsClientNotFoundIns": cSipStatsClientNotFoundIns,
       "cSipStatsClientNotFoundOuts": cSipStatsClientNotFoundOuts,
       "cSipStatsClientMethNotAllowedIns": cSipStatsClientMethNotAllowedIns,
       "cSipStatsClientMethNotAllowedOuts": cSipStatsClientMethNotAllowedOuts,
       "cSipStatsClientNotAcceptableIns": cSipStatsClientNotAcceptableIns,
       "cSipStatsClientNotAcceptableOuts": cSipStatsClientNotAcceptableOuts,
       "cSipStatsClientProxyAuthReqdIns": cSipStatsClientProxyAuthReqdIns,
       "cSipStatsClientProxyAuthReqdOuts": cSipStatsClientProxyAuthReqdOuts,
       "cSipStatsClientReqTimeoutIns": cSipStatsClientReqTimeoutIns,
       "cSipStatsClientReqTimeoutOuts": cSipStatsClientReqTimeoutOuts,
       "cSipStatsClientConflictIns": cSipStatsClientConflictIns,
       "cSipStatsClientConflictOuts": cSipStatsClientConflictOuts,
       "cSipStatsClientGoneIns": cSipStatsClientGoneIns,
       "cSipStatsClientGoneOuts": cSipStatsClientGoneOuts,
       "cSipStatsClientLengthRequiredIns": cSipStatsClientLengthRequiredIns,
       "cSipStatsClientLengthRequiredOuts": cSipStatsClientLengthRequiredOuts,
       "cSipStatsClientReqEntTooLargeIns": cSipStatsClientReqEntTooLargeIns,
       "cSipStatsClientReqEntTooLargeOuts": cSipStatsClientReqEntTooLargeOuts,
       "cSipStatsClientReqURITooLargeIns": cSipStatsClientReqURITooLargeIns,
       "cSipStatsClientReqURITooLargeOuts": cSipStatsClientReqURITooLargeOuts,
       "cSipStatsClientNoSupMediaTypeIns": cSipStatsClientNoSupMediaTypeIns,
       "cSipStatsClientNoSupMediaTypeOuts": cSipStatsClientNoSupMediaTypeOuts,
       "cSipStatsClientBadExtensionIns": cSipStatsClientBadExtensionIns,
       "cSipStatsClientBadExtensionOuts": cSipStatsClientBadExtensionOuts,
       "cSipStatsClientTempNotAvailIns": cSipStatsClientTempNotAvailIns,
       "cSipStatsClientTempNotAvailOuts": cSipStatsClientTempNotAvailOuts,
       "cSipStatsClientCallLegNoExistIns": cSipStatsClientCallLegNoExistIns,
       "cSipStatsClientCallLegNoExistOuts": cSipStatsClientCallLegNoExistOuts,
       "cSipStatsClientLoopDetectedIns": cSipStatsClientLoopDetectedIns,
       "cSipStatsClientLoopDetectedOuts": cSipStatsClientLoopDetectedOuts,
       "cSipStatsClientTooManyHopsIns": cSipStatsClientTooManyHopsIns,
       "cSipStatsClientTooManyHopsOuts": cSipStatsClientTooManyHopsOuts,
       "cSipStatsClientAddrIncompleteIns": cSipStatsClientAddrIncompleteIns,
       "cSipStatsClientAddrIncompleteOuts": cSipStatsClientAddrIncompleteOuts,
       "cSipStatsClientAmbiguousIns": cSipStatsClientAmbiguousIns,
       "cSipStatsClientAmbiguousOuts": cSipStatsClientAmbiguousOuts,
       "cSipStatsClientBusyHereIns": cSipStatsClientBusyHereIns,
       "cSipStatsClientBusyHereOuts": cSipStatsClientBusyHereOuts,
       "cSipStatsClientReqTermIns": cSipStatsClientReqTermIns,
       "cSipStatsClientReqTermOuts": cSipStatsClientReqTermOuts,
       "cSipStatsClientNoAcceptHereIns": cSipStatsClientNoAcceptHereIns,
       "cSipStatsClientNoAcceptHereOuts": cSipStatsClientNoAcceptHereOuts,
       "cSipStatsClientBadEventIns": cSipStatsClientBadEventIns,
       "cSipStatsClientBadEventOuts": cSipStatsClientBadEventOuts,
       "cSipStatsClientSTTooSmallIns": cSipStatsClientSTTooSmallIns,
       "cSipStatsClientSTTooSmallOuts": cSipStatsClientSTTooSmallOuts,
       "cSipStatsClientReqPendingIns": cSipStatsClientReqPendingIns,
       "cSipStatsClientReqPendingOuts": cSipStatsClientReqPendingOuts,
       "cSipStatsErrServer": cSipStatsErrServer,
       "cSipStatsServerIntErrorIns": cSipStatsServerIntErrorIns,
       "cSipStatsServerIntErrorOuts": cSipStatsServerIntErrorOuts,
       "cSipStatsServerNotImplementedIns": cSipStatsServerNotImplementedIns,
       "cSipStatsServerNotImplementedOuts": cSipStatsServerNotImplementedOuts,
       "cSipStatsServerBadGatewayIns": cSipStatsServerBadGatewayIns,
       "cSipStatsServerBadGatewayOuts": cSipStatsServerBadGatewayOuts,
       "cSipStatsServerServiceUnavailIns": cSipStatsServerServiceUnavailIns,
       "cSipStatsServerServiceUnavailOuts": cSipStatsServerServiceUnavailOuts,
       "cSipStatsServerGatewayTimeoutIns": cSipStatsServerGatewayTimeoutIns,
       "cSipStatsServerGatewayTimeoutOuts": cSipStatsServerGatewayTimeoutOuts,
       "cSipStatsServerBadSipVersionIns": cSipStatsServerBadSipVersionIns,
       "cSipStatsServerBadSipVersionOuts": cSipStatsServerBadSipVersionOuts,
       "cSipStatsServerPrecondFailureIns": cSipStatsServerPrecondFailureIns,
       "cSipStatsServerPrecondFailureOuts": cSipStatsServerPrecondFailureOuts,
       "cSipStatsGlobalFail": cSipStatsGlobalFail,
       "cSipStatsGlobalBusyEverywhereIns": cSipStatsGlobalBusyEverywhereIns,
       "cSipStatsGlobalBusyEverywhereOuts": cSipStatsGlobalBusyEverywhereOuts,
       "cSipStatsGlobalDeclineIns": cSipStatsGlobalDeclineIns,
       "cSipStatsGlobalDeclineOuts": cSipStatsGlobalDeclineOuts,
       "cSipStatsGlobalNotAnywhereIns": cSipStatsGlobalNotAnywhereIns,
       "cSipStatsGlobalNotAnywhereOuts": cSipStatsGlobalNotAnywhereOuts,
       "cSipStatsGlobalNotAcceptableIns": cSipStatsGlobalNotAcceptableIns,
       "cSipStatsGlobalNotAcceptableOuts": cSipStatsGlobalNotAcceptableOuts,
       "cSipStatsTraffic": cSipStatsTraffic,
       "cSipStatsTrafficInviteIns": cSipStatsTrafficInviteIns,
       "cSipStatsTrafficInviteOuts": cSipStatsTrafficInviteOuts,
       "cSipStatsTrafficAckIns": cSipStatsTrafficAckIns,
       "cSipStatsTrafficAckOuts": cSipStatsTrafficAckOuts,
       "cSipStatsTrafficByeIns": cSipStatsTrafficByeIns,
       "cSipStatsTrafficByeOuts": cSipStatsTrafficByeOuts,
       "cSipStatsTrafficCancelIns": cSipStatsTrafficCancelIns,
       "cSipStatsTrafficCancelOuts": cSipStatsTrafficCancelOuts,
       "cSipStatsTrafficOptionsIns": cSipStatsTrafficOptionsIns,
       "cSipStatsTrafficOptionsOuts": cSipStatsTrafficOptionsOuts,
       "cSipStatsTrafficRegisterIns": cSipStatsTrafficRegisterIns,
       "cSipStatsTrafficRegisterOuts": cSipStatsTrafficRegisterOuts,
       "cSipStatsTrafficCometIns": cSipStatsTrafficCometIns,
       "cSipStatsTrafficCometOuts": cSipStatsTrafficCometOuts,
       "cSipStatsTrafficPrackIns": cSipStatsTrafficPrackIns,
       "cSipStatsTrafficPrackOuts": cSipStatsTrafficPrackOuts,
       "cSipStatsTrafficReferIns": cSipStatsTrafficReferIns,
       "cSipStatsTrafficReferOuts": cSipStatsTrafficReferOuts,
       "cSipStatsTrafficNotifyIns": cSipStatsTrafficNotifyIns,
       "cSipStatsTrafficNotifyOuts": cSipStatsTrafficNotifyOuts,
       "cSipStatsTrafficInfoIns": cSipStatsTrafficInfoIns,
       "cSipStatsTrafficInfoOuts": cSipStatsTrafficInfoOuts,
       "cSipStatsTrafficSubscribeIns": cSipStatsTrafficSubscribeIns,
       "cSipStatsTrafficSubscribeOuts": cSipStatsTrafficSubscribeOuts,
       "cSipStatsTrafficUpdateIns": cSipStatsTrafficUpdateIns,
       "cSipStatsTrafficUpdateOuts": cSipStatsTrafficUpdateOuts,
       "cSipStatsRetry": cSipStatsRetry,
       "cSipStatsRetryInvites": cSipStatsRetryInvites,
       "cSipStatsRetryByes": cSipStatsRetryByes,
       "cSipStatsRetryCancels": cSipStatsRetryCancels,
       "cSipStatsRetryRegisters": cSipStatsRetryRegisters,
       "cSipStatsRetryResponses": cSipStatsRetryResponses,
       "cSipStatsRetryPracks": cSipStatsRetryPracks,
       "cSipStatsRetryComets": cSipStatsRetryComets,
       "cSipStatsRetryReliable1xxRsps": cSipStatsRetryReliable1xxRsps,
       "cSipStatsRetryNotifys": cSipStatsRetryNotifys,
       "cSipStatsRetryRefers": cSipStatsRetryRefers,
       "cSipStatsRetryInfo": cSipStatsRetryInfo,
       "cSipStatsRetrySubscribe": cSipStatsRetrySubscribe,
       "cSipStatsMisc": cSipStatsMisc,
       "cSipStatsMisc3xxMappedTo4xxRsps": cSipStatsMisc3xxMappedTo4xxRsps,
       "cSipStatsConnection": cSipStatsConnection,
       "cSipStatsConnTCPSendFailures": cSipStatsConnTCPSendFailures,
       "cSipStatsConnUDPSendFailures": cSipStatsConnUDPSendFailures,
       "cSipStatsConnTCPRemoteClosures": cSipStatsConnTCPRemoteClosures,
       "cSipStatsConnUDPCreateFailures": cSipStatsConnUDPCreateFailures,
       "cSipStatsConnTCPCreateFailures": cSipStatsConnTCPCreateFailures,
       "cSipStatsConnUDPInactiveTimeouts": cSipStatsConnUDPInactiveTimeouts,
       "cSipStatsConnTCPInactiveTimeouts": cSipStatsConnTCPInactiveTimeouts,
       "cSipStatsActiveUDPConnections": cSipStatsActiveUDPConnections,
       "cSipStatsActiveTCPConnections": cSipStatsActiveTCPConnections,
       "ciscoSipUaMIBNotificationPrefix": ciscoSipUaMIBNotificationPrefix,
       "ciscoSipUaMIBNotifications": ciscoSipUaMIBNotifications,
       "ciscoSipUaMIBConformance": ciscoSipUaMIBConformance,
       "ciscoSipUaMIBCompliances": ciscoSipUaMIBCompliances,
       "ciscoSipCompliance": ciscoSipCompliance,
       "ciscoSipComplianceRev1": ciscoSipComplianceRev1,
       "ciscoSipComplianceRev2": ciscoSipComplianceRev2,
       "ciscoSipComplianceRev3": ciscoSipComplianceRev3,
       "ciscoSipComplianceRev4": ciscoSipComplianceRev4,
       "ciscoSipComplianceRev5": ciscoSipComplianceRev5,
       "ciscoSipUaMIBGroups": ciscoSipUaMIBGroups,
       "ciscoSipBaseConfigGroup": ciscoSipBaseConfigGroup,
       "ciscoSipTimerConfigGroup": ciscoSipTimerConfigGroup,
       "ciscoSipRetryConfigGroup": ciscoSipRetryConfigGroup,
       "ciscoSipStatsInfoStatusCodesGroup": ciscoSipStatsInfoStatusCodesGroup,
       "ciscoSipStatsSuccessStatusCodesGroup": ciscoSipStatsSuccessStatusCodesGroup,
       "ciscoSipStatsRedirStatusCodesGroup": ciscoSipStatsRedirStatusCodesGroup,
       "ciscoSipStatsClientStatusCodesGroup": ciscoSipStatsClientStatusCodesGroup,
       "ciscoSipStatsServerStatusCodesGroup": ciscoSipStatsServerStatusCodesGroup,
       "ciscoSipStatsGlobalStatusCodesGroup": ciscoSipStatsGlobalStatusCodesGroup,
       "ciscoSipTrafficStatsGroup": ciscoSipTrafficStatsGroup,
       "ciscoSipRetryStatsGroup": ciscoSipRetryStatsGroup,
       "ciscoSipBaseConfigGroupRev1": ciscoSipBaseConfigGroupRev1,
       "ciscoSipTimerConfigGroupRev1": ciscoSipTimerConfigGroupRev1,
       "ciscoSipRetryConfigGroupRev1": ciscoSipRetryConfigGroupRev1,
       "ciscoSipTrafficStatsGroupRev1": ciscoSipTrafficStatsGroupRev1,
       "ciscoSipStatsServerStatusCodesGroupRev1": ciscoSipStatsServerStatusCodesGroupRev1,
       "ciscoSipRetryStatsGroupRev1": ciscoSipRetryStatsGroupRev1,
       "ciscoSipStatsClientStatusCodesGroupRev1": ciscoSipStatsClientStatusCodesGroupRev1,
       "ciscoSipCfgPeerGroup": ciscoSipCfgPeerGroup,
       "ciscoSipBaseConfigGroupRev2": ciscoSipBaseConfigGroupRev2,
       "ciscoSipStatusCauseMapGroup": ciscoSipStatusCauseMapGroup,
       "ciscoSipTrafficStatsGroupRev2": ciscoSipTrafficStatsGroupRev2,
       "ciscoSipStatsSuccessStatusCodesGroupRev1": ciscoSipStatsSuccessStatusCodesGroupRev1,
       "ciscoSipTimerConfigGroupRev2": ciscoSipTimerConfigGroupRev2,
       "ciscoSipRetryConfigGroupRev2": ciscoSipRetryConfigGroupRev2,
       "ciscoSipRetryStatsGroupRev2": ciscoSipRetryStatsGroupRev2,
       "ciscoSipCfgAaaGroup": ciscoSipCfgAaaGroup,
       "ciscoSipStatsClientStatusCodesGroupRev2": ciscoSipStatsClientStatusCodesGroupRev2,
       "ciscoSipStatsRedirStatusCodesGroupRev1": ciscoSipStatsRedirStatusCodesGroupRev1,
       "ciscoSipTimerConfigGroupRev3": ciscoSipTimerConfigGroupRev3,
       "ciscoSipRetryConfigGroupRev3": ciscoSipRetryConfigGroupRev3,
       "ciscoSipRetryStatsGroupRev3": ciscoSipRetryStatsGroupRev3,
       "ciscoSipStatsSuccessStatusCodesGroupRev2": ciscoSipStatsSuccessStatusCodesGroupRev2,
       "ciscoSipBaseConfigGroupRev3": ciscoSipBaseConfigGroupRev3,
       "ciscoSipStatsClientStatusCodesGroupRev3": ciscoSipStatsClientStatusCodesGroupRev3,
       "ciscoSipStatsMiscGroup": ciscoSipStatsMiscGroup,
       "ciscoSipBaseIOSConfigGroup": ciscoSipBaseIOSConfigGroup,
       "ciscoSipTrafficStatsGroupRev3": ciscoSipTrafficStatsGroupRev3,
       "ciscoSipStatsRedirStatusCodesGroupRev2": ciscoSipStatsRedirStatusCodesGroupRev2,
       "ciscoSipTimerConfigGroupRev4": ciscoSipTimerConfigGroupRev4,
       "ciscoSipRetryStatsGroupRev4": ciscoSipRetryStatsGroupRev4,
       "ciscoSipBaseIOSConfigGroupRev1": ciscoSipBaseIOSConfigGroupRev1,
       "ciscoSipStatsClientStatusCodesGroupRev4": ciscoSipStatsClientStatusCodesGroupRev4,
       "ciscoSipRetryConfigGroupRev4": ciscoSipRetryConfigGroupRev4,
       "ciscoSipCfgPeerGroupRev1": ciscoSipCfgPeerGroupRev1,
       "ciscoSipCfgVoiceServiceVoipGroup": ciscoSipCfgVoiceServiceVoipGroup,
       "ciscoSipStatsConnectionGroup": ciscoSipStatsConnectionGroup}
)
