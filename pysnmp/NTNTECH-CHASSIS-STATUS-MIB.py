# SNMP MIB module (NTNTECH-CHASSIS-STATUS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NTNTECH-CHASSIS-STATUS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:29:43 2024
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

(NtnDisplayString,
 NtnMacAddress,
 ntntechChassis) = mibBuilder.importSymbols(
    "NTNTECH-ROOT-MIB",
    "NtnDisplayString",
    "NtnMacAddress",
    "ntntechChassis")

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


# MODULE-IDENTITY

ntntechChassisStatusMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 2)
)
ntntechChassisStatusMIB.setRevisions(
        ("1902-05-06 10:54",
         "1902-08-06 10:45",
         "1902-08-28 09:35",
         "1902-09-24 11:24",
         "1902-10-11 09:00",
         "1902-10-22 02:00",
         "1902-11-04 10:36",
         "1903-11-14 08:42",
         "1904-03-15 10:16",
         "1904-04-27 10:42",
         "1904-10-11 09:19",
         "1904-11-17 10:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ChsStaMIBObjects_ObjectIdentity = ObjectIdentity
chsStaMIBObjects = _ChsStaMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 2, 1)
)
_ChsStaValues_ObjectIdentity = ObjectIdentity
chsStaValues = _ChsStaValues_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 2, 1, 1)
)
_ValMultiplexerUplinkModule_ObjectIdentity = ObjectIdentity
valMultiplexerUplinkModule = _ValMultiplexerUplinkModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 2, 1, 1, 1)
)


class _MumStaChassisType_Type(Integer32):
    """Custom type mumStaChassisType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("iPD12000", 1),
          ("iPD12000E", 6),
          ("iPD4000", 2),
          ("iPD4000E", 7),
          ("microDSLAM", 4),
          ("miniDSLAM", 3),
          ("networkExtender", 5))
    )


_MumStaChassisType_Type.__name__ = "Integer32"
_MumStaChassisType_Object = MibScalar
mumStaChassisType = _MumStaChassisType_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 2, 1, 1, 1, 1),
    _MumStaChassisType_Type()
)
mumStaChassisType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mumStaChassisType.setStatus("current")


class _MumStaFanState_Type(Integer32):
    """Custom type mumStaFanState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alert", 3),
          ("fault", 2),
          ("on", 1))
    )


_MumStaFanState_Type.__name__ = "Integer32"
_MumStaFanState_Object = MibScalar
mumStaFanState = _MumStaFanState_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 2, 1, 1, 1, 2),
    _MumStaFanState_Type()
)
mumStaFanState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mumStaFanState.setStatus("current")
_MumStaTable_Object = MibTable
mumStaTable = _MumStaTable_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 2, 1, 1, 1, 4)
)
if mibBuilder.loadTexts:
    mumStaTable.setStatus("current")
_MumStaEntry_Object = MibTableRow
mumStaEntry = _MumStaEntry_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 2, 1, 1, 1, 4, 1)
)
mumStaEntry.setIndexNames(
    (0, "NTNTECH-CHASSIS-STATUS-MIB", "mumStaIndex"),
)
if mibBuilder.loadTexts:
    mumStaEntry.setStatus("current")


class _MumStaIndex_Type(Integer32):
    """Custom type mumStaIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_MumStaIndex_Type.__name__ = "Integer32"
_MumStaIndex_Object = MibTableColumn
mumStaIndex = _MumStaIndex_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 2, 1, 1, 1, 4, 1, 1),
    _MumStaIndex_Type()
)
mumStaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mumStaIndex.setStatus("current")
_MumStaMacAddress_Type = NtnMacAddress
_MumStaMacAddress_Object = MibTableColumn
mumStaMacAddress = _MumStaMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 2, 1, 1, 1, 4, 1, 2),
    _MumStaMacAddress_Type()
)
mumStaMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mumStaMacAddress.setStatus("current")


class _MumStaFirmWareRev_Type(OctetString):
    """Custom type mumStaFirmWareRev based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 7),
    )


_MumStaFirmWareRev_Type.__name__ = "OctetString"
_MumStaFirmWareRev_Object = MibTableColumn
mumStaFirmWareRev = _MumStaFirmWareRev_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 2, 1, 1, 1, 4, 1, 3),
    _MumStaFirmWareRev_Type()
)
mumStaFirmWareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mumStaFirmWareRev.setStatus("current")


