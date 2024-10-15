# SNMP MIB module (CISCO-ATM-SWITCH-FR-IWF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ATM-SWITCH-FR-IWF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:56:02 2024
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

(AtmTrafficDescrParamIndex,) = mibBuilder.importSymbols(
    "ATM-MIB",
    "AtmTrafficDescrParamIndex")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(Unsigned32,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "Unsigned32")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
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
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoAtmSwitchFrIwfMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 112)
)
ciscoAtmSwitchFrIwfMIB.setRevisions(
        ("2001-05-20 00:00",
         "2000-02-29 00:00",
         "1998-07-09 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CasfTrafficDescrRow(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class DlciValue(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4194303),
    )



class ConnectionKind(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("pvc", 1),
          ("spvcInitiator", 4),
          ("spvcTarget", 5),
          ("svcIncoming", 2),
          ("svcOutgoing", 3))
    )



class AtmAddr(OctetString, TextualConvention):
    status = "current"
    displayHint = "1x"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoAtmSwitchFrIwfMIBObjects_ObjectIdentity = ObjectIdentity
ciscoAtmSwitchFrIwfMIBObjects = _CiscoAtmSwitchFrIwfMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1)
)
_CasfFrTraffic_ObjectIdentity = ObjectIdentity
casfFrTraffic = _CasfFrTraffic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 1)
)
_CasfTrafficDescrTable_Object = MibTable
casfTrafficDescrTable = _CasfTrafficDescrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 1, 1)
)
if mibBuilder.loadTexts:
    casfTrafficDescrTable.setStatus("current")
_CasfTrafficDescrEntry_Object = MibTableRow
casfTrafficDescrEntry = _CasfTrafficDescrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 1, 1, 1)
)
casfTrafficDescrEntry.setIndexNames(
    (0, "CISCO-ATM-SWITCH-FR-IWF-MIB", "casfTrafficDescrIndex"),
)
if mibBuilder.loadTexts:
    casfTrafficDescrEntry.setStatus("current")
_CasfTrafficDescrIndex_Type = CasfTrafficDescrRow
_CasfTrafficDescrIndex_Object = MibTableColumn
casfTrafficDescrIndex = _CasfTrafficDescrIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 1, 1, 1, 1),
    _CasfTrafficDescrIndex_Type()
)
casfTrafficDescrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    casfTrafficDescrIndex.setStatus("current")
_CasfTrafficDescrCIR_Type = Unsigned32
_CasfTrafficDescrCIR_Object = MibTableColumn
casfTrafficDescrCIR = _CasfTrafficDescrCIR_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 1, 1, 1, 2),
    _CasfTrafficDescrCIR_Type()
)
casfTrafficDescrCIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    casfTrafficDescrCIR.setStatus("current")
if mibBuilder.loadTexts:
    casfTrafficDescrCIR.setUnits("bits/sec")
_CasfTrafficDescrBc_Type = Unsigned32
_CasfTrafficDescrBc_Object = MibTableColumn
casfTrafficDescrBc = _CasfTrafficDescrBc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 1, 1, 1, 3),
    _CasfTrafficDescrBc_Type()
)
casfTrafficDescrBc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    casfTrafficDescrBc.setStatus("current")
if mibBuilder.loadTexts:
    casfTrafficDescrBc.setUnits("bits")
_CasfTrafficDescrBe_Type = Unsigned32
_CasfTrafficDescrBe_Object = MibTableColumn
casfTrafficDescrBe = _CasfTrafficDescrBe_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 1, 1, 1, 4),
    _CasfTrafficDescrBe_Type()
)
casfTrafficDescrBe.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    casfTrafficDescrBe.setStatus("current")
if mibBuilder.loadTexts:
    casfTrafficDescrBe.setUnits("bits")
_CasfTrafficDescrPIR_Type = Unsigned32
_CasfTrafficDescrPIR_Object = MibTableColumn
casfTrafficDescrPIR = _CasfTrafficDescrPIR_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 1, 1, 1, 5),
    _CasfTrafficDescrPIR_Type()
)
casfTrafficDescrPIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    casfTrafficDescrPIR.setStatus("current")
if mibBuilder.loadTexts:
    casfTrafficDescrPIR.setUnits("bits/sec")


class _CasfTrafficDescrServCategory_Type(Integer32):
    """Custom type casfTrafficDescrServCategory based on Integer32"""
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
        *(("abr", 2),
          ("ubr", 3),
          ("vbrNrt", 1),
          ("vbrRt", 4))
    )


_CasfTrafficDescrServCategory_Type.__name__ = "Integer32"
_CasfTrafficDescrServCategory_Object = MibTableColumn
casfTrafficDescrServCategory = _CasfTrafficDescrServCategory_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 1, 1, 1, 6),
    _CasfTrafficDescrServCategory_Type()
)
casfTrafficDescrServCategory.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    casfTrafficDescrServCategory.setStatus("current")
_CasfTrafficDescrAtmIndex_Type = AtmTrafficDescrParamIndex
_CasfTrafficDescrAtmIndex_Object = MibTableColumn
casfTrafficDescrAtmIndex = _CasfTrafficDescrAtmIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 1, 1, 1, 7),
    _CasfTrafficDescrAtmIndex_Type()
)
casfTrafficDescrAtmIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    casfTrafficDescrAtmIndex.setStatus("current")
_CasfTrafficDescrRowStatus_Type = RowStatus
_CasfTrafficDescrRowStatus_Object = MibTableColumn
casfTrafficDescrRowStatus = _CasfTrafficDescrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 1, 1, 1, 8),
    _CasfTrafficDescrRowStatus_Type()
)
casfTrafficDescrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    casfTrafficDescrRowStatus.setStatus("current")
_CasfFrVC_ObjectIdentity = ObjectIdentity
casfFrVC = _CasfFrVC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 2)
)
_CasfVcEndptTable_Object = MibTable
casfVcEndptTable = _CasfVcEndptTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 2, 1)
)
if mibBuilder.loadTexts:
    casfVcEndptTable.setStatus("current")
_CasfVcEndptEntry_Object = MibTableRow
casfVcEndptEntry = _CasfVcEndptEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 2, 1, 1)
)
casfVcEndptEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-ATM-SWITCH-FR-IWF-MIB", "casfVcEndptDlci"),
)
if mibBuilder.loadTexts:
    casfVcEndptEntry.setStatus("current")
_CasfVcEndptDlci_Type = DlciValue
_CasfVcEndptDlci_Object = MibTableColumn
casfVcEndptDlci = _CasfVcEndptDlci_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 2, 1, 1, 1),
    _CasfVcEndptDlci_Type()
)
casfVcEndptDlci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    casfVcEndptDlci.setStatus("current")
_CasfVcEndptRxTrafficDescrRow_Type = CasfTrafficDescrRow
_CasfVcEndptRxTrafficDescrRow_Object = MibTableColumn
casfVcEndptRxTrafficDescrRow = _CasfVcEndptRxTrafficDescrRow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 2, 1, 1, 2),
    _CasfVcEndptRxTrafficDescrRow_Type()
)
casfVcEndptRxTrafficDescrRow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    casfVcEndptRxTrafficDescrRow.setStatus("current")
_CasfVcEndptTxTrafficDescrRow_Type = CasfTrafficDescrRow
_CasfVcEndptTxTrafficDescrRow_Object = MibTableColumn
casfVcEndptTxTrafficDescrRow = _CasfVcEndptTxTrafficDescrRow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 2, 1, 1, 3),
    _CasfVcEndptTxTrafficDescrRow_Type()
)
casfVcEndptTxTrafficDescrRow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    casfVcEndptTxTrafficDescrRow.setStatus("current")
_CasfVcEndptRxNegTrafficDescrRow_Type = CasfTrafficDescrRow
_CasfVcEndptRxNegTrafficDescrRow_Object = MibTableColumn
casfVcEndptRxNegTrafficDescrRow = _CasfVcEndptRxNegTrafficDescrRow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 2, 1, 1, 4),
    _CasfVcEndptRxNegTrafficDescrRow_Type()
)
casfVcEndptRxNegTrafficDescrRow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casfVcEndptRxNegTrafficDescrRow.setStatus("current")
_CasfVcEndptTxNegTrafficDescrRow_Type = CasfTrafficDescrRow
_CasfVcEndptTxNegTrafficDescrRow_Object = MibTableColumn
casfVcEndptTxNegTrafficDescrRow = _CasfVcEndptTxNegTrafficDescrRow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 2, 1, 1, 5),
    _CasfVcEndptTxNegTrafficDescrRow_Type()
)
casfVcEndptTxNegTrafficDescrRow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casfVcEndptTxNegTrafficDescrRow.setStatus("current")


