# SNMP MIB module (NETSTAR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NETSTAR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:48:52 2024
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

(ifDescr,
 ifInOctets,
 ifIndex,
 ifOutOctets) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifDescr",
    "ifInOctets",
    "ifIndex",
    "ifOutOctets")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(snmp,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "snmp")

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

_Netstar_ObjectIdentity = ObjectIdentity
netstar = _Netstar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1080)
)
_Netstar_products_ObjectIdentity = ObjectIdentity
netstar_products = _Netstar_products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1080, 1)
)
_Gigarouter_ObjectIdentity = ObjectIdentity
gigarouter = _Gigarouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1)
)
_GrChassis_ObjectIdentity = ObjectIdentity
grChassis = _GrChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 1)
)
_GrPowerSupplyStatus_Type = Integer32
_GrPowerSupplyStatus_Object = MibScalar
grPowerSupplyStatus = _GrPowerSupplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 1, 1),
    _GrPowerSupplyStatus_Type()
)
grPowerSupplyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grPowerSupplyStatus.setStatus("mandatory")


class _GrTempStatus_Type(Integer32):
    """Custom type grTempStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("over-temp", 2))
    )


_GrTempStatus_Type.__name__ = "Integer32"
_GrTempStatus_Object = MibScalar
grTempStatus = _GrTempStatus_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 1, 2),
    _GrTempStatus_Type()
)
grTempStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grTempStatus.setStatus("mandatory")
_GrFanStatus_Type = Integer32
_GrFanStatus_Object = MibScalar
grFanStatus = _GrFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 1, 3),
    _GrFanStatus_Type()
)
grFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grFanStatus.setStatus("mandatory")


class _GrPortCardNumber_Type(Integer32):
    """Custom type grPortCardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_GrPortCardNumber_Type.__name__ = "Integer32"
_GrPortCardNumber_Object = MibScalar
grPortCardNumber = _GrPortCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 1, 4),
    _GrPortCardNumber_Type()
)
grPortCardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grPortCardNumber.setStatus("mandatory")
_GrPortCardTable_Object = MibTable
grPortCardTable = _GrPortCardTable_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 1, 5)
)
if mibBuilder.loadTexts:
    grPortCardTable.setStatus("mandatory")
_GrPortCardEntry_Object = MibTableRow
grPortCardEntry = _GrPortCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 1, 5, 1)
)
grPortCardEntry.setIndexNames(
    (0, "NETSTAR-MIB", "grPortCardSlot"),
)
if mibBuilder.loadTexts:
    grPortCardEntry.setStatus("mandatory")


class _GrPortCardSlot_Type(Integer32):
    """Custom type grPortCardSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_GrPortCardSlot_Type.__name__ = "Integer32"
_GrPortCardSlot_Object = MibTableColumn
grPortCardSlot = _GrPortCardSlot_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 1, 5, 1, 1),
    _GrPortCardSlot_Type()
)
grPortCardSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grPortCardSlot.setStatus("mandatory")


class _GrPortCardHWtype_Type(Integer32):
    """Custom type grPortCardHWtype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3,
              4,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("atm", 7),
          ("atm-oc12", 12),
          ("atmq-oc3", 10),
          ("cddi", 15),
          ("ethernet", 13),
          ("fddi", 4),
          ("fddiq", 11),
          ("hippi", 3),
          ("hssi", 8),
          ("ibmSP", 9),
          ("none", 0),
          ("rmb", 6),
          ("sonet-oc3", 14))
    )


_GrPortCardHWtype_Type.__name__ = "Integer32"
_GrPortCardHWtype_Object = MibTableColumn
grPortCardHWtype = _GrPortCardHWtype_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 1, 5, 1, 2),
    _GrPortCardHWtype_Type()
)
grPortCardHWtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grPortCardHWtype.setStatus("mandatory")


class _GrPortCardCurrentState_Type(Integer32):
    """Custom type grPortCardCurrentState based on Integer32"""
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
              9,
              10,
              99)
        )
    )
    namedValues = NamedValues(
        *(("boot-requested", 3),
          ("configuring", 6),
          ("dumping", 4),
          ("empty", 1),
          ("held-reset", 10),
          ("loading", 5),
          ("not-responding", 8),
          ("other", 99),
          ("panic", 9),
          ("power-up", 2),
          ("running", 7))
    )


_GrPortCardCurrentState_Type.__name__ = "Integer32"
_GrPortCardCurrentState_Object = MibTableColumn
grPortCardCurrentState = _GrPortCardCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 1, 5, 1, 3),
    _GrPortCardCurrentState_Type()
)
grPortCardCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grPortCardCurrentState.setStatus("mandatory")


class _GrGatedStatus_Type(Integer32):
    """Custom type grGatedStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-running", 2),
          ("running", 1))
    )


_GrGatedStatus_Type.__name__ = "Integer32"
_GrGatedStatus_Object = MibScalar
grGatedStatus = _GrGatedStatus_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 1, 6),
    _GrGatedStatus_Type()
)
grGatedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grGatedStatus.setStatus("mandatory")


class _GrTransportMethod_Type(Integer32):
    """Custom type grTransportMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ftp", 0),
          ("tftp", 1))
    )


_GrTransportMethod_Type.__name__ = "Integer32"
_GrTransportMethod_Object = MibScalar
grTransportMethod = _GrTransportMethod_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 1, 7),
    _GrTransportMethod_Type()
)
grTransportMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grTransportMethod.setStatus("mandatory")


class _GrFTPUserName_Type(DisplayString):
    """Custom type grFTPUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GrFTPUserName_Type.__name__ = "DisplayString"
_GrFTPUserName_Object = MibScalar
grFTPUserName = _GrFTPUserName_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 1, 8),
    _GrFTPUserName_Type()
)
grFTPUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grFTPUserName.setStatus("mandatory")


class _GrFTPPassword_Type(DisplayString):
    """Custom type grFTPPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GrFTPPassword_Type.__name__ = "DisplayString"
_GrFTPPassword_Object = MibScalar
grFTPPassword = _GrFTPPassword_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 1, 9),
    _GrFTPPassword_Type()
)
grFTPPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grFTPPassword.setStatus("mandatory")


class _GrServerName_Type(DisplayString):
    """Custom type grServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GrServerName_Type.__name__ = "DisplayString"
_GrServerName_Object = MibScalar
grServerName = _GrServerName_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 1, 10),
    _GrServerName_Type()
)
grServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grServerName.setStatus("mandatory")


class _GrFileName_Type(DisplayString):
    """Custom type grFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GrFileName_Type.__name__ = "DisplayString"