class _MumStaType_Type(Integer32):
    """Custom type mumStaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(7,
              8,
              11,
              14,
              19,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              128,
              129,
              130,
              135,
              137)
        )
    )
    namedValues = NamedValues(
        *(("amD8000p12", 11),
          ("ane8420", 135),
          ("bsx8000", 137),
          ("mum2000p2", 129),
          ("mum200p2", 128),
          ("smD2000Gp12", 19),
          ("smD2000Qp12", 8),
          ("smD2000p12", 7),
          ("smD2000p24", 130),
          ("sne2040", 14),
          ("suD2002p6E", 29),
          ("suD2002p6T", 28),
          ("suD2003p12E", 25),
          ("suD2003p12T", 24),
          ("suD2011p12E", 23),
          ("suD2011p12T", 22),
          ("suD2011p6E", 27),
          ("suD2011p6T", 26))
    )


_MumStaType_Type.__name__ = "Integer32"
_MumStaType_Object = MibTableColumn
mumStaType = _MumStaType_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 2, 1, 1, 1, 4, 1, 4),
    _MumStaType_Type()
)
mumStaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mumStaType.setStatus("current")
_MumStaMgmtPortTable_Object = MibTable
mumStaMgmtPortTable = _MumStaMgmtPortTable_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 2, 1, 1, 1, 5)
)
if mibBuilder.loadTexts:
    mumStaMgmtPortTable.setStatus("current")
_MumStaMgmtPortEntry_Object = MibTableRow
mumStaMgmtPortEntry = _MumStaMgmtPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 2, 1, 1, 1, 5, 1)
)
mumStaMgmtPortEntry.setIndexNames(
    (0, "NTNTECH-CHASSIS-STATUS-MIB", "mumStaMgmtPortMumIndex"),
)
if mibBuilder.loadTexts:
    mumStaMgmtPortEntry.setStatus("current")


class _MumStaMgmtPortMumIndex_Type(Integer32):
    """Custom type mumStaMgmtPortMumIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_MumStaMgmtPortMumIndex_Type.__name__ = "Integer32"
_MumStaMgmtPortMumIndex_Object = MibTableColumn
mumStaMgmtPortMumIndex = _MumStaMgmtPortMumIndex_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 2, 1, 1, 1, 5, 1, 1),
    _MumStaMgmtPortMumIndex_Type()
)
mumStaMgmtPortMumIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mumStaMgmtPortMumIndex.setStatus("current")


class _MumStaMgmtPortType_Type(Integer32):
    """Custom type mumStaMgmtPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mgmt", 1),
          ("uplink", 2))
    )


_MumStaMgmtPortType_Type.__name__ = "Integer32"
_MumStaMgmtPortType_Object = MibTableColumn
mumStaMgmtPortType = _MumStaMgmtPortType_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 2, 1, 1, 1, 5, 1, 2),
    _MumStaMgmtPortType_Type()
)
mumStaMgmtPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mumStaMgmtPortType.setStatus("current")


class _MumStaMgmtPortLinkState_Type(Integer32):
    """Custom type mumStaMgmtPortLinkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fault", 3),
          ("link", 1),
          ("noLink", 2))
    )


_MumStaMgmtPortLinkState_Type.__name__ = "Integer32"
_MumStaMgmtPortLinkState_Object = MibTableColumn
mumStaMgmtPortLinkState = _MumStaMgmtPortLinkState_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 2, 1, 1, 1, 5, 1, 3),
    _MumStaMgmtPortLinkState_Type()
)
mumStaMgmtPortLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mumStaMgmtPortLinkState.setStatus("current")


class _MumStaMgmtPortRxTxRate_Type(Integer32):
    """Custom type mumStaMgmtPortRxTxRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("uimEth10", 1),
          ("uimEth100", 2),
          ("uimEthGig", 3),
          ("uimEthNoLink", 0))
    )


_MumStaMgmtPortRxTxRate_Type.__name__ = "Integer32"
_MumStaMgmtPortRxTxRate_Object = MibTableColumn
mumStaMgmtPortRxTxRate = _MumStaMgmtPortRxTxRate_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 2, 1, 1, 1, 5, 1, 4),
    _MumStaMgmtPortRxTxRate_Type()
)
mumStaMgmtPortRxTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mumStaMgmtPortRxTxRate.setStatus("current")


class _MumStaMgmtPortDuplex_Type(Integer32):
    """Custom type mumStaMgmtPortDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("uimEthFull", 2),
          ("uimEthHalf", 1),
          ("uimEthNoLink", 0))
    )