class _CasfVcEndptConnKind_Type(ConnectionKind):
    """Custom type casfVcEndptConnKind based on ConnectionKind"""


_CasfVcEndptConnKind_Object = MibTableColumn
casfVcEndptConnKind = _CasfVcEndptConnKind_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 2, 1, 1, 6),
    _CasfVcEndptConnKind_Type()
)
casfVcEndptConnKind.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    casfVcEndptConnKind.setStatus("current")


class _CasfVcEndptIwfType_Type(Integer32):
    """Custom type casfVcEndptIwfType based on Integer32"""
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
        *(("network", 1),
          ("rfc1973", 4),
          ("serviceTranslation", 3),
          ("serviceTransparent", 2))
    )


_CasfVcEndptIwfType_Type.__name__ = "Integer32"
_CasfVcEndptIwfType_Object = MibTableColumn
casfVcEndptIwfType = _CasfVcEndptIwfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 2, 1, 1, 7),
    _CasfVcEndptIwfType_Type()
)
casfVcEndptIwfType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    casfVcEndptIwfType.setStatus("current")


class _CasfVcEndptClpMode_Type(Integer32):
    """Custom type casfVcEndptClpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clpIfDe", 1),
          ("clpIsOne", 3),
          ("clpIsZero", 2))
    )


_CasfVcEndptClpMode_Type.__name__ = "Integer32"
_CasfVcEndptClpMode_Object = MibTableColumn
casfVcEndptClpMode = _CasfVcEndptClpMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 2, 1, 1, 8),
    _CasfVcEndptClpMode_Type()
)
casfVcEndptClpMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    casfVcEndptClpMode.setStatus("current")


class _CasfVcEndptDeMode_Type(Integer32):
    """Custom type casfVcEndptDeMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("deIfClp", 3),
          ("deIfClpOrFrsscsDe", 1),
          ("deIfFrsscsDe", 2),
          ("deIsOne", 5),
          ("deIsZero", 4))
    )


_CasfVcEndptDeMode_Type.__name__ = "Integer32"
_CasfVcEndptDeMode_Object = MibTableColumn
casfVcEndptDeMode = _CasfVcEndptDeMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 2, 1, 1, 9),
    _CasfVcEndptDeMode_Type()
)
casfVcEndptDeMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    casfVcEndptDeMode.setStatus("current")


class _CasfVcEndptEfciMode_Type(Integer32):
    """Custom type casfVcEndptEfciMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("efciIfFecn", 1),
          ("efciIsZero", 2))
    )


_CasfVcEndptEfciMode_Type.__name__ = "Integer32"
_CasfVcEndptEfciMode_Object = MibTableColumn
casfVcEndptEfciMode = _CasfVcEndptEfciMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 2, 1, 1, 10),
    _CasfVcEndptEfciMode_Type()
)
casfVcEndptEfciMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    casfVcEndptEfciMode.setStatus("current")


class _CasfVcEndptUpcMode_Type(Integer32):
    """Custom type casfVcEndptUpcMode based on Integer32"""
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
        *(("drop", 4),
          ("pass", 1),
          ("tag", 3),
          ("tagDrop", 2))
    )


_CasfVcEndptUpcMode_Type.__name__ = "Integer32"
_CasfVcEndptUpcMode_Object = MibTableColumn
casfVcEndptUpcMode = _CasfVcEndptUpcMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 2, 1, 1, 11),
    _CasfVcEndptUpcMode_Type()
)
casfVcEndptUpcMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    casfVcEndptUpcMode.setStatus("current")
_CasfVcEndptSpvcRemoteAddr_Type = AtmAddr
_CasfVcEndptSpvcRemoteAddr_Object = MibTableColumn
casfVcEndptSpvcRemoteAddr = _CasfVcEndptSpvcRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 2, 1, 1, 12),
    _CasfVcEndptSpvcRemoteAddr_Type()
)
casfVcEndptSpvcRemoteAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    casfVcEndptSpvcRemoteAddr.setStatus("current")


class _CasfVcEndptSpvcRemoteType_Type(Integer32):
    """Custom type casfVcEndptSpvcRemoteType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("atm", 3),
          ("frameRelay", 2),
          ("other", 1))
    )


_CasfVcEndptSpvcRemoteType_Type.__name__ = "Integer32"
_CasfVcEndptSpvcRemoteType_Object = MibTableColumn
casfVcEndptSpvcRemoteType = _CasfVcEndptSpvcRemoteType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 2, 1, 1, 13),
    _CasfVcEndptSpvcRemoteType_Type()
)
casfVcEndptSpvcRemoteType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    casfVcEndptSpvcRemoteType.setStatus("current")
_CasfVcEndptSpvcRemoteDlci_Type = DlciValue
_CasfVcEndptSpvcRemoteDlci_Object = MibTableColumn
casfVcEndptSpvcRemoteDlci = _CasfVcEndptSpvcRemoteDlci_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 2, 1, 1, 14),
    _CasfVcEndptSpvcRemoteDlci_Type()
)
casfVcEndptSpvcRemoteDlci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    casfVcEndptSpvcRemoteDlci.setStatus("current")


class _CasfVcEndptSpvcRemoteVpi_Type(Integer32):
    """Custom type casfVcEndptSpvcRemoteVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CasfVcEndptSpvcRemoteVpi_Type.__name__ = "Integer32"
_CasfVcEndptSpvcRemoteVpi_Object = MibTableColumn
casfVcEndptSpvcRemoteVpi = _CasfVcEndptSpvcRemoteVpi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 2, 1, 1, 15),
    _CasfVcEndptSpvcRemoteVpi_Type()
)
casfVcEndptSpvcRemoteVpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    casfVcEndptSpvcRemoteVpi.setStatus("current")


class _CasfVcEndptSpvcRemoteVci_Type(Integer32):
    """Custom type casfVcEndptSpvcRemoteVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CasfVcEndptSpvcRemoteVci_Type.__name__ = "Integer32"
_CasfVcEndptSpvcRemoteVci_Object = MibTableColumn
casfVcEndptSpvcRemoteVci = _CasfVcEndptSpvcRemoteVci_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 2, 1, 1, 16),
    _CasfVcEndptSpvcRemoteVci_Type()
)
casfVcEndptSpvcRemoteVci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    casfVcEndptSpvcRemoteVci.setStatus("current")
_CasfVcEndptCreationTime_Type = TimeStamp
_CasfVcEndptCreationTime_Object = MibTableColumn
casfVcEndptCreationTime = _CasfVcEndptCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 2, 1, 1, 17),
    _CasfVcEndptCreationTime_Type()
)
casfVcEndptCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casfVcEndptCreationTime.setStatus("current")


class _CasfVcEndptRcvdSigStatus_Type(Integer32):
    """Custom type casfVcEndptRcvdSigStatus based on Integer32"""
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
        *(("active", 2),
          ("deleted", 1),
          ("inactive", 3),
          ("none", 4))
    )


