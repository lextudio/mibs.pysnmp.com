# SNMP MIB module (NOVELL-NLSP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NOVELL-NLSP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:29:02 2024
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

(mibDoc,) = mibBuilder.importSymbols(
    "NOVELL-IPX-MIB",
    "mibDoc")

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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class SystemID(OctetString):
    """Custom type SystemID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )





class NLSPID(OctetString):
    """Custom type NLSPID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 7),
    )





class NetNumber(OctetString):
    """Custom type NetNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Nlsp_ObjectIdentity = ObjectIdentity
nlsp = _Nlsp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 19)
)
_NlspSystem_ObjectIdentity = ObjectIdentity
nlspSystem = _NlspSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 1)
)
_NlspSysTable_Object = MibTable
nlspSysTable = _NlspSysTable_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 1, 1)
)
if mibBuilder.loadTexts:
    nlspSysTable.setStatus("mandatory")
_NlspSysEntry_Object = MibTableRow
nlspSysEntry = _NlspSysEntry_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 1, 1, 1)
)
nlspSysEntry.setIndexNames(
    (0, "NOVELL-NLSP-MIB", "nlspSysInstance"),
)
if mibBuilder.loadTexts:
    nlspSysEntry.setStatus("mandatory")
_NlspSysInstance_Type = Integer32
_NlspSysInstance_Object = MibTableColumn
nlspSysInstance = _NlspSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 1, 1, 1, 1),
    _NlspSysInstance_Type()
)
nlspSysInstance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlspSysInstance.setStatus("mandatory")


class _NlspSysState_Type(Integer32):
    """Custom type nlspSysState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nlspLevel1Router", 2),
          ("off", 1))
    )


_NlspSysState_Type.__name__ = "Integer32"
_NlspSysState_Object = MibTableColumn
nlspSysState = _NlspSysState_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 1, 1, 1, 2),
    _NlspSysState_Type()
)
nlspSysState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlspSysState.setStatus("mandatory")
_NlspSysID_Type = SystemID
_NlspSysID_Object = MibTableColumn
nlspSysID = _NlspSysID_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 1, 1, 1, 3),
    _NlspSysID_Type()
)
nlspSysID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlspSysID.setStatus("mandatory")


class _NlspSysMinNonBcastLSPTransInt_Type(Integer32):
    """Custom type nlspSysMinNonBcastLSPTransInt based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_NlspSysMinNonBcastLSPTransInt_Type.__name__ = "Integer32"
_NlspSysMinNonBcastLSPTransInt_Object = MibTableColumn
nlspSysMinNonBcastLSPTransInt = _NlspSysMinNonBcastLSPTransInt_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 1, 1, 1, 4),
    _NlspSysMinNonBcastLSPTransInt_Type()
)
nlspSysMinNonBcastLSPTransInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlspSysMinNonBcastLSPTransInt.setStatus("mandatory")


class _NlspSysMinBcastLSPTransInt_Type(Integer32):
    """Custom type nlspSysMinBcastLSPTransInt based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_NlspSysMinBcastLSPTransInt_Type.__name__ = "Integer32"
_NlspSysMinBcastLSPTransInt_Object = MibTableColumn
nlspSysMinBcastLSPTransInt = _NlspSysMinBcastLSPTransInt_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 1, 1, 1, 5),
    _NlspSysMinBcastLSPTransInt_Type()
)
nlspSysMinBcastLSPTransInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlspSysMinBcastLSPTransInt.setStatus("mandatory")


class _NlspSysMinLSPGenInt_Type(Integer32):
    """Custom type nlspSysMinLSPGenInt based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_NlspSysMinLSPGenInt_Type.__name__ = "Integer32"
_NlspSysMinLSPGenInt_Object = MibTableColumn
nlspSysMinLSPGenInt = _NlspSysMinLSPGenInt_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 1, 1, 1, 6),
    _NlspSysMinLSPGenInt_Type()
)
nlspSysMinLSPGenInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlspSysMinLSPGenInt.setStatus("mandatory")


class _NlspSysMaxLSPGenInt_Type(Integer32):
    """Custom type nlspSysMaxLSPGenInt based on Integer32"""
    defaultValue = 7200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50000),
    )


_NlspSysMaxLSPGenInt_Type.__name__ = "Integer32"
_NlspSysMaxLSPGenInt_Object = MibTableColumn
nlspSysMaxLSPGenInt = _NlspSysMaxLSPGenInt_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 1, 1, 1, 7),
    _NlspSysMaxLSPGenInt_Type()
)
nlspSysMaxLSPGenInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlspSysMaxLSPGenInt.setStatus("mandatory")


class _NlspSysMaxLSPAge_Type(Integer32):
    """Custom type nlspSysMaxLSPAge based on Integer32"""
    defaultValue = 7500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50000),
    )


_NlspSysMaxLSPAge_Type.__name__ = "Integer32"
_NlspSysMaxLSPAge_Object = MibTableColumn
nlspSysMaxLSPAge = _NlspSysMaxLSPAge_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 1, 1, 1, 8),
    _NlspSysMaxLSPAge_Type()
)
nlspSysMaxLSPAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlspSysMaxLSPAge.setStatus("mandatory")


class _NlspSysBcastHelloInt_Type(Integer32):
    """Custom type nlspSysBcastHelloInt based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_NlspSysBcastHelloInt_Type.__name__ = "Integer32"
_NlspSysBcastHelloInt_Object = MibTableColumn
nlspSysBcastHelloInt = _NlspSysBcastHelloInt_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 1, 1, 1, 9),
    _NlspSysBcastHelloInt_Type()
)
nlspSysBcastHelloInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlspSysBcastHelloInt.setStatus("mandatory")


class _NlspSysNonBcastHelloInt_Type(Integer32):
    """Custom type nlspSysNonBcastHelloInt based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_NlspSysNonBcastHelloInt_Type.__name__ = "Integer32"
_NlspSysNonBcastHelloInt_Object = MibTableColumn
nlspSysNonBcastHelloInt = _NlspSysNonBcastHelloInt_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 1, 1, 1, 10),
    _NlspSysNonBcastHelloInt_Type()
)
nlspSysNonBcastHelloInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlspSysNonBcastHelloInt.setStatus("mandatory")


class _NlspSysDRBcastHelloInt_Type(Integer32):
    """Custom type nlspSysDRBcastHelloInt based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_NlspSysDRBcastHelloInt_Type.__name__ = "Integer32"
_NlspSysDRBcastHelloInt_Object = MibTableColumn
nlspSysDRBcastHelloInt = _NlspSysDRBcastHelloInt_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 1, 1, 1, 11),
    _NlspSysDRBcastHelloInt_Type()
)
nlspSysDRBcastHelloInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlspSysDRBcastHelloInt.setStatus("mandatory")


class _NlspSysHoldTimeMultiplier_Type(Integer32):
    """Custom type nlspSysHoldTimeMultiplier based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 20),
    )


_NlspSysHoldTimeMultiplier_Type.__name__ = "Integer32"
_NlspSysHoldTimeMultiplier_Object = MibTableColumn
nlspSysHoldTimeMultiplier = _NlspSysHoldTimeMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 1, 1, 1, 12),
    _NlspSysHoldTimeMultiplier_Type()
)
nlspSysHoldTimeMultiplier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlspSysHoldTimeMultiplier.setStatus("mandatory")


class _NlspSysCompSNPInt_Type(Integer32):
    """Custom type nlspSysCompSNPInt based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_NlspSysCompSNPInt_Type.__name__ = "Integer32"
_NlspSysCompSNPInt_Object = MibTableColumn
nlspSysCompSNPInt = _NlspSysCompSNPInt_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 1, 1, 1, 13),
    _NlspSysCompSNPInt_Type()
)
nlspSysCompSNPInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlspSysCompSNPInt.setStatus("mandatory")


class _NlspSysPartSNPInt_Type(Integer32):
    """Custom type nlspSysPartSNPInt based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_NlspSysPartSNPInt_Type.__name__ = "Integer32"
_NlspSysPartSNPInt_Object = MibTableColumn
nlspSysPartSNPInt = _NlspSysPartSNPInt_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 1, 1, 1, 14),
    _NlspSysPartSNPInt_Type()
)
nlspSysPartSNPInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlspSysPartSNPInt.setStatus("mandatory")


class _NlspSysWaitTime_Type(Integer32):
    """Custom type nlspSysWaitTime based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_NlspSysWaitTime_Type.__name__ = "Integer32"
_NlspSysWaitTime_Object = MibTableColumn
nlspSysWaitTime = _NlspSysWaitTime_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 1, 1, 1, 15),
    _NlspSysWaitTime_Type()
)
nlspSysWaitTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlspSysWaitTime.setStatus("mandatory")


class _NlspSysOrigL1LSPBufSize_Type(Integer32):
    """Custom type nlspSysOrigL1LSPBufSize based on Integer32"""
    defaultValue = 512

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 4096),
    )


_NlspSysOrigL1LSPBufSize_Type.__name__ = "Integer32"
_NlspSysOrigL1LSPBufSize_Object = MibTableColumn
nlspSysOrigL1LSPBufSize = _NlspSysOrigL1LSPBufSize_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 1, 1, 1, 16),
    _NlspSysOrigL1LSPBufSize_Type()
)
nlspSysOrigL1LSPBufSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlspSysOrigL1LSPBufSize.setStatus("mandatory")
_NlspSysVersion_Type = Integer32
_NlspSysVersion_Object = MibTableColumn
nlspSysVersion = _NlspSysVersion_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 1, 1, 1, 17),
    _NlspSysVersion_Type()
)
nlspSysVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspSysVersion.setStatus("mandatory")
_NlspSysCorrLSPs_Type = Counter32
_NlspSysCorrLSPs_Object = MibTableColumn
nlspSysCorrLSPs = _NlspSysCorrLSPs_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 1, 1, 1, 18),
    _NlspSysCorrLSPs_Type()
)
nlspSysCorrLSPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspSysCorrLSPs.setStatus("mandatory")


