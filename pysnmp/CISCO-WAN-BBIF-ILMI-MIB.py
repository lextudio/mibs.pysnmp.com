# SNMP MIB module (CISCO-WAN-BBIF-ILMI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-WAN-BBIF-ILMI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:12:54 2024
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

(AtmIlmiNetworkPrefix,) = mibBuilder.importSymbols(
    "ATM-TC-MIB",
    "AtmIlmiNetworkPrefix")

(bbIfCnf,
 bbIfCnt) = mibBuilder.importSymbols(
    "BASIS-MIB",
    "bbIfCnf",
    "bbIfCnt")

(ciscoWan,) = mibBuilder.importSymbols(
    "CISCOWAN-SMI",
    "ciscoWan")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

ciscoWanBbifIlmiMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 33)
)
ciscoWanBbifIlmiMIB.setRevisions(
        ("2002-12-20 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BbIfCnfSigILMIGrp_ObjectIdentity = ObjectIdentity
bbIfCnfSigILMIGrp = _BbIfCnfSigILMIGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 6, 1, 2)
)
_BbIfCnfSigILMIGrpTable_Object = MibTable
bbIfCnfSigILMIGrpTable = _BbIfCnfSigILMIGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 6, 1, 2, 1)
)
if mibBuilder.loadTexts:
    bbIfCnfSigILMIGrpTable.setStatus("current")
_BbIfCnfSigILMIGrpEntry_Object = MibTableRow
bbIfCnfSigILMIGrpEntry = _BbIfCnfSigILMIGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 6, 1, 2, 1, 1)
)
bbIfCnfSigILMIGrpEntry.setIndexNames(
    (0, "CISCO-WAN-BBIF-ILMI-MIB", "bbIfSigPortNum"),
)
if mibBuilder.loadTexts:
    bbIfCnfSigILMIGrpEntry.setStatus("current")


class _BbIfSigPortNum_Type(Integer32):
    """Custom type bbIfSigPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_BbIfSigPortNum_Type.__name__ = "Integer32"
_BbIfSigPortNum_Object = MibTableColumn
bbIfSigPortNum = _BbIfSigPortNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 6, 1, 2, 1, 1, 1),
    _BbIfSigPortNum_Type()
)
bbIfSigPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bbIfSigPortNum.setStatus("current")


class _BbIfIlmiEnable_Type(Integer32):
    """Custom type bbIfIlmiEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_BbIfIlmiEnable_Type.__name__ = "Integer32"
_BbIfIlmiEnable_Object = MibTableColumn
bbIfIlmiEnable = _BbIfIlmiEnable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 6, 1, 2, 1, 1, 2),
    _BbIfIlmiEnable_Type()
)
bbIfIlmiEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bbIfIlmiEnable.setStatus("current")


class _BbIfSignallingProtocolType_Type(Integer32):
    """Custom type bbIfSignallingProtocolType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("iLMI", 3),
          ("noSignalling", 2),
          ("other", 1))
    )


_BbIfSignallingProtocolType_Type.__name__ = "Integer32"
_BbIfSignallingProtocolType_Object = MibTableColumn
bbIfSignallingProtocolType = _BbIfSignallingProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 6, 1, 2, 1, 1, 3),
    _BbIfSignallingProtocolType_Type()
)
bbIfSignallingProtocolType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bbIfSignallingProtocolType.setStatus("current")


class _BbIfSignallingVpi_Type(Integer32):
    """Custom type bbIfSignallingVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_BbIfSignallingVpi_Type.__name__ = "Integer32"
_BbIfSignallingVpi_Object = MibTableColumn
bbIfSignallingVpi = _BbIfSignallingVpi_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 6, 1, 2, 1, 1, 4),
    _BbIfSignallingVpi_Type()
)
bbIfSignallingVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bbIfSignallingVpi.setStatus("current")


