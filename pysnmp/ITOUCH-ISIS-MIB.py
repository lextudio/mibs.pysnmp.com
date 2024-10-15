# SNMP MIB module (ITOUCH-ISIS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ITOUCH-ISIS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:12:15 2024
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

(iTouch,) = mibBuilder.importSymbols(
    "ITOUCH-MIB",
    "iTouch")

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


# Types definitions



class ExistState(Integer32):
    """Custom type ExistState based on Integer32"""
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





class SupportedProtocol(Integer32):
    """Custom type SupportedProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(129,
              204)
        )
    )
    namedValues = NamedValues(
        *(("ip", 204),
          ("iso8473", 129))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_XIsis_ObjectIdentity = ObjectIdentity
xIsis = _XIsis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 26)
)
_XIsisSystem_ObjectIdentity = ObjectIdentity
xIsisSystem = _XIsisSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 26, 1)
)
_XIsisSysTable_Object = MibTable
xIsisSysTable = _XIsisSysTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 1, 1)
)
if mibBuilder.loadTexts:
    xIsisSysTable.setStatus("mandatory")
_XIsisSysEntry_Object = MibTableRow
xIsisSysEntry = _XIsisSysEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 1, 1, 1)
)
xIsisSysEntry.setIndexNames(
    (0, "ITOUCH-ISIS-MIB", "xIsisSysInstance"),
)
if mibBuilder.loadTexts:
    xIsisSysEntry.setStatus("mandatory")
_XIsisSysInstance_Type = Integer32
_XIsisSysInstance_Object = MibTableColumn
xIsisSysInstance = _XIsisSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 1, 1, 1, 1),
    _XIsisSysInstance_Type()
)
xIsisSysInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisSysInstance.setStatus("mandatory")


class _XIsisSysExistState_Type(Integer32):
    """Custom type xIsisSysExistState based on Integer32"""
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


_XIsisSysExistState_Type.__name__ = "Integer32"
_XIsisSysExistState_Object = MibTableColumn
xIsisSysExistState = _XIsisSysExistState_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 1, 1, 1, 2),
    _XIsisSysExistState_Type()
)
xIsisSysExistState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisSysExistState.setStatus("mandatory")
_XIsisSysVersion_Type = Integer32
_XIsisSysVersion_Object = MibTableColumn
xIsisSysVersion = _XIsisSysVersion_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 1, 1, 1, 3),
    _XIsisSysVersion_Type()
)
xIsisSysVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisSysVersion.setStatus("mandatory")


class _XIsisSysType_Type(Integer32):
    """Custom type xIsisSysType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("level1IS", 1),
          ("level2IS", 2))
    )


_XIsisSysType_Type.__name__ = "Integer32"
_XIsisSysType_Object = MibTableColumn
xIsisSysType = _XIsisSysType_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 1, 1, 1, 4),
    _XIsisSysType_Type()
)
xIsisSysType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xIsisSysType.setStatus("mandatory")
_XIsisSysNET_Type = OctetString
_XIsisSysNET_Object = MibTableColumn
xIsisSysNET = _XIsisSysNET_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 1, 1, 1, 5),
    _XIsisSysNET_Type()
)
xIsisSysNET.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisSysNET.setStatus("mandatory")


class _XIsisSysMaxPathSplits_Type(Integer32):
    """Custom type xIsisSysMaxPathSplits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_XIsisSysMaxPathSplits_Type.__name__ = "Integer32"
_XIsisSysMaxPathSplits_Object = MibTableColumn
xIsisSysMaxPathSplits = _XIsisSysMaxPathSplits_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 1, 1, 1, 6),
    _XIsisSysMaxPathSplits_Type()
)
xIsisSysMaxPathSplits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xIsisSysMaxPathSplits.setStatus("mandatory")


class _XIsisSysMinLSPTransInt_Type(Integer32):
    """Custom type xIsisSysMinLSPTransInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_XIsisSysMinLSPTransInt_Type.__name__ = "Integer32"
_XIsisSysMinLSPTransInt_Object = MibTableColumn
xIsisSysMinLSPTransInt = _XIsisSysMinLSPTransInt_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 1, 1, 1, 7),
    _XIsisSysMinLSPTransInt_Type()
)
xIsisSysMinLSPTransInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xIsisSysMinLSPTransInt.setStatus("mandatory")


class _XIsisSysMaxLSPGenInt_Type(Integer32):
    """Custom type xIsisSysMaxLSPGenInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_XIsisSysMaxLSPGenInt_Type.__name__ = "Integer32"
_XIsisSysMaxLSPGenInt_Object = MibTableColumn
xIsisSysMaxLSPGenInt = _XIsisSysMaxLSPGenInt_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 1, 1, 1, 8),
    _XIsisSysMaxLSPGenInt_Type()
)
xIsisSysMaxLSPGenInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xIsisSysMaxLSPGenInt.setStatus("mandatory")


class _XIsisSysMinBroadLSPTransInt_Type(Integer32):
    """Custom type xIsisSysMinBroadLSPTransInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_XIsisSysMinBroadLSPTransInt_Type.__name__ = "Integer32"
_XIsisSysMinBroadLSPTransInt_Object = MibTableColumn
xIsisSysMinBroadLSPTransInt = _XIsisSysMinBroadLSPTransInt_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 1, 1, 1, 9),
    _XIsisSysMinBroadLSPTransInt_Type()
)
xIsisSysMinBroadLSPTransInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xIsisSysMinBroadLSPTransInt.setStatus("mandatory")


class _XIsisSysCompSNPInt_Type(Integer32):
    """Custom type xIsisSysCompSNPInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_XIsisSysCompSNPInt_Type.__name__ = "Integer32"
_XIsisSysCompSNPInt_Object = MibTableColumn
xIsisSysCompSNPInt = _XIsisSysCompSNPInt_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 1, 1, 1, 10),
    _XIsisSysCompSNPInt_Type()
)
xIsisSysCompSNPInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xIsisSysCompSNPInt.setStatus("mandatory")


class _XIsisSysOrigL1LSPBuffSize_Type(Integer32):
    """Custom type xIsisSysOrigL1LSPBuffSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 1492),
    )


_XIsisSysOrigL1LSPBuffSize_Type.__name__ = "Integer32"
_XIsisSysOrigL1LSPBuffSize_Object = MibTableColumn
xIsisSysOrigL1LSPBuffSize = _XIsisSysOrigL1LSPBuffSize_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 1, 1, 1, 11),
    _XIsisSysOrigL1LSPBuffSize_Type()
)
xIsisSysOrigL1LSPBuffSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xIsisSysOrigL1LSPBuffSize.setStatus("mandatory")


class _XIsisSysMaxAreaAddr_Type(Integer32):
    """Custom type xIsisSysMaxAreaAddr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_XIsisSysMaxAreaAddr_Type.__name__ = "Integer32"
_XIsisSysMaxAreaAddr_Object = MibTableColumn
xIsisSysMaxAreaAddr = _XIsisSysMaxAreaAddr_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 1, 1, 1, 12),
    _XIsisSysMaxAreaAddr_Type()
)
xIsisSysMaxAreaAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xIsisSysMaxAreaAddr.setStatus("mandatory")


class _XIsisSysMinLSPGenInt_Type(Integer32):
    """Custom type xIsisSysMinLSPGenInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_XIsisSysMinLSPGenInt_Type.__name__ = "Integer32"
_XIsisSysMinLSPGenInt_Object = MibTableColumn
xIsisSysMinLSPGenInt = _XIsisSysMinLSPGenInt_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 1, 1, 1, 13),
    _XIsisSysMinLSPGenInt_Type()
)
xIsisSysMinLSPGenInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xIsisSysMinLSPGenInt.setStatus("mandatory")


class _XIsisSysPollESHelloRate_Type(Integer32):
    """Custom type xIsisSysPollESHelloRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_XIsisSysPollESHelloRate_Type.__name__ = "Integer32"
_XIsisSysPollESHelloRate_Object = MibTableColumn
xIsisSysPollESHelloRate = _XIsisSysPollESHelloRate_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 1, 1, 1, 14),
    _XIsisSysPollESHelloRate_Type()
)
xIsisSysPollESHelloRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xIsisSysPollESHelloRate.setStatus("mandatory")


class _XIsisSysPartSNPInt_Type(Integer32):
    """Custom type xIsisSysPartSNPInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_XIsisSysPartSNPInt_Type.__name__ = "Integer32"
_XIsisSysPartSNPInt_Object = MibTableColumn
xIsisSysPartSNPInt = _XIsisSysPartSNPInt_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 1, 1, 1, 15),
    _XIsisSysPartSNPInt_Type()
)
xIsisSysPartSNPInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xIsisSysPartSNPInt.setStatus("mandatory")


class _XIsisSysWaitTime_Type(Integer32):
    """Custom type xIsisSysWaitTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_XIsisSysWaitTime_Type.__name__ = "Integer32"
_XIsisSysWaitTime_Object = MibTableColumn
xIsisSysWaitTime = _XIsisSysWaitTime_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 1, 1, 1, 16),
    _XIsisSysWaitTime_Type()
)
xIsisSysWaitTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xIsisSysWaitTime.setStatus("mandatory")


class _XIsisSysDRISISHelloTimer_Type(Integer32):
    """Custom type xIsisSysDRISISHelloTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_XIsisSysDRISISHelloTimer_Type.__name__ = "Integer32"
_XIsisSysDRISISHelloTimer_Object = MibTableColumn
xIsisSysDRISISHelloTimer = _XIsisSysDRISISHelloTimer_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 1, 1, 1, 17),
    _XIsisSysDRISISHelloTimer_Type()
)
xIsisSysDRISISHelloTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xIsisSysDRISISHelloTimer.setStatus("mandatory")


class _XIsisSysOperState_Type(Integer32):
    """Custom type xIsisSysOperState based on Integer32"""
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


_XIsisSysOperState_Type.__name__ = "Integer32"
_XIsisSysOperState_Object = MibTableColumn
xIsisSysOperState = _XIsisSysOperState_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 1, 1, 1, 18),
    _XIsisSysOperState_Type()
)
xIsisSysOperState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xIsisSysOperState.setStatus("mandatory")


class _XIsisSysL1State_Type(Integer32):
    """Custom type xIsisSysL1State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2),
          ("waiting", 3))
    )


_XIsisSysL1State_Type.__name__ = "Integer32"
_XIsisSysL1State_Object = MibTableColumn
xIsisSysL1State = _XIsisSysL1State_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 1, 1, 1, 19),
    _XIsisSysL1State_Type()
)
xIsisSysL1State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisSysL1State.setStatus("mandatory")
_XIsisSysCorrLSPs_Type = Counter32
_XIsisSysCorrLSPs_Object = MibTableColumn
xIsisSysCorrLSPs = _XIsisSysCorrLSPs_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 1, 1, 1, 20),
    _XIsisSysCorrLSPs_Type()
)
xIsisSysCorrLSPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisSysCorrLSPs.setStatus("mandatory")
_XIsisSysL1LSPDbaseOloads_Type = Counter32
_XIsisSysL1LSPDbaseOloads_Object = MibTableColumn
xIsisSysL1LSPDbaseOloads = _XIsisSysL1LSPDbaseOloads_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 1, 1, 1, 21),
    _XIsisSysL1LSPDbaseOloads_Type()
)
xIsisSysL1LSPDbaseOloads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisSysL1LSPDbaseOloads.setStatus("mandatory")
_XIsisSysManAddrsDropFromArea_Type = Counter32
_XIsisSysManAddrsDropFromArea_Object = MibTableColumn
xIsisSysManAddrsDropFromArea = _XIsisSysManAddrsDropFromArea_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 1, 1, 1, 22),
    _XIsisSysManAddrsDropFromArea_Type()
)
xIsisSysManAddrsDropFromArea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisSysManAddrsDropFromArea.setStatus("mandatory")
_XIsisSysAttmptsToExMaxSeqNum_Type = Counter32
_XIsisSysAttmptsToExMaxSeqNum_Object = MibTableColumn
xIsisSysAttmptsToExMaxSeqNum = _XIsisSysAttmptsToExMaxSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 1, 1, 1, 23),
    _XIsisSysAttmptsToExMaxSeqNum_Type()
)
xIsisSysAttmptsToExMaxSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisSysAttmptsToExMaxSeqNum.setStatus("mandatory")
_XIsisSysSeqNumSkips_Type = Counter32
_XIsisSysSeqNumSkips_Object = MibTableColumn
xIsisSysSeqNumSkips = _XIsisSysSeqNumSkips_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 1, 1, 1, 24),
    _XIsisSysSeqNumSkips_Type()
)
xIsisSysSeqNumSkips.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisSysSeqNumSkips.setStatus("mandatory")
_XIsisSysOwnLSPPurges_Type = Counter32
_XIsisSysOwnLSPPurges_Object = MibTableColumn
xIsisSysOwnLSPPurges = _XIsisSysOwnLSPPurges_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 1, 1, 1, 25),
    _XIsisSysOwnLSPPurges_Type()
)
xIsisSysOwnLSPPurges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisSysOwnLSPPurges.setStatus("mandatory")
_XIsisSysIDFieldLenMismatches_Type = Counter32
_XIsisSysIDFieldLenMismatches_Object = MibTableColumn
xIsisSysIDFieldLenMismatches = _XIsisSysIDFieldLenMismatches_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 1, 1, 1, 26),
    _XIsisSysIDFieldLenMismatches_Type()
)
xIsisSysIDFieldLenMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisSysIDFieldLenMismatches.setStatus("mandatory")
_XIsisSysMaxAreaMis_Type = Counter32
_XIsisSysMaxAreaMis_Object = MibTableColumn
xIsisSysMaxAreaMis = _XIsisSysMaxAreaMis_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 1, 1, 1, 27),
    _XIsisSysMaxAreaMis_Type()
)
xIsisSysMaxAreaMis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisSysMaxAreaMis.setStatus("mandatory")


class _XIsisSysOrigL2LSPBuffSize_Type(Integer32):
    """Custom type xIsisSysOrigL2LSPBuffSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 1492),
    )