_CasfVcEndptRcvdSigStatus_Type.__name__ = "Integer32"
_CasfVcEndptRcvdSigStatus_Object = MibTableColumn
casfVcEndptRcvdSigStatus = _CasfVcEndptRcvdSigStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 2, 1, 1, 18),
    _CasfVcEndptRcvdSigStatus_Type()
)
casfVcEndptRcvdSigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casfVcEndptRcvdSigStatus.setStatus("current")
_CasfVcEndptRowStatus_Type = RowStatus
_CasfVcEndptRowStatus_Object = MibTableColumn
casfVcEndptRowStatus = _CasfVcEndptRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 2, 1, 1, 19),
    _CasfVcEndptRowStatus_Type()
)
casfVcEndptRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    casfVcEndptRowStatus.setStatus("current")


class _CasfVcSignalStandardCalledIe_Type(TruthValue):
    """Custom type casfVcSignalStandardCalledIe based on TruthValue"""


_CasfVcSignalStandardCalledIe_Object = MibTableColumn
casfVcSignalStandardCalledIe = _CasfVcSignalStandardCalledIe_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 2, 1, 1, 20),
    _CasfVcSignalStandardCalledIe_Type()
)
casfVcSignalStandardCalledIe.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    casfVcSignalStandardCalledIe.setStatus("current")
_CasfFrInterface_ObjectIdentity = ObjectIdentity
casfFrInterface = _CasfFrInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 3)
)
_CasfFrLmiTable_Object = MibTable
casfFrLmiTable = _CasfFrLmiTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 3, 1)
)
if mibBuilder.loadTexts:
    casfFrLmiTable.setStatus("current")
_CasfFrLmiEntry_Object = MibTableRow
casfFrLmiEntry = _CasfFrLmiEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 3, 1, 1)
)
casfFrLmiEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    casfFrLmiEntry.setStatus("current")


class _CasfFrLmiProtocol_Type(Integer32):
    """Custom type casfFrLmiProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ansiT1617B", 4),
          ("ansiT1617D", 3),
          ("ccittQ933A", 5),
          ("lmi", 2),
          ("none", 1))
    )


_CasfFrLmiProtocol_Type.__name__ = "Integer32"
_CasfFrLmiProtocol_Object = MibTableColumn
casfFrLmiProtocol = _CasfFrLmiProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 3, 1, 1, 1),
    _CasfFrLmiProtocol_Type()
)
casfFrLmiProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    casfFrLmiProtocol.setStatus("current")


class _CasfFrLmiType_Type(Integer32):
    """Custom type casfFrLmiType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dce", 2),
          ("dte", 1),
          ("nni", 3))
    )


_CasfFrLmiType_Type.__name__ = "Integer32"
_CasfFrLmiType_Object = MibTableColumn
casfFrLmiType = _CasfFrLmiType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 3, 1, 1, 2),
    _CasfFrLmiType_Type()
)
casfFrLmiType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    casfFrLmiType.setStatus("current")


class _CasfFrLmiUserN391_Type(Integer32):
    """Custom type casfFrLmiUserN391 based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CasfFrLmiUserN391_Type.__name__ = "Integer32"
_CasfFrLmiUserN391_Object = MibTableColumn
casfFrLmiUserN391 = _CasfFrLmiUserN391_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 3, 1, 1, 3),
    _CasfFrLmiUserN391_Type()
)
casfFrLmiUserN391.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    casfFrLmiUserN391.setStatus("current")


class _CasfFrLmiUserN392_Type(Integer32):
    """Custom type casfFrLmiUserN392 based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_CasfFrLmiUserN392_Type.__name__ = "Integer32"
_CasfFrLmiUserN392_Object = MibTableColumn
casfFrLmiUserN392 = _CasfFrLmiUserN392_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 3, 1, 1, 4),
    _CasfFrLmiUserN392_Type()
)
casfFrLmiUserN392.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    casfFrLmiUserN392.setStatus("current")


class _CasfFrLmiUserN393_Type(Integer32):
    """Custom type casfFrLmiUserN393 based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_CasfFrLmiUserN393_Type.__name__ = "Integer32"
_CasfFrLmiUserN393_Object = MibTableColumn
casfFrLmiUserN393 = _CasfFrLmiUserN393_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 3, 1, 1, 5),
    _CasfFrLmiUserN393_Type()
)
casfFrLmiUserN393.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    casfFrLmiUserN393.setStatus("current")


class _CasfFrLmiUserT391_Type(Integer32):
    """Custom type casfFrLmiUserT391 based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_CasfFrLmiUserT391_Type.__name__ = "Integer32"
_CasfFrLmiUserT391_Object = MibTableColumn
casfFrLmiUserT391 = _CasfFrLmiUserT391_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 3, 1, 1, 6),
    _CasfFrLmiUserT391_Type()
)
casfFrLmiUserT391.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    casfFrLmiUserT391.setStatus("current")
if mibBuilder.loadTexts:
    casfFrLmiUserT391.setUnits("seconds")


class _CasfFrLmiNetN392_Type(Integer32):
    """Custom type casfFrLmiNetN392 based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_CasfFrLmiNetN392_Type.__name__ = "Integer32"
_CasfFrLmiNetN392_Object = MibTableColumn
casfFrLmiNetN392 = _CasfFrLmiNetN392_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 3, 1, 1, 7),
    _CasfFrLmiNetN392_Type()
)
casfFrLmiNetN392.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    casfFrLmiNetN392.setStatus("current")


class _CasfFrLmiNetN393_Type(Integer32):
    """Custom type casfFrLmiNetN393 based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_CasfFrLmiNetN393_Type.__name__ = "Integer32"
_CasfFrLmiNetN393_Object = MibTableColumn
casfFrLmiNetN393 = _CasfFrLmiNetN393_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 3, 1, 1, 8),
    _CasfFrLmiNetN393_Type()
)
casfFrLmiNetN393.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    casfFrLmiNetN393.setStatus("current")