class _BbIfSignallingVci_Type(Integer32):
    """Custom type bbIfSignallingVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BbIfSignallingVci_Type.__name__ = "Integer32"
_BbIfSignallingVci_Object = MibTableColumn
bbIfSignallingVci = _BbIfSignallingVci_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 6, 1, 2, 1, 1, 5),
    _BbIfSignallingVci_Type()
)
bbIfSignallingVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bbIfSignallingVci.setStatus("current")
_BbIfAddrPrefix_Type = AtmIlmiNetworkPrefix
_BbIfAddrPrefix_Object = MibTableColumn
bbIfAddrPrefix = _BbIfAddrPrefix_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 6, 1, 2, 1, 1, 6),
    _BbIfAddrPrefix_Type()
)
bbIfAddrPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bbIfAddrPrefix.setStatus("current")
_BbIfCustomerId_Type = Integer32
_BbIfCustomerId_Object = MibTableColumn
bbIfCustomerId = _BbIfCustomerId_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 6, 1, 2, 1, 1, 7),
    _BbIfCustomerId_Type()
)
bbIfCustomerId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bbIfCustomerId.setStatus("current")
_BbIfProtocolRevNo_Type = Integer32
_BbIfProtocolRevNo_Object = MibTableColumn
bbIfProtocolRevNo = _BbIfProtocolRevNo_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 6, 1, 2, 1, 1, 8),
    _BbIfProtocolRevNo_Type()
)
bbIfProtocolRevNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bbIfProtocolRevNo.setStatus("current")


class _BbIfIlmiTrapEnable_Type(Integer32):
    """Custom type bbIfIlmiTrapEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_BbIfIlmiTrapEnable_Type.__name__ = "Integer32"
_BbIfIlmiTrapEnable_Object = MibTableColumn
bbIfIlmiTrapEnable = _BbIfIlmiTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 6, 1, 2, 1, 1, 9),
    _BbIfIlmiTrapEnable_Type()
)
bbIfIlmiTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bbIfIlmiTrapEnable.setStatus("current")


class _BbIfMinTrapInterval_Type(Integer32):
    """Custom type bbIfMinTrapInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_BbIfMinTrapInterval_Type.__name__ = "Integer32"
_BbIfMinTrapInterval_Object = MibTableColumn
bbIfMinTrapInterval = _BbIfMinTrapInterval_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 6, 1, 2, 1, 1, 10),
    _BbIfMinTrapInterval_Type()
)
bbIfMinTrapInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bbIfMinTrapInterval.setStatus("current")
if mibBuilder.loadTexts:
    bbIfMinTrapInterval.setUnits("seconds")


class _BbIfKeepAlivePollingEnable_Type(Integer32):
    """Custom type bbIfKeepAlivePollingEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_BbIfKeepAlivePollingEnable_Type.__name__ = "Integer32"
_BbIfKeepAlivePollingEnable_Object = MibTableColumn
bbIfKeepAlivePollingEnable = _BbIfKeepAlivePollingEnable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 6, 1, 2, 1, 1, 11),
    _BbIfKeepAlivePollingEnable_Type()
)
bbIfKeepAlivePollingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bbIfKeepAlivePollingEnable.setStatus("current")


class _BbIfErrorThresholdN491_Type(Integer32):
    """Custom type bbIfErrorThresholdN491 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_BbIfErrorThresholdN491_Type.__name__ = "Integer32"
_BbIfErrorThresholdN491_Object = MibTableColumn
bbIfErrorThresholdN491 = _BbIfErrorThresholdN491_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 6, 1, 2, 1, 1, 12),
    _BbIfErrorThresholdN491_Type()
)
bbIfErrorThresholdN491.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bbIfErrorThresholdN491.setStatus("current")


class _BbIfEventThresholdN492_Type(Integer32):
    """Custom type bbIfEventThresholdN492 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_BbIfEventThresholdN492_Type.__name__ = "Integer32"
_BbIfEventThresholdN492_Object = MibTableColumn
bbIfEventThresholdN492 = _BbIfEventThresholdN492_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 6, 1, 2, 1, 1, 13),
    _BbIfEventThresholdN492_Type()
)
bbIfEventThresholdN492.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bbIfEventThresholdN492.setStatus("current")