_XIsisSysOrigL2LSPBuffSize_Type.__name__ = "Integer32"
_XIsisSysOrigL2LSPBuffSize_Object = MibTableColumn
xIsisSysOrigL2LSPBuffSize = _XIsisSysOrigL2LSPBuffSize_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 1, 1, 1, 28),
    _XIsisSysOrigL2LSPBuffSize_Type()
)
xIsisSysOrigL2LSPBuffSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xIsisSysOrigL2LSPBuffSize.setStatus("mandatory")


class _XIsisSysL2State_Type(Integer32):
    """Custom type xIsisSysL2State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2),
          ("waiting", 3))
    )


_XIsisSysL2State_Type.__name__ = "Integer32"
_XIsisSysL2State_Object = MibTableColumn
xIsisSysL2State = _XIsisSysL2State_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 1, 1, 1, 29),
    _XIsisSysL2State_Type()
)
xIsisSysL2State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisSysL2State.setStatus("mandatory")
_XIsisSysL2LSPDbaseOloads_Type = Counter32
_XIsisSysL2LSPDbaseOloads_Object = MibTableColumn
xIsisSysL2LSPDbaseOloads = _XIsisSysL2LSPDbaseOloads_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 1, 1, 1, 30),
    _XIsisSysL2LSPDbaseOloads_Type()
)
xIsisSysL2LSPDbaseOloads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisSysL2LSPDbaseOloads.setStatus("mandatory")
_XIsisSysMaxAreaCheck_Type = Integer32
_XIsisSysMaxAreaCheck_Object = MibTableColumn
xIsisSysMaxAreaCheck = _XIsisSysMaxAreaCheck_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 1, 1, 1, 31),
    _XIsisSysMaxAreaCheck_Type()
)
xIsisSysMaxAreaCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xIsisSysMaxAreaCheck.setStatus("mandatory")
_XIsisManAreaAddrTable_Object = MibTable
xIsisManAreaAddrTable = _XIsisManAreaAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 1, 2)
)
if mibBuilder.loadTexts:
    xIsisManAreaAddrTable.setStatus("mandatory")
_XIsisManAreaAddrEntry_Object = MibTableRow
xIsisManAreaAddrEntry = _XIsisManAreaAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 1, 2, 1)
)
xIsisManAreaAddrEntry.setIndexNames(
    (0, "ITOUCH-ISIS-MIB", "xIsisManAreaAddrSysInstance"),
    (0, "ITOUCH-ISIS-MIB", "xIsisManAreaAddr"),
)
if mibBuilder.loadTexts:
    xIsisManAreaAddrEntry.setStatus("mandatory")
_XIsisManAreaAddrSysInstance_Type = Integer32
_XIsisManAreaAddrSysInstance_Object = MibTableColumn
xIsisManAreaAddrSysInstance = _XIsisManAreaAddrSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 1, 2, 1, 1),
    _XIsisManAreaAddrSysInstance_Type()
)
xIsisManAreaAddrSysInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisManAreaAddrSysInstance.setStatus("mandatory")
_XIsisManAreaAddr_Type = OctetString
_XIsisManAreaAddr_Object = MibTableColumn
xIsisManAreaAddr = _XIsisManAreaAddr_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 1, 2, 1, 2),
    _XIsisManAreaAddr_Type()
)
xIsisManAreaAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisManAreaAddr.setStatus("mandatory")


class _XIsisManAreaAddrExistState_Type(Integer32):
    """Custom type xIsisManAreaAddrExistState based on Integer32"""
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


_XIsisManAreaAddrExistState_Type.__name__ = "Integer32"
_XIsisManAreaAddrExistState_Object = MibTableColumn
xIsisManAreaAddrExistState = _XIsisManAreaAddrExistState_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 1, 2, 1, 3),
    _XIsisManAreaAddrExistState_Type()
)
xIsisManAreaAddrExistState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xIsisManAreaAddrExistState.setStatus("mandatory")
_XIsisAreaAddrTable_Object = MibTable
xIsisAreaAddrTable = _XIsisAreaAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 1, 3)
)
if mibBuilder.loadTexts:
    xIsisAreaAddrTable.setStatus("mandatory")
_XIsisAreaAddrEntry_Object = MibTableRow
xIsisAreaAddrEntry = _XIsisAreaAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 1, 3, 1)
)
xIsisAreaAddrEntry.setIndexNames(
    (0, "ITOUCH-ISIS-MIB", "xIsisAreaAddrSysInstance"),
    (0, "ITOUCH-ISIS-MIB", "xIsisAreaAddr"),
)
if mibBuilder.loadTexts:
    xIsisAreaAddrEntry.setStatus("mandatory")
_XIsisAreaAddrSysInstance_Type = Integer32
_XIsisAreaAddrSysInstance_Object = MibTableColumn
xIsisAreaAddrSysInstance = _XIsisAreaAddrSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 1, 3, 1, 1),
    _XIsisAreaAddrSysInstance_Type()
)
xIsisAreaAddrSysInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisAreaAddrSysInstance.setStatus("mandatory")
_XIsisAreaAddr_Type = OctetString
_XIsisAreaAddr_Object = MibTableColumn
xIsisAreaAddr = _XIsisAreaAddr_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 1, 3, 1, 2),
    _XIsisAreaAddr_Type()
)
xIsisAreaAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisAreaAddr.setStatus("mandatory")
_XIsisSysProtSuppTable_Object = MibTable
xIsisSysProtSuppTable = _XIsisSysProtSuppTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 1, 4)
)
if mibBuilder.loadTexts:
    xIsisSysProtSuppTable.setStatus("mandatory")
_XIsisSysProtSuppEntry_Object = MibTableRow
xIsisSysProtSuppEntry = _XIsisSysProtSuppEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 1, 4, 1)
)
xIsisSysProtSuppEntry.setIndexNames(
    (0, "ITOUCH-ISIS-MIB", "xIsisSysProtSuppSysInstance"),
    (0, "ITOUCH-ISIS-MIB", "xIsisSysProtSuppProtocol"),
)
if mibBuilder.loadTexts:
    xIsisSysProtSuppEntry.setStatus("mandatory")
_XIsisSysProtSuppSysInstance_Type = Integer32
_XIsisSysProtSuppSysInstance_Object = MibTableColumn
xIsisSysProtSuppSysInstance = _XIsisSysProtSuppSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 1, 4, 1, 1),
    _XIsisSysProtSuppSysInstance_Type()
)
xIsisSysProtSuppSysInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisSysProtSuppSysInstance.setStatus("mandatory")
_XIsisSysProtSuppProtocol_Type = SupportedProtocol
_XIsisSysProtSuppProtocol_Object = MibTableColumn
xIsisSysProtSuppProtocol = _XIsisSysProtSuppProtocol_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 1, 4, 1, 2),
    _XIsisSysProtSuppProtocol_Type()
)
xIsisSysProtSuppProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisSysProtSuppProtocol.setStatus("mandatory")


class _XIsisSysProtSuppExistState_Type(ExistState):
    """Custom type xIsisSysProtSuppExistState based on ExistState"""


_XIsisSysProtSuppExistState_Object = MibTableColumn
xIsisSysProtSuppExistState = _XIsisSysProtSuppExistState_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 1, 4, 1, 3),
    _XIsisSysProtSuppExistState_Type()
)
xIsisSysProtSuppExistState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xIsisSysProtSuppExistState.setStatus("mandatory")
_XIsisCirc_ObjectIdentity = ObjectIdentity
xIsisCirc = _XIsisCirc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 26, 2)
)
_XIsisCircTable_Object = MibTable
xIsisCircTable = _XIsisCircTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 2, 1)
)
if mibBuilder.loadTexts:
    xIsisCircTable.setStatus("mandatory")
_XIsisCircEntry_Object = MibTableRow
xIsisCircEntry = _XIsisCircEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 2, 1, 1)
)
xIsisCircEntry.setIndexNames(
    (0, "ITOUCH-ISIS-MIB", "xIsisCircSysInstance"),
    (0, "ITOUCH-ISIS-MIB", "xIsisCircIndex"),
)
if mibBuilder.loadTexts:
    xIsisCircEntry.setStatus("mandatory")
_XIsisCircSysInstance_Type = Integer32
_XIsisCircSysInstance_Object = MibTableColumn
xIsisCircSysInstance = _XIsisCircSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 2, 1, 1, 1),
    _XIsisCircSysInstance_Type()
)
xIsisCircSysInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisCircSysInstance.setStatus("mandatory")


class _XIsisCircIndex_Type(Integer32):
    """Custom type xIsisCircIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_XIsisCircIndex_Type.__name__ = "Integer32"
_XIsisCircIndex_Object = MibTableColumn
xIsisCircIndex = _XIsisCircIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 2, 1, 1, 2),
    _XIsisCircIndex_Type()
)
xIsisCircIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisCircIndex.setStatus("mandatory")
_XIsisCircIfIndex_Type = Integer32
_XIsisCircIfIndex_Object = MibTableColumn
xIsisCircIfIndex = _XIsisCircIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 2, 1, 1, 3),
    _XIsisCircIfIndex_Type()
)
xIsisCircIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisCircIfIndex.setStatus("mandatory")


class _XIsisCircOperState_Type(Integer32):
    """Custom type xIsisCircOperState based on Integer32"""
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


_XIsisCircOperState_Type.__name__ = "Integer32"
_XIsisCircOperState_Object = MibTableColumn
xIsisCircOperState = _XIsisCircOperState_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 2, 1, 1, 4),
    _XIsisCircOperState_Type()
)
xIsisCircOperState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xIsisCircOperState.setStatus("mandatory")


class _XIsisCircExistState_Type(Integer32):
    """Custom type xIsisCircExistState based on Integer32"""
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


_XIsisCircExistState_Type.__name__ = "Integer32"
_XIsisCircExistState_Object = MibTableColumn
xIsisCircExistState = _XIsisCircExistState_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 2, 1, 1, 5),
    _XIsisCircExistState_Type()
)
xIsisCircExistState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisCircExistState.setStatus("mandatory")


class _XIsisCircType_Type(Integer32):
    """Custom type xIsisCircType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("broadcast", 2),
          ("ptToPt", 3))
    )


_XIsisCircType_Type.__name__ = "Integer32"
_XIsisCircType_Object = MibTableColumn
xIsisCircType = _XIsisCircType_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 2, 1, 1, 6),
    _XIsisCircType_Type()
)
xIsisCircType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xIsisCircType.setStatus("mandatory")


class _XIsisCircHelloTimer_Type(Integer32):
    """Custom type xIsisCircHelloTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_XIsisCircHelloTimer_Type.__name__ = "Integer32"
_XIsisCircHelloTimer_Object = MibTableColumn
xIsisCircHelloTimer = _XIsisCircHelloTimer_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 2, 1, 1, 7),
    _XIsisCircHelloTimer_Type()
)
xIsisCircHelloTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xIsisCircHelloTimer.setStatus("mandatory")