class _NlspSysL1Overloaded_Type(Integer32):
    """Custom type nlspSysL1Overloaded based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NlspSysL1Overloaded_Type.__name__ = "Integer32"
_NlspSysL1Overloaded_Object = MibTableColumn
nlspSysL1Overloaded = _NlspSysL1Overloaded_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 1, 1, 1, 19),
    _NlspSysL1Overloaded_Type()
)
nlspSysL1Overloaded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspSysL1Overloaded.setStatus("mandatory")
_NlspSysL1DbaseOverloads_Type = Counter32
_NlspSysL1DbaseOverloads_Object = MibTableColumn
nlspSysL1DbaseOverloads = _NlspSysL1DbaseOverloads_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 1, 1, 1, 20),
    _NlspSysL1DbaseOverloads_Type()
)
nlspSysL1DbaseOverloads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspSysL1DbaseOverloads.setStatus("mandatory")
_NlspSysMaxSeqNums_Type = Counter32
_NlspSysMaxSeqNums_Object = MibTableColumn
nlspSysMaxSeqNums = _NlspSysMaxSeqNums_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 1, 1, 1, 21),
    _NlspSysMaxSeqNums_Type()
)
nlspSysMaxSeqNums.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspSysMaxSeqNums.setStatus("mandatory")
_NlspSysSeqNumSkips_Type = Counter32
_NlspSysSeqNumSkips_Object = MibTableColumn
nlspSysSeqNumSkips = _NlspSysSeqNumSkips_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 1, 1, 1, 22),
    _NlspSysSeqNumSkips_Type()
)
nlspSysSeqNumSkips.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspSysSeqNumSkips.setStatus("mandatory")
_NlspSysTransmittedLSPs_Type = Counter32
_NlspSysTransmittedLSPs_Object = MibTableColumn
nlspSysTransmittedLSPs = _NlspSysTransmittedLSPs_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 1, 1, 1, 23),
    _NlspSysTransmittedLSPs_Type()
)
nlspSysTransmittedLSPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspSysTransmittedLSPs.setStatus("mandatory")
_NlspSysReceivedLSPs_Type = Counter32
_NlspSysReceivedLSPs_Object = MibTableColumn
nlspSysReceivedLSPs = _NlspSysReceivedLSPs_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 1, 1, 1, 24),
    _NlspSysReceivedLSPs_Type()
)
nlspSysReceivedLSPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspSysReceivedLSPs.setStatus("mandatory")
_NlspSysOwnLSPPurges_Type = Counter32
_NlspSysOwnLSPPurges_Object = MibTableColumn
nlspSysOwnLSPPurges = _NlspSysOwnLSPPurges_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 1, 1, 1, 25),
    _NlspSysOwnLSPPurges_Type()
)
nlspSysOwnLSPPurges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspSysOwnLSPPurges.setStatus("mandatory")
_NlspSysVersionErrors_Type = Counter32
_NlspSysVersionErrors_Object = MibTableColumn
nlspSysVersionErrors = _NlspSysVersionErrors_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 1, 1, 1, 26),
    _NlspSysVersionErrors_Type()
)
nlspSysVersionErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspSysVersionErrors.setStatus("mandatory")
_NlspSysIncorrectPackets_Type = Counter32
_NlspSysIncorrectPackets_Object = MibTableColumn
nlspSysIncorrectPackets = _NlspSysIncorrectPackets_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 1, 1, 1, 27),
    _NlspSysIncorrectPackets_Type()
)
nlspSysIncorrectPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspSysIncorrectPackets.setStatus("mandatory")


class _NlspSysNearestL2DefaultExists_Type(Integer32):
    """Custom type nlspSysNearestL2DefaultExists based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NlspSysNearestL2DefaultExists_Type.__name__ = "Integer32"
_NlspSysNearestL2DefaultExists_Object = MibTableColumn
nlspSysNearestL2DefaultExists = _NlspSysNearestL2DefaultExists_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 1, 1, 1, 28),
    _NlspSysNearestL2DefaultExists_Type()
)
nlspSysNearestL2DefaultExists.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspSysNearestL2DefaultExists.setStatus("mandatory")
_NlspSysNearestL2DefaultRouter_Type = SystemID
_NlspSysNearestL2DefaultRouter_Object = MibTableColumn
nlspSysNearestL2DefaultRouter = _NlspSysNearestL2DefaultRouter_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 1, 1, 1, 29),
    _NlspSysNearestL2DefaultRouter_Type()
)
nlspSysNearestL2DefaultRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspSysNearestL2DefaultRouter.setStatus("mandatory")
_NlspSysResourceFailures_Type = Counter32
_NlspSysResourceFailures_Object = MibTableColumn
nlspSysResourceFailures = _NlspSysResourceFailures_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 1, 1, 1, 30),
    _NlspSysResourceFailures_Type()
)
nlspSysResourceFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspSysResourceFailures.setStatus("mandatory")
_NlspSysAreaTable_Object = MibTable
nlspSysAreaTable = _NlspSysAreaTable_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 1, 2)
)
if mibBuilder.loadTexts:
    nlspSysAreaTable.setStatus("mandatory")
_NlspSysAreaEntry_Object = MibTableRow
nlspSysAreaEntry = _NlspSysAreaEntry_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 1, 2, 1)
)
nlspSysAreaEntry.setIndexNames(
    (0, "NOVELL-NLSP-MIB", "nlspSysAreaSysInstance"),
    (0, "NOVELL-NLSP-MIB", "nlspSysAreaNet"),
    (0, "NOVELL-NLSP-MIB", "nlspSysAreaMask"),
)
if mibBuilder.loadTexts:
    nlspSysAreaEntry.setStatus("mandatory")
_NlspSysAreaSysInstance_Type = Integer32
_NlspSysAreaSysInstance_Object = MibTableColumn
nlspSysAreaSysInstance = _NlspSysAreaSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 1, 2, 1, 1),
    _NlspSysAreaSysInstance_Type()
)
nlspSysAreaSysInstance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlspSysAreaSysInstance.setStatus("mandatory")


class _NlspSysAreaNet_Type(OctetString):
    """Custom type nlspSysAreaNet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_NlspSysAreaNet_Type.__name__ = "OctetString"
_NlspSysAreaNet_Object = MibTableColumn
nlspSysAreaNet = _NlspSysAreaNet_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 1, 2, 1, 2),
    _NlspSysAreaNet_Type()
)
nlspSysAreaNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlspSysAreaNet.setStatus("mandatory")


class _NlspSysAreaMask_Type(OctetString):
    """Custom type nlspSysAreaMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_NlspSysAreaMask_Type.__name__ = "OctetString"
_NlspSysAreaMask_Object = MibTableColumn
nlspSysAreaMask = _NlspSysAreaMask_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 1, 2, 1, 3),
    _NlspSysAreaMask_Type()
)
nlspSysAreaMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlspSysAreaMask.setStatus("mandatory")
_NlspActAreaTable_Object = MibTable
nlspActAreaTable = _NlspActAreaTable_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 1, 3)
)
if mibBuilder.loadTexts:
    nlspActAreaTable.setStatus("mandatory")
_NlspActAreaEntry_Object = MibTableRow
nlspActAreaEntry = _NlspActAreaEntry_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 1, 3, 1)
)
nlspActAreaEntry.setIndexNames(
    (0, "NOVELL-NLSP-MIB", "nlspActAreaSysInstance"),
    (0, "NOVELL-NLSP-MIB", "nlspActAreaNet"),
    (0, "NOVELL-NLSP-MIB", "nlspActAreaMask"),
)
if mibBuilder.loadTexts:
    nlspActAreaEntry.setStatus("mandatory")
_NlspActAreaSysInstance_Type = Integer32
_NlspActAreaSysInstance_Object = MibTableColumn
nlspActAreaSysInstance = _NlspActAreaSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 1, 3, 1, 1),
    _NlspActAreaSysInstance_Type()
)
nlspActAreaSysInstance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlspActAreaSysInstance.setStatus("mandatory")


class _NlspActAreaNet_Type(OctetString):
    """Custom type nlspActAreaNet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_NlspActAreaNet_Type.__name__ = "OctetString"
_NlspActAreaNet_Object = MibTableColumn
nlspActAreaNet = _NlspActAreaNet_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 1, 3, 1, 2),
    _NlspActAreaNet_Type()
)
nlspActAreaNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlspActAreaNet.setStatus("mandatory")


class _NlspActAreaMask_Type(OctetString):
    """Custom type nlspActAreaMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_NlspActAreaMask_Type.__name__ = "OctetString"
_NlspActAreaMask_Object = MibTableColumn
nlspActAreaMask = _NlspActAreaMask_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 1, 3, 1, 3),
    _NlspActAreaMask_Type()
)
nlspActAreaMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlspActAreaMask.setStatus("mandatory")
_NlspCircuit_ObjectIdentity = ObjectIdentity
nlspCircuit = _NlspCircuit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 2)
)
_NlspCircTable_Object = MibTable
nlspCircTable = _NlspCircTable_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 2, 1)
)
if mibBuilder.loadTexts:
    nlspCircTable.setStatus("mandatory")