_MumStaMgmtPortDuplex_Type.__name__ = "Integer32"
_MumStaMgmtPortDuplex_Object = MibTableColumn
mumStaMgmtPortDuplex = _MumStaMgmtPortDuplex_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 2, 1, 1, 1, 5, 1, 5),
    _MumStaMgmtPortDuplex_Type()
)
mumStaMgmtPortDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mumStaMgmtPortDuplex.setStatus("current")
_MumStaUplinkInterfaceModule_ObjectIdentity = ObjectIdentity
mumStaUplinkInterfaceModule = _MumStaUplinkInterfaceModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 2, 1, 1, 1, 6)
)
_UimStaTable_Object = MibTable
uimStaTable = _UimStaTable_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 2, 1, 1, 1, 6, 1)
)
if mibBuilder.loadTexts:
    uimStaTable.setStatus("current")
_UimStaEntry_Object = MibTableRow
uimStaEntry = _UimStaEntry_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 2, 1, 1, 1, 6, 1, 1)
)
uimStaEntry.setIndexNames(
    (0, "NTNTECH-CHASSIS-STATUS-MIB", "uimStaMumIndex"),
    (0, "NTNTECH-CHASSIS-STATUS-MIB", "uimStaIndex"),
)
if mibBuilder.loadTexts:
    uimStaEntry.setStatus("current")


class _UimStaMumIndex_Type(Integer32):
    """Custom type uimStaMumIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_UimStaMumIndex_Type.__name__ = "Integer32"
_UimStaMumIndex_Object = MibTableColumn
uimStaMumIndex = _UimStaMumIndex_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 2, 1, 1, 1, 6, 1, 1, 1),
    _UimStaMumIndex_Type()
)
uimStaMumIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uimStaMumIndex.setStatus("current")


class _UimStaIndex_Type(Integer32):
    """Custom type uimStaIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_UimStaIndex_Type.__name__ = "Integer32"
_UimStaIndex_Object = MibTableColumn
uimStaIndex = _UimStaIndex_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 2, 1, 1, 1, 6, 1, 1, 2),
    _UimStaIndex_Type()
)
uimStaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uimStaIndex.setStatus("current")


class _UimStaType_Type(Integer32):
    """Custom type uimStaType based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("uim100Fx", 8),
          ("uimDS3", 3),
          ("uimE1", 4),
          ("uimE3", 5),
          ("uimEther100", 1),
          ("uimGig", 6),
          ("uimGigFx", 7),
          ("uimT1", 2))
    )


_UimStaType_Type.__name__ = "Integer32"
_UimStaType_Object = MibTableColumn
uimStaType = _UimStaType_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 2, 1, 1, 1, 6, 1, 1, 3),
    _UimStaType_Type()
)
uimStaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uimStaType.setStatus("current")


class _UimStaLinkState_Type(Integer32):
    """Custom type uimStaLinkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fault", 3),
          ("link", 1),
          ("noLink", 2))
    )


_UimStaLinkState_Type.__name__ = "Integer32"
_UimStaLinkState_Object = MibTableColumn
uimStaLinkState = _UimStaLinkState_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 2, 1, 1, 1, 6, 1, 1, 4),
    _UimStaLinkState_Type()
)
uimStaLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uimStaLinkState.setStatus("current")
_UimStaEthTable_Object = MibTable
uimStaEthTable = _UimStaEthTable_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 2, 1, 1, 1, 6, 2)
)
if mibBuilder.loadTexts:
    uimStaEthTable.setStatus("current")
_UimStaEthEntry_Object = MibTableRow
uimStaEthEntry = _UimStaEthEntry_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 2, 1, 1, 1, 6, 2, 1)
)
uimStaEthEntry.setIndexNames(
    (0, "NTNTECH-CHASSIS-STATUS-MIB", "uimStaEthMumIndex"),
    (0, "NTNTECH-CHASSIS-STATUS-MIB", "uimStaEthIndex"),
)
if mibBuilder.loadTexts:
    uimStaEthEntry.setStatus("current")


class _UimStaEthMumIndex_Type(Integer32):
    """Custom type uimStaEthMumIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_UimStaEthMumIndex_Type.__name__ = "Integer32"
_UimStaEthMumIndex_Object = MibTableColumn
uimStaEthMumIndex = _UimStaEthMumIndex_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 2, 1, 1, 1, 6, 2, 1, 1),
    _UimStaEthMumIndex_Type()
)
uimStaEthMumIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uimStaEthMumIndex.setStatus("current")


class _UimStaEthIndex_Type(Integer32):
    """Custom type uimStaEthIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_UimStaEthIndex_Type.__name__ = "Integer32"