_GrFileName_Object = MibScalar
grFileName = _GrFileName_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 1, 11),
    _GrFileName_Type()
)
grFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grFileName.setStatus("mandatory")


class _GrLastOperation_Type(DisplayString):
    """Custom type grLastOperation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GrLastOperation_Type.__name__ = "DisplayString"
_GrLastOperation_Object = MibScalar
grLastOperation = _GrLastOperation_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 1, 12),
    _GrLastOperation_Type()
)
grLastOperation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grLastOperation.setStatus("mandatory")


class _GrStatusMsg_Type(DisplayString):
    """Custom type grStatusMsg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GrStatusMsg_Type.__name__ = "DisplayString"
_GrStatusMsg_Object = MibScalar
grStatusMsg = _GrStatusMsg_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 1, 13),
    _GrStatusMsg_Type()
)
grStatusMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grStatusMsg.setStatus("mandatory")


class _GrBackup_Type(Integer32):
    """Custom type grBackup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_GrBackup_Type.__name__ = "Integer32"
_GrBackup_Object = MibScalar
grBackup = _GrBackup_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 1, 14),
    _GrBackup_Type()
)
grBackup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grBackup.setStatus("mandatory")


class _GrCompare_Type(Integer32):
    """Custom type grCompare based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_GrCompare_Type.__name__ = "Integer32"
_GrCompare_Object = MibScalar
grCompare = _GrCompare_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 1, 15),
    _GrCompare_Type()
)
grCompare.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grCompare.setStatus("mandatory")


class _GrRestore_Type(Integer32):
    """Custom type grRestore based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_GrRestore_Type.__name__ = "Integer32"
_GrRestore_Object = MibScalar
grRestore = _GrRestore_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 1, 16),
    _GrRestore_Type()
)
grRestore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grRestore.setStatus("mandatory")
_GrHIPPI_ObjectIdentity = ObjectIdentity
grHIPPI = _GrHIPPI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 2)
)
_GrFDDI4_ObjectIdentity = ObjectIdentity
grFDDI4 = _GrFDDI4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 3)
)
_GrAtmV1_ObjectIdentity = ObjectIdentity
grAtmV1 = _GrAtmV1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 4)
)
_GrAtmV1VcTable_Object = MibTable
grAtmV1VcTable = _GrAtmV1VcTable_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    grAtmV1VcTable.setStatus("mandatory")
_GrAtmV1VcEntry_Object = MibTableRow
grAtmV1VcEntry = _GrAtmV1VcEntry_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 4, 1, 1)
)
grAtmV1VcEntry.setIndexNames(
    (0, "NETSTAR-MIB", "grAtmV1VcIfIndex"),
    (0, "NETSTAR-MIB", "grAtmV1VcVpi"),
    (0, "NETSTAR-MIB", "grAtmV1VcVci"),
)
if mibBuilder.loadTexts:
    grAtmV1VcEntry.setStatus("mandatory")
_GrAtmV1VcIfIndex_Type = Integer32
_GrAtmV1VcIfIndex_Object = MibTableColumn
grAtmV1VcIfIndex = _GrAtmV1VcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 4, 1, 1, 1),
    _GrAtmV1VcIfIndex_Type()
)
grAtmV1VcIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grAtmV1VcIfIndex.setStatus("mandatory")
_GrAtmV1VcVpi_Type = Integer32
_GrAtmV1VcVpi_Object = MibTableColumn
grAtmV1VcVpi = _GrAtmV1VcVpi_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 4, 1, 1, 2),
    _GrAtmV1VcVpi_Type()
)
grAtmV1VcVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grAtmV1VcVpi.setStatus("mandatory")
_GrAtmV1VcVci_Type = Integer32
_GrAtmV1VcVci_Object = MibTableColumn
grAtmV1VcVci = _GrAtmV1VcVci_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 4, 1, 1, 3),
    _GrAtmV1VcVci_Type()
)
grAtmV1VcVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grAtmV1VcVci.setStatus("mandatory")


class _GrAtmV1VcAal_Type(Integer32):
    """Custom type grAtmV1VcAal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aal3", 1),
          ("aal5", 2),
          ("other", 3))
    )


_GrAtmV1VcAal_Type.__name__ = "Integer32"
_GrAtmV1VcAal_Object = MibTableColumn
grAtmV1VcAal = _GrAtmV1VcAal_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 4, 1, 1, 4),
    _GrAtmV1VcAal_Type()
)
grAtmV1VcAal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grAtmV1VcAal.setStatus("mandatory")


class _GrAtmV1VcProtocol_Type(Integer32):
    """Custom type grAtmV1VcProtocol based on Integer32"""
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
        *(("diag0", 4),
          ("diag1", 5),
          ("ip-llc", 1),
          ("ip-null", 2),
          ("other", 7),
          ("raw", 6),
          ("uni", 3))
    )


_GrAtmV1VcProtocol_Type.__name__ = "Integer32"
_GrAtmV1VcProtocol_Object = MibTableColumn
grAtmV1VcProtocol = _GrAtmV1VcProtocol_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 4, 1, 1, 5),
    _GrAtmV1VcProtocol_Type()
)
grAtmV1VcProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grAtmV1VcProtocol.setStatus("mandatory")
_GrAtmV1VcDestIfIndex_Type = Integer32
_GrAtmV1VcDestIfIndex_Object = MibTableColumn
grAtmV1VcDestIfIndex = _GrAtmV1VcDestIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 4, 1, 1, 6),
    _GrAtmV1VcDestIfIndex_Type()
)
grAtmV1VcDestIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grAtmV1VcDestIfIndex.setStatus("mandatory")
_GrAtmV1VcDestVpi_Type = Integer32
_GrAtmV1VcDestVpi_Object = MibTableColumn
grAtmV1VcDestVpi = _GrAtmV1VcDestVpi_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 4, 1, 1, 7),
    _GrAtmV1VcDestVpi_Type()
)
grAtmV1VcDestVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grAtmV1VcDestVpi.setStatus("mandatory")
_GrAtmV1VcDestVci_Type = Integer32
_GrAtmV1VcDestVci_Object = MibTableColumn
grAtmV1VcDestVci = _GrAtmV1VcDestVci_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 4, 1, 1, 8),
    _GrAtmV1VcDestVci_Type()
)
grAtmV1VcDestVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grAtmV1VcDestVci.setStatus("mandatory")
_GrAtmV1VcRateq_Type = Integer32
_GrAtmV1VcRateq_Object = MibTableColumn
grAtmV1VcRateq = _GrAtmV1VcRateq_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 4, 1, 1, 9),
    _GrAtmV1VcRateq_Type()
)
grAtmV1VcRateq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grAtmV1VcRateq.setStatus("mandatory")