_NlspCircEntry_Object = MibTableRow
nlspCircEntry = _NlspCircEntry_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 2, 1, 1)
)
nlspCircEntry.setIndexNames(
    (0, "NOVELL-NLSP-MIB", "nlspCircSysInstance"),
    (0, "NOVELL-NLSP-MIB", "nlspCircIndex"),
)
if mibBuilder.loadTexts:
    nlspCircEntry.setStatus("mandatory")
_NlspCircSysInstance_Type = Integer32
_NlspCircSysInstance_Object = MibTableColumn
nlspCircSysInstance = _NlspCircSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 2, 1, 1, 1),
    _NlspCircSysInstance_Type()
)
nlspCircSysInstance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlspCircSysInstance.setStatus("mandatory")
_NlspCircIndex_Type = Integer32
_NlspCircIndex_Object = MibTableColumn
nlspCircIndex = _NlspCircIndex_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 2, 1, 1, 2),
    _NlspCircIndex_Type()
)
nlspCircIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlspCircIndex.setStatus("mandatory")


class _NlspCircState_Type(Integer32):
    """Custom type nlspCircState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_NlspCircState_Type.__name__ = "Integer32"
_NlspCircState_Object = MibTableColumn
nlspCircState = _NlspCircState_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 2, 1, 1, 3),
    _NlspCircState_Type()
)
nlspCircState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlspCircState.setStatus("mandatory")
_NlspCircPace_Type = Integer32
_NlspCircPace_Object = MibTableColumn
nlspCircPace = _NlspCircPace_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 2, 1, 1, 4),
    _NlspCircPace_Type()
)
nlspCircPace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlspCircPace.setStatus("mandatory")


class _NlspCircHelloTimer_Type(Integer32):
    """Custom type nlspCircHelloTimer based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_NlspCircHelloTimer_Type.__name__ = "Integer32"
_NlspCircHelloTimer_Object = MibTableColumn
nlspCircHelloTimer = _NlspCircHelloTimer_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 2, 1, 1, 5),
    _NlspCircHelloTimer_Type()
)
nlspCircHelloTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlspCircHelloTimer.setStatus("mandatory")


class _NlspCircL1DefaultCost_Type(Integer32):
    """Custom type nlspCircL1DefaultCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_NlspCircL1DefaultCost_Type.__name__ = "Integer32"
_NlspCircL1DefaultCost_Object = MibTableColumn
nlspCircL1DefaultCost = _NlspCircL1DefaultCost_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 2, 1, 1, 6),
    _NlspCircL1DefaultCost_Type()
)
nlspCircL1DefaultCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlspCircL1DefaultCost.setStatus("mandatory")


class _NlspCircL1DesRouterPriority_Type(Integer32):
    """Custom type nlspCircL1DesRouterPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_NlspCircL1DesRouterPriority_Type.__name__ = "Integer32"
_NlspCircL1DesRouterPriority_Object = MibTableColumn
nlspCircL1DesRouterPriority = _NlspCircL1DesRouterPriority_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 2, 1, 1, 7),
    _NlspCircL1DesRouterPriority_Type()
)
nlspCircL1DesRouterPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlspCircL1DesRouterPriority.setStatus("mandatory")


class _NlspCircL1CircID_Type(OctetString):
    """Custom type nlspCircL1CircID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 7),
    )


_NlspCircL1CircID_Type.__name__ = "OctetString"
_NlspCircL1CircID_Object = MibTableColumn
nlspCircL1CircID = _NlspCircL1CircID_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 2, 1, 1, 8),
    _NlspCircL1CircID_Type()
)
nlspCircL1CircID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspCircL1CircID.setStatus("mandatory")
_NlspCircL1DesRouter_Type = SystemID
_NlspCircL1DesRouter_Object = MibTableColumn
nlspCircL1DesRouter = _NlspCircL1DesRouter_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 2, 1, 1, 9),
    _NlspCircL1DesRouter_Type()
)
nlspCircL1DesRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspCircL1DesRouter.setStatus("mandatory")
_NlspCircLANL1DesRouterChanges_Type = Counter32
_NlspCircLANL1DesRouterChanges_Object = MibTableColumn
nlspCircLANL1DesRouterChanges = _NlspCircLANL1DesRouterChanges_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 2, 1, 1, 10),
    _NlspCircLANL1DesRouterChanges_Type()
)
nlspCircLANL1DesRouterChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspCircLANL1DesRouterChanges.setStatus("mandatory")
_NlspCircNeighChanges_Type = Counter32
_NlspCircNeighChanges_Object = MibTableColumn
nlspCircNeighChanges = _NlspCircNeighChanges_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 2, 1, 1, 11),
    _NlspCircNeighChanges_Type()
)
nlspCircNeighChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspCircNeighChanges.setStatus("mandatory")
_NlspCircRejNeighbors_Type = Counter32
_NlspCircRejNeighbors_Object = MibTableColumn
nlspCircRejNeighbors = _NlspCircRejNeighbors_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 2, 1, 1, 12),
    _NlspCircRejNeighbors_Type()
)
nlspCircRejNeighbors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspCircRejNeighbors.setStatus("mandatory")
_NlspCircOutPackets_Type = Counter32
_NlspCircOutPackets_Object = MibTableColumn
nlspCircOutPackets = _NlspCircOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 2, 1, 1, 13),
    _NlspCircOutPackets_Type()
)
nlspCircOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspCircOutPackets.setStatus("mandatory")
_NlspCircInPackets_Type = Counter32
_NlspCircInPackets_Object = MibTableColumn
nlspCircInPackets = _NlspCircInPackets_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 2, 1, 1, 14),
    _NlspCircInPackets_Type()
)
nlspCircInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspCircInPackets.setStatus("mandatory")
_NlspCircActualMaxPacketSize_Type = Integer32
_NlspCircActualMaxPacketSize_Object = MibTableColumn
nlspCircActualMaxPacketSize = _NlspCircActualMaxPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 2, 1, 1, 15),
    _NlspCircActualMaxPacketSize_Type()
)
nlspCircActualMaxPacketSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspCircActualMaxPacketSize.setStatus("mandatory")
_NlspCircPSNPsSent_Type = Counter32
_NlspCircPSNPsSent_Object = MibTableColumn
nlspCircPSNPsSent = _NlspCircPSNPsSent_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 2, 1, 1, 16),
    _NlspCircPSNPsSent_Type()
)
nlspCircPSNPsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspCircPSNPsSent.setStatus("mandatory")
_NlspCircPSNPsReceived_Type = Counter32
_NlspCircPSNPsReceived_Object = MibTableColumn
nlspCircPSNPsReceived = _NlspCircPSNPsReceived_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 2, 1, 1, 17),
    _NlspCircPSNPsReceived_Type()
)
nlspCircPSNPsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspCircPSNPsReceived.setStatus("mandatory")
_NlspForwarding_ObjectIdentity = ObjectIdentity
nlspForwarding = _NlspForwarding_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 3)
)
_NlspDestTable_Object = MibTable
nlspDestTable = _NlspDestTable_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 3, 1)
)
if mibBuilder.loadTexts:
    nlspDestTable.setStatus("mandatory")
_NlspDestEntry_Object = MibTableRow
nlspDestEntry = _NlspDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 3, 1, 1)
)
nlspDestEntry.setIndexNames(
    (0, "NOVELL-NLSP-MIB", "nlspDestSysInstance"),
    (0, "NOVELL-NLSP-MIB", "nlspDestNetNum"),
)
if mibBuilder.loadTexts:
    nlspDestEntry.setStatus("mandatory")
_NlspDestSysInstance_Type = Integer32
_NlspDestSysInstance_Object = MibTableColumn
nlspDestSysInstance = _NlspDestSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 3, 1, 1, 1),
    _NlspDestSysInstance_Type()
)
nlspDestSysInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspDestSysInstance.setStatus("mandatory")
_NlspDestNetNum_Type = NetNumber
_NlspDestNetNum_Object = MibTableColumn
nlspDestNetNum = _NlspDestNetNum_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 3, 1, 1, 2),
    _NlspDestNetNum_Type()
)
nlspDestNetNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspDestNetNum.setStatus("mandatory")
_NlspDestID_Type = NLSPID
_NlspDestID_Object = MibTableColumn
nlspDestID = _NlspDestID_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 3, 1, 1, 3),
    _NlspDestID_Type()
)
nlspDestID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspDestID.setStatus("mandatory")
_NlspDestEstDelay_Type = Integer32
_NlspDestEstDelay_Object = MibTableColumn
nlspDestEstDelay = _NlspDestEstDelay_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 3, 1, 1, 4),
    _NlspDestEstDelay_Type()
)
nlspDestEstDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspDestEstDelay.setStatus("mandatory")
_NlspDestEstThroughput_Type = Integer32
_NlspDestEstThroughput_Object = MibTableColumn
nlspDestEstThroughput = _NlspDestEstThroughput_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 3, 1, 1, 5),
    _NlspDestEstThroughput_Type()
)
nlspDestEstThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspDestEstThroughput.setStatus("mandatory")
_NlspDestNextHopID_Type = NLSPID
_NlspDestNextHopID_Object = MibTableColumn
nlspDestNextHopID = _NlspDestNextHopID_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 3, 1, 1, 6),
    _NlspDestNextHopID_Type()
)
nlspDestNextHopID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspDestNextHopID.setStatus("mandatory")
_NlspDestCost_Type = Integer32
_NlspDestCost_Object = MibTableColumn
nlspDestCost = _NlspDestCost_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 3, 1, 1, 7),
    _NlspDestCost_Type()
)
nlspDestCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspDestCost.setStatus("mandatory")
_NlspNeighbors_ObjectIdentity = ObjectIdentity
nlspNeighbors = _NlspNeighbors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 4)
)
_NlspNeighTable_Object = MibTable
nlspNeighTable = _NlspNeighTable_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 4, 1)
)
if mibBuilder.loadTexts:
    nlspNeighTable.setStatus("mandatory")
_NlspNeighEntry_Object = MibTableRow
nlspNeighEntry = _NlspNeighEntry_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 4, 1, 1)
)
nlspNeighEntry.setIndexNames(
    (0, "NOVELL-NLSP-MIB", "nlspNeighSysInstance"),
    (0, "NOVELL-NLSP-MIB", "nlspNeighCircIndex"),
    (0, "NOVELL-NLSP-MIB", "nlspNeighIndex"),
)
if mibBuilder.loadTexts:
    nlspNeighEntry.setStatus("mandatory")
_NlspNeighSysInstance_Type = Integer32
_NlspNeighSysInstance_Object = MibTableColumn
nlspNeighSysInstance = _NlspNeighSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 4, 1, 1, 1),
    _NlspNeighSysInstance_Type()
)
nlspNeighSysInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspNeighSysInstance.setStatus("mandatory")
_NlspNeighCircIndex_Type = Integer32
_NlspNeighCircIndex_Object = MibTableColumn
nlspNeighCircIndex = _NlspNeighCircIndex_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 4, 1, 1, 2),
    _NlspNeighCircIndex_Type()
)
nlspNeighCircIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspNeighCircIndex.setStatus("mandatory")
_NlspNeighIndex_Type = Integer32
_NlspNeighIndex_Object = MibTableColumn
nlspNeighIndex = _NlspNeighIndex_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 4, 1, 1, 3),
    _NlspNeighIndex_Type()
)
nlspNeighIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspNeighIndex.setStatus("mandatory")


class _NlspNeighState_Type(Integer32):
    """Custom type nlspNeighState based on Integer32"""
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
        *(("down", 4),
          ("failed", 3),
          ("initializing", 1),
          ("up", 2))
    )


_NlspNeighState_Type.__name__ = "Integer32"
_NlspNeighState_Object = MibTableColumn
nlspNeighState = _NlspNeighState_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 4, 1, 1, 4),
    _NlspNeighState_Type()
)
nlspNeighState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspNeighState.setStatus("mandatory")
_NlspNeighNICAddress_Type = PhysAddress
_NlspNeighNICAddress_Object = MibTableColumn
nlspNeighNICAddress = _NlspNeighNICAddress_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 4, 1, 1, 5),
    _NlspNeighNICAddress_Type()
)
nlspNeighNICAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspNeighNICAddress.setStatus("mandatory")


class _NlspNeighSysType_Type(Integer32):
    """Custom type nlspNeighSysType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nlspLevel1Router", 2),
          ("unknown", 1))
    )