class _CasfFrLmiNetT392_Type(Integer32):
    """Custom type casfFrLmiNetT392 based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_CasfFrLmiNetT392_Type.__name__ = "Integer32"
_CasfFrLmiNetT392_Object = MibTableColumn
casfFrLmiNetT392 = _CasfFrLmiNetT392_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 3, 1, 1, 9),
    _CasfFrLmiNetT392_Type()
)
casfFrLmiNetT392.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    casfFrLmiNetT392.setStatus("current")
if mibBuilder.loadTexts:
    casfFrLmiNetT392.setUnits("seconds")
_CasfFrLmiEnquiryIns_Type = Counter32
_CasfFrLmiEnquiryIns_Object = MibTableColumn
casfFrLmiEnquiryIns = _CasfFrLmiEnquiryIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 3, 1, 1, 10),
    _CasfFrLmiEnquiryIns_Type()
)
casfFrLmiEnquiryIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casfFrLmiEnquiryIns.setStatus("current")
if mibBuilder.loadTexts:
    casfFrLmiEnquiryIns.setUnits("messages")
_CasfFrLmiEnquiryOuts_Type = Counter32
_CasfFrLmiEnquiryOuts_Object = MibTableColumn
casfFrLmiEnquiryOuts = _CasfFrLmiEnquiryOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 3, 1, 1, 11),
    _CasfFrLmiEnquiryOuts_Type()
)
casfFrLmiEnquiryOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casfFrLmiEnquiryOuts.setStatus("current")
if mibBuilder.loadTexts:
    casfFrLmiEnquiryOuts.setUnits("messages")
_CasfFrLmiStatusIns_Type = Counter32
_CasfFrLmiStatusIns_Object = MibTableColumn
casfFrLmiStatusIns = _CasfFrLmiStatusIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 3, 1, 1, 12),
    _CasfFrLmiStatusIns_Type()
)
casfFrLmiStatusIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casfFrLmiStatusIns.setStatus("current")
if mibBuilder.loadTexts:
    casfFrLmiStatusIns.setUnits("messages")
_CasfFrLmiStatusOuts_Type = Counter32
_CasfFrLmiStatusOuts_Object = MibTableColumn
casfFrLmiStatusOuts = _CasfFrLmiStatusOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 3, 1, 1, 13),
    _CasfFrLmiStatusOuts_Type()
)
casfFrLmiStatusOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casfFrLmiStatusOuts.setStatus("current")
if mibBuilder.loadTexts:
    casfFrLmiStatusOuts.setUnits("messages")
_CasfFrLmiStatusTimeouts_Type = Counter32
_CasfFrLmiStatusTimeouts_Object = MibTableColumn
casfFrLmiStatusTimeouts = _CasfFrLmiStatusTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 3, 1, 1, 14),
    _CasfFrLmiStatusTimeouts_Type()
)
casfFrLmiStatusTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casfFrLmiStatusTimeouts.setStatus("current")
_CasfFrLmiStatusEnqTimeouts_Type = Counter32
_CasfFrLmiStatusEnqTimeouts_Object = MibTableColumn
casfFrLmiStatusEnqTimeouts = _CasfFrLmiStatusEnqTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 3, 1, 1, 15),
    _CasfFrLmiStatusEnqTimeouts_Type()
)
casfFrLmiStatusEnqTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casfFrLmiStatusEnqTimeouts.setStatus("current")
_CasfConfIfTable_Object = MibTable
casfConfIfTable = _CasfConfIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 3, 2)
)
if mibBuilder.loadTexts:
    casfConfIfTable.setStatus("current")
_CasfConfIfEntry_Object = MibTableRow
casfConfIfEntry = _CasfConfIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 3, 2, 1)
)
casfConfIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    casfConfIfEntry.setStatus("current")
_CasfConfIfAtmAddress_Type = AtmAddr
_CasfConfIfAtmAddress_Object = MibTableColumn
casfConfIfAtmAddress = _CasfConfIfAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 3, 2, 1, 1),
    _CasfConfIfAtmAddress_Type()
)
casfConfIfAtmAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casfConfIfAtmAddress.setStatus("current")


class _CasfConfIfUpcIntent_Type(Integer32):
    """Custom type casfConfIfUpcIntent based on Integer32"""
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
        *(("drop", 4),
          ("pass", 1),
          ("tag", 3),
          ("tagDrop", 2))
    )


_CasfConfIfUpcIntent_Type.__name__ = "Integer32"
_CasfConfIfUpcIntent_Object = MibTableColumn
casfConfIfUpcIntent = _CasfConfIfUpcIntent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 3, 2, 1, 2),
    _CasfConfIfUpcIntent_Type()
)
casfConfIfUpcIntent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    casfConfIfUpcIntent.setStatus("current")


class _CasfConfIfBcDefault_Type(Integer32):
    """Custom type casfConfIfBcDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32768),
    )


_CasfConfIfBcDefault_Type.__name__ = "Integer32"
_CasfConfIfBcDefault_Object = MibTableColumn
casfConfIfBcDefault = _CasfConfIfBcDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 3, 2, 1, 3),
    _CasfConfIfBcDefault_Type()
)
casfConfIfBcDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    casfConfIfBcDefault.setStatus("current")
if mibBuilder.loadTexts:
    casfConfIfBcDefault.setUnits("bits")