class _BbIfPollingIntervalT491_Type(Integer32):
    """Custom type bbIfPollingIntervalT491 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              10,
              15,
              20,
              25,
              30,
              35,
              40,
              45,
              50,
              55,
              60)
        )
    )
    namedValues = NamedValues(
        *(("v1", 5),
          ("v10", 50),
          ("v11", 55),
          ("v12", 60),
          ("v2", 10),
          ("v3", 15),
          ("v4", 20),
          ("v5", 25),
          ("v6", 30),
          ("v7", 35),
          ("v8", 40),
          ("v9", 45))
    )


_BbIfPollingIntervalT491_Type.__name__ = "Integer32"
_BbIfPollingIntervalT491_Object = MibTableColumn
bbIfPollingIntervalT491 = _BbIfPollingIntervalT491_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 6, 1, 2, 1, 1, 14),
    _BbIfPollingIntervalT491_Type()
)
bbIfPollingIntervalT491.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bbIfPollingIntervalT491.setStatus("current")
if mibBuilder.loadTexts:
    bbIfPollingIntervalT491.setUnits("seconds")


class _BbIfMinEnquiryIntervalT493_Type(Integer32):
    """Custom type bbIfMinEnquiryIntervalT493 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_BbIfMinEnquiryIntervalT493_Type.__name__ = "Integer32"
_BbIfMinEnquiryIntervalT493_Object = MibTableColumn
bbIfMinEnquiryIntervalT493 = _BbIfMinEnquiryIntervalT493_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 6, 1, 2, 1, 1, 15),
    _BbIfMinEnquiryIntervalT493_Type()
)
bbIfMinEnquiryIntervalT493.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bbIfMinEnquiryIntervalT493.setStatus("current")


class _BbIfAddrRegEnable_Type(Integer32):
    """Custom type bbIfAddrRegEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_BbIfAddrRegEnable_Type.__name__ = "Integer32"
_BbIfAddrRegEnable_Object = MibTableColumn
bbIfAddrRegEnable = _BbIfAddrRegEnable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 6, 1, 2, 1, 1, 16),
    _BbIfAddrRegEnable_Type()
)
bbIfAddrRegEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bbIfAddrRegEnable.setStatus("current")
_BbIfCntSigILMIGrp_ObjectIdentity = ObjectIdentity
bbIfCntSigILMIGrp = _BbIfCntSigILMIGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 6, 4, 2)
)
_BbIfCntSigILMIGrpTable_Object = MibTable
bbIfCntSigILMIGrpTable = _BbIfCntSigILMIGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 6, 4, 2, 1)
)
if mibBuilder.loadTexts:
    bbIfCntSigILMIGrpTable.setStatus("current")
_BbIfCntSigILMIGrpEntry_Object = MibTableRow
bbIfCntSigILMIGrpEntry = _BbIfCntSigILMIGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 6, 4, 2, 1, 1)
)
bbIfCntSigILMIGrpEntry.setIndexNames(
    (0, "CISCO-WAN-BBIF-ILMI-MIB", "sigCntBbIfNum"),
)
if mibBuilder.loadTexts:
    bbIfCntSigILMIGrpEntry.setStatus("current")


class _SigCntBbIfNum_Type(Integer32):
    """Custom type sigCntBbIfNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_SigCntBbIfNum_Type.__name__ = "Integer32"