_NlspNeighSysType_Type.__name__ = "Integer32"
_NlspNeighSysType_Object = MibTableColumn
nlspNeighSysType = _NlspNeighSysType_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 4, 1, 1, 6),
    _NlspNeighSysType_Type()
)
nlspNeighSysType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspNeighSysType.setStatus("mandatory")
_NlspNeighSysID_Type = SystemID
_NlspNeighSysID_Object = MibTableColumn
nlspNeighSysID = _NlspNeighSysID_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 4, 1, 1, 7),
    _NlspNeighSysID_Type()
)
nlspNeighSysID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspNeighSysID.setStatus("mandatory")


class _NlspNeighName_Type(OctetString):
    """Custom type nlspNeighName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_NlspNeighName_Type.__name__ = "OctetString"
_NlspNeighName_Object = MibTableColumn
nlspNeighName = _NlspNeighName_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 4, 1, 1, 8),
    _NlspNeighName_Type()
)
nlspNeighName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspNeighName.setStatus("mandatory")


class _NlspNeighUsage_Type(Integer32):
    """Custom type nlspNeighUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("level1", 2),
          ("undefined", 1))
    )


_NlspNeighUsage_Type.__name__ = "Integer32"
_NlspNeighUsage_Object = MibTableColumn
nlspNeighUsage = _NlspNeighUsage_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 4, 1, 1, 9),
    _NlspNeighUsage_Type()
)
nlspNeighUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspNeighUsage.setStatus("mandatory")


class _NlspNeighHoldTimer_Type(Integer32):
    """Custom type nlspNeighHoldTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NlspNeighHoldTimer_Type.__name__ = "Integer32"
_NlspNeighHoldTimer_Object = MibTableColumn
nlspNeighHoldTimer = _NlspNeighHoldTimer_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 4, 1, 1, 10),
    _NlspNeighHoldTimer_Type()
)
nlspNeighHoldTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspNeighHoldTimer.setStatus("mandatory")
_NlspNeighRemainingTime_Type = Integer32
_NlspNeighRemainingTime_Object = MibTableColumn
nlspNeighRemainingTime = _NlspNeighRemainingTime_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 4, 1, 1, 11),
    _NlspNeighRemainingTime_Type()
)
nlspNeighRemainingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspNeighRemainingTime.setStatus("mandatory")


class _NlspNeighPriority_Type(Integer32):
    """Custom type nlspNeighPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_NlspNeighPriority_Type.__name__ = "Integer32"
_NlspNeighPriority_Object = MibTableColumn
nlspNeighPriority = _NlspNeighPriority_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 4, 1, 1, 12),
    _NlspNeighPriority_Type()
)
nlspNeighPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspNeighPriority.setStatus("mandatory")
_NlspTranslation_ObjectIdentity = ObjectIdentity
nlspTranslation = _NlspTranslation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 5)
)
_NlspIDMapTable_Object = MibTable
nlspIDMapTable = _NlspIDMapTable_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 5, 1)
)
if mibBuilder.loadTexts:
    nlspIDMapTable.setStatus("mandatory")
_NlspIDMapEntry_Object = MibTableRow
nlspIDMapEntry = _NlspIDMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 5, 1, 1)
)
nlspIDMapEntry.setIndexNames(
    (0, "NOVELL-NLSP-MIB", "nlspIDMapSysInstance"),
    (0, "NOVELL-NLSP-MIB", "nlspIDMapID"),
)
if mibBuilder.loadTexts:
    nlspIDMapEntry.setStatus("mandatory")
_NlspIDMapSysInstance_Type = Integer32
_NlspIDMapSysInstance_Object = MibTableColumn
nlspIDMapSysInstance = _NlspIDMapSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 5, 1, 1, 1),
    _NlspIDMapSysInstance_Type()
)
nlspIDMapSysInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspIDMapSysInstance.setStatus("mandatory")
_NlspIDMapID_Type = NLSPID
_NlspIDMapID_Object = MibTableColumn
nlspIDMapID = _NlspIDMapID_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 5, 1, 1, 2),
    _NlspIDMapID_Type()
)
nlspIDMapID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspIDMapID.setStatus("mandatory")


class _NlspIDMapServerName_Type(OctetString):
    """Custom type nlspIDMapServerName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_NlspIDMapServerName_Type.__name__ = "OctetString"
_NlspIDMapServerName_Object = MibTableColumn
nlspIDMapServerName = _NlspIDMapServerName_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 5, 1, 1, 3),
    _NlspIDMapServerName_Type()
)
nlspIDMapServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspIDMapServerName.setStatus("mandatory")
_NlspIDMapNetNum_Type = NetNumber
_NlspIDMapNetNum_Object = MibTableColumn
nlspIDMapNetNum = _NlspIDMapNetNum_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 5, 1, 1, 4),
    _NlspIDMapNetNum_Type()
)
nlspIDMapNetNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspIDMapNetNum.setStatus("mandatory")
_NlspNetMapTable_Object = MibTable
nlspNetMapTable = _NlspNetMapTable_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 5, 2)
)
if mibBuilder.loadTexts:
    nlspNetMapTable.setStatus("mandatory")
_NlspNetMapEntry_Object = MibTableRow
nlspNetMapEntry = _NlspNetMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 5, 2, 1)
)
nlspNetMapEntry.setIndexNames(
    (0, "NOVELL-NLSP-MIB", "nlspNetMapSysInstance"),
    (0, "NOVELL-NLSP-MIB", "nlspNetMapNetNum"),
)
if mibBuilder.loadTexts:
    nlspNetMapEntry.setStatus("mandatory")
_NlspNetMapSysInstance_Type = Integer32
_NlspNetMapSysInstance_Object = MibTableColumn
nlspNetMapSysInstance = _NlspNetMapSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 5, 2, 1, 1),
    _NlspNetMapSysInstance_Type()
)
nlspNetMapSysInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspNetMapSysInstance.setStatus("mandatory")
_NlspNetMapNetNum_Type = NetNumber
_NlspNetMapNetNum_Object = MibTableColumn
nlspNetMapNetNum = _NlspNetMapNetNum_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 5, 2, 1, 2),
    _NlspNetMapNetNum_Type()
)
nlspNetMapNetNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspNetMapNetNum.setStatus("mandatory")


class _NlspNetMapServerName_Type(OctetString):
    """Custom type nlspNetMapServerName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_NlspNetMapServerName_Type.__name__ = "OctetString"