class _XIsisCircL1DefaultMetric_Type(Integer32):
    """Custom type xIsisCircL1DefaultMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_XIsisCircL1DefaultMetric_Type.__name__ = "Integer32"
_XIsisCircL1DefaultMetric_Object = MibTableColumn
xIsisCircL1DefaultMetric = _XIsisCircL1DefaultMetric_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 2, 1, 1, 8),
    _XIsisCircL1DefaultMetric_Type()
)
xIsisCircL1DefaultMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xIsisCircL1DefaultMetric.setStatus("mandatory")


class _XIsisCircL1DelayMetric_Type(Integer32):
    """Custom type xIsisCircL1DelayMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_XIsisCircL1DelayMetric_Type.__name__ = "Integer32"
_XIsisCircL1DelayMetric_Object = MibTableColumn
xIsisCircL1DelayMetric = _XIsisCircL1DelayMetric_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 2, 1, 1, 9),
    _XIsisCircL1DelayMetric_Type()
)
xIsisCircL1DelayMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xIsisCircL1DelayMetric.setStatus("mandatory")


class _XIsisCircL1ExpenseMetric_Type(Integer32):
    """Custom type xIsisCircL1ExpenseMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_XIsisCircL1ExpenseMetric_Type.__name__ = "Integer32"
_XIsisCircL1ExpenseMetric_Object = MibTableColumn
xIsisCircL1ExpenseMetric = _XIsisCircL1ExpenseMetric_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 2, 1, 1, 10),
    _XIsisCircL1ExpenseMetric_Type()
)
xIsisCircL1ExpenseMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xIsisCircL1ExpenseMetric.setStatus("mandatory")


class _XIsisCircL1ErrorMetric_Type(Integer32):
    """Custom type xIsisCircL1ErrorMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_XIsisCircL1ErrorMetric_Type.__name__ = "Integer32"
_XIsisCircL1ErrorMetric_Object = MibTableColumn
xIsisCircL1ErrorMetric = _XIsisCircL1ErrorMetric_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 2, 1, 1, 11),
    _XIsisCircL1ErrorMetric_Type()
)
xIsisCircL1ErrorMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xIsisCircL1ErrorMetric.setStatus("mandatory")


class _XIsisCircExtDomain_Type(Integer32):
    """Custom type xIsisCircExtDomain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_XIsisCircExtDomain_Type.__name__ = "Integer32"
_XIsisCircExtDomain_Object = MibTableColumn
xIsisCircExtDomain = _XIsisCircExtDomain_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 2, 1, 1, 12),
    _XIsisCircExtDomain_Type()
)
xIsisCircExtDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xIsisCircExtDomain.setStatus("mandatory")
_XIsisCircAdjChanges_Type = Counter32
_XIsisCircAdjChanges_Object = MibTableColumn
xIsisCircAdjChanges = _XIsisCircAdjChanges_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 2, 1, 1, 13),
    _XIsisCircAdjChanges_Type()
)
xIsisCircAdjChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisCircAdjChanges.setStatus("mandatory")
_XIsisCircInitFails_Type = Counter32
_XIsisCircInitFails_Object = MibTableColumn
xIsisCircInitFails = _XIsisCircInitFails_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 2, 1, 1, 14),
    _XIsisCircInitFails_Type()
)
xIsisCircInitFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisCircInitFails.setStatus("mandatory")
_XIsisCircRejAdjs_Type = Counter32
_XIsisCircRejAdjs_Object = MibTableColumn
xIsisCircRejAdjs = _XIsisCircRejAdjs_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 2, 1, 1, 15),
    _XIsisCircRejAdjs_Type()
)
xIsisCircRejAdjs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisCircRejAdjs.setStatus("mandatory")
_XIsisCircOutCtrlPDUs_Type = Counter32
_XIsisCircOutCtrlPDUs_Object = MibTableColumn
xIsisCircOutCtrlPDUs = _XIsisCircOutCtrlPDUs_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 2, 1, 1, 16),
    _XIsisCircOutCtrlPDUs_Type()
)
xIsisCircOutCtrlPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisCircOutCtrlPDUs.setStatus("mandatory")
_XIsisCircInCtrlPDUs_Type = Counter32
_XIsisCircInCtrlPDUs_Object = MibTableColumn
xIsisCircInCtrlPDUs = _XIsisCircInCtrlPDUs_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 2, 1, 1, 17),
    _XIsisCircInCtrlPDUs_Type()
)
xIsisCircInCtrlPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisCircInCtrlPDUs.setStatus("mandatory")
_XIsisCircIDFieldLenMismatches_Type = Counter32
_XIsisCircIDFieldLenMismatches_Object = MibTableColumn
xIsisCircIDFieldLenMismatches = _XIsisCircIDFieldLenMismatches_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 2, 1, 1, 18),
    _XIsisCircIDFieldLenMismatches_Type()
)
xIsisCircIDFieldLenMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisCircIDFieldLenMismatches.setStatus("mandatory")


class _XIsisCircL2DefaultMetric_Type(Integer32):
    """Custom type xIsisCircL2DefaultMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_XIsisCircL2DefaultMetric_Type.__name__ = "Integer32"
_XIsisCircL2DefaultMetric_Object = MibTableColumn
xIsisCircL2DefaultMetric = _XIsisCircL2DefaultMetric_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 2, 1, 1, 20),
    _XIsisCircL2DefaultMetric_Type()
)
xIsisCircL2DefaultMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xIsisCircL2DefaultMetric.setStatus("mandatory")


class _XIsisCircL2DelayMetric_Type(Integer32):
    """Custom type xIsisCircL2DelayMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_XIsisCircL2DelayMetric_Type.__name__ = "Integer32"
_XIsisCircL2DelayMetric_Object = MibTableColumn
xIsisCircL2DelayMetric = _XIsisCircL2DelayMetric_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 2, 1, 1, 21),
    _XIsisCircL2DelayMetric_Type()
)
xIsisCircL2DelayMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xIsisCircL2DelayMetric.setStatus("mandatory")


class _XIsisCircL2ExpenseMetric_Type(Integer32):
    """Custom type xIsisCircL2ExpenseMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_XIsisCircL2ExpenseMetric_Type.__name__ = "Integer32"
_XIsisCircL2ExpenseMetric_Object = MibTableColumn
xIsisCircL2ExpenseMetric = _XIsisCircL2ExpenseMetric_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 2, 1, 1, 22),
    _XIsisCircL2ExpenseMetric_Type()
)
xIsisCircL2ExpenseMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xIsisCircL2ExpenseMetric.setStatus("mandatory")


class _XIsisCircL2ErrorMetric_Type(Integer32):
    """Custom type xIsisCircL2ErrorMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_XIsisCircL2ErrorMetric_Type.__name__ = "Integer32"
_XIsisCircL2ErrorMetric_Object = MibTableColumn
xIsisCircL2ErrorMetric = _XIsisCircL2ErrorMetric_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 2, 1, 1, 23),
    _XIsisCircL2ErrorMetric_Type()
)
xIsisCircL2ErrorMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xIsisCircL2ErrorMetric.setStatus("mandatory")


class _XIsisCircManL2Only_Type(Integer32):
    """Custom type xIsisCircManL2Only based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_XIsisCircManL2Only_Type.__name__ = "Integer32"
_XIsisCircManL2Only_Object = MibTableColumn
xIsisCircManL2Only = _XIsisCircManL2Only_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 2, 1, 1, 24),
    _XIsisCircManL2Only_Type()
)
xIsisCircManL2Only.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xIsisCircManL2Only.setStatus("mandatory")


class _XIsisCircL1ISPriority_Type(Integer32):
    """Custom type xIsisCircL1ISPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_XIsisCircL1ISPriority_Type.__name__ = "Integer32"
_XIsisCircL1ISPriority_Object = MibTableColumn
xIsisCircL1ISPriority = _XIsisCircL1ISPriority_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 2, 1, 1, 25),
    _XIsisCircL1ISPriority_Type()
)
xIsisCircL1ISPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xIsisCircL1ISPriority.setStatus("mandatory")
_XIsisCircL1CircID_Type = OctetString
_XIsisCircL1CircID_Object = MibTableColumn
xIsisCircL1CircID = _XIsisCircL1CircID_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 2, 1, 1, 26),
    _XIsisCircL1CircID_Type()
)
xIsisCircL1CircID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisCircL1CircID.setStatus("mandatory")
_XIsisCircL1DesIS_Type = OctetString
_XIsisCircL1DesIS_Object = MibTableColumn
xIsisCircL1DesIS = _XIsisCircL1DesIS_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 2, 1, 1, 27),
    _XIsisCircL1DesIS_Type()
)
xIsisCircL1DesIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisCircL1DesIS.setStatus("mandatory")
_XIsisCircLANL1DesISChanges_Type = Counter32
_XIsisCircLANL1DesISChanges_Object = MibTableColumn
xIsisCircLANL1DesISChanges = _XIsisCircLANL1DesISChanges_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 2, 1, 1, 28),
    _XIsisCircLANL1DesISChanges_Type()
)
xIsisCircLANL1DesISChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisCircLANL1DesISChanges.setStatus("mandatory")


class _XIsisCircL2ISPriority_Type(Integer32):
    """Custom type xIsisCircL2ISPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_XIsisCircL2ISPriority_Type.__name__ = "Integer32"
_XIsisCircL2ISPriority_Object = MibTableColumn
xIsisCircL2ISPriority = _XIsisCircL2ISPriority_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 2, 1, 1, 29),
    _XIsisCircL2ISPriority_Type()
)
xIsisCircL2ISPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xIsisCircL2ISPriority.setStatus("mandatory")
_XIsisCircL2CircID_Type = OctetString
_XIsisCircL2CircID_Object = MibTableColumn
xIsisCircL2CircID = _XIsisCircL2CircID_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 2, 1, 1, 30),
    _XIsisCircL2CircID_Type()
)
xIsisCircL2CircID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisCircL2CircID.setStatus("mandatory")
_XIsisCircL2DesIS_Type = OctetString
_XIsisCircL2DesIS_Object = MibTableColumn
xIsisCircL2DesIS = _XIsisCircL2DesIS_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 2, 1, 1, 31),
    _XIsisCircL2DesIS_Type()
)
xIsisCircL2DesIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisCircL2DesIS.setStatus("mandatory")
_XIsisCircLANL2DesISChanges_Type = Counter32
_XIsisCircLANL2DesISChanges_Object = MibTableColumn
xIsisCircLANL2DesISChanges = _XIsisCircLANL2DesISChanges_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 2, 1, 1, 32),
    _XIsisCircLANL2DesISChanges_Type()
)
xIsisCircLANL2DesISChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisCircLANL2DesISChanges.setStatus("mandatory")
_XIsisCircISTable_Object = MibTable
xIsisCircISTable = _XIsisCircISTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 2, 2)
)
if mibBuilder.loadTexts:
    xIsisCircISTable.setStatus("mandatory")
_XIsisCircISEntry_Object = MibTableRow
xIsisCircISEntry = _XIsisCircISEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 2, 2, 1)
)
xIsisCircISEntry.setIndexNames(
    (0, "ITOUCH-ISIS-MIB", "xIsisCircISIndex"),
)
if mibBuilder.loadTexts:
    xIsisCircISEntry.setStatus("mandatory")
_XIsisCircISSysInstance_Type = Integer32
_XIsisCircISSysInstance_Object = MibTableColumn
xIsisCircISSysInstance = _XIsisCircISSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 2, 2, 1, 1),
    _XIsisCircISSysInstance_Type()
)
xIsisCircISSysInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisCircISSysInstance.setStatus("mandatory")
_XIsisCircISIndex_Type = Integer32
_XIsisCircISIndex_Object = MibTableColumn
xIsisCircISIndex = _XIsisCircISIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 2, 2, 1, 2),
    _XIsisCircISIndex_Type()
)
xIsisCircISIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisCircISIndex.setStatus("mandatory")


class _XIsisCircISExistState_Type(Integer32):
    """Custom type xIsisCircISExistState based on Integer32"""
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


_XIsisCircISExistState_Type.__name__ = "Integer32"
_XIsisCircISExistState_Object = MibTableColumn
xIsisCircISExistState = _XIsisCircISExistState_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 2, 2, 1, 3),
    _XIsisCircISExistState_Type()
)
xIsisCircISExistState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisCircISExistState.setStatus("mandatory")


class _XIsisCircISOperState_Type(Integer32):
    """Custom type xIsisCircISOperState based on Integer32"""
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