class _GrAtmV1VcType_Type(Integer32):
    """Custom type grAtmV1VcType based on Integer32"""
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
        *(("invalid", 2),
          ("other", 1),
          ("permanent", 3),
          ("switched", 4))
    )


_GrAtmV1VcType_Type.__name__ = "Integer32"
_GrAtmV1VcType_Object = MibTableColumn
grAtmV1VcType = _GrAtmV1VcType_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 4, 1, 1, 10),
    _GrAtmV1VcType_Type()
)
grAtmV1VcType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grAtmV1VcType.setStatus("mandatory")
_GrAtmV1RateqTable_Object = MibTable
grAtmV1RateqTable = _GrAtmV1RateqTable_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 4, 3)
)
if mibBuilder.loadTexts:
    grAtmV1RateqTable.setStatus("mandatory")
_GrAtmV1RateqEntry_Object = MibTableRow
grAtmV1RateqEntry = _GrAtmV1RateqEntry_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 4, 3, 1)
)
grAtmV1RateqEntry.setIndexNames(
    (0, "NETSTAR-MIB", "grAtmV1RateqIfIndex"),
    (0, "NETSTAR-MIB", "grAtmV1RateqIndex"),
)
if mibBuilder.loadTexts:
    grAtmV1RateqEntry.setStatus("mandatory")
_GrAtmV1RateqIfIndex_Type = Integer32
_GrAtmV1RateqIfIndex_Object = MibTableColumn
grAtmV1RateqIfIndex = _GrAtmV1RateqIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 4, 3, 1, 1),
    _GrAtmV1RateqIfIndex_Type()
)
grAtmV1RateqIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grAtmV1RateqIfIndex.setStatus("mandatory")


class _GrAtmV1RateqIndex_Type(Integer32):
    """Custom type grAtmV1RateqIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_GrAtmV1RateqIndex_Type.__name__ = "Integer32"
_GrAtmV1RateqIndex_Object = MibTableColumn
grAtmV1RateqIndex = _GrAtmV1RateqIndex_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 4, 3, 1, 2),
    _GrAtmV1RateqIndex_Type()
)
grAtmV1RateqIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grAtmV1RateqIndex.setStatus("mandatory")
_GrAtmV1RateqRate_Type = Integer32
_GrAtmV1RateqRate_Object = MibTableColumn
grAtmV1RateqRate = _GrAtmV1RateqRate_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 4, 3, 1, 3),
    _GrAtmV1RateqRate_Type()
)
grAtmV1RateqRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grAtmV1RateqRate.setStatus("mandatory")


class _GrAtmV1RateqState_Type(Integer32):
    """Custom type grAtmV1RateqState based on Integer32"""
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


_GrAtmV1RateqState_Type.__name__ = "Integer32"
_GrAtmV1RateqState_Object = MibTableColumn
grAtmV1RateqState = _GrAtmV1RateqState_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 4, 3, 1, 4),
    _GrAtmV1RateqState_Type()
)
grAtmV1RateqState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grAtmV1RateqState.setStatus("mandatory")
_GrAtmV1NetToVcTable_Object = MibTable
grAtmV1NetToVcTable = _GrAtmV1NetToVcTable_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 4, 4)
)
if mibBuilder.loadTexts:
    grAtmV1NetToVcTable.setStatus("mandatory")
_GrAtmV1NetToVcEntry_Object = MibTableRow
grAtmV1NetToVcEntry = _GrAtmV1NetToVcEntry_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 4, 4, 1)
)
grAtmV1NetToVcEntry.setIndexNames(
    (0, "NETSTAR-MIB", "grAtmV1NetToVcIfIndex"),
    (0, "NETSTAR-MIB", "grAtmV1NetToVcNetAddress"),
)
if mibBuilder.loadTexts:
    grAtmV1NetToVcEntry.setStatus("mandatory")
_GrAtmV1NetToVcIfIndex_Type = Integer32
_GrAtmV1NetToVcIfIndex_Object = MibTableColumn
grAtmV1NetToVcIfIndex = _GrAtmV1NetToVcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 4, 4, 1, 1),
    _GrAtmV1NetToVcIfIndex_Type()
)
grAtmV1NetToVcIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grAtmV1NetToVcIfIndex.setStatus("mandatory")
_GrAtmV1NetToVcNetAddress_Type = IpAddress
_GrAtmV1NetToVcNetAddress_Object = MibTableColumn
grAtmV1NetToVcNetAddress = _GrAtmV1NetToVcNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 4, 4, 1, 2),
    _GrAtmV1NetToVcNetAddress_Type()
)
grAtmV1NetToVcNetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grAtmV1NetToVcNetAddress.setStatus("mandatory")
_GrAtmV1NetToVcVpi_Type = Integer32
_GrAtmV1NetToVcVpi_Object = MibTableColumn
grAtmV1NetToVcVpi = _GrAtmV1NetToVcVpi_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 4, 4, 1, 3),
    _GrAtmV1NetToVcVpi_Type()
)
grAtmV1NetToVcVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grAtmV1NetToVcVpi.setStatus("mandatory")
_GrAtmV1NetToVcVci_Type = Integer32
_GrAtmV1NetToVcVci_Object = MibTableColumn
grAtmV1NetToVcVci = _GrAtmV1NetToVcVci_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 4, 4, 1, 4),
    _GrAtmV1NetToVcVci_Type()
)
grAtmV1NetToVcVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grAtmV1NetToVcVci.setStatus("mandatory")


class _GrAtmV1NetToVcState_Type(Integer32):
    """Custom type grAtmV1NetToVcState based on Integer32"""
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


_GrAtmV1NetToVcState_Type.__name__ = "Integer32"
_GrAtmV1NetToVcState_Object = MibTableColumn
grAtmV1NetToVcState = _GrAtmV1NetToVcState_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 4, 4, 1, 5),
    _GrAtmV1NetToVcState_Type()
)
grAtmV1NetToVcState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grAtmV1NetToVcState.setStatus("mandatory")
_GrAtmUNI_ObjectIdentity = ObjectIdentity
grAtmUNI = _GrAtmUNI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 5)
)
_GrThreshPoll_ObjectIdentity = ObjectIdentity
grThreshPoll = _GrThreshPoll_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 6)
)
_GrThreshPollTable_Object = MibTable
grThreshPollTable = _GrThreshPollTable_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 6, 3)
)
if mibBuilder.loadTexts:
    grThreshPollTable.setStatus("mandatory")
_GrThreshPollEntry_Object = MibTableRow
grThreshPollEntry = _GrThreshPollEntry_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 6, 3, 1)
)
grThreshPollEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    grThreshPollEntry.setStatus("mandatory")
_GrTPCurrentCount_Type = Counter32
_GrTPCurrentCount_Object = MibTableColumn
grTPCurrentCount = _GrTPCurrentCount_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 6, 3, 1, 1),
    _GrTPCurrentCount_Type()
)
grTPCurrentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grTPCurrentCount.setStatus("mandatory")
_GrTPPreviousCount_Type = Counter32
_GrTPPreviousCount_Object = MibTableColumn
grTPPreviousCount = _GrTPPreviousCount_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 6, 3, 1, 2),
    _GrTPPreviousCount_Type()
)
grTPPreviousCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grTPPreviousCount.setStatus("mandatory")
_GrTPCurrentCountUpper_Type = Counter32
_GrTPCurrentCountUpper_Object = MibTableColumn
grTPCurrentCountUpper = _GrTPCurrentCountUpper_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 6, 3, 1, 3),
    _GrTPCurrentCountUpper_Type()
)
grTPCurrentCountUpper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grTPCurrentCountUpper.setStatus("mandatory")
_GrTPPreviousCountUpper_Type = Counter32
_GrTPPreviousCountUpper_Object = MibTableColumn
grTPPreviousCountUpper = _GrTPPreviousCountUpper_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 6, 3, 1, 4),
    _GrTPPreviousCountUpper_Type()
)
grTPPreviousCountUpper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grTPPreviousCountUpper.setStatus("mandatory")
_GrPingLog_ObjectIdentity = ObjectIdentity
grPingLog = _GrPingLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 7)
)
_GrPingLogTable_Object = MibTable
grPingLogTable = _GrPingLogTable_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 7, 1)
)
if mibBuilder.loadTexts:
    grPingLogTable.setStatus("mandatory")
_GrPingLogEntry_Object = MibTableRow
grPingLogEntry = _GrPingLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 7, 1, 1)
)
grPingLogEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    grPingLogEntry.setStatus("mandatory")


class _GrPLDevDownMsg_Type(DisplayString):
    """Custom type grPLDevDownMsg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GrPLDevDownMsg_Type.__name__ = "DisplayString"