_NlspNetMapServerName_Object = MibTableColumn
nlspNetMapServerName = _NlspNetMapServerName_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 5, 2, 1, 3),
    _NlspNetMapServerName_Type()
)
nlspNetMapServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspNetMapServerName.setStatus("mandatory")
_NlspNetMapID_Type = NLSPID
_NlspNetMapID_Object = MibTableColumn
nlspNetMapID = _NlspNetMapID_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 5, 2, 1, 4),
    _NlspNetMapID_Type()
)
nlspNetMapID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspNetMapID.setStatus("mandatory")
_NlspNameMapTable_Object = MibTable
nlspNameMapTable = _NlspNameMapTable_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 5, 3)
)
if mibBuilder.loadTexts:
    nlspNameMapTable.setStatus("mandatory")
_NlspNameMapEntry_Object = MibTableRow
nlspNameMapEntry = _NlspNameMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 5, 3, 1)
)
nlspNameMapEntry.setIndexNames(
    (0, "NOVELL-NLSP-MIB", "nlspNameMapSysInstance"),
    (0, "NOVELL-NLSP-MIB", "nlspNameMapServerName"),
)
if mibBuilder.loadTexts:
    nlspNameMapEntry.setStatus("mandatory")
_NlspNameMapSysInstance_Type = Integer32
_NlspNameMapSysInstance_Object = MibTableColumn
nlspNameMapSysInstance = _NlspNameMapSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 5, 3, 1, 1),
    _NlspNameMapSysInstance_Type()
)
nlspNameMapSysInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspNameMapSysInstance.setStatus("mandatory")


class _NlspNameMapServerName_Type(OctetString):
    """Custom type nlspNameMapServerName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_NlspNameMapServerName_Type.__name__ = "OctetString"
_NlspNameMapServerName_Object = MibTableColumn
nlspNameMapServerName = _NlspNameMapServerName_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 5, 3, 1, 2),
    _NlspNameMapServerName_Type()
)
nlspNameMapServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspNameMapServerName.setStatus("mandatory")
_NlspNameMapNetNum_Type = NetNumber
_NlspNameMapNetNum_Object = MibTableColumn
nlspNameMapNetNum = _NlspNameMapNetNum_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 5, 3, 1, 3),
    _NlspNameMapNetNum_Type()
)
nlspNameMapNetNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspNameMapNetNum.setStatus("mandatory")
_NlspNameMapID_Type = NLSPID
_NlspNameMapID_Object = MibTableColumn
nlspNameMapID = _NlspNameMapID_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 5, 3, 1, 4),
    _NlspNameMapID_Type()
)
nlspNameMapID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspNameMapID.setStatus("mandatory")
_NlspGraph_ObjectIdentity = ObjectIdentity
nlspGraph = _NlspGraph_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 6)
)
_NlspNodeTable_Object = MibTable
nlspNodeTable = _NlspNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 6, 1)
)
if mibBuilder.loadTexts:
    nlspNodeTable.setStatus("mandatory")
_NlspNodeEntry_Object = MibTableRow
nlspNodeEntry = _NlspNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 6, 1, 1)
)
nlspNodeEntry.setIndexNames(
    (0, "NOVELL-NLSP-MIB", "nlspNodeSysInstance"),
    (0, "NOVELL-NLSP-MIB", "nlspNodeID"),
)
if mibBuilder.loadTexts:
    nlspNodeEntry.setStatus("mandatory")
_NlspNodeSysInstance_Type = Integer32
_NlspNodeSysInstance_Object = MibTableColumn
nlspNodeSysInstance = _NlspNodeSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 6, 1, 1, 1),
    _NlspNodeSysInstance_Type()
)
nlspNodeSysInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspNodeSysInstance.setStatus("mandatory")
_NlspNodeID_Type = NLSPID
_NlspNodeID_Object = MibTableColumn
nlspNodeID = _NlspNodeID_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 6, 1, 1, 2),
    _NlspNodeID_Type()
)
nlspNodeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspNodeID.setStatus("mandatory")
_NlspNodeNetNum_Type = NetNumber
_NlspNodeNetNum_Object = MibTableColumn
nlspNodeNetNum = _NlspNodeNetNum_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 6, 1, 1, 3),
    _NlspNodeNetNum_Type()
)
nlspNodeNetNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspNodeNetNum.setStatus("mandatory")


class _NlspNodeType_Type(Integer32):
    """Custom type nlspNodeType based on Integer32"""
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
        *(("network", 5),
          ("nlspLevel1Router", 2),
          ("nlspLevel2Router", 3),
          ("router", 4),
          ("unknown", 1))
    )


_NlspNodeType_Type.__name__ = "Integer32"
_NlspNodeType_Object = MibTableColumn
nlspNodeType = _NlspNodeType_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 6, 1, 1, 4),
    _NlspNodeType_Type()
)
nlspNodeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspNodeType.setStatus("mandatory")
_NlspNodeEstDelay_Type = Integer32
_NlspNodeEstDelay_Object = MibTableColumn
nlspNodeEstDelay = _NlspNodeEstDelay_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 6, 1, 1, 5),
    _NlspNodeEstDelay_Type()
)
nlspNodeEstDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspNodeEstDelay.setStatus("mandatory")
_NlspNodeEstThroughput_Type = Integer32
_NlspNodeEstThroughput_Object = MibTableColumn
nlspNodeEstThroughput = _NlspNodeEstThroughput_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 6, 1, 1, 6),
    _NlspNodeEstThroughput_Type()
)
nlspNodeEstThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspNodeEstThroughput.setStatus("mandatory")
_NlspNodeMaxPacketSize_Type = Integer32
_NlspNodeMaxPacketSize_Object = MibTableColumn
nlspNodeMaxPacketSize = _NlspNodeMaxPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 6, 1, 1, 7),
    _NlspNodeMaxPacketSize_Type()
)
nlspNodeMaxPacketSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspNodeMaxPacketSize.setStatus("mandatory")
_NlspNodeCost_Type = Integer32
_NlspNodeCost_Object = MibTableColumn
nlspNodeCost = _NlspNodeCost_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 6, 1, 1, 8),
    _NlspNodeCost_Type()
)
nlspNodeCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspNodeCost.setStatus("mandatory")


class _NlspNodeOverload_Type(Integer32):
    """Custom type nlspNodeOverload based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NlspNodeOverload_Type.__name__ = "Integer32"
_NlspNodeOverload_Object = MibTableColumn
nlspNodeOverload = _NlspNodeOverload_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 6, 1, 1, 9),
    _NlspNodeOverload_Type()
)
nlspNodeOverload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspNodeOverload.setStatus("mandatory")


class _NlspNodeReachable_Type(Integer32):
    """Custom type nlspNodeReachable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NlspNodeReachable_Type.__name__ = "Integer32"
_NlspNodeReachable_Object = MibTableColumn
nlspNodeReachable = _NlspNodeReachable_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 6, 1, 1, 10),
    _NlspNodeReachable_Type()
)
nlspNodeReachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspNodeReachable.setStatus("mandatory")
_NlspLinkTable_Object = MibTable
nlspLinkTable = _NlspLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 6, 2)
)
if mibBuilder.loadTexts:
    nlspLinkTable.setStatus("mandatory")
_NlspLinkEntry_Object = MibTableRow
nlspLinkEntry = _NlspLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 6, 2, 1)
)
nlspLinkEntry.setIndexNames(
    (0, "NOVELL-NLSP-MIB", "nlspLinkSysInstance"),
    (0, "NOVELL-NLSP-MIB", "nlspLinkNLSPID"),
    (0, "NOVELL-NLSP-MIB", "nlspLinkIndex"),
)
if mibBuilder.loadTexts:
    nlspLinkEntry.setStatus("mandatory")
_NlspLinkSysInstance_Type = Integer32
_NlspLinkSysInstance_Object = MibTableColumn
nlspLinkSysInstance = _NlspLinkSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 6, 2, 1, 1),
    _NlspLinkSysInstance_Type()
)
nlspLinkSysInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspLinkSysInstance.setStatus("mandatory")
_NlspLinkNLSPID_Type = NLSPID
_NlspLinkNLSPID_Object = MibTableColumn
nlspLinkNLSPID = _NlspLinkNLSPID_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 6, 2, 1, 2),
    _NlspLinkNLSPID_Type()
)
nlspLinkNLSPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspLinkNLSPID.setStatus("mandatory")
_NlspLinkIndex_Type = Integer32
_NlspLinkIndex_Object = MibTableColumn
nlspLinkIndex = _NlspLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 6, 2, 1, 3),
    _NlspLinkIndex_Type()
)
nlspLinkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspLinkIndex.setStatus("mandatory")
_NlspLinkNeighNLSPID_Type = NLSPID
_NlspLinkNeighNLSPID_Object = MibTableColumn
nlspLinkNeighNLSPID = _NlspLinkNeighNLSPID_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 6, 2, 1, 4),
    _NlspLinkNeighNLSPID_Type()
)
nlspLinkNeighNLSPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspLinkNeighNLSPID.setStatus("mandatory")
_NlspLinkFromNeighCost_Type = Integer32
_NlspLinkFromNeighCost_Object = MibTableColumn
nlspLinkFromNeighCost = _NlspLinkFromNeighCost_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 6, 2, 1, 5),
    _NlspLinkFromNeighCost_Type()
)
nlspLinkFromNeighCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspLinkFromNeighCost.setStatus("mandatory")
_NlspLinkMaxPacketSize_Type = Integer32
_NlspLinkMaxPacketSize_Object = MibTableColumn
nlspLinkMaxPacketSize = _NlspLinkMaxPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 6, 2, 1, 6),
    _NlspLinkMaxPacketSize_Type()
)
nlspLinkMaxPacketSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspLinkMaxPacketSize.setStatus("mandatory")
_NlspLinkThroughput_Type = Integer32
_NlspLinkThroughput_Object = MibTableColumn
nlspLinkThroughput = _NlspLinkThroughput_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 6, 2, 1, 7),
    _NlspLinkThroughput_Type()
)
nlspLinkThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspLinkThroughput.setStatus("mandatory")
_NlspLinkDelay_Type = Integer32
_NlspLinkDelay_Object = MibTableColumn
nlspLinkDelay = _NlspLinkDelay_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 6, 2, 1, 8),
    _NlspLinkDelay_Type()
)
nlspLinkDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspLinkDelay.setStatus("mandatory")


class _NlspLinkMediaType_Type(OctetString):
    """Custom type nlspLinkMediaType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_NlspLinkMediaType_Type.__name__ = "OctetString"