class _CasfConfIfCledSpvcDeModeDef_Type(Integer32):
    """Custom type casfConfIfCledSpvcDeModeDef based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deIfClpOrFrsscsDe", 1),
          ("deIfFrsscsDe", 2))
    )


_CasfConfIfCledSpvcDeModeDef_Type.__name__ = "Integer32"
_CasfConfIfCledSpvcDeModeDef_Object = MibTableColumn
casfConfIfCledSpvcDeModeDef = _CasfConfIfCledSpvcDeModeDef_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 3, 2, 1, 4),
    _CasfConfIfCledSpvcDeModeDef_Type()
)
casfConfIfCledSpvcDeModeDef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    casfConfIfCledSpvcDeModeDef.setStatus("current")


class _CasfConfIfCledSpvcClpModeDef_Type(Integer32):
    """Custom type casfConfIfCledSpvcClpModeDef based on Integer32"""
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
        *(("clpIfDe", 1),
          ("clpIfIsOne", 3),
          ("clpIfIsZero", 2))
    )


_CasfConfIfCledSpvcClpModeDef_Type.__name__ = "Integer32"
_CasfConfIfCledSpvcClpModeDef_Object = MibTableColumn
casfConfIfCledSpvcClpModeDef = _CasfConfIfCledSpvcClpModeDef_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 3, 2, 1, 5),
    _CasfConfIfCledSpvcClpModeDef_Type()
)
casfConfIfCledSpvcClpModeDef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    casfConfIfCledSpvcClpModeDef.setStatus("current")
_CasfFrCounts_ObjectIdentity = ObjectIdentity
casfFrCounts = _CasfFrCounts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 4)
)
_CasfVcCountTable_Object = MibTable
casfVcCountTable = _CasfVcCountTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 4, 1)
)
if mibBuilder.loadTexts:
    casfVcCountTable.setStatus("current")
_CasfVcCountEntry_Object = MibTableRow
casfVcCountEntry = _CasfVcCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 4, 1, 1)
)
casfVcCountEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-ATM-SWITCH-FR-IWF-MIB", "casfVcEndptDlci"),
)
if mibBuilder.loadTexts:
    casfVcCountEntry.setStatus("current")
_CasfVcCountReceivedFrames_Type = Counter32
_CasfVcCountReceivedFrames_Object = MibTableColumn
casfVcCountReceivedFrames = _CasfVcCountReceivedFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 4, 1, 1, 1),
    _CasfVcCountReceivedFrames_Type()
)
casfVcCountReceivedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casfVcCountReceivedFrames.setStatus("current")
if mibBuilder.loadTexts:
    casfVcCountReceivedFrames.setUnits("frames")
_CasfVcCountReceivedOctets_Type = Counter32
_CasfVcCountReceivedOctets_Object = MibTableColumn
casfVcCountReceivedOctets = _CasfVcCountReceivedOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 4, 1, 1, 2),
    _CasfVcCountReceivedOctets_Type()
)
casfVcCountReceivedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casfVcCountReceivedOctets.setStatus("current")
if mibBuilder.loadTexts:
    casfVcCountReceivedOctets.setUnits("octets")
_CasfVcCountReceivedFECNs_Type = Counter32
_CasfVcCountReceivedFECNs_Object = MibTableColumn
casfVcCountReceivedFECNs = _CasfVcCountReceivedFECNs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 4, 1, 1, 3),
    _CasfVcCountReceivedFECNs_Type()
)
casfVcCountReceivedFECNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casfVcCountReceivedFECNs.setStatus("current")
if mibBuilder.loadTexts:
    casfVcCountReceivedFECNs.setUnits("frames")
_CasfVcCountReceivedBECNs_Type = Counter32
_CasfVcCountReceivedBECNs_Object = MibTableColumn
casfVcCountReceivedBECNs = _CasfVcCountReceivedBECNs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 4, 1, 1, 4),
    _CasfVcCountReceivedBECNs_Type()
)
casfVcCountReceivedBECNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casfVcCountReceivedBECNs.setStatus("current")
if mibBuilder.loadTexts:
    casfVcCountReceivedBECNs.setUnits("frames")
_CasfVcCountReceivedDEs_Type = Counter32
_CasfVcCountReceivedDEs_Object = MibTableColumn
casfVcCountReceivedDEs = _CasfVcCountReceivedDEs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 4, 1, 1, 5),
    _CasfVcCountReceivedDEs_Type()
)
casfVcCountReceivedDEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casfVcCountReceivedDEs.setStatus("current")
if mibBuilder.loadTexts:
    casfVcCountReceivedDEs.setUnits("frames")
_CasfVcCountInDiscards_Type = Counter32
_CasfVcCountInDiscards_Object = MibTableColumn
casfVcCountInDiscards = _CasfVcCountInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 4, 1, 1, 6),
    _CasfVcCountInDiscards_Type()
)
casfVcCountInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casfVcCountInDiscards.setStatus("current")
if mibBuilder.loadTexts:
    casfVcCountInDiscards.setUnits("frames")
_CasfVcCountOutDiscards_Type = Counter32
_CasfVcCountOutDiscards_Object = MibTableColumn
casfVcCountOutDiscards = _CasfVcCountOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 4, 1, 1, 7),
    _CasfVcCountOutDiscards_Type()
)
casfVcCountOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casfVcCountOutDiscards.setStatus("current")
if mibBuilder.loadTexts:
    casfVcCountOutDiscards.setUnits("frames")
_CasfVcCountSentFrames_Type = Counter32
_CasfVcCountSentFrames_Object = MibTableColumn
casfVcCountSentFrames = _CasfVcCountSentFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 4, 1, 1, 8),
    _CasfVcCountSentFrames_Type()
)
casfVcCountSentFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casfVcCountSentFrames.setStatus("current")
if mibBuilder.loadTexts:
    casfVcCountSentFrames.setUnits("frames")
_CasfVcCountSentOctets_Type = Counter32
_CasfVcCountSentOctets_Object = MibTableColumn
casfVcCountSentOctets = _CasfVcCountSentOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 4, 1, 1, 9),
    _CasfVcCountSentOctets_Type()
)
casfVcCountSentOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casfVcCountSentOctets.setStatus("current")
if mibBuilder.loadTexts:
    casfVcCountSentOctets.setUnits("octets")
_CasfVcCountSentFECNs_Type = Counter32
_CasfVcCountSentFECNs_Object = MibTableColumn
casfVcCountSentFECNs = _CasfVcCountSentFECNs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 4, 1, 1, 10),
    _CasfVcCountSentFECNs_Type()
)
casfVcCountSentFECNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casfVcCountSentFECNs.setStatus("current")
if mibBuilder.loadTexts:
    casfVcCountSentFECNs.setUnits("frames")
_CasfVcCountSentBECNs_Type = Counter32
_CasfVcCountSentBECNs_Object = MibTableColumn
casfVcCountSentBECNs = _CasfVcCountSentBECNs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 4, 1, 1, 11),
    _CasfVcCountSentBECNs_Type()
)
casfVcCountSentBECNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casfVcCountSentBECNs.setStatus("current")
if mibBuilder.loadTexts:
    casfVcCountSentBECNs.setUnits("frames")
_CasfVcCountSentDEs_Type = Counter32
_CasfVcCountSentDEs_Object = MibTableColumn
casfVcCountSentDEs = _CasfVcCountSentDEs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 4, 1, 1, 12),
    _CasfVcCountSentDEs_Type()
)
casfVcCountSentDEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casfVcCountSentDEs.setStatus("current")
if mibBuilder.loadTexts:
    casfVcCountSentDEs.setUnits("frames")
_CasfVcCountTaggedFECNs_Type = Counter32
_CasfVcCountTaggedFECNs_Object = MibTableColumn
casfVcCountTaggedFECNs = _CasfVcCountTaggedFECNs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 4, 1, 1, 13),
    _CasfVcCountTaggedFECNs_Type()
)
casfVcCountTaggedFECNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casfVcCountTaggedFECNs.setStatus("current")
if mibBuilder.loadTexts:
    casfVcCountTaggedFECNs.setUnits("frames")
_CasfVcCountTaggedBECNs_Type = Counter32
_CasfVcCountTaggedBECNs_Object = MibTableColumn
casfVcCountTaggedBECNs = _CasfVcCountTaggedBECNs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 4, 1, 1, 14),
    _CasfVcCountTaggedBECNs_Type()
)
casfVcCountTaggedBECNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casfVcCountTaggedBECNs.setStatus("current")
if mibBuilder.loadTexts:
    casfVcCountTaggedBECNs.setUnits("frames")
_CasfVcCountTaggedDEs_Type = Counter32
_CasfVcCountTaggedDEs_Object = MibTableColumn
casfVcCountTaggedDEs = _CasfVcCountTaggedDEs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 4, 1, 1, 15),
    _CasfVcCountTaggedDEs_Type()
)
casfVcCountTaggedDEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casfVcCountTaggedDEs.setStatus("current")
if mibBuilder.loadTexts:
    casfVcCountTaggedDEs.setUnits("frames")
_CasfVcIwfCountTable_Object = MibTable
casfVcIwfCountTable = _CasfVcIwfCountTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 4, 2)
)
if mibBuilder.loadTexts:
    casfVcIwfCountTable.setStatus("current")
_CasfVcIwfCountEntry_Object = MibTableRow
casfVcIwfCountEntry = _CasfVcIwfCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 4, 2, 1)
)
casfVcIwfCountEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-ATM-SWITCH-FR-IWF-MIB", "casfVcEndptDlci"),
)
if mibBuilder.loadTexts:
    casfVcIwfCountEntry.setStatus("current")
_CasfVcIwfCountInUnknownProts_Type = Counter32
_CasfVcIwfCountInUnknownProts_Object = MibTableColumn
casfVcIwfCountInUnknownProts = _CasfVcIwfCountInUnknownProts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 4, 2, 1, 1),
    _CasfVcIwfCountInUnknownProts_Type()
)
casfVcIwfCountInUnknownProts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casfVcIwfCountInUnknownProts.setStatus("current")
_CasfVcIwfCountOutUnknownProts_Type = Counter32
_CasfVcIwfCountOutUnknownProts_Object = MibTableColumn
casfVcIwfCountOutUnknownProts = _CasfVcIwfCountOutUnknownProts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 4, 2, 1, 2),
    _CasfVcIwfCountOutUnknownProts_Type()
)
casfVcIwfCountOutUnknownProts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casfVcIwfCountOutUnknownProts.setStatus("current")
_CasfVcIwfCountReassemblyTimeouts_Type = Counter32
_CasfVcIwfCountReassemblyTimeouts_Object = MibTableColumn
casfVcIwfCountReassemblyTimeouts = _CasfVcIwfCountReassemblyTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 4, 2, 1, 3),
    _CasfVcIwfCountReassemblyTimeouts_Type()
)
casfVcIwfCountReassemblyTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casfVcIwfCountReassemblyTimeouts.setStatus("current")
_CasfVcIwfCountLengthErrors_Type = Counter32
_CasfVcIwfCountLengthErrors_Object = MibTableColumn
casfVcIwfCountLengthErrors = _CasfVcIwfCountLengthErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 4, 2, 1, 4),
    _CasfVcIwfCountLengthErrors_Type()
)
casfVcIwfCountLengthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casfVcIwfCountLengthErrors.setStatus("current")
_CasfVcIwfCountCrcErrors_Type = Counter32
_CasfVcIwfCountCrcErrors_Object = MibTableColumn
casfVcIwfCountCrcErrors = _CasfVcIwfCountCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 4, 2, 1, 5),
    _CasfVcIwfCountCrcErrors_Type()
)
casfVcIwfCountCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casfVcIwfCountCrcErrors.setStatus("current")
_CasfVcIwfCountTotalDiscardFrames_Type = Counter32
_CasfVcIwfCountTotalDiscardFrames_Object = MibTableColumn
casfVcIwfCountTotalDiscardFrames = _CasfVcIwfCountTotalDiscardFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 4, 2, 1, 6),
    _CasfVcIwfCountTotalDiscardFrames_Type()
)
casfVcIwfCountTotalDiscardFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casfVcIwfCountTotalDiscardFrames.setStatus("current")
_CasfMapping_ObjectIdentity = ObjectIdentity
casfMapping = _CasfMapping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 5)
)
_CasfFAMapTable_Object = MibTable
casfFAMapTable = _CasfFAMapTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 5, 1)
)
if mibBuilder.loadTexts:
    casfFAMapTable.setStatus("current")
_CasfFAMapEntry_Object = MibTableRow
casfFAMapEntry = _CasfFAMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 5, 1, 1)
)
casfFAMapEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-ATM-SWITCH-FR-IWF-MIB", "casfFAMapDlci"),
)
if mibBuilder.loadTexts:
    casfFAMapEntry.setStatus("current")
_CasfFAMapDlci_Type = DlciValue
_CasfFAMapDlci_Object = MibTableColumn
casfFAMapDlci = _CasfFAMapDlci_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 5, 1, 1, 1),
    _CasfFAMapDlci_Type()
)
casfFAMapDlci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    casfFAMapDlci.setStatus("current")
_CasfFAMapInternalAtmInterface_Type = InterfaceIndex
_CasfFAMapInternalAtmInterface_Object = MibTableColumn
casfFAMapInternalAtmInterface = _CasfFAMapInternalAtmInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 5, 1, 1, 2),
    _CasfFAMapInternalAtmInterface_Type()
)
casfFAMapInternalAtmInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casfFAMapInternalAtmInterface.setStatus("current")


class _CasfFAMapInternalAtmVpi_Type(Integer32):
    """Custom type casfFAMapInternalAtmVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CasfFAMapInternalAtmVpi_Type.__name__ = "Integer32"