_UimStaEthIndex_Object = MibTableColumn
uimStaEthIndex = _UimStaEthIndex_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 2, 1, 1, 1, 6, 2, 1, 2),
    _UimStaEthIndex_Type()
)
uimStaEthIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uimStaEthIndex.setStatus("current")


class _UimStaEthRxTxRate_Type(Integer32):
    """Custom type uimStaEthRxTxRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("uimEth10", 1),
          ("uimEth100", 2),
          ("uimEthGig", 3),
          ("uimEthNoLink", 0))
    )


_UimStaEthRxTxRate_Type.__name__ = "Integer32"
_UimStaEthRxTxRate_Object = MibTableColumn
uimStaEthRxTxRate = _UimStaEthRxTxRate_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 2, 1, 1, 1, 6, 2, 1, 3),
    _UimStaEthRxTxRate_Type()
)
uimStaEthRxTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uimStaEthRxTxRate.setStatus("current")


class _UimStaEthDuplex_Type(Integer32):
    """Custom type uimStaEthDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("uimEthFull", 2),
          ("uimEthHalf", 1),
          ("uimEthNoLink", 0))
    )


_UimStaEthDuplex_Type.__name__ = "Integer32"
_UimStaEthDuplex_Object = MibTableColumn
uimStaEthDuplex = _UimStaEthDuplex_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 2, 1, 1, 1, 6, 2, 1, 4),
    _UimStaEthDuplex_Type()
)
uimStaEthDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uimStaEthDuplex.setStatus("current")
_UimStaT1Table_Object = MibTable
uimStaT1Table = _UimStaT1Table_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 2, 1, 1, 1, 6, 3)
)
if mibBuilder.loadTexts:
    uimStaT1Table.setStatus("current")
_UimStaT1Entry_Object = MibTableRow
uimStaT1Entry = _UimStaT1Entry_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 2, 1, 1, 1, 6, 3, 1)
)
uimStaT1Entry.setIndexNames(
    (0, "NTNTECH-CHASSIS-STATUS-MIB", "uimStaT1MumIndex"),
    (0, "NTNTECH-CHASSIS-STATUS-MIB", "uimStaT1Index"),
)
if mibBuilder.loadTexts:
    uimStaT1Entry.setStatus("current")


class _UimStaT1MumIndex_Type(Integer32):
    """Custom type uimStaT1MumIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_UimStaT1MumIndex_Type.__name__ = "Integer32"
_UimStaT1MumIndex_Object = MibTableColumn
uimStaT1MumIndex = _UimStaT1MumIndex_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 2, 1, 1, 1, 6, 3, 1, 1),
    _UimStaT1MumIndex_Type()
)
uimStaT1MumIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uimStaT1MumIndex.setStatus("current")


class _UimStaT1Index_Type(Integer32):
    """Custom type uimStaT1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_UimStaT1Index_Type.__name__ = "Integer32"
_UimStaT1Index_Object = MibTableColumn
uimStaT1Index = _UimStaT1Index_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 2, 1, 1, 1, 6, 3, 1, 2),
    _UimStaT1Index_Type()
)
uimStaT1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uimStaT1Index.setStatus("current")


class _UimStaT1RxTxRate_Type(Integer32):
    """Custom type uimStaT1RxTxRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("uimT1NoLink", 0),
          ("uimT1Rate1152", 6),
          ("uimT1Rate1344", 7),
          ("uimT1Rate1536", 8),
          ("uimT1Rate192", 1),
          ("uimT1Rate384", 2),
          ("uimT1Rate576", 3),
          ("uimT1Rate768", 4),
          ("uimT1Rate960", 5))
    )


_UimStaT1RxTxRate_Type.__name__ = "Integer32"
_UimStaT1RxTxRate_Object = MibTableColumn
uimStaT1RxTxRate = _UimStaT1RxTxRate_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 2, 1, 1, 1, 6, 3, 1, 3),
    _UimStaT1RxTxRate_Type()
)
uimStaT1RxTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uimStaT1RxTxRate.setStatus("current")
_UimStaE1Table_Object = MibTable
uimStaE1Table = _UimStaE1Table_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 2, 1, 1, 1, 6, 4)
)
if mibBuilder.loadTexts:
    uimStaE1Table.setStatus("current")
_UimStaE1Entry_Object = MibTableRow
uimStaE1Entry = _UimStaE1Entry_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 2, 1, 1, 1, 6, 4, 1)
)
uimStaE1Entry.setIndexNames(
    (0, "NTNTECH-CHASSIS-STATUS-MIB", "uimStaE1MumIndex"),
    (0, "NTNTECH-CHASSIS-STATUS-MIB", "uimStaE1Index"),
)
if mibBuilder.loadTexts:
    uimStaE1Entry.setStatus("current")


class _UimStaE1MumIndex_Type(Integer32):
    """Custom type uimStaE1MumIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_UimStaE1MumIndex_Type.__name__ = "Integer32"