_NlspLinkMediaType_Object = MibTableColumn
nlspLinkMediaType = _NlspLinkMediaType_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 6, 2, 1, 9),
    _NlspLinkMediaType_Type()
)
nlspLinkMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspLinkMediaType.setStatus("mandatory")
_NlspLinkToNeighCost_Type = Integer32
_NlspLinkToNeighCost_Object = MibTableColumn
nlspLinkToNeighCost = _NlspLinkToNeighCost_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 6, 2, 1, 10),
    _NlspLinkToNeighCost_Type()
)
nlspLinkToNeighCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspLinkToNeighCost.setStatus("mandatory")
_NlspPathTable_Object = MibTable
nlspPathTable = _NlspPathTable_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 6, 3)
)
if mibBuilder.loadTexts:
    nlspPathTable.setStatus("mandatory")
_NlspPathEntry_Object = MibTableRow
nlspPathEntry = _NlspPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 6, 3, 1)
)
nlspPathEntry.setIndexNames(
    (0, "NOVELL-NLSP-MIB", "nlspPathSysInstance"),
    (0, "NOVELL-NLSP-MIB", "nlspPathDestNLSPID"),
    (0, "NOVELL-NLSP-MIB", "nlspPathLinkIndex"),
)
if mibBuilder.loadTexts:
    nlspPathEntry.setStatus("mandatory")
_NlspPathSysInstance_Type = Integer32
_NlspPathSysInstance_Object = MibTableColumn
nlspPathSysInstance = _NlspPathSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 6, 3, 1, 1),
    _NlspPathSysInstance_Type()
)
nlspPathSysInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspPathSysInstance.setStatus("mandatory")
_NlspPathDestNLSPID_Type = NLSPID
_NlspPathDestNLSPID_Object = MibTableColumn
nlspPathDestNLSPID = _NlspPathDestNLSPID_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 6, 3, 1, 2),
    _NlspPathDestNLSPID_Type()
)
nlspPathDestNLSPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspPathDestNLSPID.setStatus("mandatory")
_NlspPathLinkIndex_Type = Integer32
_NlspPathLinkIndex_Object = MibTableColumn
nlspPathLinkIndex = _NlspPathLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 6, 3, 1, 3),
    _NlspPathLinkIndex_Type()
)
nlspPathLinkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspPathLinkIndex.setStatus("mandatory")
_NlspGraphXRouteTable_Object = MibTable
nlspGraphXRouteTable = _NlspGraphXRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 6, 4)
)
if mibBuilder.loadTexts:
    nlspGraphXRouteTable.setStatus("mandatory")
_NlspGraphXRouteEntry_Object = MibTableRow
nlspGraphXRouteEntry = _NlspGraphXRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 6, 4, 1)
)
nlspGraphXRouteEntry.setIndexNames(
    (0, "NOVELL-NLSP-MIB", "nlspGraphXRouteSysInstance"),
    (0, "NOVELL-NLSP-MIB", "nlspGraphXRouteNLSPID"),
    (0, "NOVELL-NLSP-MIB", "nlspGraphXRouteNetNum"),
)
if mibBuilder.loadTexts:
    nlspGraphXRouteEntry.setStatus("mandatory")
_NlspGraphXRouteSysInstance_Type = Integer32
_NlspGraphXRouteSysInstance_Object = MibTableColumn
nlspGraphXRouteSysInstance = _NlspGraphXRouteSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 6, 4, 1, 1),
    _NlspGraphXRouteSysInstance_Type()
)
nlspGraphXRouteSysInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspGraphXRouteSysInstance.setStatus("mandatory")
_NlspGraphXRouteNLSPID_Type = NLSPID
_NlspGraphXRouteNLSPID_Object = MibTableColumn
nlspGraphXRouteNLSPID = _NlspGraphXRouteNLSPID_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 6, 4, 1, 2),
    _NlspGraphXRouteNLSPID_Type()
)
nlspGraphXRouteNLSPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspGraphXRouteNLSPID.setStatus("mandatory")
_NlspGraphXRouteNetNum_Type = NetNumber
_NlspGraphXRouteNetNum_Object = MibTableColumn
nlspGraphXRouteNetNum = _NlspGraphXRouteNetNum_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 6, 4, 1, 3),
    _NlspGraphXRouteNetNum_Type()
)
nlspGraphXRouteNetNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspGraphXRouteNetNum.setStatus("mandatory")
_NlspGraphXRouteCost_Type = Integer32
_NlspGraphXRouteCost_Object = MibTableColumn
nlspGraphXRouteCost = _NlspGraphXRouteCost_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 6, 4, 1, 4),
    _NlspGraphXRouteCost_Type()
)
nlspGraphXRouteCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspGraphXRouteCost.setStatus("mandatory")
_NlspGraphXRouteHopCount_Type = Integer32
_NlspGraphXRouteHopCount_Object = MibTableColumn
nlspGraphXRouteHopCount = _NlspGraphXRouteHopCount_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 6, 4, 1, 5),
    _NlspGraphXRouteHopCount_Type()
)
nlspGraphXRouteHopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspGraphXRouteHopCount.setStatus("mandatory")
_NlspGraphServTable_Object = MibTable
nlspGraphServTable = _NlspGraphServTable_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 6, 5)
)
if mibBuilder.loadTexts:
    nlspGraphServTable.setStatus("mandatory")
_NlspGraphServEntry_Object = MibTableRow
nlspGraphServEntry = _NlspGraphServEntry_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 6, 5, 1)
)
nlspGraphServEntry.setIndexNames(
    (0, "NOVELL-NLSP-MIB", "nlspGraphServSysInstance"),
    (0, "NOVELL-NLSP-MIB", "nlspGraphServNLSPID"),
    (0, "NOVELL-NLSP-MIB", "nlspGraphServName"),
    (0, "NOVELL-NLSP-MIB", "nlspGraphServTypeValue"),
)
if mibBuilder.loadTexts:
    nlspGraphServEntry.setStatus("mandatory")
_NlspGraphServSysInstance_Type = Integer32
_NlspGraphServSysInstance_Object = MibTableColumn
nlspGraphServSysInstance = _NlspGraphServSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 6, 5, 1, 1),
    _NlspGraphServSysInstance_Type()
)
nlspGraphServSysInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspGraphServSysInstance.setStatus("mandatory")
_NlspGraphServNLSPID_Type = NLSPID
_NlspGraphServNLSPID_Object = MibTableColumn
nlspGraphServNLSPID = _NlspGraphServNLSPID_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 6, 5, 1, 2),
    _NlspGraphServNLSPID_Type()
)
nlspGraphServNLSPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspGraphServNLSPID.setStatus("mandatory")


class _NlspGraphServName_Type(OctetString):
    """Custom type nlspGraphServName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_NlspGraphServName_Type.__name__ = "OctetString"
_NlspGraphServName_Object = MibTableColumn
nlspGraphServName = _NlspGraphServName_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 6, 5, 1, 3),
    _NlspGraphServName_Type()
)
nlspGraphServName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspGraphServName.setStatus("mandatory")


class _NlspGraphServTypeValue_Type(OctetString):
    """Custom type nlspGraphServTypeValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_NlspGraphServTypeValue_Type.__name__ = "OctetString"
_NlspGraphServTypeValue_Object = MibTableColumn
nlspGraphServTypeValue = _NlspGraphServTypeValue_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 6, 5, 1, 4),
    _NlspGraphServTypeValue_Type()
)
nlspGraphServTypeValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspGraphServTypeValue.setStatus("mandatory")


class _NlspGraphServType_Type(Integer32):
    """Custom type nlspGraphServType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("unknown", 1)
    )


_NlspGraphServType_Type.__name__ = "Integer32"
_NlspGraphServType_Object = MibTableColumn
nlspGraphServType = _NlspGraphServType_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 6, 5, 1, 5),
    _NlspGraphServType_Type()
)
nlspGraphServType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspGraphServType.setStatus("mandatory")
_NlspGraphServNetNum_Type = NetNumber
_NlspGraphServNetNum_Object = MibTableColumn
nlspGraphServNetNum = _NlspGraphServNetNum_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 6, 5, 1, 6),
    _NlspGraphServNetNum_Type()
)
nlspGraphServNetNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspGraphServNetNum.setStatus("mandatory")


class _NlspGraphServNode_Type(OctetString):
    """Custom type nlspGraphServNode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_NlspGraphServNode_Type.__name__ = "OctetString"
_NlspGraphServNode_Object = MibTableColumn
nlspGraphServNode = _NlspGraphServNode_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 6, 5, 1, 7),
    _NlspGraphServNode_Type()
)
nlspGraphServNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspGraphServNode.setStatus("mandatory")