_CasfFAMapInternalAtmVpi_Object = MibTableColumn
casfFAMapInternalAtmVpi = _CasfFAMapInternalAtmVpi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 5, 1, 1, 3),
    _CasfFAMapInternalAtmVpi_Type()
)
casfFAMapInternalAtmVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casfFAMapInternalAtmVpi.setStatus("current")


class _CasfFAMapInternalAtmVci_Type(Integer32):
    """Custom type casfFAMapInternalAtmVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CasfFAMapInternalAtmVci_Type.__name__ = "Integer32"
_CasfFAMapInternalAtmVci_Object = MibTableColumn
casfFAMapInternalAtmVci = _CasfFAMapInternalAtmVci_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 5, 1, 1, 4),
    _CasfFAMapInternalAtmVci_Type()
)
casfFAMapInternalAtmVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casfFAMapInternalAtmVci.setStatus("current")
_CasfAFMapTable_Object = MibTable
casfAFMapTable = _CasfAFMapTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 5, 2)
)
if mibBuilder.loadTexts:
    casfAFMapTable.setStatus("current")
_CasfAFMapEntry_Object = MibTableRow
casfAFMapEntry = _CasfAFMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 5, 2, 1)
)
casfAFMapEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-ATM-SWITCH-FR-IWF-MIB", "casfAFMapAtmVpi"),
    (0, "CISCO-ATM-SWITCH-FR-IWF-MIB", "casfAFMapAtmVci"),
)
if mibBuilder.loadTexts:
    casfAFMapEntry.setStatus("current")


class _CasfAFMapAtmVpi_Type(Integer32):
    """Custom type casfAFMapAtmVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CasfAFMapAtmVpi_Type.__name__ = "Integer32"
_CasfAFMapAtmVpi_Object = MibTableColumn
casfAFMapAtmVpi = _CasfAFMapAtmVpi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 5, 2, 1, 1),
    _CasfAFMapAtmVpi_Type()
)
casfAFMapAtmVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    casfAFMapAtmVpi.setStatus("current")