_UimStaE1MumIndex_Object = MibTableColumn
uimStaE1MumIndex = _UimStaE1MumIndex_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 2, 1, 1, 1, 6, 4, 1, 1),
    _UimStaE1MumIndex_Type()
)
uimStaE1MumIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uimStaE1MumIndex.setStatus("current")


class _UimStaE1Index_Type(Integer32):
    """Custom type uimStaE1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_UimStaE1Index_Type.__name__ = "Integer32"
_UimStaE1Index_Object = MibTableColumn
uimStaE1Index = _UimStaE1Index_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 2, 1, 1, 1, 6, 4, 1, 2),
    _UimStaE1Index_Type()
)
uimStaE1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uimStaE1Index.setStatus("current")


class _UimStaE1RxTxRate_Type(Integer32):
    """Custom type uimStaE1RxTxRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("uimE1NoLink", 0),
          ("uimE1Rate1024", 4),
          ("uimE1Rate1280", 5),
          ("uimE1Rate1536", 6),
          ("uimE1Rate1792", 7),
          ("uimE1Rate1984", 8),
          ("uimE1Rate256", 1),
          ("uimE1Rate512", 2),
          ("uimE1Rate768", 3))
    )


_UimStaE1RxTxRate_Type.__name__ = "Integer32"
_UimStaE1RxTxRate_Object = MibTableColumn
uimStaE1RxTxRate = _UimStaE1RxTxRate_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 2, 1, 1, 1, 6, 4, 1, 3),
    _UimStaE1RxTxRate_Type()
)
uimStaE1RxTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uimStaE1RxTxRate.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NTNTECH-CHASSIS-STATUS-MIB",
    **{"ntntechChassisStatusMIB": ntntechChassisStatusMIB,
       "chsStaMIBObjects": chsStaMIBObjects,
       "chsStaValues": chsStaValues,
       "valMultiplexerUplinkModule": valMultiplexerUplinkModule,
       "mumStaChassisType": mumStaChassisType,
       "mumStaFanState": mumStaFanState,
       "mumStaTable": mumStaTable,
       "mumStaEntry": mumStaEntry,
       "mumStaIndex": mumStaIndex,
       "mumStaMacAddress": mumStaMacAddress,
       "mumStaFirmWareRev": mumStaFirmWareRev,
       "mumStaType": mumStaType,
       "mumStaMgmtPortTable": mumStaMgmtPortTable,
       "mumStaMgmtPortEntry": mumStaMgmtPortEntry,
       "mumStaMgmtPortMumIndex": mumStaMgmtPortMumIndex,
       "mumStaMgmtPortType": mumStaMgmtPortType,
       "mumStaMgmtPortLinkState": mumStaMgmtPortLinkState,
       "mumStaMgmtPortRxTxRate": mumStaMgmtPortRxTxRate,
       "mumStaMgmtPortDuplex": mumStaMgmtPortDuplex,
       "mumStaUplinkInterfaceModule": mumStaUplinkInterfaceModule,
       "uimStaTable": uimStaTable,
       "uimStaEntry": uimStaEntry,
       "uimStaMumIndex": uimStaMumIndex,
       "uimStaIndex": uimStaIndex,
       "uimStaType": uimStaType,
       "uimStaLinkState": uimStaLinkState,
       "uimStaEthTable": uimStaEthTable,
       "uimStaEthEntry": uimStaEthEntry,
       "uimStaEthMumIndex": uimStaEthMumIndex,
       "uimStaEthIndex": uimStaEthIndex,
       "uimStaEthRxTxRate": uimStaEthRxTxRate,
       "uimStaEthDuplex": uimStaEthDuplex,
       "uimStaT1Table": uimStaT1Table,
       "uimStaT1Entry": uimStaT1Entry,
       "uimStaT1MumIndex": uimStaT1MumIndex,
       "uimStaT1Index": uimStaT1Index,
       "uimStaT1RxTxRate": uimStaT1RxTxRate,
       "uimStaE1Table": uimStaE1Table,
       "uimStaE1Entry": uimStaE1Entry,
       "uimStaE1MumIndex": uimStaE1MumIndex,
       "uimStaE1Index": uimStaE1Index,
       "uimStaE1RxTxRate": uimStaE1RxTxRate}
)