class _NlspGraphServSocket_Type(OctetString):
    """Custom type nlspGraphServSocket based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_NlspGraphServSocket_Type.__name__ = "OctetString"
_NlspGraphServSocket_Object = MibTableColumn
nlspGraphServSocket = _NlspGraphServSocket_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 6, 5, 1, 8),
    _NlspGraphServSocket_Type()
)
nlspGraphServSocket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspGraphServSocket.setStatus("mandatory")
_NlspLSP_ObjectIdentity = ObjectIdentity
nlspLSP = _NlspLSP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 7)
)
_NlspLSPTable_Object = MibTable
nlspLSPTable = _NlspLSPTable_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 7, 1)
)
if mibBuilder.loadTexts:
    nlspLSPTable.setStatus("mandatory")
_NlspLSPEntry_Object = MibTableRow
nlspLSPEntry = _NlspLSPEntry_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 7, 1, 1)
)
nlspLSPEntry.setIndexNames(
    (0, "NOVELL-NLSP-MIB", "nlspLSPSysInstance"),
    (0, "NOVELL-NLSP-MIB", "nlspLSPID"),
)
if mibBuilder.loadTexts:
    nlspLSPEntry.setStatus("mandatory")
_NlspLSPSysInstance_Type = Integer32
_NlspLSPSysInstance_Object = MibTableColumn
nlspLSPSysInstance = _NlspLSPSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 7, 1, 1, 1),
    _NlspLSPSysInstance_Type()
)
nlspLSPSysInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspLSPSysInstance.setStatus("mandatory")


class _NlspLSPID_Type(OctetString):
    """Custom type nlspLSPID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_NlspLSPID_Type.__name__ = "OctetString"
_NlspLSPID_Object = MibTableColumn
nlspLSPID = _NlspLSPID_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 7, 1, 1, 2),
    _NlspLSPID_Type()
)
nlspLSPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspLSPID.setStatus("mandatory")


class _NlspLSPLifetime_Type(Integer32):
    """Custom type nlspLSPLifetime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NlspLSPLifetime_Type.__name__ = "Integer32"
_NlspLSPLifetime_Object = MibTableColumn
nlspLSPLifetime = _NlspLSPLifetime_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 7, 1, 1, 3),
    _NlspLSPLifetime_Type()
)
nlspLSPLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspLSPLifetime.setStatus("mandatory")


class _NlspLSPSeqNum_Type(Integer32):
    """Custom type nlspLSPSeqNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NlspLSPSeqNum_Type.__name__ = "Integer32"
_NlspLSPSeqNum_Object = MibTableColumn
nlspLSPSeqNum = _NlspLSPSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 7, 1, 1, 4),
    _NlspLSPSeqNum_Type()
)
nlspLSPSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspLSPSeqNum.setStatus("mandatory")


class _NlspLSPChecksum_Type(Integer32):
    """Custom type nlspLSPChecksum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NlspLSPChecksum_Type.__name__ = "Integer32"
_NlspLSPChecksum_Object = MibTableColumn
nlspLSPChecksum = _NlspLSPChecksum_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 7, 1, 1, 5),
    _NlspLSPChecksum_Type()
)
nlspLSPChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspLSPChecksum.setStatus("mandatory")


class _NlspLSPRouterType_Type(Integer32):
    """Custom type nlspLSPRouterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nlspLevel1Router", 2),
          ("unknown", 1))
    )


_NlspLSPRouterType_Type.__name__ = "Integer32"
_NlspLSPRouterType_Object = MibTableColumn
nlspLSPRouterType = _NlspLSPRouterType_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 7, 1, 1, 6),
    _NlspLSPRouterType_Type()
)
nlspLSPRouterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspLSPRouterType.setStatus("mandatory")


class _NlspLSPOverload_Type(Integer32):
    """Custom type nlspLSPOverload based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NlspLSPOverload_Type.__name__ = "Integer32"
_NlspLSPOverload_Object = MibTableColumn
nlspLSPOverload = _NlspLSPOverload_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 7, 1, 1, 7),
    _NlspLSPOverload_Type()
)
nlspLSPOverload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspLSPOverload.setStatus("mandatory")


class _NlspLSPHeader_Type(OctetString):
    """Custom type nlspLSPHeader based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(27, 27),
    )


_NlspLSPHeader_Type.__name__ = "OctetString"
_NlspLSPHeader_Object = MibTableColumn
nlspLSPHeader = _NlspLSPHeader_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 7, 1, 1, 8),
    _NlspLSPHeader_Type()
)
nlspLSPHeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspLSPHeader.setStatus("mandatory")
_NlspLSPOptTable_Object = MibTable
nlspLSPOptTable = _NlspLSPOptTable_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 7, 2)
)
if mibBuilder.loadTexts:
    nlspLSPOptTable.setStatus("mandatory")
_NlspLSPOptEntry_Object = MibTableRow
nlspLSPOptEntry = _NlspLSPOptEntry_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 7, 2, 1)
)
nlspLSPOptEntry.setIndexNames(
    (0, "NOVELL-NLSP-MIB", "nlspLSPOptSysInstance"),
    (0, "NOVELL-NLSP-MIB", "nlspLSPOptLSPID"),
    (0, "NOVELL-NLSP-MIB", "nlspLSPOptIndex"),
)
if mibBuilder.loadTexts:
    nlspLSPOptEntry.setStatus("mandatory")
_NlspLSPOptSysInstance_Type = Integer32
_NlspLSPOptSysInstance_Object = MibTableColumn
nlspLSPOptSysInstance = _NlspLSPOptSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 7, 2, 1, 1),
    _NlspLSPOptSysInstance_Type()
)
nlspLSPOptSysInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspLSPOptSysInstance.setStatus("mandatory")


class _NlspLSPOptLSPID_Type(OctetString):
    """Custom type nlspLSPOptLSPID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_NlspLSPOptLSPID_Type.__name__ = "OctetString"
_NlspLSPOptLSPID_Object = MibTableColumn
nlspLSPOptLSPID = _NlspLSPOptLSPID_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 7, 2, 1, 2),
    _NlspLSPOptLSPID_Type()
)
nlspLSPOptLSPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspLSPOptLSPID.setStatus("mandatory")
_NlspLSPOptIndex_Type = Integer32
_NlspLSPOptIndex_Object = MibTableColumn
nlspLSPOptIndex = _NlspLSPOptIndex_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 7, 2, 1, 3),
    _NlspLSPOptIndex_Type()
)
nlspLSPOptIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspLSPOptIndex.setStatus("mandatory")


class _NlspLSPOptCode_Type(Integer32):
    """Custom type nlspLSPOptCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NlspLSPOptCode_Type.__name__ = "Integer32"
_NlspLSPOptCode_Object = MibTableColumn
nlspLSPOptCode = _NlspLSPOptCode_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 7, 2, 1, 4),
    _NlspLSPOptCode_Type()
)
nlspLSPOptCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspLSPOptCode.setStatus("mandatory")


class _NlspLSPOptLength_Type(Integer32):
    """Custom type nlspLSPOptLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NlspLSPOptLength_Type.__name__ = "Integer32"
_NlspLSPOptLength_Object = MibTableColumn
nlspLSPOptLength = _NlspLSPOptLength_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 7, 2, 1, 5),
    _NlspLSPOptLength_Type()
)
nlspLSPOptLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspLSPOptLength.setStatus("mandatory")


class _NlspLSPOptValue_Type(OctetString):
    """Custom type nlspLSPOptValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NlspLSPOptValue_Type.__name__ = "OctetString"