_XIsisCircISOperState_Type.__name__ = "Integer32"
_XIsisCircISOperState_Object = MibTableColumn
xIsisCircISOperState = _XIsisCircISOperState_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 2, 2, 1, 4),
    _XIsisCircISOperState_Type()
)
xIsisCircISOperState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xIsisCircISOperState.setStatus("mandatory")


class _XIsisCircISHoldTimerMult_Type(Integer32):
    """Custom type xIsisCircISHoldTimerMult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 63),
    )


_XIsisCircISHoldTimerMult_Type.__name__ = "Integer32"
_XIsisCircISHoldTimerMult_Object = MibTableColumn
xIsisCircISHoldTimerMult = _XIsisCircISHoldTimerMult_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 2, 2, 1, 5),
    _XIsisCircISHoldTimerMult_Type()
)
xIsisCircISHoldTimerMult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisCircISHoldTimerMult.setStatus("mandatory")
_XIsisCircISConfTimer_Type = Integer32
_XIsisCircISConfTimer_Object = MibTableColumn
xIsisCircISConfTimer = _XIsisCircISConfTimer_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 2, 2, 1, 6),
    _XIsisCircISConfTimer_Type()
)
xIsisCircISConfTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xIsisCircISConfTimer.setStatus("mandatory")
_XIsisCircISSuggESConfTimer_Type = Integer32
_XIsisCircISSuggESConfTimer_Object = MibTableColumn
xIsisCircISSuggESConfTimer = _XIsisCircISSuggESConfTimer_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 2, 2, 1, 7),
    _XIsisCircISSuggESConfTimer_Type()
)
xIsisCircISSuggESConfTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xIsisCircISSuggESConfTimer.setStatus("mandatory")


class _XIsisCircISRedHoldTime_Type(Integer32):
    """Custom type xIsisCircISRedHoldTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_XIsisCircISRedHoldTime_Type.__name__ = "Integer32"
_XIsisCircISRedHoldTime_Object = MibTableColumn
xIsisCircISRedHoldTime = _XIsisCircISRedHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 2, 2, 1, 8),
    _XIsisCircISRedHoldTime_Type()
)
xIsisCircISRedHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xIsisCircISRedHoldTime.setStatus("mandatory")
_XIsisCircISESReachChgs_Type = Counter32
_XIsisCircISESReachChgs_Object = MibTableColumn
xIsisCircISESReachChgs = _XIsisCircISESReachChgs_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 2, 2, 1, 9),
    _XIsisCircISESReachChgs_Type()
)
xIsisCircISESReachChgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisCircISESReachChgs.setStatus("mandatory")
_XIsisCircISInv9542PDUs_Type = Counter32
_XIsisCircISInv9542PDUs_Object = MibTableColumn
xIsisCircISInv9542PDUs = _XIsisCircISInv9542PDUs_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 2, 2, 1, 10),
    _XIsisCircISInv9542PDUs_Type()
)
xIsisCircISInv9542PDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisCircISInv9542PDUs.setStatus("mandatory")
_XIsisCircClnsTable_Object = MibTable
xIsisCircClnsTable = _XIsisCircClnsTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 2, 3)
)
if mibBuilder.loadTexts:
    xIsisCircClnsTable.setStatus("mandatory")
_XIsisCircClnsEntry_Object = MibTableRow
xIsisCircClnsEntry = _XIsisCircClnsEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 2, 3, 1)
)
xIsisCircClnsEntry.setIndexNames(
    (0, "ITOUCH-ISIS-MIB", "xIsisCircClnsIndex"),
)
if mibBuilder.loadTexts:
    xIsisCircClnsEntry.setStatus("mandatory")
_XIsisCircClnsSysInstance_Type = Integer32
_XIsisCircClnsSysInstance_Object = MibTableColumn
xIsisCircClnsSysInstance = _XIsisCircClnsSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 2, 3, 1, 1),
    _XIsisCircClnsSysInstance_Type()
)
xIsisCircClnsSysInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisCircClnsSysInstance.setStatus("mandatory")
_XIsisCircClnsIndex_Type = Integer32
_XIsisCircClnsIndex_Object = MibTableColumn
xIsisCircClnsIndex = _XIsisCircClnsIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 2, 3, 1, 2),
    _XIsisCircClnsIndex_Type()
)
xIsisCircClnsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisCircClnsIndex.setStatus("mandatory")


class _XIsisCircClnsExistState_Type(Integer32):
    """Custom type xIsisCircClnsExistState based on Integer32"""
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


_XIsisCircClnsExistState_Type.__name__ = "Integer32"
_XIsisCircClnsExistState_Object = MibTableColumn
xIsisCircClnsExistState = _XIsisCircClnsExistState_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 2, 3, 1, 3),
    _XIsisCircClnsExistState_Type()
)
xIsisCircClnsExistState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisCircClnsExistState.setStatus("mandatory")


class _XIsisCircClnsOperState_Type(Integer32):
    """Custom type xIsisCircClnsOperState based on Integer32"""
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


_XIsisCircClnsOperState_Type.__name__ = "Integer32"
_XIsisCircClnsOperState_Object = MibTableColumn
xIsisCircClnsOperState = _XIsisCircClnsOperState_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 2, 3, 1, 4),
    _XIsisCircClnsOperState_Type()
)
xIsisCircClnsOperState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xIsisCircClnsOperState.setStatus("mandatory")
_XIsisCircClnsRxPDUs_Type = Counter32
_XIsisCircClnsRxPDUs_Object = MibTableColumn
xIsisCircClnsRxPDUs = _XIsisCircClnsRxPDUs_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 2, 3, 1, 5),
    _XIsisCircClnsRxPDUs_Type()
)
xIsisCircClnsRxPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisCircClnsRxPDUs.setStatus("mandatory")
_XIsisCircClnsTxPDUs_Type = Counter32
_XIsisCircClnsTxPDUs_Object = MibTableColumn
xIsisCircClnsTxPDUs = _XIsisCircClnsTxPDUs_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 2, 3, 1, 6),
    _XIsisCircClnsTxPDUs_Type()
)
xIsisCircClnsTxPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisCircClnsTxPDUs.setStatus("mandatory")
_XIsisISAdj_ObjectIdentity = ObjectIdentity
xIsisISAdj = _XIsisISAdj_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 26, 3)
)
_XIsisISAdjTable_Object = MibTable
xIsisISAdjTable = _XIsisISAdjTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 3, 1)
)
if mibBuilder.loadTexts:
    xIsisISAdjTable.setStatus("mandatory")
_XIsisISAdjEntry_Object = MibTableRow
xIsisISAdjEntry = _XIsisISAdjEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 3, 1, 1)
)
xIsisISAdjEntry.setIndexNames(
    (0, "ITOUCH-ISIS-MIB", "xIsisISAdjSysInstance"),
    (0, "ITOUCH-ISIS-MIB", "xIsisISAdjCircIndex"),
    (0, "ITOUCH-ISIS-MIB", "xIsisISAdjIndex"),
)
if mibBuilder.loadTexts:
    xIsisISAdjEntry.setStatus("mandatory")
_XIsisISAdjSysInstance_Type = Integer32
_XIsisISAdjSysInstance_Object = MibTableColumn
xIsisISAdjSysInstance = _XIsisISAdjSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 3, 1, 1, 1),
    _XIsisISAdjSysInstance_Type()
)
xIsisISAdjSysInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisISAdjSysInstance.setStatus("mandatory")
_XIsisISAdjCircIndex_Type = Integer32
_XIsisISAdjCircIndex_Object = MibTableColumn
xIsisISAdjCircIndex = _XIsisISAdjCircIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 3, 1, 1, 2),
    _XIsisISAdjCircIndex_Type()
)
xIsisISAdjCircIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisISAdjCircIndex.setStatus("mandatory")
_XIsisISAdjIndex_Type = Integer32
_XIsisISAdjIndex_Object = MibTableColumn
xIsisISAdjIndex = _XIsisISAdjIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 3, 1, 1, 3),
    _XIsisISAdjIndex_Type()
)
xIsisISAdjIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisISAdjIndex.setStatus("mandatory")


class _XIsisISAdjState_Type(Integer32):
    """Custom type xIsisISAdjState based on Integer32"""
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


_XIsisISAdjState_Type.__name__ = "Integer32"
_XIsisISAdjState_Object = MibTableColumn
xIsisISAdjState = _XIsisISAdjState_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 3, 1, 1, 4),
    _XIsisISAdjState_Type()
)
xIsisISAdjState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisISAdjState.setStatus("mandatory")
_XIsisISAdjNeighSNPAAddress_Type = OctetString
_XIsisISAdjNeighSNPAAddress_Object = MibTableColumn
xIsisISAdjNeighSNPAAddress = _XIsisISAdjNeighSNPAAddress_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 3, 1, 1, 5),
    _XIsisISAdjNeighSNPAAddress_Type()
)
xIsisISAdjNeighSNPAAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisISAdjNeighSNPAAddress.setStatus("mandatory")


class _XIsisISAdjNeighSysType_Type(Integer32):
    """Custom type xIsisISAdjNeighSysType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("intermediateSystem", 3),
          ("l1IntermediateSystem", 4),
          ("l2IntermediateSystem", 5),
          ("unknown", 1))
    )


_XIsisISAdjNeighSysType_Type.__name__ = "Integer32"
_XIsisISAdjNeighSysType_Object = MibTableColumn
xIsisISAdjNeighSysType = _XIsisISAdjNeighSysType_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 3, 1, 1, 6),
    _XIsisISAdjNeighSysType_Type()
)
xIsisISAdjNeighSysType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisISAdjNeighSysType.setStatus("mandatory")
_XIsisISAdjNeighSysID_Type = OctetString
_XIsisISAdjNeighSysID_Object = MibTableColumn
xIsisISAdjNeighSysID = _XIsisISAdjNeighSysID_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 3, 1, 1, 7),
    _XIsisISAdjNeighSysID_Type()
)
xIsisISAdjNeighSysID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisISAdjNeighSysID.setStatus("mandatory")


class _XIsisISAdjUsage_Type(Integer32):
    """Custom type xIsisISAdjUsage based on Integer32"""
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
        *(("level1", 2),
          ("level1and2", 4),
          ("level2", 3),
          ("undefined", 1))
    )


_XIsisISAdjUsage_Type.__name__ = "Integer32"
_XIsisISAdjUsage_Object = MibTableColumn
xIsisISAdjUsage = _XIsisISAdjUsage_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 3, 1, 1, 8),
    _XIsisISAdjUsage_Type()
)
xIsisISAdjUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisISAdjUsage.setStatus("mandatory")


class _XIsisISAdjHoldTimer_Type(Integer32):
    """Custom type xIsisISAdjHoldTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_XIsisISAdjHoldTimer_Type.__name__ = "Integer32"
_XIsisISAdjHoldTimer_Object = MibTableColumn
xIsisISAdjHoldTimer = _XIsisISAdjHoldTimer_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 3, 1, 1, 9),
    _XIsisISAdjHoldTimer_Type()
)
xIsisISAdjHoldTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisISAdjHoldTimer.setStatus("mandatory")