class _CasfAFMapAtmVci_Type(Integer32):
    """Custom type casfAFMapAtmVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CasfAFMapAtmVci_Type.__name__ = "Integer32"
_CasfAFMapAtmVci_Object = MibTableColumn
casfAFMapAtmVci = _CasfAFMapAtmVci_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 5, 2, 1, 2),
    _CasfAFMapAtmVci_Type()
)
casfAFMapAtmVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    casfAFMapAtmVci.setStatus("current")
_CasfAFMapFrIndex_Type = InterfaceIndex
_CasfAFMapFrIndex_Object = MibTableColumn
casfAFMapFrIndex = _CasfAFMapFrIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 5, 2, 1, 3),
    _CasfAFMapFrIndex_Type()
)
casfAFMapFrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casfAFMapFrIndex.setStatus("current")
_CasfAFMapFrDlci_Type = DlciValue
_CasfAFMapFrDlci_Object = MibTableColumn
casfAFMapFrDlci = _CasfAFMapFrDlci_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 1, 5, 2, 1, 4),
    _CasfAFMapFrDlci_Type()
)
casfAFMapFrDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casfAFMapFrDlci.setStatus("current")
_CiscoAtmSFrIwfMIBConformance_ObjectIdentity = ObjectIdentity
ciscoAtmSFrIwfMIBConformance = _CiscoAtmSFrIwfMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 3)
)
_CiscoAtmSFrIwfMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoAtmSFrIwfMIBCompliances = _CiscoAtmSFrIwfMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 3, 1)
)
_CiscoAtmSFrIwfMIBGroups_ObjectIdentity = ObjectIdentity
ciscoAtmSFrIwfMIBGroups = _CiscoAtmSFrIwfMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 3, 2)
)

# Managed Objects groups

ciscoAtmSFrIwfConfConnGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 3, 2, 1)
)
ciscoAtmSFrIwfConfConnGroup.setObjects(
      *(("CISCO-ATM-SWITCH-FR-IWF-MIB", "casfTrafficDescrCIR"),
        ("CISCO-ATM-SWITCH-FR-IWF-MIB", "casfTrafficDescrBc"),
        ("CISCO-ATM-SWITCH-FR-IWF-MIB", "casfTrafficDescrBe"),
        ("CISCO-ATM-SWITCH-FR-IWF-MIB", "casfTrafficDescrPIR"),
        ("CISCO-ATM-SWITCH-FR-IWF-MIB", "casfTrafficDescrServCategory"),
        ("CISCO-ATM-SWITCH-FR-IWF-MIB", "casfTrafficDescrAtmIndex"),
        ("CISCO-ATM-SWITCH-FR-IWF-MIB", "casfTrafficDescrRowStatus"),
        ("CISCO-ATM-SWITCH-FR-IWF-MIB", "casfVcEndptRxTrafficDescrRow"),
        ("CISCO-ATM-SWITCH-FR-IWF-MIB", "casfVcEndptTxTrafficDescrRow"),
        ("CISCO-ATM-SWITCH-FR-IWF-MIB", "casfVcEndptRxNegTrafficDescrRow"),
        ("CISCO-ATM-SWITCH-FR-IWF-MIB", "casfVcEndptTxNegTrafficDescrRow"),
        ("CISCO-ATM-SWITCH-FR-IWF-MIB", "casfVcEndptConnKind"),
        ("CISCO-ATM-SWITCH-FR-IWF-MIB", "casfVcEndptIwfType"),
        ("CISCO-ATM-SWITCH-FR-IWF-MIB", "casfVcEndptClpMode"),
        ("CISCO-ATM-SWITCH-FR-IWF-MIB", "casfVcEndptDeMode"),
        ("CISCO-ATM-SWITCH-FR-IWF-MIB", "casfVcEndptEfciMode"),
        ("CISCO-ATM-SWITCH-FR-IWF-MIB", "casfVcEndptUpcMode"),
        ("CISCO-ATM-SWITCH-FR-IWF-MIB", "casfVcEndptCreationTime"),
        ("CISCO-ATM-SWITCH-FR-IWF-MIB", "casfVcEndptRcvdSigStatus"),
        ("CISCO-ATM-SWITCH-FR-IWF-MIB", "casfVcEndptSpvcRemoteAddr"),
        ("CISCO-ATM-SWITCH-FR-IWF-MIB", "casfVcEndptSpvcRemoteType"),
        ("CISCO-ATM-SWITCH-FR-IWF-MIB", "casfVcEndptSpvcRemoteDlci"),
        ("CISCO-ATM-SWITCH-FR-IWF-MIB", "casfVcEndptSpvcRemoteVpi"),
        ("CISCO-ATM-SWITCH-FR-IWF-MIB", "casfVcEndptSpvcRemoteVci"),
        ("CISCO-ATM-SWITCH-FR-IWF-MIB", "casfVcEndptRowStatus"),
        ("CISCO-ATM-SWITCH-FR-IWF-MIB", "casfVcSignalStandardCalledIe"))
)
if mibBuilder.loadTexts:
    ciscoAtmSFrIwfConfConnGroup.setStatus("current")

ciscoAtmSFrIwfLmiGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 3, 2, 2)
)
ciscoAtmSFrIwfLmiGroup.setObjects(
      *(("CISCO-ATM-SWITCH-FR-IWF-MIB", "casfFrLmiProtocol"),
        ("CISCO-ATM-SWITCH-FR-IWF-MIB", "casfFrLmiType"),
        ("CISCO-ATM-SWITCH-FR-IWF-MIB", "casfFrLmiUserN391"),
        ("CISCO-ATM-SWITCH-FR-IWF-MIB", "casfFrLmiUserN392"),
        ("CISCO-ATM-SWITCH-FR-IWF-MIB", "casfFrLmiUserN393"),
        ("CISCO-ATM-SWITCH-FR-IWF-MIB", "casfFrLmiUserT391"),
        ("CISCO-ATM-SWITCH-FR-IWF-MIB", "casfFrLmiNetN392"),
        ("CISCO-ATM-SWITCH-FR-IWF-MIB", "casfFrLmiNetN393"),
        ("CISCO-ATM-SWITCH-FR-IWF-MIB", "casfFrLmiNetT392"),
        ("CISCO-ATM-SWITCH-FR-IWF-MIB", "casfFrLmiEnquiryIns"),
        ("CISCO-ATM-SWITCH-FR-IWF-MIB", "casfFrLmiEnquiryOuts"),
        ("CISCO-ATM-SWITCH-FR-IWF-MIB", "casfFrLmiStatusIns"),
        ("CISCO-ATM-SWITCH-FR-IWF-MIB", "casfFrLmiStatusOuts"),
        ("CISCO-ATM-SWITCH-FR-IWF-MIB", "casfFrLmiStatusTimeouts"),
        ("CISCO-ATM-SWITCH-FR-IWF-MIB", "casfFrLmiStatusEnqTimeouts"))
)
if mibBuilder.loadTexts:
    ciscoAtmSFrIwfLmiGroup.setStatus("current")

ciscoAtmSFrIwfConfIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 3, 2, 3)
)
ciscoAtmSFrIwfConfIfGroup.setObjects(
      *(("CISCO-ATM-SWITCH-FR-IWF-MIB", "casfConfIfAtmAddress"),
        ("CISCO-ATM-SWITCH-FR-IWF-MIB", "casfConfIfUpcIntent"),
        ("CISCO-ATM-SWITCH-FR-IWF-MIB", "casfConfIfBcDefault"),
        ("CISCO-ATM-SWITCH-FR-IWF-MIB", "casfConfIfCledSpvcDeModeDef"),
        ("CISCO-ATM-SWITCH-FR-IWF-MIB", "casfConfIfCledSpvcClpModeDef"))
)
if mibBuilder.loadTexts:
    ciscoAtmSFrIwfConfIfGroup.setStatus("current")

ciscoAtmSFrIwfVcStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 3, 2, 4)
)
ciscoAtmSFrIwfVcStatsGroup.setObjects(
      *(("CISCO-ATM-SWITCH-FR-IWF-MIB", "casfVcCountReceivedFrames"),
        ("CISCO-ATM-SWITCH-FR-IWF-MIB", "casfVcCountReceivedOctets"),
        ("CISCO-ATM-SWITCH-FR-IWF-MIB", "casfVcCountReceivedFECNs"),
        ("CISCO-ATM-SWITCH-FR-IWF-MIB", "casfVcCountReceivedBECNs"),
        ("CISCO-ATM-SWITCH-FR-IWF-MIB", "casfVcCountReceivedDEs"),
        ("CISCO-ATM-SWITCH-FR-IWF-MIB", "casfVcCountInDiscards"),
        ("CISCO-ATM-SWITCH-FR-IWF-MIB", "casfVcCountOutDiscards"),
        ("CISCO-ATM-SWITCH-FR-IWF-MIB", "casfVcCountSentFrames"),
        ("CISCO-ATM-SWITCH-FR-IWF-MIB", "casfVcCountSentOctets"),
        ("CISCO-ATM-SWITCH-FR-IWF-MIB", "casfVcCountSentFECNs"),
        ("CISCO-ATM-SWITCH-FR-IWF-MIB", "casfVcCountSentBECNs"),
        ("CISCO-ATM-SWITCH-FR-IWF-MIB", "casfVcCountSentDEs"),
        ("CISCO-ATM-SWITCH-FR-IWF-MIB", "casfVcCountTaggedFECNs"),
        ("CISCO-ATM-SWITCH-FR-IWF-MIB", "casfVcCountTaggedBECNs"),
        ("CISCO-ATM-SWITCH-FR-IWF-MIB", "casfVcCountTaggedDEs"))
)
if mibBuilder.loadTexts:
    ciscoAtmSFrIwfVcStatsGroup.setStatus("current")

ciscoAtmSFrIwfVcIwStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 3, 2, 5)
)
ciscoAtmSFrIwfVcIwStatsGroup.setObjects(
      *(("CISCO-ATM-SWITCH-FR-IWF-MIB", "casfVcIwfCountInUnknownProts"),
        ("CISCO-ATM-SWITCH-FR-IWF-MIB", "casfVcIwfCountOutUnknownProts"),
        ("CISCO-ATM-SWITCH-FR-IWF-MIB", "casfVcIwfCountReassemblyTimeouts"),
        ("CISCO-ATM-SWITCH-FR-IWF-MIB", "casfVcIwfCountLengthErrors"),
        ("CISCO-ATM-SWITCH-FR-IWF-MIB", "casfVcIwfCountCrcErrors"),
        ("CISCO-ATM-SWITCH-FR-IWF-MIB", "casfVcIwfCountTotalDiscardFrames"))
)
if mibBuilder.loadTexts:
    ciscoAtmSFrIwfVcIwStatsGroup.setStatus("current")

ciscoAtmSFrIwfMappingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 3, 2, 6)
)
ciscoAtmSFrIwfMappingGroup.setObjects(
      *(("CISCO-ATM-SWITCH-FR-IWF-MIB", "casfFAMapInternalAtmInterface"),
        ("CISCO-ATM-SWITCH-FR-IWF-MIB", "casfFAMapInternalAtmVpi"),
        ("CISCO-ATM-SWITCH-FR-IWF-MIB", "casfFAMapInternalAtmVci"),
        ("CISCO-ATM-SWITCH-FR-IWF-MIB", "casfAFMapFrIndex"),
        ("CISCO-ATM-SWITCH-FR-IWF-MIB", "casfAFMapFrDlci"))
)
if mibBuilder.loadTexts:
    ciscoAtmSFrIwfMappingGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoAtmSFrIwfMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 112, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoAtmSFrIwfMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ATM-SWITCH-FR-IWF-MIB",
    **{"CasfTrafficDescrRow": CasfTrafficDescrRow,
       "DlciValue": DlciValue,
       "ConnectionKind": ConnectionKind,
       "AtmAddr": AtmAddr,
       "ciscoAtmSwitchFrIwfMIB": ciscoAtmSwitchFrIwfMIB,
       "ciscoAtmSwitchFrIwfMIBObjects": ciscoAtmSwitchFrIwfMIBObjects,
       "casfFrTraffic": casfFrTraffic,
       "casfTrafficDescrTable": casfTrafficDescrTable,
       "casfTrafficDescrEntry": casfTrafficDescrEntry,
       "casfTrafficDescrIndex": casfTrafficDescrIndex,
       "casfTrafficDescrCIR": casfTrafficDescrCIR,
       "casfTrafficDescrBc": casfTrafficDescrBc,
       "casfTrafficDescrBe": casfTrafficDescrBe,
       "casfTrafficDescrPIR": casfTrafficDescrPIR,
       "casfTrafficDescrServCategory": casfTrafficDescrServCategory,
       "casfTrafficDescrAtmIndex": casfTrafficDescrAtmIndex,
       "casfTrafficDescrRowStatus": casfTrafficDescrRowStatus,
       "casfFrVC": casfFrVC,
       "casfVcEndptTable": casfVcEndptTable,
       "casfVcEndptEntry": casfVcEndptEntry,
       "casfVcEndptDlci": casfVcEndptDlci,
       "casfVcEndptRxTrafficDescrRow": casfVcEndptRxTrafficDescrRow,
       "casfVcEndptTxTrafficDescrRow": casfVcEndptTxTrafficDescrRow,
       "casfVcEndptRxNegTrafficDescrRow": casfVcEndptRxNegTrafficDescrRow,
       "casfVcEndptTxNegTrafficDescrRow": casfVcEndptTxNegTrafficDescrRow,
       "casfVcEndptConnKind": casfVcEndptConnKind,
       "casfVcEndptIwfType": casfVcEndptIwfType,
       "casfVcEndptClpMode": casfVcEndptClpMode,
       "casfVcEndptDeMode": casfVcEndptDeMode,
       "casfVcEndptEfciMode": casfVcEndptEfciMode,
       "casfVcEndptUpcMode": casfVcEndptUpcMode,
       "casfVcEndptSpvcRemoteAddr": casfVcEndptSpvcRemoteAddr,
       "casfVcEndptSpvcRemoteType": casfVcEndptSpvcRemoteType,
       "casfVcEndptSpvcRemoteDlci": casfVcEndptSpvcRemoteDlci,
       "casfVcEndptSpvcRemoteVpi": casfVcEndptSpvcRemoteVpi,
       "casfVcEndptSpvcRemoteVci": casfVcEndptSpvcRemoteVci,
       "casfVcEndptCreationTime": casfVcEndptCreationTime,
       "casfVcEndptRcvdSigStatus": casfVcEndptRcvdSigStatus,
       "casfVcEndptRowStatus": casfVcEndptRowStatus,
       "casfVcSignalStandardCalledIe": casfVcSignalStandardCalledIe,
       "casfFrInterface": casfFrInterface,
       "casfFrLmiTable": casfFrLmiTable,
       "casfFrLmiEntry": casfFrLmiEntry,
       "casfFrLmiProtocol": casfFrLmiProtocol,
       "casfFrLmiType": casfFrLmiType,
       "casfFrLmiUserN391": casfFrLmiUserN391,
       "casfFrLmiUserN392": casfFrLmiUserN392,
       "casfFrLmiUserN393": casfFrLmiUserN393,
       "casfFrLmiUserT391": casfFrLmiUserT391,
       "casfFrLmiNetN392": casfFrLmiNetN392,
       "casfFrLmiNetN393": casfFrLmiNetN393,
       "casfFrLmiNetT392": casfFrLmiNetT392,
       "casfFrLmiEnquiryIns": casfFrLmiEnquiryIns,
       "casfFrLmiEnquiryOuts": casfFrLmiEnquiryOuts,
       "casfFrLmiStatusIns": casfFrLmiStatusIns,
       "casfFrLmiStatusOuts": casfFrLmiStatusOuts,
       "casfFrLmiStatusTimeouts": casfFrLmiStatusTimeouts,
       "casfFrLmiStatusEnqTimeouts": casfFrLmiStatusEnqTimeouts,
       "casfConfIfTable": casfConfIfTable,
       "casfConfIfEntry": casfConfIfEntry,
       "casfConfIfAtmAddress": casfConfIfAtmAddress,
       "casfConfIfUpcIntent": casfConfIfUpcIntent,
       "casfConfIfBcDefault": casfConfIfBcDefault,
       "casfConfIfCledSpvcDeModeDef": casfConfIfCledSpvcDeModeDef,
       "casfConfIfCledSpvcClpModeDef": casfConfIfCledSpvcClpModeDef,
       "casfFrCounts": casfFrCounts,
       "casfVcCountTable": casfVcCountTable,
       "casfVcCountEntry": casfVcCountEntry,
       "casfVcCountReceivedFrames": casfVcCountReceivedFrames,
       "casfVcCountReceivedOctets": casfVcCountReceivedOctets,
       "casfVcCountReceivedFECNs": casfVcCountReceivedFECNs,
       "casfVcCountReceivedBECNs": casfVcCountReceivedBECNs,
       "casfVcCountReceivedDEs": casfVcCountReceivedDEs,
       "casfVcCountInDiscards": casfVcCountInDiscards,
       "casfVcCountOutDiscards": casfVcCountOutDiscards,
       "casfVcCountSentFrames": casfVcCountSentFrames,
       "casfVcCountSentOctets": casfVcCountSentOctets,
       "casfVcCountSentFECNs": casfVcCountSentFECNs,
       "casfVcCountSentBECNs": casfVcCountSentBECNs,
       "casfVcCountSentDEs": casfVcCountSentDEs,
       "casfVcCountTaggedFECNs": casfVcCountTaggedFECNs,
       "casfVcCountTaggedBECNs": casfVcCountTaggedBECNs,
       "casfVcCountTaggedDEs": casfVcCountTaggedDEs,
       "casfVcIwfCountTable": casfVcIwfCountTable,
       "casfVcIwfCountEntry": casfVcIwfCountEntry,
       "casfVcIwfCountInUnknownProts": casfVcIwfCountInUnknownProts,
       "casfVcIwfCountOutUnknownProts": casfVcIwfCountOutUnknownProts,
       "casfVcIwfCountReassemblyTimeouts": casfVcIwfCountReassemblyTimeouts,
       "casfVcIwfCountLengthErrors": casfVcIwfCountLengthErrors,
       "casfVcIwfCountCrcErrors": casfVcIwfCountCrcErrors,
       "casfVcIwfCountTotalDiscardFrames": casfVcIwfCountTotalDiscardFrames,
       "casfMapping": casfMapping,
       "casfFAMapTable": casfFAMapTable,
       "casfFAMapEntry": casfFAMapEntry,
       "casfFAMapDlci": casfFAMapDlci,
       "casfFAMapInternalAtmInterface": casfFAMapInternalAtmInterface,
       "casfFAMapInternalAtmVpi": casfFAMapInternalAtmVpi,
       "casfFAMapInternalAtmVci": casfFAMapInternalAtmVci,
       "casfAFMapTable": casfAFMapTable,
       "casfAFMapEntry": casfAFMapEntry,
       "casfAFMapAtmVpi": casfAFMapAtmVpi,
       "casfAFMapAtmVci": casfAFMapAtmVci,
       "casfAFMapFrIndex": casfAFMapFrIndex,
       "casfAFMapFrDlci": casfAFMapFrDlci,
       "ciscoAtmSFrIwfMIBConformance": ciscoAtmSFrIwfMIBConformance,
       "ciscoAtmSFrIwfMIBCompliances": ciscoAtmSFrIwfMIBCompliances,
       "ciscoAtmSFrIwfMIBCompliance": ciscoAtmSFrIwfMIBCompliance,
       "ciscoAtmSFrIwfMIBGroups": ciscoAtmSFrIwfMIBGroups,
       "ciscoAtmSFrIwfConfConnGroup": ciscoAtmSFrIwfConfConnGroup,
       "ciscoAtmSFrIwfLmiGroup": ciscoAtmSFrIwfLmiGroup,
       "ciscoAtmSFrIwfConfIfGroup": ciscoAtmSFrIwfConfIfGroup,
       "ciscoAtmSFrIwfVcStatsGroup": ciscoAtmSFrIwfVcStatsGroup,
       "ciscoAtmSFrIwfVcIwStatsGroup": ciscoAtmSFrIwfVcIwStatsGroup,
       "ciscoAtmSFrIwfMappingGroup": ciscoAtmSFrIwfMappingGroup}
)