_GrPLDevDownMsg_Object = MibTableColumn
grPLDevDownMsg = _GrPLDevDownMsg_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 7, 1, 1, 1),
    _GrPLDevDownMsg_Type()
)
grPLDevDownMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grPLDevDownMsg.setStatus("mandatory")
_GrAtmp_ObjectIdentity = ObjectIdentity
grAtmp = _GrAtmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8)
)
_Clusterswitch_ObjectIdentity = ObjectIdentity
clusterswitch = _Clusterswitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1080, 1, 2)
)
_Gr2_ObjectIdentity = ObjectIdentity
gr2 = _Gr2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1080, 1, 3)
)
_Grf_ObjectIdentity = ObjectIdentity
grf = _Grf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1080, 1, 4)
)
_Grf400_ObjectIdentity = ObjectIdentity
grf400 = _Grf400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1080, 1, 4, 1)
)
_Grf1600_ObjectIdentity = ObjectIdentity
grf1600 = _Grf1600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1080, 1, 4, 2)
)
_Netstar_daemons_ObjectIdentity = ObjectIdentity
netstar_daemons = _Netstar_daemons_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1080, 2)
)
_Mib2Daemon_ObjectIdentity = ObjectIdentity
mib2Daemon = _Mib2Daemon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1080, 2, 1)
)
_FrameRelayDaemon_ObjectIdentity = ObjectIdentity
frameRelayDaemon = _FrameRelayDaemon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1080, 2, 2)
)
_DynamicRoutingDaemon_ObjectIdentity = ObjectIdentity
dynamicRoutingDaemon = _DynamicRoutingDaemon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1080, 2, 3)
)
_MibmgrDaemon_ObjectIdentity = ObjectIdentity
mibmgrDaemon = _MibmgrDaemon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1080, 2, 4)
)
_AtmpDaemon_ObjectIdentity = ObjectIdentity
atmpDaemon = _AtmpDaemon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1080, 2, 5)
)

# Managed Objects groups


# Notification objects

coldStart = NotificationType(
    (1, 3, 6, 1, 2, 1, 11, 0, 0)
)
if mibBuilder.loadTexts:
    coldStart.setStatus(
        ""
    )

warmStart = NotificationType(
    (1, 3, 6, 1, 2, 1, 11, 0, 1)
)
if mibBuilder.loadTexts:
    warmStart.setStatus(
        ""
    )

linkDown = NotificationType(
    (1, 3, 6, 1, 2, 1, 11, 0, 2)
)
linkDown.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    linkDown.setStatus(
        ""
    )

linkUp = NotificationType(
    (1, 3, 6, 1, 2, 1, 11, 0, 3)
)
linkUp.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    linkUp.setStatus(
        ""
    )

authenticationFailure = NotificationType(
    (1, 3, 6, 1, 2, 1, 11, 0, 4)
)
if mibBuilder.loadTexts:
    authenticationFailure.setStatus(
        ""
    )

grPowerSupplyFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 0, 1)
)
grPowerSupplyFailure.setObjects(
    ("NETSTAR-MIB", "grPowerSupplyStatus")
)
if mibBuilder.loadTexts:
    grPowerSupplyFailure.setStatus(
        ""
    )

grOverTemp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 0, 2)
)
grOverTemp.setObjects(
    ("NETSTAR-MIB", "grTempStatus")
)
if mibBuilder.loadTexts:
    grOverTemp.setStatus(
        ""
    )

grFanFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 0, 3)
)
grFanFailure.setObjects(
    ("NETSTAR-MIB", "grFanStatus")
)
if mibBuilder.loadTexts:
    grFanFailure.setStatus(
        ""
    )

grCardDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 0, 4)
)
grCardDown.setObjects(
      *(("NETSTAR-MIB", "grPortCardSlot"),
        ("NETSTAR-MIB", "grPortCardCurrentState"))
)
if mibBuilder.loadTexts:
    grCardDown.setStatus(
        ""
    )

grCardUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 0, 5)
)
grCardUp.setObjects(
    ("NETSTAR-MIB", "grPortCardSlot")
)
if mibBuilder.loadTexts:
    grCardUp.setStatus(
        ""
    )

grSONETLossOfFrame = NotificationType(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 0, 6)
)
grSONETLossOfFrame.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    grSONETLossOfFrame.setStatus(
        ""
    )

grSONETLossOfSignal = NotificationType(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 0, 7)
)
grSONETLossOfSignal.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    grSONETLossOfSignal.setStatus(
        ""
    )

grSONETSTSPathLossOfPointer = NotificationType(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 0, 8)
)
grSONETSTSPathLossOfPointer.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    grSONETSTSPathLossOfPointer.setStatus(
        ""
    )

grSONETVTLossOfPointer = NotificationType(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 0, 9)
)
grSONETVTLossOfPointer.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    grSONETVTLossOfPointer.setStatus(
        ""
    )

grSONETLineAlarmIndicationSignal = NotificationType(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 0, 10)
)
grSONETLineAlarmIndicationSignal.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    grSONETLineAlarmIndicationSignal.setStatus(
        ""
    )

grSONETSTSPathAlarmIndicationSignal = NotificationType(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 0, 11)
)
grSONETSTSPathAlarmIndicationSignal.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    grSONETSTSPathAlarmIndicationSignal.setStatus(
        ""
    )

grSONETVTPathAlarmIndicationSignal = NotificationType(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 0, 12)
)
grSONETVTPathAlarmIndicationSignal.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    grSONETVTPathAlarmIndicationSignal.setStatus(
        ""
    )

grSONETLineRemoteDefectIndication = NotificationType(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 0, 13)
)
grSONETLineRemoteDefectIndication.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    grSONETLineRemoteDefectIndication.setStatus(
        ""
    )

grSONETVTPathRemoteDefectIndication = NotificationType(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 0, 14)
)
grSONETVTPathRemoteDefectIndication.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    grSONETVTPathRemoteDefectIndication.setStatus(
        ""
    )

grSONETTCLossOfCellDelineation = NotificationType(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 0, 15)
)
grSONETTCLossOfCellDelineation.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    grSONETTCLossOfCellDelineation.setStatus(
        ""
    )

grAtmPVCUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 0, 16)
)
grAtmPVCUp.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("NETSTAR-MIB", "grAtmV1VcVpi"),
        ("NETSTAR-MIB", "grAtmV1VcVci"))
)
if mibBuilder.loadTexts:
    grAtmPVCUp.setStatus(
        ""
    )

grAtmPVCDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 0, 17)
)
grAtmPVCDown.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("NETSTAR-MIB", "grAtmV1VcVpi"),
        ("NETSTAR-MIB", "grAtmV1VcVci"))
)
if mibBuilder.loadTexts:
    grAtmPVCDown.setStatus(
        ""
    )

grInterfaceDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 0, 18)
)
grInterfaceDown.setObjects(
    ("NETSTAR-MIB", "grPLDevDownMsg")
)
if mibBuilder.loadTexts:
    grInterfaceDown.setStatus(
        ""
    )

grIfInOctetsHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 0, 19)
)
grIfInOctetsHigh.setObjects(
      *(("NETSTAR-MIB", "grTPPreviousCount"),
        ("NETSTAR-MIB", "grTPCurrentCount"))
)
if mibBuilder.loadTexts:
    grIfInOctetsHigh.setStatus(
        ""
    )

grIfInOctetsLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 0, 20)
)
grIfInOctetsLow.setObjects(
      *(("NETSTAR-MIB", "grTPPreviousCount"),
        ("NETSTAR-MIB", "grTPCurrentCount"))
)
if mibBuilder.loadTexts:
    grIfInOctetsLow.setStatus(
        ""
    )

grIfOutOctetsHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 0, 21)
)
grIfOutOctetsHigh.setObjects(
      *(("NETSTAR-MIB", "grTPPreviousCount"),
        ("NETSTAR-MIB", "grTPCurrentCount"))
)
if mibBuilder.loadTexts:
    grIfOutOctetsHigh.setStatus(
        ""
    )

grIfOutOctetsLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 0, 22)
)
grIfOutOctetsLow.setObjects(
      *(("NETSTAR-MIB", "grTPPreviousCount"),
        ("NETSTAR-MIB", "grTPCurrentCount"))
)
if mibBuilder.loadTexts:
    grIfOutOctetsLow.setStatus(
        ""
    )

grIfInUcastPktsHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 0, 23)
)
grIfInUcastPktsHigh.setObjects(
      *(("NETSTAR-MIB", "grTPPreviousCount"),
        ("NETSTAR-MIB", "grTPCurrentCount"))
)
if mibBuilder.loadTexts:
    grIfInUcastPktsHigh.setStatus(
        ""
    )

grIfInUcastPktsLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 0, 24)
)
grIfInUcastPktsLow.setObjects(
      *(("NETSTAR-MIB", "grTPPreviousCount"),
        ("NETSTAR-MIB", "grTPCurrentCount"))
)
if mibBuilder.loadTexts:
    grIfInUcastPktsLow.setStatus(
        ""
    )

grIfOutUcastPktsHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 0, 25)
)
grIfOutUcastPktsHigh.setObjects(
      *(("NETSTAR-MIB", "grTPPreviousCount"),
        ("NETSTAR-MIB", "grTPCurrentCount"))
)
if mibBuilder.loadTexts:
    grIfOutUcastPktsHigh.setStatus(
        ""
    )

grIfOutUcastPktsLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 0, 26)
)
grIfOutUcastPktsLow.setObjects(
      *(("NETSTAR-MIB", "grTPPreviousCount"),
        ("NETSTAR-MIB", "grTPCurrentCount"))
)
if mibBuilder.loadTexts:
    grIfOutUcastPktsLow.setStatus(
        ""
    )

grIfInErrorsHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 0, 27)
)
grIfInErrorsHigh.setObjects(
      *(("NETSTAR-MIB", "grTPPreviousCount"),
        ("NETSTAR-MIB", "grTPCurrentCount"))
)
if mibBuilder.loadTexts:
    grIfInErrorsHigh.setStatus(
        ""
    )

grIfInErrorsLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 0, 28)
)
grIfInErrorsLow.setObjects(
      *(("NETSTAR-MIB", "grTPPreviousCount"),
        ("NETSTAR-MIB", "grTPCurrentCount"))
)
if mibBuilder.loadTexts:
    grIfInErrorsLow.setStatus(
        ""
    )

grIfOutErrorsHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 0, 29)
)
grIfOutErrorsHigh.setObjects(
      *(("NETSTAR-MIB", "grTPPreviousCount"),
        ("NETSTAR-MIB", "grTPCurrentCount"))
)
if mibBuilder.loadTexts:
    grIfOutErrorsHigh.setStatus(
        ""
    )

grIfOutErrorsLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 0, 30)
)
grIfOutErrorsLow.setObjects(
      *(("NETSTAR-MIB", "grTPPreviousCount"),
        ("NETSTAR-MIB", "grTPCurrentCount"))
)
if mibBuilder.loadTexts:
    grIfOutErrorsLow.setStatus(
        ""
    )

grIfInDiscardsHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 0, 31)
)
grIfInDiscardsHigh.setObjects(
      *(("NETSTAR-MIB", "grTPPreviousCount"),
        ("NETSTAR-MIB", "grTPCurrentCount"))
)
if mibBuilder.loadTexts:
    grIfInDiscardsHigh.setStatus(
        ""
    )

grIfInDiscardsLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 0, 32)
)
grIfInDiscardsLow.setObjects(
      *(("NETSTAR-MIB", "grTPPreviousCount"),
        ("NETSTAR-MIB", "grTPCurrentCount"))
)
if mibBuilder.loadTexts:
    grIfInDiscardsLow.setStatus(
        ""
    )

grIfOutDiscardsHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 0, 33)
)
grIfOutDiscardsHigh.setObjects(
      *(("NETSTAR-MIB", "grTPPreviousCount"),
        ("NETSTAR-MIB", "grTPCurrentCount"))
)
if mibBuilder.loadTexts:
    grIfOutDiscardsHigh.setStatus(
        ""
    )

grIfOutDiscardsLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 0, 34)
)
grIfOutDiscardsLow.setObjects(
      *(("NETSTAR-MIB", "grTPPreviousCount"),
        ("NETSTAR-MIB", "grTPCurrentCount"))
)
if mibBuilder.loadTexts:
    grIfOutDiscardsLow.setStatus(
        ""
    )

grGatedDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 0, 35)
)
if mibBuilder.loadTexts:
    grGatedDown.setStatus(
        ""
    )

grSnmpReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 0, 36)
)
if mibBuilder.loadTexts:
    grSnmpReset.setStatus(
        ""
    )

grIfHCInOctetsHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 0, 37)
)
grIfHCInOctetsHigh.setObjects(
      *(("NETSTAR-MIB", "grTPPreviousCountUpper"),
        ("NETSTAR-MIB", "grTPPreviousCount"),
        ("NETSTAR-MIB", "grTPCurrentCountUpper"),
        ("NETSTAR-MIB", "grTPCurrentCount"))
)
if mibBuilder.loadTexts:
    grIfHCInOctetsHigh.setStatus(
        ""
    )

grIfHCInOctetsLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 0, 38)
)
grIfHCInOctetsLow.setObjects(
      *(("NETSTAR-MIB", "grTPPreviousCountUpper"),
        ("NETSTAR-MIB", "grTPPreviousCount"),
        ("NETSTAR-MIB", "grTPCurrentCountUpper"),
        ("NETSTAR-MIB", "grTPCurrentCount"))
)
if mibBuilder.loadTexts:
    grIfHCInOctetsLow.setStatus(
        ""
    )

grIfHCInUcastPktsHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 0, 39)
)
grIfHCInUcastPktsHigh.setObjects(
      *(("NETSTAR-MIB", "grTPPreviousCountUpper"),
        ("NETSTAR-MIB", "grTPPreviousCount"),
        ("NETSTAR-MIB", "grTPCurrentCountUpper"),
        ("NETSTAR-MIB", "grTPCurrentCount"))
)
if mibBuilder.loadTexts:
    grIfHCInUcastPktsHigh.setStatus(
        ""
    )

grIfHCInUcastPktsLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 0, 40)
)
grIfHCInUcastPktsLow.setObjects(
      *(("NETSTAR-MIB", "grTPPreviousCountUpper"),
        ("NETSTAR-MIB", "grTPPreviousCount"),
        ("NETSTAR-MIB", "grTPCurrentCountUpper"),
        ("NETSTAR-MIB", "grTPCurrentCount"))
)
if mibBuilder.loadTexts:
    grIfHCInUcastPktsLow.setStatus(
        ""
    )

grIfHCInMulticastPktsHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 0, 41)
)
grIfHCInMulticastPktsHigh.setObjects(
      *(("NETSTAR-MIB", "grTPPreviousCountUpper"),
        ("NETSTAR-MIB", "grTPPreviousCount"),
        ("NETSTAR-MIB", "grTPCurrentCountUpper"),
        ("NETSTAR-MIB", "grTPCurrentCount"))
)
if mibBuilder.loadTexts:
    grIfHCInMulticastPktsHigh.setStatus(
        ""
    )

grIfHCInMulticastPktsLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 0, 42)
)
grIfHCInMulticastPktsLow.setObjects(
      *(("NETSTAR-MIB", "grTPPreviousCountUpper"),
        ("NETSTAR-MIB", "grTPPreviousCount"),
        ("NETSTAR-MIB", "grTPCurrentCountUpper"),
        ("NETSTAR-MIB", "grTPCurrentCount"))
)
if mibBuilder.loadTexts:
    grIfHCInMulticastPktsLow.setStatus(
        ""
    )

grIfHCInBroadcastPktsHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 0, 43)
)
grIfHCInBroadcastPktsHigh.setObjects(
      *(("NETSTAR-MIB", "grTPPreviousCountUpper"),
        ("NETSTAR-MIB", "grTPPreviousCount"),
        ("NETSTAR-MIB", "grTPCurrentCountUpper"),
        ("NETSTAR-MIB", "grTPCurrentCount"))
)
if mibBuilder.loadTexts:
    grIfHCInBroadcastPktsHigh.setStatus(
        ""
    )

grIfHCInBroadcastPktsLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 0, 44)
)
grIfHCInBroadcastPktsLow.setObjects(
      *(("NETSTAR-MIB", "grTPPreviousCountUpper"),
        ("NETSTAR-MIB", "grTPPreviousCount"),
        ("NETSTAR-MIB", "grTPCurrentCountUpper"),
        ("NETSTAR-MIB", "grTPCurrentCount"))
)
if mibBuilder.loadTexts:
    grIfHCInBroadcastPktsLow.setStatus(
        ""
    )

grIfHCOutOctetsHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 0, 45)
)
grIfHCOutOctetsHigh.setObjects(
      *(("NETSTAR-MIB", "grTPPreviousCountUpper"),
        ("NETSTAR-MIB", "grTPPreviousCount"),
        ("NETSTAR-MIB", "grTPCurrentCountUpper"),
        ("NETSTAR-MIB", "grTPCurrentCount"))
)
if mibBuilder.loadTexts:
    grIfHCOutOctetsHigh.setStatus(
        ""
    )

grIfHCOutOctetsLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 0, 46)
)
grIfHCOutOctetsLow.setObjects(
      *(("NETSTAR-MIB", "grTPPreviousCountUpper"),
        ("NETSTAR-MIB", "grTPPreviousCount"),
        ("NETSTAR-MIB", "grTPCurrentCountUpper"),
        ("NETSTAR-MIB", "grTPCurrentCount"))
)
if mibBuilder.loadTexts:
    grIfHCOutOctetsLow.setStatus(
        ""
    )

grIfHCOutUcastPktsHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 0, 47)
)
grIfHCOutUcastPktsHigh.setObjects(
      *(("NETSTAR-MIB", "grTPPreviousCountUpper"),
        ("NETSTAR-MIB", "grTPPreviousCount"),
        ("NETSTAR-MIB", "grTPCurrentCountUpper"),
        ("NETSTAR-MIB", "grTPCurrentCount"))
)
if mibBuilder.loadTexts:
    grIfHCOutUcastPktsHigh.setStatus(
        ""
    )

grIfHCOutUcastPktsLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 0, 48)
)
grIfHCOutUcastPktsLow.setObjects(
      *(("NETSTAR-MIB", "grTPPreviousCountUpper"),
        ("NETSTAR-MIB", "grTPPreviousCount"),
        ("NETSTAR-MIB", "grTPCurrentCountUpper"),
        ("NETSTAR-MIB", "grTPCurrentCount"))
)
if mibBuilder.loadTexts:
    grIfHCOutUcastPktsLow.setStatus(
        ""
    )

grIfHCOutMulticastPktsHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 0, 49)
)
grIfHCOutMulticastPktsHigh.setObjects(
      *(("NETSTAR-MIB", "grTPPreviousCountUpper"),
        ("NETSTAR-MIB", "grTPPreviousCount"),
        ("NETSTAR-MIB", "grTPCurrentCountUpper"),
        ("NETSTAR-MIB", "grTPCurrentCount"))
)
if mibBuilder.loadTexts:
    grIfHCOutMulticastPktsHigh.setStatus(
        ""
    )

grIfHCOutMulticastPktsLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 0, 50)
)
grIfHCOutMulticastPktsLow.setObjects(
      *(("NETSTAR-MIB", "grTPPreviousCountUpper"),
        ("NETSTAR-MIB", "grTPPreviousCount"),
        ("NETSTAR-MIB", "grTPCurrentCountUpper"),
        ("NETSTAR-MIB", "grTPCurrentCount"))
)
if mibBuilder.loadTexts:
    grIfHCOutMulticastPktsLow.setStatus(
        ""
    )

grIfHCOutBroadcastPktsHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 0, 51)
)
grIfHCOutBroadcastPktsHigh.setObjects(
      *(("NETSTAR-MIB", "grTPPreviousCountUpper"),
        ("NETSTAR-MIB", "grTPPreviousCount"),
        ("NETSTAR-MIB", "grTPCurrentCountUpper"),
        ("NETSTAR-MIB", "grTPCurrentCount"))
)
if mibBuilder.loadTexts:
    grIfHCOutBroadcastPktsHigh.setStatus(
        ""
    )

grIfHCOutBroadcastPktsLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 0, 52)
)
grIfHCOutBroadcastPktsLow.setObjects(
      *(("NETSTAR-MIB", "grTPPreviousCountUpper"),
        ("NETSTAR-MIB", "grTPPreviousCount"),
        ("NETSTAR-MIB", "grTPCurrentCountUpper"),
        ("NETSTAR-MIB", "grTPCurrentCount"))
)
if mibBuilder.loadTexts:
    grIfHCOutBroadcastPktsLow.setStatus(
        ""
    )