class _XIsisISAdjNeighPriority_Type(Integer32):
    """Custom type xIsisISAdjNeighPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_XIsisISAdjNeighPriority_Type.__name__ = "Integer32"
_XIsisISAdjNeighPriority_Object = MibTableColumn
xIsisISAdjNeighPriority = _XIsisISAdjNeighPriority_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 3, 1, 1, 10),
    _XIsisISAdjNeighPriority_Type()
)
xIsisISAdjNeighPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisISAdjNeighPriority.setStatus("mandatory")
_XIsisISAdjAreaAddrTable_Object = MibTable
xIsisISAdjAreaAddrTable = _XIsisISAdjAreaAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 3, 2)
)
if mibBuilder.loadTexts:
    xIsisISAdjAreaAddrTable.setStatus("mandatory")
_XIsisISAdjAreaAddrEntry_Object = MibTableRow
xIsisISAdjAreaAddrEntry = _XIsisISAdjAreaAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 3, 2, 1)
)
xIsisISAdjAreaAddrEntry.setIndexNames(
    (0, "ITOUCH-ISIS-MIB", "xIsisISAdjAreaAddrSysInstance"),
    (0, "ITOUCH-ISIS-MIB", "xIsisISAdjAreaAddrCircIndex"),
    (0, "ITOUCH-ISIS-MIB", "xIsisISAdjAreaAddrAdjIndex"),
    (0, "ITOUCH-ISIS-MIB", "xIsisISAdjAreaAddress"),
)
if mibBuilder.loadTexts:
    xIsisISAdjAreaAddrEntry.setStatus("mandatory")
_XIsisISAdjAreaAddrSysInstance_Type = Integer32
_XIsisISAdjAreaAddrSysInstance_Object = MibTableColumn
xIsisISAdjAreaAddrSysInstance = _XIsisISAdjAreaAddrSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 3, 2, 1, 1),
    _XIsisISAdjAreaAddrSysInstance_Type()
)
xIsisISAdjAreaAddrSysInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisISAdjAreaAddrSysInstance.setStatus("mandatory")
_XIsisISAdjAreaAddrCircIndex_Type = Integer32
_XIsisISAdjAreaAddrCircIndex_Object = MibTableColumn
xIsisISAdjAreaAddrCircIndex = _XIsisISAdjAreaAddrCircIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 3, 2, 1, 2),
    _XIsisISAdjAreaAddrCircIndex_Type()
)
xIsisISAdjAreaAddrCircIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisISAdjAreaAddrCircIndex.setStatus("mandatory")
_XIsisISAdjAreaAddrAdjIndex_Type = Integer32
_XIsisISAdjAreaAddrAdjIndex_Object = MibTableColumn
xIsisISAdjAreaAddrAdjIndex = _XIsisISAdjAreaAddrAdjIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 3, 2, 1, 3),
    _XIsisISAdjAreaAddrAdjIndex_Type()
)
xIsisISAdjAreaAddrAdjIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisISAdjAreaAddrAdjIndex.setStatus("mandatory")
_XIsisISAdjAreaAddress_Type = OctetString
_XIsisISAdjAreaAddress_Object = MibTableColumn
xIsisISAdjAreaAddress = _XIsisISAdjAreaAddress_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 3, 2, 1, 4),
    _XIsisISAdjAreaAddress_Type()
)
xIsisISAdjAreaAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisISAdjAreaAddress.setStatus("mandatory")
_XIsisISAdjIPAddrTable_Object = MibTable
xIsisISAdjIPAddrTable = _XIsisISAdjIPAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 3, 3)
)
if mibBuilder.loadTexts:
    xIsisISAdjIPAddrTable.setStatus("mandatory")
_XIsisISAdjIPAddrEntry_Object = MibTableRow
xIsisISAdjIPAddrEntry = _XIsisISAdjIPAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 3, 3, 1)
)
xIsisISAdjIPAddrEntry.setIndexNames(
    (0, "ITOUCH-ISIS-MIB", "xIsisISAdjIPAddrSysInstance"),
    (0, "ITOUCH-ISIS-MIB", "xIsisISAdjIPAddrCircIndex"),
    (0, "ITOUCH-ISIS-MIB", "xIsisISAdjIPAddrAdjIndex"),
)
if mibBuilder.loadTexts:
    xIsisISAdjIPAddrEntry.setStatus("mandatory")
_XIsisISAdjIPAddrSysInstance_Type = Integer32
_XIsisISAdjIPAddrSysInstance_Object = MibTableColumn
xIsisISAdjIPAddrSysInstance = _XIsisISAdjIPAddrSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 3, 3, 1, 1),
    _XIsisISAdjIPAddrSysInstance_Type()
)
xIsisISAdjIPAddrSysInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisISAdjIPAddrSysInstance.setStatus("mandatory")
_XIsisISAdjIPAddrCircIndex_Type = Integer32
_XIsisISAdjIPAddrCircIndex_Object = MibTableColumn
xIsisISAdjIPAddrCircIndex = _XIsisISAdjIPAddrCircIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 3, 3, 1, 2),
    _XIsisISAdjIPAddrCircIndex_Type()
)
xIsisISAdjIPAddrCircIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisISAdjIPAddrCircIndex.setStatus("mandatory")
_XIsisISAdjIPAddrAdjIndex_Type = Integer32
_XIsisISAdjIPAddrAdjIndex_Object = MibTableColumn
xIsisISAdjIPAddrAdjIndex = _XIsisISAdjIPAddrAdjIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 3, 3, 1, 3),
    _XIsisISAdjIPAddrAdjIndex_Type()
)
xIsisISAdjIPAddrAdjIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisISAdjIPAddrAdjIndex.setStatus("mandatory")
_XIsisISAdjIPAddress_Type = IpAddress
_XIsisISAdjIPAddress_Object = MibTableColumn
xIsisISAdjIPAddress = _XIsisISAdjIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 3, 3, 1, 4),
    _XIsisISAdjIPAddress_Type()
)
xIsisISAdjIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisISAdjIPAddress.setStatus("mandatory")
_XIsisISAdjProtSuppTable_Object = MibTable
xIsisISAdjProtSuppTable = _XIsisISAdjProtSuppTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 3, 4)
)
if mibBuilder.loadTexts:
    xIsisISAdjProtSuppTable.setStatus("mandatory")
_XIsisISAdjProtSuppEntry_Object = MibTableRow
xIsisISAdjProtSuppEntry = _XIsisISAdjProtSuppEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 3, 4, 1)
)
xIsisISAdjProtSuppEntry.setIndexNames(
    (0, "ITOUCH-ISIS-MIB", "xIsisISAdjProtSuppSysInstance"),
    (0, "ITOUCH-ISIS-MIB", "xIsisISAdjProtSuppCircIndex"),
    (0, "ITOUCH-ISIS-MIB", "xIsisISAdjProtSuppAdjIndex"),
    (0, "ITOUCH-ISIS-MIB", "xIsisISAdjProtSuppProtocol"),
)
if mibBuilder.loadTexts:
    xIsisISAdjProtSuppEntry.setStatus("mandatory")
_XIsisISAdjProtSuppSysInstance_Type = Integer32
_XIsisISAdjProtSuppSysInstance_Object = MibTableColumn
xIsisISAdjProtSuppSysInstance = _XIsisISAdjProtSuppSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 3, 4, 1, 1),
    _XIsisISAdjProtSuppSysInstance_Type()
)
xIsisISAdjProtSuppSysInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisISAdjProtSuppSysInstance.setStatus("mandatory")
_XIsisISAdjProtSuppCircIndex_Type = Integer32
_XIsisISAdjProtSuppCircIndex_Object = MibTableColumn
xIsisISAdjProtSuppCircIndex = _XIsisISAdjProtSuppCircIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 3, 4, 1, 2),
    _XIsisISAdjProtSuppCircIndex_Type()
)
xIsisISAdjProtSuppCircIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisISAdjProtSuppCircIndex.setStatus("mandatory")
_XIsisISAdjProtSuppAdjIndex_Type = Integer32
_XIsisISAdjProtSuppAdjIndex_Object = MibTableColumn
xIsisISAdjProtSuppAdjIndex = _XIsisISAdjProtSuppAdjIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 3, 4, 1, 3),
    _XIsisISAdjProtSuppAdjIndex_Type()
)
xIsisISAdjProtSuppAdjIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisISAdjProtSuppAdjIndex.setStatus("mandatory")
_XIsisISAdjProtSuppProtocol_Type = SupportedProtocol
_XIsisISAdjProtSuppProtocol_Object = MibTableColumn
xIsisISAdjProtSuppProtocol = _XIsisISAdjProtSuppProtocol_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 3, 4, 1, 4),
    _XIsisISAdjProtSuppProtocol_Type()
)
xIsisISAdjProtSuppProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisISAdjProtSuppProtocol.setStatus("mandatory")
_XIsisESAdj_ObjectIdentity = ObjectIdentity
xIsisESAdj = _XIsisESAdj_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 26, 4)
)
_XIsisESAdjTable_Object = MibTable
xIsisESAdjTable = _XIsisESAdjTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 4, 1)
)
if mibBuilder.loadTexts:
    xIsisESAdjTable.setStatus("mandatory")
_XIsisESAdjEntry_Object = MibTableRow
xIsisESAdjEntry = _XIsisESAdjEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 4, 1, 1)
)
xIsisESAdjEntry.setIndexNames(
    (0, "ITOUCH-ISIS-MIB", "xIsisESAdjSysInstance"),
    (0, "ITOUCH-ISIS-MIB", "xIsisESAdjCircIndex"),
    (0, "ITOUCH-ISIS-MIB", "xIsisESAdjIndex"),
    (0, "ITOUCH-ISIS-MIB", "xIsisESAdjESID"),
)
if mibBuilder.loadTexts:
    xIsisESAdjEntry.setStatus("mandatory")
_XIsisESAdjSysInstance_Type = Integer32
_XIsisESAdjSysInstance_Object = MibTableColumn
xIsisESAdjSysInstance = _XIsisESAdjSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 4, 1, 1, 1),
    _XIsisESAdjSysInstance_Type()
)
xIsisESAdjSysInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisESAdjSysInstance.setStatus("mandatory")
_XIsisESAdjCircIndex_Type = Integer32
_XIsisESAdjCircIndex_Object = MibTableColumn
xIsisESAdjCircIndex = _XIsisESAdjCircIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 4, 1, 1, 2),
    _XIsisESAdjCircIndex_Type()
)
xIsisESAdjCircIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisESAdjCircIndex.setStatus("mandatory")
_XIsisESAdjIndex_Type = Integer32
_XIsisESAdjIndex_Object = MibTableColumn
xIsisESAdjIndex = _XIsisESAdjIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 4, 1, 1, 3),
    _XIsisESAdjIndex_Type()
)
xIsisESAdjIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisESAdjIndex.setStatus("mandatory")


class _XIsisESAdjType_Type(Integer32):
    """Custom type xIsisESAdjType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("manual", 2))
    )


_XIsisESAdjType_Type.__name__ = "Integer32"
_XIsisESAdjType_Object = MibTableColumn
xIsisESAdjType = _XIsisESAdjType_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 4, 1, 1, 4),
    _XIsisESAdjType_Type()
)
xIsisESAdjType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisESAdjType.setStatus("mandatory")


class _XIsisESAdjState_Type(Integer32):
    """Custom type xIsisESAdjState based on Integer32"""
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


_XIsisESAdjState_Type.__name__ = "Integer32"
_XIsisESAdjState_Object = MibTableColumn
xIsisESAdjState = _XIsisESAdjState_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 4, 1, 1, 5),
    _XIsisESAdjState_Type()
)
xIsisESAdjState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xIsisESAdjState.setStatus("mandatory")
_XIsisESAdjNeighSNPAAddress_Type = OctetString
_XIsisESAdjNeighSNPAAddress_Object = MibTableColumn
xIsisESAdjNeighSNPAAddress = _XIsisESAdjNeighSNPAAddress_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 4, 1, 1, 6),
    _XIsisESAdjNeighSNPAAddress_Type()
)
xIsisESAdjNeighSNPAAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xIsisESAdjNeighSNPAAddress.setStatus("mandatory")


class _XIsisESAdjExistState_Type(Integer32):
    """Custom type xIsisESAdjExistState based on Integer32"""
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


_XIsisESAdjExistState_Type.__name__ = "Integer32"
_XIsisESAdjExistState_Object = MibTableColumn
xIsisESAdjExistState = _XIsisESAdjExistState_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 4, 1, 1, 7),
    _XIsisESAdjExistState_Type()
)
xIsisESAdjExistState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xIsisESAdjExistState.setStatus("mandatory")
_XIsisESAdjESID_Type = OctetString
_XIsisESAdjESID_Object = MibTableColumn
xIsisESAdjESID = _XIsisESAdjESID_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 4, 1, 1, 8),
    _XIsisESAdjESID_Type()
)
xIsisESAdjESID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisESAdjESID.setStatus("mandatory")
_XIsisReachAddr_ObjectIdentity = ObjectIdentity
xIsisReachAddr = _XIsisReachAddr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 26, 5)
)
_XIsisRATable_Object = MibTable
xIsisRATable = _XIsisRATable_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 5, 1)
)
if mibBuilder.loadTexts:
    xIsisRATable.setStatus("mandatory")
_XIsisRAEntry_Object = MibTableRow
xIsisRAEntry = _XIsisRAEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 5, 1, 1)
)
xIsisRAEntry.setIndexNames(
    (0, "ITOUCH-ISIS-MIB", "xIsisRASysInstance"),
    (0, "ITOUCH-ISIS-MIB", "xIsisRACircIndex"),
    (0, "ITOUCH-ISIS-MIB", "xIsisRAIndex"),
)
if mibBuilder.loadTexts:
    xIsisRAEntry.setStatus("mandatory")