_NlspLSPOptValue_Object = MibTableColumn
nlspLSPOptValue = _NlspLSPOptValue_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 19, 7, 2, 1, 6),
    _NlspLSPOptValue_Type()
)
nlspLSPOptValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlspLSPOptValue.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NOVELL-NLSP-MIB",
    **{"SystemID": SystemID,
       "NLSPID": NLSPID,
       "NetNumber": NetNumber,
       "nlsp": nlsp,
       "nlspSystem": nlspSystem,
       "nlspSysTable": nlspSysTable,
       "nlspSysEntry": nlspSysEntry,
       "nlspSysInstance": nlspSysInstance,
       "nlspSysState": nlspSysState,
       "nlspSysID": nlspSysID,
       "nlspSysMinNonBcastLSPTransInt": nlspSysMinNonBcastLSPTransInt,
       "nlspSysMinBcastLSPTransInt": nlspSysMinBcastLSPTransInt,
       "nlspSysMinLSPGenInt": nlspSysMinLSPGenInt,
       "nlspSysMaxLSPGenInt": nlspSysMaxLSPGenInt,
       "nlspSysMaxLSPAge": nlspSysMaxLSPAge,
       "nlspSysBcastHelloInt": nlspSysBcastHelloInt,
       "nlspSysNonBcastHelloInt": nlspSysNonBcastHelloInt,
       "nlspSysDRBcastHelloInt": nlspSysDRBcastHelloInt,
       "nlspSysHoldTimeMultiplier": nlspSysHoldTimeMultiplier,
       "nlspSysCompSNPInt": nlspSysCompSNPInt,
       "nlspSysPartSNPInt": nlspSysPartSNPInt,
       "nlspSysWaitTime": nlspSysWaitTime,
       "nlspSysOrigL1LSPBufSize": nlspSysOrigL1LSPBufSize,
       "nlspSysVersion": nlspSysVersion,
       "nlspSysCorrLSPs": nlspSysCorrLSPs,
       "nlspSysL1Overloaded": nlspSysL1Overloaded,
       "nlspSysL1DbaseOverloads": nlspSysL1DbaseOverloads,
       "nlspSysMaxSeqNums": nlspSysMaxSeqNums,
       "nlspSysSeqNumSkips": nlspSysSeqNumSkips,
       "nlspSysTransmittedLSPs": nlspSysTransmittedLSPs,
       "nlspSysReceivedLSPs": nlspSysReceivedLSPs,
       "nlspSysOwnLSPPurges": nlspSysOwnLSPPurges,
       "nlspSysVersionErrors": nlspSysVersionErrors,
       "nlspSysIncorrectPackets": nlspSysIncorrectPackets,
       "nlspSysNearestL2DefaultExists": nlspSysNearestL2DefaultExists,
       "nlspSysNearestL2DefaultRouter": nlspSysNearestL2DefaultRouter,
       "nlspSysResourceFailures": nlspSysResourceFailures,
       "nlspSysAreaTable": nlspSysAreaTable,
       "nlspSysAreaEntry": nlspSysAreaEntry,
       "nlspSysAreaSysInstance": nlspSysAreaSysInstance,
       "nlspSysAreaNet": nlspSysAreaNet,
       "nlspSysAreaMask": nlspSysAreaMask,
       "nlspActAreaTable": nlspActAreaTable,
       "nlspActAreaEntry": nlspActAreaEntry,
       "nlspActAreaSysInstance": nlspActAreaSysInstance,
       "nlspActAreaNet": nlspActAreaNet,
       "nlspActAreaMask": nlspActAreaMask,
       "nlspCircuit": nlspCircuit,
       "nlspCircTable": nlspCircTable,
       "nlspCircEntry": nlspCircEntry,
       "nlspCircSysInstance": nlspCircSysInstance,
       "nlspCircIndex": nlspCircIndex,
       "nlspCircState": nlspCircState,
       "nlspCircPace": nlspCircPace,
       "nlspCircHelloTimer": nlspCircHelloTimer,
       "nlspCircL1DefaultCost": nlspCircL1DefaultCost,
       "nlspCircL1DesRouterPriority": nlspCircL1DesRouterPriority,
       "nlspCircL1CircID": nlspCircL1CircID,
       "nlspCircL1DesRouter": nlspCircL1DesRouter,
       "nlspCircLANL1DesRouterChanges": nlspCircLANL1DesRouterChanges,
       "nlspCircNeighChanges": nlspCircNeighChanges,
       "nlspCircRejNeighbors": nlspCircRejNeighbors,
       "nlspCircOutPackets": nlspCircOutPackets,
       "nlspCircInPackets": nlspCircInPackets,
       "nlspCircActualMaxPacketSize": nlspCircActualMaxPacketSize,
       "nlspCircPSNPsSent": nlspCircPSNPsSent,
       "nlspCircPSNPsReceived": nlspCircPSNPsReceived,
       "nlspForwarding": nlspForwarding,
       "nlspDestTable": nlspDestTable,
       "nlspDestEntry": nlspDestEntry,
       "nlspDestSysInstance": nlspDestSysInstance,
       "nlspDestNetNum": nlspDestNetNum,
       "nlspDestID": nlspDestID,
       "nlspDestEstDelay": nlspDestEstDelay,
       "nlspDestEstThroughput": nlspDestEstThroughput,
       "nlspDestNextHopID": nlspDestNextHopID,
       "nlspDestCost": nlspDestCost,
       "nlspNeighbors": nlspNeighbors,
       "nlspNeighTable": nlspNeighTable,
       "nlspNeighEntry": nlspNeighEntry,
       "nlspNeighSysInstance": nlspNeighSysInstance,
       "nlspNeighCircIndex": nlspNeighCircIndex,
       "nlspNeighIndex": nlspNeighIndex,
       "nlspNeighState": nlspNeighState,
       "nlspNeighNICAddress": nlspNeighNICAddress,
       "nlspNeighSysType": nlspNeighSysType,
       "nlspNeighSysID": nlspNeighSysID,
       "nlspNeighName": nlspNeighName,
       "nlspNeighUsage": nlspNeighUsage,
       "nlspNeighHoldTimer": nlspNeighHoldTimer,
       "nlspNeighRemainingTime": nlspNeighRemainingTime,
       "nlspNeighPriority": nlspNeighPriority,
       "nlspTranslation": nlspTranslation,
       "nlspIDMapTable": nlspIDMapTable,
       "nlspIDMapEntry": nlspIDMapEntry,
       "nlspIDMapSysInstance": nlspIDMapSysInstance,
       "nlspIDMapID": nlspIDMapID,
       "nlspIDMapServerName": nlspIDMapServerName,
       "nlspIDMapNetNum": nlspIDMapNetNum,
       "nlspNetMapTable": nlspNetMapTable,
       "nlspNetMapEntry": nlspNetMapEntry,
       "nlspNetMapSysInstance": nlspNetMapSysInstance,
       "nlspNetMapNetNum": nlspNetMapNetNum,
       "nlspNetMapServerName": nlspNetMapServerName,
       "nlspNetMapID": nlspNetMapID,
       "nlspNameMapTable": nlspNameMapTable,
       "nlspNameMapEntry": nlspNameMapEntry,
       "nlspNameMapSysInstance": nlspNameMapSysInstance,
       "nlspNameMapServerName": nlspNameMapServerName,
       "nlspNameMapNetNum": nlspNameMapNetNum,
       "nlspNameMapID": nlspNameMapID,
       "nlspGraph": nlspGraph,
       "nlspNodeTable": nlspNodeTable,
       "nlspNodeEntry": nlspNodeEntry,
       "nlspNodeSysInstance": nlspNodeSysInstance,
       "nlspNodeID": nlspNodeID,
       "nlspNodeNetNum": nlspNodeNetNum,
       "nlspNodeType": nlspNodeType,
       "nlspNodeEstDelay": nlspNodeEstDelay,
       "nlspNodeEstThroughput": nlspNodeEstThroughput,
       "nlspNodeMaxPacketSize": nlspNodeMaxPacketSize,
       "nlspNodeCost": nlspNodeCost,
       "nlspNodeOverload": nlspNodeOverload,
       "nlspNodeReachable": nlspNodeReachable,
       "nlspLinkTable": nlspLinkTable,
       "nlspLinkEntry": nlspLinkEntry,
       "nlspLinkSysInstance": nlspLinkSysInstance,
       "nlspLinkNLSPID": nlspLinkNLSPID,
       "nlspLinkIndex": nlspLinkIndex,
       "nlspLinkNeighNLSPID": nlspLinkNeighNLSPID,
       "nlspLinkFromNeighCost": nlspLinkFromNeighCost,
       "nlspLinkMaxPacketSize": nlspLinkMaxPacketSize,
       "nlspLinkThroughput": nlspLinkThroughput,
       "nlspLinkDelay": nlspLinkDelay,
       "nlspLinkMediaType": nlspLinkMediaType,
       "nlspLinkToNeighCost": nlspLinkToNeighCost,
       "nlspPathTable": nlspPathTable,
       "nlspPathEntry": nlspPathEntry,
       "nlspPathSysInstance": nlspPathSysInstance,
       "nlspPathDestNLSPID": nlspPathDestNLSPID,
       "nlspPathLinkIndex": nlspPathLinkIndex,
       "nlspGraphXRouteTable": nlspGraphXRouteTable,
       "nlspGraphXRouteEntry": nlspGraphXRouteEntry,
       "nlspGraphXRouteSysInstance": nlspGraphXRouteSysInstance,
       "nlspGraphXRouteNLSPID": nlspGraphXRouteNLSPID,
       "nlspGraphXRouteNetNum": nlspGraphXRouteNetNum,
       "nlspGraphXRouteCost": nlspGraphXRouteCost,
       "nlspGraphXRouteHopCount": nlspGraphXRouteHopCount,
       "nlspGraphServTable": nlspGraphServTable,
       "nlspGraphServEntry": nlspGraphServEntry,
       "nlspGraphServSysInstance": nlspGraphServSysInstance,
       "nlspGraphServNLSPID": nlspGraphServNLSPID,
       "nlspGraphServName": nlspGraphServName,
       "nlspGraphServTypeValue": nlspGraphServTypeValue,
       "nlspGraphServType": nlspGraphServType,
       "nlspGraphServNetNum": nlspGraphServNetNum,
       "nlspGraphServNode": nlspGraphServNode,
       "nlspGraphServSocket": nlspGraphServSocket,
       "nlspLSP": nlspLSP,
       "nlspLSPTable": nlspLSPTable,
       "nlspLSPEntry": nlspLSPEntry,
       "nlspLSPSysInstance": nlspLSPSysInstance,
       "nlspLSPID": nlspLSPID,
       "nlspLSPLifetime": nlspLSPLifetime,
       "nlspLSPSeqNum": nlspLSPSeqNum,
       "nlspLSPChecksum": nlspLSPChecksum,
       "nlspLSPRouterType": nlspLSPRouterType,
       "nlspLSPOverload": nlspLSPOverload,
       "nlspLSPHeader": nlspLSPHeader,
       "nlspLSPOptTable": nlspLSPOptTable,
       "nlspLSPOptEntry": nlspLSPOptEntry,
       "nlspLSPOptSysInstance": nlspLSPOptSysInstance,
       "nlspLSPOptLSPID": nlspLSPOptLSPID,
       "nlspLSPOptIndex": nlspLSPOptIndex,
       "nlspLSPOptCode": nlspLSPOptCode,
       "nlspLSPOptLength": nlspLSPOptLength,
       "nlspLSPOptValue": nlspLSPOptValue}
)