grBackupRestoreMessages = NotificationType(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 0, 53)
)
grBackupRestoreMessages.setObjects(
    ("NETSTAR-MIB", "grStatusMsg")
)
if mibBuilder.loadTexts:
    grBackupRestoreMessages.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETSTAR-MIB",
    **{"coldStart": coldStart,
       "warmStart": warmStart,
       "linkDown": linkDown,
       "linkUp": linkUp,
       "authenticationFailure": authenticationFailure,
       "netstar": netstar,
       "netstar-products": netstar_products,
       "gigarouter": gigarouter,
       "grPowerSupplyFailure": grPowerSupplyFailure,
       "grOverTemp": grOverTemp,
       "grFanFailure": grFanFailure,
       "grCardDown": grCardDown,
       "grCardUp": grCardUp,
       "grSONETLossOfFrame": grSONETLossOfFrame,
       "grSONETLossOfSignal": grSONETLossOfSignal,
       "grSONETSTSPathLossOfPointer": grSONETSTSPathLossOfPointer,
       "grSONETVTLossOfPointer": grSONETVTLossOfPointer,
       "grSONETLineAlarmIndicationSignal": grSONETLineAlarmIndicationSignal,
       "grSONETSTSPathAlarmIndicationSignal": grSONETSTSPathAlarmIndicationSignal,
       "grSONETVTPathAlarmIndicationSignal": grSONETVTPathAlarmIndicationSignal,
       "grSONETLineRemoteDefectIndication": grSONETLineRemoteDefectIndication,
       "grSONETVTPathRemoteDefectIndication": grSONETVTPathRemoteDefectIndication,
       "grSONETTCLossOfCellDelineation": grSONETTCLossOfCellDelineation,
       "grAtmPVCUp": grAtmPVCUp,
       "grAtmPVCDown": grAtmPVCDown,
       "grInterfaceDown": grInterfaceDown,
       "grIfInOctetsHigh": grIfInOctetsHigh,
       "grIfInOctetsLow": grIfInOctetsLow,
       "grIfOutOctetsHigh": grIfOutOctetsHigh,
       "grIfOutOctetsLow": grIfOutOctetsLow,
       "grIfInUcastPktsHigh": grIfInUcastPktsHigh,
       "grIfInUcastPktsLow": grIfInUcastPktsLow,
       "grIfOutUcastPktsHigh": grIfOutUcastPktsHigh,
       "grIfOutUcastPktsLow": grIfOutUcastPktsLow,
       "grIfInErrorsHigh": grIfInErrorsHigh,
       "grIfInErrorsLow": grIfInErrorsLow,
       "grIfOutErrorsHigh": grIfOutErrorsHigh,
       "grIfOutErrorsLow": grIfOutErrorsLow,
       "grIfInDiscardsHigh": grIfInDiscardsHigh,
       "grIfInDiscardsLow": grIfInDiscardsLow,
       "grIfOutDiscardsHigh": grIfOutDiscardsHigh,
       "grIfOutDiscardsLow": grIfOutDiscardsLow,
       "grGatedDown": grGatedDown,
       "grSnmpReset": grSnmpReset,
       "grIfHCInOctetsHigh": grIfHCInOctetsHigh,
       "grIfHCInOctetsLow": grIfHCInOctetsLow,
       "grIfHCInUcastPktsHigh": grIfHCInUcastPktsHigh,
       "grIfHCInUcastPktsLow": grIfHCInUcastPktsLow,
       "grIfHCInMulticastPktsHigh": grIfHCInMulticastPktsHigh,
       "grIfHCInMulticastPktsLow": grIfHCInMulticastPktsLow,
       "grIfHCInBroadcastPktsHigh": grIfHCInBroadcastPktsHigh,
       "grIfHCInBroadcastPktsLow": grIfHCInBroadcastPktsLow,
       "grIfHCOutOctetsHigh": grIfHCOutOctetsHigh,
       "grIfHCOutOctetsLow": grIfHCOutOctetsLow,
       "grIfHCOutUcastPktsHigh": grIfHCOutUcastPktsHigh,
       "grIfHCOutUcastPktsLow": grIfHCOutUcastPktsLow,
       "grIfHCOutMulticastPktsHigh": grIfHCOutMulticastPktsHigh,
       "grIfHCOutMulticastPktsLow": grIfHCOutMulticastPktsLow,
       "grIfHCOutBroadcastPktsHigh": grIfHCOutBroadcastPktsHigh,
       "grIfHCOutBroadcastPktsLow": grIfHCOutBroadcastPktsLow,
       "grBackupRestoreMessages": grBackupRestoreMessages,
       "grChassis": grChassis,
       "grPowerSupplyStatus": grPowerSupplyStatus,
       "grTempStatus": grTempStatus,
       "grFanStatus": grFanStatus,
       "grPortCardNumber": grPortCardNumber,
       "grPortCardTable": grPortCardTable,
       "grPortCardEntry": grPortCardEntry,
       "grPortCardSlot": grPortCardSlot,
       "grPortCardHWtype": grPortCardHWtype,
       "grPortCardCurrentState": grPortCardCurrentState,
       "grGatedStatus": grGatedStatus,
       "grTransportMethod": grTransportMethod,
       "grFTPUserName": grFTPUserName,
       "grFTPPassword": grFTPPassword,
       "grServerName": grServerName,
       "grFileName": grFileName,
       "grLastOperation": grLastOperation,
       "grStatusMsg": grStatusMsg,
       "grBackup": grBackup,
       "grCompare": grCompare,
       "grRestore": grRestore,
       "grHIPPI": grHIPPI,
       "grFDDI4": grFDDI4,
       "grAtmV1": grAtmV1,
       "grAtmV1VcTable": grAtmV1VcTable,
       "grAtmV1VcEntry": grAtmV1VcEntry,
       "grAtmV1VcIfIndex": grAtmV1VcIfIndex,
       "grAtmV1VcVpi": grAtmV1VcVpi,
       "grAtmV1VcVci": grAtmV1VcVci,
       "grAtmV1VcAal": grAtmV1VcAal,
       "grAtmV1VcProtocol": grAtmV1VcProtocol,
       "grAtmV1VcDestIfIndex": grAtmV1VcDestIfIndex,
       "grAtmV1VcDestVpi": grAtmV1VcDestVpi,
       "grAtmV1VcDestVci": grAtmV1VcDestVci,
       "grAtmV1VcRateq": grAtmV1VcRateq,
       "grAtmV1VcType": grAtmV1VcType,
       "grAtmV1RateqTable": grAtmV1RateqTable,
       "grAtmV1RateqEntry": grAtmV1RateqEntry,
       "grAtmV1RateqIfIndex": grAtmV1RateqIfIndex,
       "grAtmV1RateqIndex": grAtmV1RateqIndex,
       "grAtmV1RateqRate": grAtmV1RateqRate,
       "grAtmV1RateqState": grAtmV1RateqState,
       "grAtmV1NetToVcTable": grAtmV1NetToVcTable,
       "grAtmV1NetToVcEntry": grAtmV1NetToVcEntry,
       "grAtmV1NetToVcIfIndex": grAtmV1NetToVcIfIndex,
       "grAtmV1NetToVcNetAddress": grAtmV1NetToVcNetAddress,
       "grAtmV1NetToVcVpi": grAtmV1NetToVcVpi,
       "grAtmV1NetToVcVci": grAtmV1NetToVcVci,
       "grAtmV1NetToVcState": grAtmV1NetToVcState,
       "grAtmUNI": grAtmUNI,
       "grThreshPoll": grThreshPoll,
       "grThreshPollTable": grThreshPollTable,
       "grThreshPollEntry": grThreshPollEntry,
       "grTPCurrentCount": grTPCurrentCount,
       "grTPPreviousCount": grTPPreviousCount,
       "grTPCurrentCountUpper": grTPCurrentCountUpper,
       "grTPPreviousCountUpper": grTPPreviousCountUpper,
       "grPingLog": grPingLog,
       "grPingLogTable": grPingLogTable,
       "grPingLogEntry": grPingLogEntry,
       "grPLDevDownMsg": grPLDevDownMsg,
       "grAtmp": grAtmp,
       "clusterswitch": clusterswitch,
       "gr2": gr2,
       "grf": grf,
       "grf400": grf400,
       "grf1600": grf1600,
       "netstar-daemons": netstar_daemons,
       "mib2Daemon": mib2Daemon,
       "frameRelayDaemon": frameRelayDaemon,
       "dynamicRoutingDaemon": dynamicRoutingDaemon,
       "mibmgrDaemon": mibmgrDaemon,
       "atmpDaemon": atmpDaemon}
)