_XIsisRASysInstance_Type = Integer32
_XIsisRASysInstance_Object = MibTableColumn
xIsisRASysInstance = _XIsisRASysInstance_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 5, 1, 1, 1),
    _XIsisRASysInstance_Type()
)
xIsisRASysInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisRASysInstance.setStatus("mandatory")
_XIsisRACircIndex_Type = Integer32
_XIsisRACircIndex_Object = MibTableColumn
xIsisRACircIndex = _XIsisRACircIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 5, 1, 1, 2),
    _XIsisRACircIndex_Type()
)
xIsisRACircIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisRACircIndex.setStatus("mandatory")
_XIsisRAIndex_Type = Integer32
_XIsisRAIndex_Object = MibTableColumn
xIsisRAIndex = _XIsisRAIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 5, 1, 1, 3),
    _XIsisRAIndex_Type()
)
xIsisRAIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisRAIndex.setStatus("mandatory")


class _XIsisRAExistState_Type(Integer32):
    """Custom type xIsisRAExistState based on Integer32"""
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


_XIsisRAExistState_Type.__name__ = "Integer32"
_XIsisRAExistState_Object = MibTableColumn
xIsisRAExistState = _XIsisRAExistState_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 5, 1, 1, 4),
    _XIsisRAExistState_Type()
)
xIsisRAExistState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xIsisRAExistState.setStatus("mandatory")


class _XIsisRAOperState_Type(Integer32):
    """Custom type xIsisRAOperState based on Integer32"""
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


_XIsisRAOperState_Type.__name__ = "Integer32"
_XIsisRAOperState_Object = MibTableColumn
xIsisRAOperState = _XIsisRAOperState_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 5, 1, 1, 5),
    _XIsisRAOperState_Type()
)
xIsisRAOperState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xIsisRAOperState.setStatus("mandatory")
_XIsisRAAddrPrefix_Type = OctetString
_XIsisRAAddrPrefix_Object = MibTableColumn
xIsisRAAddrPrefix = _XIsisRAAddrPrefix_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 5, 1, 1, 6),
    _XIsisRAAddrPrefix_Type()
)
xIsisRAAddrPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xIsisRAAddrPrefix.setStatus("mandatory")


class _XIsisRAMapType_Type(Integer32):
    """Custom type xIsisRAMapType based on Integer32"""
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
        *(("explicit", 2),
          ("extractDSP", 4),
          ("extractIDI", 3),
          ("none", 1))
    )


_XIsisRAMapType_Type.__name__ = "Integer32"
_XIsisRAMapType_Object = MibTableColumn
xIsisRAMapType = _XIsisRAMapType_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 5, 1, 1, 7),
    _XIsisRAMapType_Type()
)
xIsisRAMapType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xIsisRAMapType.setStatus("mandatory")


class _XIsisRADefMetric_Type(Integer32):
    """Custom type xIsisRADefMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_XIsisRADefMetric_Type.__name__ = "Integer32"
_XIsisRADefMetric_Object = MibTableColumn
xIsisRADefMetric = _XIsisRADefMetric_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 5, 1, 1, 8),
    _XIsisRADefMetric_Type()
)
xIsisRADefMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xIsisRADefMetric.setStatus("mandatory")


class _XIsisRADelMetric_Type(Integer32):
    """Custom type xIsisRADelMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_XIsisRADelMetric_Type.__name__ = "Integer32"
_XIsisRADelMetric_Object = MibTableColumn
xIsisRADelMetric = _XIsisRADelMetric_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 5, 1, 1, 9),
    _XIsisRADelMetric_Type()
)
xIsisRADelMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xIsisRADelMetric.setStatus("mandatory")


class _XIsisRAExpMetric_Type(Integer32):
    """Custom type xIsisRAExpMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_XIsisRAExpMetric_Type.__name__ = "Integer32"
_XIsisRAExpMetric_Object = MibTableColumn
xIsisRAExpMetric = _XIsisRAExpMetric_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 5, 1, 1, 10),
    _XIsisRAExpMetric_Type()
)
xIsisRAExpMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xIsisRAExpMetric.setStatus("mandatory")


class _XIsisRAErrMetric_Type(Integer32):
    """Custom type xIsisRAErrMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_XIsisRAErrMetric_Type.__name__ = "Integer32"
_XIsisRAErrMetric_Object = MibTableColumn
xIsisRAErrMetric = _XIsisRAErrMetric_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 5, 1, 1, 11),
    _XIsisRAErrMetric_Type()
)
xIsisRAErrMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xIsisRAErrMetric.setStatus("mandatory")


class _XIsisRADefMetricType_Type(Integer32):
    """Custom type xIsisRADefMetricType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("external", 2),
          ("internal", 1))
    )


_XIsisRADefMetricType_Type.__name__ = "Integer32"
_XIsisRADefMetricType_Object = MibTableColumn
xIsisRADefMetricType = _XIsisRADefMetricType_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 5, 1, 1, 12),
    _XIsisRADefMetricType_Type()
)
xIsisRADefMetricType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xIsisRADefMetricType.setStatus("mandatory")


class _XIsisRADelMetricType_Type(Integer32):
    """Custom type xIsisRADelMetricType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("external", 2),
          ("internal", 1))
    )


_XIsisRADelMetricType_Type.__name__ = "Integer32"
_XIsisRADelMetricType_Object = MibTableColumn
xIsisRADelMetricType = _XIsisRADelMetricType_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 5, 1, 1, 13),
    _XIsisRADelMetricType_Type()
)
xIsisRADelMetricType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xIsisRADelMetricType.setStatus("mandatory")


class _XIsisRAExpMetricType_Type(Integer32):
    """Custom type xIsisRAExpMetricType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("external", 2),
          ("internal", 1))
    )


_XIsisRAExpMetricType_Type.__name__ = "Integer32"
_XIsisRAExpMetricType_Object = MibTableColumn
xIsisRAExpMetricType = _XIsisRAExpMetricType_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 5, 1, 1, 14),
    _XIsisRAExpMetricType_Type()
)
xIsisRAExpMetricType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xIsisRAExpMetricType.setStatus("mandatory")


class _XIsisRAErrMetricType_Type(Integer32):
    """Custom type xIsisRAErrMetricType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("external", 2),
          ("internal", 1))
    )


_XIsisRAErrMetricType_Type.__name__ = "Integer32"
_XIsisRAErrMetricType_Object = MibTableColumn
xIsisRAErrMetricType = _XIsisRAErrMetricType_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 5, 1, 1, 15),
    _XIsisRAErrMetricType_Type()
)
xIsisRAErrMetricType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xIsisRAErrMetricType.setStatus("mandatory")
_XIsisRASNPAAddress_Type = OctetString
_XIsisRASNPAAddress_Object = MibTableColumn
xIsisRASNPAAddress = _XIsisRASNPAAddress_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 5, 1, 1, 16),
    _XIsisRASNPAAddress_Type()
)
xIsisRASNPAAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xIsisRASNPAAddress.setStatus("mandatory")
_XIsisRASNPAMask_Type = OctetString
_XIsisRASNPAMask_Object = MibTableColumn
xIsisRASNPAMask = _XIsisRASNPAMask_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 5, 1, 1, 17),
    _XIsisRASNPAMask_Type()
)
xIsisRASNPAMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xIsisRASNPAMask.setStatus("mandatory")
_XIsisRASNPAPrefix_Type = OctetString
_XIsisRASNPAPrefix_Object = MibTableColumn
xIsisRASNPAPrefix = _XIsisRASNPAPrefix_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 5, 1, 1, 18),
    _XIsisRASNPAPrefix_Type()
)
xIsisRASNPAPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xIsisRASNPAPrefix.setStatus("mandatory")


class _XIsisRAType_Type(Integer32):
    """Custom type xIsisRAType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 2),
          ("manual", 1))
    )


_XIsisRAType_Type.__name__ = "Integer32"
_XIsisRAType_Object = MibTableColumn
xIsisRAType = _XIsisRAType_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 5, 1, 1, 20),
    _XIsisRAType_Type()
)
xIsisRAType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisRAType.setStatus("mandatory")
_XIsisCLNPDest_ObjectIdentity = ObjectIdentity
xIsisCLNPDest = _XIsisCLNPDest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 26, 7)
)
_XIsisL1CLNPDestTable_Object = MibTable
xIsisL1CLNPDestTable = _XIsisL1CLNPDestTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 7, 1)
)
if mibBuilder.loadTexts:
    xIsisL1CLNPDestTable.setStatus("mandatory")
_XIsisL1CLNPDestEntry_Object = MibTableRow
xIsisL1CLNPDestEntry = _XIsisL1CLNPDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 7, 1, 1)
)
xIsisL1CLNPDestEntry.setIndexNames(
    (0, "ITOUCH-ISIS-MIB", "xIsisL1CLNPSysInstance"),
    (0, "ITOUCH-ISIS-MIB", "xIsisL1CLNPRouteMetricQOS"),
    (0, "ITOUCH-ISIS-MIB", "xIsisL1CLNPRouteDest"),
    (0, "ITOUCH-ISIS-MIB", "xIsisL1CLNPRouteForw"),
)
if mibBuilder.loadTexts:
    xIsisL1CLNPDestEntry.setStatus("mandatory")
_XIsisL1CLNPSysInstance_Type = Integer32
_XIsisL1CLNPSysInstance_Object = MibTableColumn
xIsisL1CLNPSysInstance = _XIsisL1CLNPSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 7, 1, 1, 1),
    _XIsisL1CLNPSysInstance_Type()
)
xIsisL1CLNPSysInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisL1CLNPSysInstance.setStatus("mandatory")
_XIsisL1CLNPRouteDest_Type = OctetString
_XIsisL1CLNPRouteDest_Object = MibTableColumn
xIsisL1CLNPRouteDest = _XIsisL1CLNPRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 7, 1, 1, 2),
    _XIsisL1CLNPRouteDest_Type()
)
xIsisL1CLNPRouteDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisL1CLNPRouteDest.setStatus("mandatory")


class _XIsisL1CLNPRouteMetricQOS_Type(Integer32):
    """Custom type xIsisL1CLNPRouteMetricQOS based on Integer32"""
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
        *(("default", 1),
          ("delay", 2),
          ("error", 4),
          ("expense", 3))
    )


_XIsisL1CLNPRouteMetricQOS_Type.__name__ = "Integer32"
_XIsisL1CLNPRouteMetricQOS_Object = MibTableColumn
xIsisL1CLNPRouteMetricQOS = _XIsisL1CLNPRouteMetricQOS_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 7, 1, 1, 3),
    _XIsisL1CLNPRouteMetricQOS_Type()
)
xIsisL1CLNPRouteMetricQOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisL1CLNPRouteMetricQOS.setStatus("mandatory")


class _XIsisL1CLNPRouteMetricType_Type(Integer32):
    """Custom type xIsisL1CLNPRouteMetricType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("external", 2),
          ("internal", 1))
    )


_XIsisL1CLNPRouteMetricType_Type.__name__ = "Integer32"
_XIsisL1CLNPRouteMetricType_Object = MibTableColumn
xIsisL1CLNPRouteMetricType = _XIsisL1CLNPRouteMetricType_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 7, 1, 1, 4),
    _XIsisL1CLNPRouteMetricType_Type()
)
xIsisL1CLNPRouteMetricType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisL1CLNPRouteMetricType.setStatus("mandatory")


class _XIsisL1CLNPRouteMetricValue_Type(Integer32):
    """Custom type xIsisL1CLNPRouteMetricValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_XIsisL1CLNPRouteMetricValue_Type.__name__ = "Integer32"
_XIsisL1CLNPRouteMetricValue_Object = MibTableColumn
xIsisL1CLNPRouteMetricValue = _XIsisL1CLNPRouteMetricValue_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 7, 1, 1, 5),
    _XIsisL1CLNPRouteMetricValue_Type()
)
xIsisL1CLNPRouteMetricValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisL1CLNPRouteMetricValue.setStatus("mandatory")
_XIsisL1CLNPRouteForw_Type = ObjectIdentifier
_XIsisL1CLNPRouteForw_Object = MibTableColumn
xIsisL1CLNPRouteForw = _XIsisL1CLNPRouteForw_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 7, 1, 1, 6),
    _XIsisL1CLNPRouteForw_Type()
)
xIsisL1CLNPRouteForw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisL1CLNPRouteForw.setStatus("mandatory")


class _XIsisL1CLNPRouteSource_Type(Integer32):
    """Custom type xIsisL1CLNPRouteSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("esis", 3),
          ("level1", 2),
          ("manual", 1))
    )