_SigCntBbIfNum_Object = MibTableColumn
sigCntBbIfNum = _SigCntBbIfNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 6, 4, 2, 1, 1, 1),
    _SigCntBbIfNum_Type()
)
sigCntBbIfNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigCntBbIfNum.setStatus("current")
_BbIfSnmpPduReceived_Type = Counter32
_BbIfSnmpPduReceived_Object = MibTableColumn
bbIfSnmpPduReceived = _BbIfSnmpPduReceived_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 6, 4, 2, 1, 1, 2),
    _BbIfSnmpPduReceived_Type()
)
bbIfSnmpPduReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bbIfSnmpPduReceived.setStatus("current")
_BbIfGetRequestReceived_Type = Counter32
_BbIfGetRequestReceived_Object = MibTableColumn
bbIfGetRequestReceived = _BbIfGetRequestReceived_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 6, 4, 2, 1, 1, 3),
    _BbIfGetRequestReceived_Type()
)
bbIfGetRequestReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bbIfGetRequestReceived.setStatus("current")
_BbIfGetNextRequestReceived_Type = Counter32
_BbIfGetNextRequestReceived_Object = MibTableColumn
bbIfGetNextRequestReceived = _BbIfGetNextRequestReceived_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 6, 4, 2, 1, 1, 4),
    _BbIfGetNextRequestReceived_Type()
)
bbIfGetNextRequestReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bbIfGetNextRequestReceived.setStatus("current")
_BbIfSetRequestReceived_Type = Counter32
_BbIfSetRequestReceived_Object = MibTableColumn
bbIfSetRequestReceived = _BbIfSetRequestReceived_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 6, 4, 2, 1, 1, 5),
    _BbIfSetRequestReceived_Type()
)
bbIfSetRequestReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bbIfSetRequestReceived.setStatus("current")
_BbIfTrapReceived_Type = Counter32
_BbIfTrapReceived_Object = MibTableColumn
bbIfTrapReceived = _BbIfTrapReceived_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 6, 4, 2, 1, 1, 6),
    _BbIfTrapReceived_Type()
)
bbIfTrapReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bbIfTrapReceived.setStatus("current")
_BbIfGetResponseReceived_Type = Counter32
_BbIfGetResponseReceived_Object = MibTableColumn
bbIfGetResponseReceived = _BbIfGetResponseReceived_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 6, 4, 2, 1, 1, 7),
    _BbIfGetResponseReceived_Type()
)
bbIfGetResponseReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bbIfGetResponseReceived.setStatus("current")
_BbIfGetResponseTransmitted_Type = Counter32
_BbIfGetResponseTransmitted_Object = MibTableColumn
bbIfGetResponseTransmitted = _BbIfGetResponseTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 6, 4, 2, 1, 1, 8),
    _BbIfGetResponseTransmitted_Type()
)
bbIfGetResponseTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bbIfGetResponseTransmitted.setStatus("current")
_BbIfGetRequestTransmitted_Type = Counter32
_BbIfGetRequestTransmitted_Object = MibTableColumn
bbIfGetRequestTransmitted = _BbIfGetRequestTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 6, 4, 2, 1, 1, 9),
    _BbIfGetRequestTransmitted_Type()
)
bbIfGetRequestTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bbIfGetRequestTransmitted.setStatus("current")
_BbIfTrapTransmitted_Type = Counter32
_BbIfTrapTransmitted_Object = MibTableColumn
bbIfTrapTransmitted = _BbIfTrapTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 6, 4, 2, 1, 1, 10),
    _BbIfTrapTransmitted_Type()
)
bbIfTrapTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bbIfTrapTransmitted.setStatus("current")
_BbIfInvalidPDUReceived_Type = Counter32
_BbIfInvalidPDUReceived_Object = MibTableColumn
bbIfInvalidPDUReceived = _BbIfInvalidPDUReceived_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 6, 4, 2, 1, 1, 11),
    _BbIfInvalidPDUReceived_Type()
)
bbIfInvalidPDUReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bbIfInvalidPDUReceived.setStatus("current")
_BbIfAsn1ParseError_Type = Counter32
_BbIfAsn1ParseError_Object = MibTableColumn
bbIfAsn1ParseError = _BbIfAsn1ParseError_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 6, 4, 2, 1, 1, 12),
    _BbIfAsn1ParseError_Type()
)
bbIfAsn1ParseError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bbIfAsn1ParseError.setStatus("current")
_BbIfNoSuchNameError_Type = Counter32
_BbIfNoSuchNameError_Object = MibTableColumn
bbIfNoSuchNameError = _BbIfNoSuchNameError_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 6, 4, 2, 1, 1, 13),
    _BbIfNoSuchNameError_Type()
)
bbIfNoSuchNameError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bbIfNoSuchNameError.setStatus("current")
_BbIfTooBigError_Type = Counter32
_BbIfTooBigError_Object = MibTableColumn
bbIfTooBigError = _BbIfTooBigError_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 6, 4, 2, 1, 1, 14),
    _BbIfTooBigError_Type()
)
bbIfTooBigError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bbIfTooBigError.setStatus("current")