_XIsisL1CLNPRouteSource_Type.__name__ = "Integer32"
_XIsisL1CLNPRouteSource_Object = MibTableColumn
xIsisL1CLNPRouteSource = _XIsisL1CLNPRouteSource_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 7, 1, 1, 7),
    _XIsisL1CLNPRouteSource_Type()
)
xIsisL1CLNPRouteSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisL1CLNPRouteSource.setStatus("mandatory")
_XIsisL2CLNPDestTable_Object = MibTable
xIsisL2CLNPDestTable = _XIsisL2CLNPDestTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 7, 2)
)
if mibBuilder.loadTexts:
    xIsisL2CLNPDestTable.setStatus("mandatory")
_XIsisL2CLNPDestEntry_Object = MibTableRow
xIsisL2CLNPDestEntry = _XIsisL2CLNPDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 7, 2, 1)
)
xIsisL2CLNPDestEntry.setIndexNames(
    (0, "ITOUCH-ISIS-MIB", "xIsisL2CLNPSysInstance"),
    (0, "ITOUCH-ISIS-MIB", "xIsisL2CLNPRouteMetricQOS"),
    (0, "ITOUCH-ISIS-MIB", "xIsisL2CLNPRouteDest"),
    (0, "ITOUCH-ISIS-MIB", "xIsisL2CLNPRouteForw"),
)
if mibBuilder.loadTexts:
    xIsisL2CLNPDestEntry.setStatus("mandatory")
_XIsisL2CLNPSysInstance_Type = Integer32
_XIsisL2CLNPSysInstance_Object = MibTableColumn
xIsisL2CLNPSysInstance = _XIsisL2CLNPSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 7, 2, 1, 1),
    _XIsisL2CLNPSysInstance_Type()
)
xIsisL2CLNPSysInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisL2CLNPSysInstance.setStatus("mandatory")
_XIsisL2CLNPRouteDest_Type = OctetString
_XIsisL2CLNPRouteDest_Object = MibTableColumn
xIsisL2CLNPRouteDest = _XIsisL2CLNPRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 7, 2, 1, 2),
    _XIsisL2CLNPRouteDest_Type()
)
xIsisL2CLNPRouteDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisL2CLNPRouteDest.setStatus("mandatory")


class _XIsisL2CLNPRouteMetricQOS_Type(Integer32):
    """Custom type xIsisL2CLNPRouteMetricQOS based on Integer32"""
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
        *(("default", 1),
          ("delay", 2),
          ("error", 4),
          ("expense", 3))
    )


_XIsisL2CLNPRouteMetricQOS_Type.__name__ = "Integer32"
_XIsisL2CLNPRouteMetricQOS_Object = MibTableColumn
xIsisL2CLNPRouteMetricQOS = _XIsisL2CLNPRouteMetricQOS_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 7, 2, 1, 3),
    _XIsisL2CLNPRouteMetricQOS_Type()
)
xIsisL2CLNPRouteMetricQOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisL2CLNPRouteMetricQOS.setStatus("mandatory")


class _XIsisL2CLNPRouteMetricType_Type(Integer32):
    """Custom type xIsisL2CLNPRouteMetricType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("external", 2),
          ("internal", 1))
    )


_XIsisL2CLNPRouteMetricType_Type.__name__ = "Integer32"
_XIsisL2CLNPRouteMetricType_Object = MibTableColumn
xIsisL2CLNPRouteMetricType = _XIsisL2CLNPRouteMetricType_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 7, 2, 1, 4),
    _XIsisL2CLNPRouteMetricType_Type()
)
xIsisL2CLNPRouteMetricType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisL2CLNPRouteMetricType.setStatus("mandatory")


class _XIsisL2CLNPRouteMetricValue_Type(Integer32):
    """Custom type xIsisL2CLNPRouteMetricValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_XIsisL2CLNPRouteMetricValue_Type.__name__ = "Integer32"
_XIsisL2CLNPRouteMetricValue_Object = MibTableColumn
xIsisL2CLNPRouteMetricValue = _XIsisL2CLNPRouteMetricValue_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 7, 2, 1, 5),
    _XIsisL2CLNPRouteMetricValue_Type()
)
xIsisL2CLNPRouteMetricValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisL2CLNPRouteMetricValue.setStatus("mandatory")
_XIsisL2CLNPRouteForw_Type = ObjectIdentifier
_XIsisL2CLNPRouteForw_Object = MibTableColumn
xIsisL2CLNPRouteForw = _XIsisL2CLNPRouteForw_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 7, 2, 1, 6),
    _XIsisL2CLNPRouteForw_Type()
)
xIsisL2CLNPRouteForw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisL2CLNPRouteForw.setStatus("mandatory")


class _XIsisL2CLNPRouteSource_Type(Integer32):
    """Custom type xIsisL2CLNPRouteSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("level2", 2),
          ("manual", 1))
    )


_XIsisL2CLNPRouteSource_Type.__name__ = "Integer32"
_XIsisL2CLNPRouteSource_Object = MibTableColumn
xIsisL2CLNPRouteSource = _XIsisL2CLNPRouteSource_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 7, 2, 1, 7),
    _XIsisL2CLNPRouteSource_Type()
)
xIsisL2CLNPRouteSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisL2CLNPRouteSource.setStatus("mandatory")
_XIsisL3CLNPDestTable_Object = MibTable
xIsisL3CLNPDestTable = _XIsisL3CLNPDestTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 7, 3)
)
if mibBuilder.loadTexts:
    xIsisL3CLNPDestTable.setStatus("mandatory")
_XIsisL3CLNPDestEntry_Object = MibTableRow
xIsisL3CLNPDestEntry = _XIsisL3CLNPDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 7, 3, 1)
)
xIsisL3CLNPDestEntry.setIndexNames(
    (0, "ITOUCH-ISIS-MIB", "xIsisL3CLNPSysInstance"),
    (0, "ITOUCH-ISIS-MIB", "xIsisL3CLNPRouteMetricQOS"),
    (0, "ITOUCH-ISIS-MIB", "xIsisL3CLNPRouteDest"),
    (0, "ITOUCH-ISIS-MIB", "xIsisL3CLNPRouteForw"),
)
if mibBuilder.loadTexts:
    xIsisL3CLNPDestEntry.setStatus("mandatory")
_XIsisL3CLNPSysInstance_Type = Integer32
_XIsisL3CLNPSysInstance_Object = MibTableColumn
xIsisL3CLNPSysInstance = _XIsisL3CLNPSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 7, 3, 1, 1),
    _XIsisL3CLNPSysInstance_Type()
)
xIsisL3CLNPSysInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisL3CLNPSysInstance.setStatus("mandatory")
_XIsisL3CLNPRouteDest_Type = OctetString
_XIsisL3CLNPRouteDest_Object = MibTableColumn
xIsisL3CLNPRouteDest = _XIsisL3CLNPRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 7, 3, 1, 2),
    _XIsisL3CLNPRouteDest_Type()
)
xIsisL3CLNPRouteDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisL3CLNPRouteDest.setStatus("mandatory")


class _XIsisL3CLNPRouteMetricQOS_Type(Integer32):
    """Custom type xIsisL3CLNPRouteMetricQOS based on Integer32"""
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
        *(("default", 1),
          ("delay", 2),
          ("error", 4),
          ("expense", 3))
    )


_XIsisL3CLNPRouteMetricQOS_Type.__name__ = "Integer32"
_XIsisL3CLNPRouteMetricQOS_Object = MibTableColumn
xIsisL3CLNPRouteMetricQOS = _XIsisL3CLNPRouteMetricQOS_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 7, 3, 1, 3),
    _XIsisL3CLNPRouteMetricQOS_Type()
)
xIsisL3CLNPRouteMetricQOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisL3CLNPRouteMetricQOS.setStatus("mandatory")


class _XIsisL3CLNPRouteMetricType_Type(Integer32):
    """Custom type xIsisL3CLNPRouteMetricType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("external", 2),
          ("internal", 1))
    )


_XIsisL3CLNPRouteMetricType_Type.__name__ = "Integer32"
_XIsisL3CLNPRouteMetricType_Object = MibTableColumn
xIsisL3CLNPRouteMetricType = _XIsisL3CLNPRouteMetricType_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 7, 3, 1, 4),
    _XIsisL3CLNPRouteMetricType_Type()
)
xIsisL3CLNPRouteMetricType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisL3CLNPRouteMetricType.setStatus("mandatory")


class _XIsisL3CLNPRouteMetricValue_Type(Integer32):
    """Custom type xIsisL3CLNPRouteMetricValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_XIsisL3CLNPRouteMetricValue_Type.__name__ = "Integer32"
_XIsisL3CLNPRouteMetricValue_Object = MibTableColumn
xIsisL3CLNPRouteMetricValue = _XIsisL3CLNPRouteMetricValue_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 7, 3, 1, 5),
    _XIsisL3CLNPRouteMetricValue_Type()
)
xIsisL3CLNPRouteMetricValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisL3CLNPRouteMetricValue.setStatus("mandatory")
_XIsisL3CLNPRouteForw_Type = ObjectIdentifier
_XIsisL3CLNPRouteForw_Object = MibTableColumn
xIsisL3CLNPRouteForw = _XIsisL3CLNPRouteForw_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 7, 3, 1, 6),
    _XIsisL3CLNPRouteForw_Type()
)
xIsisL3CLNPRouteForw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisL3CLNPRouteForw.setStatus("mandatory")


class _XIsisL3CLNPRouteSource_Type(Integer32):
    """Custom type xIsisL3CLNPRouteSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("level2", 2),
          ("manual", 1))
    )


_XIsisL3CLNPRouteSource_Type.__name__ = "Integer32"
_XIsisL3CLNPRouteSource_Object = MibTableColumn
xIsisL3CLNPRouteSource = _XIsisL3CLNPRouteSource_Object(
    (1, 3, 6, 1, 4, 1, 33, 26, 7, 3, 1, 7),
    _XIsisL3CLNPRouteSource_Type()
)
xIsisL3CLNPRouteSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xIsisL3CLNPRouteSource.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ITOUCH-ISIS-MIB",
    **{"ExistState": ExistState,
       "SupportedProtocol": SupportedProtocol,
       "xIsis": xIsis,
       "xIsisSystem": xIsisSystem,
       "xIsisSysTable": xIsisSysTable,
       "xIsisSysEntry": xIsisSysEntry,
       "xIsisSysInstance": xIsisSysInstance,
       "xIsisSysExistState": xIsisSysExistState,
       "xIsisSysVersion": xIsisSysVersion,
       "xIsisSysType": xIsisSysType,
       "xIsisSysNET": xIsisSysNET,
       "xIsisSysMaxPathSplits": xIsisSysMaxPathSplits,
       "xIsisSysMinLSPTransInt": xIsisSysMinLSPTransInt,
       "xIsisSysMaxLSPGenInt": xIsisSysMaxLSPGenInt,
       "xIsisSysMinBroadLSPTransInt": xIsisSysMinBroadLSPTransInt,
       "xIsisSysCompSNPInt": xIsisSysCompSNPInt,
       "xIsisSysOrigL1LSPBuffSize": xIsisSysOrigL1LSPBuffSize,
       "xIsisSysMaxAreaAddr": xIsisSysMaxAreaAddr,
       "xIsisSysMinLSPGenInt": xIsisSysMinLSPGenInt,
       "xIsisSysPollESHelloRate": xIsisSysPollESHelloRate,
       "xIsisSysPartSNPInt": xIsisSysPartSNPInt,
       "xIsisSysWaitTime": xIsisSysWaitTime,
       "xIsisSysDRISISHelloTimer": xIsisSysDRISISHelloTimer,
       "xIsisSysOperState": xIsisSysOperState,
       "xIsisSysL1State": xIsisSysL1State,
       "xIsisSysCorrLSPs": xIsisSysCorrLSPs,
       "xIsisSysL1LSPDbaseOloads": xIsisSysL1LSPDbaseOloads,
       "xIsisSysManAddrsDropFromArea": xIsisSysManAddrsDropFromArea,
       "xIsisSysAttmptsToExMaxSeqNum": xIsisSysAttmptsToExMaxSeqNum,
       "xIsisSysSeqNumSkips": xIsisSysSeqNumSkips,
       "xIsisSysOwnLSPPurges": xIsisSysOwnLSPPurges,
       "xIsisSysIDFieldLenMismatches": xIsisSysIDFieldLenMismatches,
       "xIsisSysMaxAreaMis": xIsisSysMaxAreaMis,
       "xIsisSysOrigL2LSPBuffSize": xIsisSysOrigL2LSPBuffSize,
       "xIsisSysL2State": xIsisSysL2State,
       "xIsisSysL2LSPDbaseOloads": xIsisSysL2LSPDbaseOloads,
       "xIsisSysMaxAreaCheck": xIsisSysMaxAreaCheck,
       "xIsisManAreaAddrTable": xIsisManAreaAddrTable,
       "xIsisManAreaAddrEntry": xIsisManAreaAddrEntry,
       "xIsisManAreaAddrSysInstance": xIsisManAreaAddrSysInstance,
       "xIsisManAreaAddr": xIsisManAreaAddr,
       "xIsisManAreaAddrExistState": xIsisManAreaAddrExistState,
       "xIsisAreaAddrTable": xIsisAreaAddrTable,
       "xIsisAreaAddrEntry": xIsisAreaAddrEntry,
       "xIsisAreaAddrSysInstance": xIsisAreaAddrSysInstance,
       "xIsisAreaAddr": xIsisAreaAddr,
       "xIsisSysProtSuppTable": xIsisSysProtSuppTable,
       "xIsisSysProtSuppEntry": xIsisSysProtSuppEntry,
       "xIsisSysProtSuppSysInstance": xIsisSysProtSuppSysInstance,
       "xIsisSysProtSuppProtocol": xIsisSysProtSuppProtocol,
       "xIsisSysProtSuppExistState": xIsisSysProtSuppExistState,
       "xIsisCirc": xIsisCirc,
       "xIsisCircTable": xIsisCircTable,
       "xIsisCircEntry": xIsisCircEntry,
       "xIsisCircSysInstance": xIsisCircSysInstance,
       "xIsisCircIndex": xIsisCircIndex,
       "xIsisCircIfIndex": xIsisCircIfIndex,
       "xIsisCircOperState": xIsisCircOperState,
       "xIsisCircExistState": xIsisCircExistState,
       "xIsisCircType": xIsisCircType,
       "xIsisCircHelloTimer": xIsisCircHelloTimer,
       "xIsisCircL1DefaultMetric": xIsisCircL1DefaultMetric,
       "xIsisCircL1DelayMetric": xIsisCircL1DelayMetric,
       "xIsisCircL1ExpenseMetric": xIsisCircL1ExpenseMetric,
       "xIsisCircL1ErrorMetric": xIsisCircL1ErrorMetric,
       "xIsisCircExtDomain": xIsisCircExtDomain,
       "xIsisCircAdjChanges": xIsisCircAdjChanges,
       "xIsisCircInitFails": xIsisCircInitFails,
       "xIsisCircRejAdjs": xIsisCircRejAdjs,
       "xIsisCircOutCtrlPDUs": xIsisCircOutCtrlPDUs,
       "xIsisCircInCtrlPDUs": xIsisCircInCtrlPDUs,
       "xIsisCircIDFieldLenMismatches": xIsisCircIDFieldLenMismatches,
       "xIsisCircL2DefaultMetric": xIsisCircL2DefaultMetric,
       "xIsisCircL2DelayMetric": xIsisCircL2DelayMetric,
       "xIsisCircL2ExpenseMetric": xIsisCircL2ExpenseMetric,
       "xIsisCircL2ErrorMetric": xIsisCircL2ErrorMetric,
       "xIsisCircManL2Only": xIsisCircManL2Only,
       "xIsisCircL1ISPriority": xIsisCircL1ISPriority,
       "xIsisCircL1CircID": xIsisCircL1CircID,
       "xIsisCircL1DesIS": xIsisCircL1DesIS,
       "xIsisCircLANL1DesISChanges": xIsisCircLANL1DesISChanges,
       "xIsisCircL2ISPriority": xIsisCircL2ISPriority,
       "xIsisCircL2CircID": xIsisCircL2CircID,
       "xIsisCircL2DesIS": xIsisCircL2DesIS,
       "xIsisCircLANL2DesISChanges": xIsisCircLANL2DesISChanges,
       "xIsisCircISTable": xIsisCircISTable,
       "xIsisCircISEntry": xIsisCircISEntry,
       "xIsisCircISSysInstance": xIsisCircISSysInstance,
       "xIsisCircISIndex": xIsisCircISIndex,
       "xIsisCircISExistState": xIsisCircISExistState,
       "xIsisCircISOperState": xIsisCircISOperState,
       "xIsisCircISHoldTimerMult": xIsisCircISHoldTimerMult,
       "xIsisCircISConfTimer": xIsisCircISConfTimer,
       "xIsisCircISSuggESConfTimer": xIsisCircISSuggESConfTimer,
       "xIsisCircISRedHoldTime": xIsisCircISRedHoldTime,
       "xIsisCircISESReachChgs": xIsisCircISESReachChgs,
       "xIsisCircISInv9542PDUs": xIsisCircISInv9542PDUs,
       "xIsisCircClnsTable": xIsisCircClnsTable,
       "xIsisCircClnsEntry": xIsisCircClnsEntry,
       "xIsisCircClnsSysInstance": xIsisCircClnsSysInstance,
       "xIsisCircClnsIndex": xIsisCircClnsIndex,
       "xIsisCircClnsExistState": xIsisCircClnsExistState,
       "xIsisCircClnsOperState": xIsisCircClnsOperState,
       "xIsisCircClnsRxPDUs": xIsisCircClnsRxPDUs,
       "xIsisCircClnsTxPDUs": xIsisCircClnsTxPDUs,
       "xIsisISAdj": xIsisISAdj,
       "xIsisISAdjTable": xIsisISAdjTable,
       "xIsisISAdjEntry": xIsisISAdjEntry,
       "xIsisISAdjSysInstance": xIsisISAdjSysInstance,
       "xIsisISAdjCircIndex": xIsisISAdjCircIndex,
       "xIsisISAdjIndex": xIsisISAdjIndex,
       "xIsisISAdjState": xIsisISAdjState,
       "xIsisISAdjNeighSNPAAddress": xIsisISAdjNeighSNPAAddress,
       "xIsisISAdjNeighSysType": xIsisISAdjNeighSysType,
       "xIsisISAdjNeighSysID": xIsisISAdjNeighSysID,
       "xIsisISAdjUsage": xIsisISAdjUsage,
       "xIsisISAdjHoldTimer": xIsisISAdjHoldTimer,
       "xIsisISAdjNeighPriority": xIsisISAdjNeighPriority,
       "xIsisISAdjAreaAddrTable": xIsisISAdjAreaAddrTable,
       "xIsisISAdjAreaAddrEntry": xIsisISAdjAreaAddrEntry,
       "xIsisISAdjAreaAddrSysInstance": xIsisISAdjAreaAddrSysInstance,
       "xIsisISAdjAreaAddrCircIndex": xIsisISAdjAreaAddrCircIndex,
       "xIsisISAdjAreaAddrAdjIndex": xIsisISAdjAreaAddrAdjIndex,
       "xIsisISAdjAreaAddress": xIsisISAdjAreaAddress,
       "xIsisISAdjIPAddrTable": xIsisISAdjIPAddrTable,
       "xIsisISAdjIPAddrEntry": xIsisISAdjIPAddrEntry,
       "xIsisISAdjIPAddrSysInstance": xIsisISAdjIPAddrSysInstance,
       "xIsisISAdjIPAddrCircIndex": xIsisISAdjIPAddrCircIndex,
       "xIsisISAdjIPAddrAdjIndex": xIsisISAdjIPAddrAdjIndex,
       "xIsisISAdjIPAddress": xIsisISAdjIPAddress,
       "xIsisISAdjProtSuppTable": xIsisISAdjProtSuppTable,
       "xIsisISAdjProtSuppEntry": xIsisISAdjProtSuppEntry,
       "xIsisISAdjProtSuppSysInstance": xIsisISAdjProtSuppSysInstance,
       "xIsisISAdjProtSuppCircIndex": xIsisISAdjProtSuppCircIndex,
       "xIsisISAdjProtSuppAdjIndex": xIsisISAdjProtSuppAdjIndex,
       "xIsisISAdjProtSuppProtocol": xIsisISAdjProtSuppProtocol,
       "xIsisESAdj": xIsisESAdj,
       "xIsisESAdjTable": xIsisESAdjTable,
       "xIsisESAdjEntry": xIsisESAdjEntry,
       "xIsisESAdjSysInstance": xIsisESAdjSysInstance,
       "xIsisESAdjCircIndex": xIsisESAdjCircIndex,
       "xIsisESAdjIndex": xIsisESAdjIndex,
       "xIsisESAdjType": xIsisESAdjType,
       "xIsisESAdjState": xIsisESAdjState,
       "xIsisESAdjNeighSNPAAddress": xIsisESAdjNeighSNPAAddress,
       "xIsisESAdjExistState": xIsisESAdjExistState,
       "xIsisESAdjESID": xIsisESAdjESID,
       "xIsisReachAddr": xIsisReachAddr,
       "xIsisRATable": xIsisRATable,
       "xIsisRAEntry": xIsisRAEntry,
       "xIsisRASysInstance": xIsisRASysInstance,
       "xIsisRACircIndex": xIsisRACircIndex,
       "xIsisRAIndex": xIsisRAIndex,
       "xIsisRAExistState": xIsisRAExistState,
       "xIsisRAOperState": xIsisRAOperState,
       "xIsisRAAddrPrefix": xIsisRAAddrPrefix,
       "xIsisRAMapType": xIsisRAMapType,
       "xIsisRADefMetric": xIsisRADefMetric,
       "xIsisRADelMetric": xIsisRADelMetric,
       "xIsisRAExpMetric": xIsisRAExpMetric,
       "xIsisRAErrMetric": xIsisRAErrMetric,
       "xIsisRADefMetricType": xIsisRADefMetricType,
       "xIsisRADelMetricType": xIsisRADelMetricType,
       "xIsisRAExpMetricType": xIsisRAExpMetricType,
       "xIsisRAErrMetricType": xIsisRAErrMetricType,
       "xIsisRASNPAAddress": xIsisRASNPAAddress,
       "xIsisRASNPAMask": xIsisRASNPAMask,
       "xIsisRASNPAPrefix": xIsisRASNPAPrefix,
       "xIsisRAType": xIsisRAType,
       "xIsisCLNPDest": xIsisCLNPDest,
       "xIsisL1CLNPDestTable": xIsisL1CLNPDestTable,
       "xIsisL1CLNPDestEntry": xIsisL1CLNPDestEntry,
       "xIsisL1CLNPSysInstance": xIsisL1CLNPSysInstance,
       "xIsisL1CLNPRouteDest": xIsisL1CLNPRouteDest,
       "xIsisL1CLNPRouteMetricQOS": xIsisL1CLNPRouteMetricQOS,
       "xIsisL1CLNPRouteMetricType": xIsisL1CLNPRouteMetricType,
       "xIsisL1CLNPRouteMetricValue": xIsisL1CLNPRouteMetricValue,
       "xIsisL1CLNPRouteForw": xIsisL1CLNPRouteForw,
       "xIsisL1CLNPRouteSource": xIsisL1CLNPRouteSource,
       "xIsisL2CLNPDestTable": xIsisL2CLNPDestTable,
       "xIsisL2CLNPDestEntry": xIsisL2CLNPDestEntry,
       "xIsisL2CLNPSysInstance": xIsisL2CLNPSysInstance,
       "xIsisL2CLNPRouteDest": xIsisL2CLNPRouteDest,
       "xIsisL2CLNPRouteMetricQOS": xIsisL2CLNPRouteMetricQOS,
       "xIsisL2CLNPRouteMetricType": xIsisL2CLNPRouteMetricType,
       "xIsisL2CLNPRouteMetricValue": xIsisL2CLNPRouteMetricValue,
       "xIsisL2CLNPRouteForw": xIsisL2CLNPRouteForw,
       "xIsisL2CLNPRouteSource": xIsisL2CLNPRouteSource,
       "xIsisL3CLNPDestTable": xIsisL3CLNPDestTable,
       "xIsisL3CLNPDestEntry": xIsisL3CLNPDestEntry,
       "xIsisL3CLNPSysInstance": xIsisL3CLNPSysInstance,
       "xIsisL3CLNPRouteDest": xIsisL3CLNPRouteDest,
       "xIsisL3CLNPRouteMetricQOS": xIsisL3CLNPRouteMetricQOS,
       "xIsisL3CLNPRouteMetricType": xIsisL3CLNPRouteMetricType,
       "xIsisL3CLNPRouteMetricValue": xIsisL3CLNPRouteMetricValue,
       "xIsisL3CLNPRouteForw": xIsisL3CLNPRouteForw,
       "xIsisL3CLNPRouteSource": xIsisL3CLNPRouteSource}
)