class _BbIfSigCntClrButton_Type(Integer32):
    """Custom type bbIfSigCntClrButton based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("resetCounters", 2))
    )


_BbIfSigCntClrButton_Type.__name__ = "Integer32"
_BbIfSigCntClrButton_Object = MibTableColumn
bbIfSigCntClrButton = _BbIfSigCntClrButton_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 6, 4, 2, 1, 1, 15),
    _BbIfSigCntClrButton_Type()
)
bbIfSigCntClrButton.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bbIfSigCntClrButton.setStatus("current")
_CwbIlmiMIBConformance_ObjectIdentity = ObjectIdentity
cwbIlmiMIBConformance = _CwbIlmiMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 33, 2)
)
_CwbIlmiMIBGroups_ObjectIdentity = ObjectIdentity
cwbIlmiMIBGroups = _CwbIlmiMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 33, 2, 1)
)
_CwbIlmiMIBCompliances_ObjectIdentity = ObjectIdentity
cwbIlmiMIBCompliances = _CwbIlmiMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 33, 2, 2)
)

# Managed Objects groups

cwbIlmiConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 33, 2, 1, 1)
)
cwbIlmiConfGroup.setObjects(
      *(("CISCO-WAN-BBIF-ILMI-MIB", "bbIfSigPortNum"),
        ("CISCO-WAN-BBIF-ILMI-MIB", "bbIfIlmiEnable"),
        ("CISCO-WAN-BBIF-ILMI-MIB", "bbIfSignallingProtocolType"),
        ("CISCO-WAN-BBIF-ILMI-MIB", "bbIfSignallingVpi"),
        ("CISCO-WAN-BBIF-ILMI-MIB", "bbIfSignallingVci"),
        ("CISCO-WAN-BBIF-ILMI-MIB", "bbIfAddrPrefix"),
        ("CISCO-WAN-BBIF-ILMI-MIB", "bbIfCustomerId"),
        ("CISCO-WAN-BBIF-ILMI-MIB", "bbIfProtocolRevNo"),
        ("CISCO-WAN-BBIF-ILMI-MIB", "bbIfIlmiTrapEnable"),
        ("CISCO-WAN-BBIF-ILMI-MIB", "bbIfMinTrapInterval"),
        ("CISCO-WAN-BBIF-ILMI-MIB", "bbIfKeepAlivePollingEnable"),
        ("CISCO-WAN-BBIF-ILMI-MIB", "bbIfErrorThresholdN491"),
        ("CISCO-WAN-BBIF-ILMI-MIB", "bbIfEventThresholdN492"),
        ("CISCO-WAN-BBIF-ILMI-MIB", "bbIfPollingIntervalT491"),
        ("CISCO-WAN-BBIF-ILMI-MIB", "bbIfMinEnquiryIntervalT493"),
        ("CISCO-WAN-BBIF-ILMI-MIB", "bbIfAddrRegEnable"))
)
if mibBuilder.loadTexts:
    cwbIlmiConfGroup.setStatus("current")

cwbIlmiStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 33, 2, 1, 2)
)
cwbIlmiStatsGroup.setObjects(
      *(("CISCO-WAN-BBIF-ILMI-MIB", "sigCntBbIfNum"),
        ("CISCO-WAN-BBIF-ILMI-MIB", "bbIfSnmpPduReceived"),
        ("CISCO-WAN-BBIF-ILMI-MIB", "bbIfGetRequestReceived"),
        ("CISCO-WAN-BBIF-ILMI-MIB", "bbIfGetNextRequestReceived"),
        ("CISCO-WAN-BBIF-ILMI-MIB", "bbIfSetRequestReceived"),
        ("CISCO-WAN-BBIF-ILMI-MIB", "bbIfTrapReceived"),
        ("CISCO-WAN-BBIF-ILMI-MIB", "bbIfGetResponseReceived"),
        ("CISCO-WAN-BBIF-ILMI-MIB", "bbIfGetResponseTransmitted"),
        ("CISCO-WAN-BBIF-ILMI-MIB", "bbIfGetRequestTransmitted"),
        ("CISCO-WAN-BBIF-ILMI-MIB", "bbIfTrapTransmitted"),
        ("CISCO-WAN-BBIF-ILMI-MIB", "bbIfInvalidPDUReceived"),
        ("CISCO-WAN-BBIF-ILMI-MIB", "bbIfAsn1ParseError"),
        ("CISCO-WAN-BBIF-ILMI-MIB", "bbIfNoSuchNameError"),
        ("CISCO-WAN-BBIF-ILMI-MIB", "bbIfTooBigError"),
        ("CISCO-WAN-BBIF-ILMI-MIB", "bbIfSigCntClrButton"))
)
if mibBuilder.loadTexts:
    cwbIlmiStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cwbIlmiCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 33, 2, 2, 1)
)
if mibBuilder.loadTexts:
    cwbIlmiCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-WAN-BBIF-ILMI-MIB",
    **{"bbIfCnfSigILMIGrp": bbIfCnfSigILMIGrp,
       "bbIfCnfSigILMIGrpTable": bbIfCnfSigILMIGrpTable,
       "bbIfCnfSigILMIGrpEntry": bbIfCnfSigILMIGrpEntry,
       "bbIfSigPortNum": bbIfSigPortNum,
       "bbIfIlmiEnable": bbIfIlmiEnable,
       "bbIfSignallingProtocolType": bbIfSignallingProtocolType,
       "bbIfSignallingVpi": bbIfSignallingVpi,
       "bbIfSignallingVci": bbIfSignallingVci,
       "bbIfAddrPrefix": bbIfAddrPrefix,
       "bbIfCustomerId": bbIfCustomerId,
       "bbIfProtocolRevNo": bbIfProtocolRevNo,
       "bbIfIlmiTrapEnable": bbIfIlmiTrapEnable,
       "bbIfMinTrapInterval": bbIfMinTrapInterval,
       "bbIfKeepAlivePollingEnable": bbIfKeepAlivePollingEnable,
       "bbIfErrorThresholdN491": bbIfErrorThresholdN491,
       "bbIfEventThresholdN492": bbIfEventThresholdN492,
       "bbIfPollingIntervalT491": bbIfPollingIntervalT491,
       "bbIfMinEnquiryIntervalT493": bbIfMinEnquiryIntervalT493,
       "bbIfAddrRegEnable": bbIfAddrRegEnable,
       "bbIfCntSigILMIGrp": bbIfCntSigILMIGrp,
       "bbIfCntSigILMIGrpTable": bbIfCntSigILMIGrpTable,
       "bbIfCntSigILMIGrpEntry": bbIfCntSigILMIGrpEntry,
       "sigCntBbIfNum": sigCntBbIfNum,
       "bbIfSnmpPduReceived": bbIfSnmpPduReceived,
       "bbIfGetRequestReceived": bbIfGetRequestReceived,
       "bbIfGetNextRequestReceived": bbIfGetNextRequestReceived,
       "bbIfSetRequestReceived": bbIfSetRequestReceived,
       "bbIfTrapReceived": bbIfTrapReceived,
       "bbIfGetResponseReceived": bbIfGetResponseReceived,
       "bbIfGetResponseTransmitted": bbIfGetResponseTransmitted,
       "bbIfGetRequestTransmitted": bbIfGetRequestTransmitted,
       "bbIfTrapTransmitted": bbIfTrapTransmitted,
       "bbIfInvalidPDUReceived": bbIfInvalidPDUReceived,
       "bbIfAsn1ParseError": bbIfAsn1ParseError,
       "bbIfNoSuchNameError": bbIfNoSuchNameError,
       "bbIfTooBigError": bbIfTooBigError,
       "bbIfSigCntClrButton": bbIfSigCntClrButton,
       "ciscoWanBbifIlmiMIB": ciscoWanBbifIlmiMIB,
       "cwbIlmiMIBConformance": cwbIlmiMIBConformance,
       "cwbIlmiMIBGroups": cwbIlmiMIBGroups,
       "cwbIlmiConfGroup": cwbIlmiConfGroup,
       "cwbIlmiStatsGroup": cwbIlmiStatsGroup,
       "cwbIlmiMIBCompliances": cwbIlmiMIBCompliances,
       "cwbIlmiCompliance": cwbIlmiCompliance}
)
