# SNMP MIB module (FRAMEVISIONSTD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FRAMEVISIONSTD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:46:20 2024
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



class FribDLCI(Integer32):
    """Custom type FribDLCI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483646),
    )





class Counter32(Counter32):
    """Custom type Counter32 based on Counter32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Framevisionstd_ObjectIdentity = ObjectIdentity
framevisionstd = _Framevisionstd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 181, 100, 1)
)
_FribStd_ObjectIdentity = ObjectIdentity
fribStd = _FribStd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 1)
)


class _FribMibVersion_Type(Integer32):
    """Custom type fribMibVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("version1", 1)
    )


_FribMibVersion_Type.__name__ = "Integer32"
_FribMibVersion_Object = MibScalar
fribMibVersion = _FribMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 1, 1),
    _FribMibVersion_Type()
)
fribMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fribMibVersion.setStatus("mandatory")
_FribMibLastChange_Type = TimeTicks
_FribMibLastChange_Object = MibScalar
fribMibLastChange = _FribMibLastChange_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 1, 2),
    _FribMibLastChange_Type()
)
fribMibLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fribMibLastChange.setStatus("mandatory")
_FribCfg_ObjectIdentity = ObjectIdentity
fribCfg = _FribCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 2)
)
_FribCfgTable_Object = MibTable
fribCfgTable = _FribCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 2, 1)
)
if mibBuilder.loadTexts:
    fribCfgTable.setStatus("mandatory")
_FribCfgEntry_Object = MibTableRow
fribCfgEntry = _FribCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 2, 1, 1)
)
fribCfgEntry.setIndexNames(
    (0, "FRAMEVISIONSTD-MIB", "fribCfgIfIndex"),
)
if mibBuilder.loadTexts:
    fribCfgEntry.setStatus("mandatory")
_FribCfgIfIndex_Type = Integer32
_FribCfgIfIndex_Object = MibTableColumn
fribCfgIfIndex = _FribCfgIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 2, 1, 1, 1),
    _FribCfgIfIndex_Type()
)
fribCfgIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fribCfgIfIndex.setStatus("mandatory")
_FribCfgLastChange_Type = TimeTicks
_FribCfgLastChange_Object = MibTableColumn
fribCfgLastChange = _FribCfgLastChange_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 2, 1, 1, 2),
    _FribCfgLastChange_Type()
)
fribCfgLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fribCfgLastChange.setStatus("mandatory")


class _FribCfgFrameType_Type(Integer32):
    """Custom type fribCfgFrameType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("frameTypeEther", 2),
          ("frameTypeNlpid", 1))
    )


_FribCfgFrameType_Type.__name__ = "Integer32"
_FribCfgFrameType_Object = MibTableColumn
fribCfgFrameType = _FribCfgFrameType_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 2, 1, 1, 3),
    _FribCfgFrameType_Type()
)
fribCfgFrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fribCfgFrameType.setStatus("mandatory")


class _FribCfgAddrOctets_Type(Integer32):
    """Custom type fribCfgAddrOctets based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fourOctets", 2),
          ("twoOctets", 1))
    )


_FribCfgAddrOctets_Type.__name__ = "Integer32"
_FribCfgAddrOctets_Object = MibTableColumn
fribCfgAddrOctets = _FribCfgAddrOctets_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 2, 1, 1, 4),
    _FribCfgAddrOctets_Type()
)
fribCfgAddrOctets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fribCfgAddrOctets.setStatus("mandatory")


class _FribCfgFcsBitLength_Type(Integer32):
    """Custom type fribCfgFcsBitLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("frib16BitFcs", 1),
          ("frib32BitFcs", 2))
    )


_FribCfgFcsBitLength_Type.__name__ = "Integer32"
_FribCfgFcsBitLength_Object = MibTableColumn
fribCfgFcsBitLength = _FribCfgFcsBitLength_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 2, 1, 1, 5),
    _FribCfgFcsBitLength_Type()
)
fribCfgFcsBitLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fribCfgFcsBitLength.setStatus("mandatory")
_FribCfgTimeInterval_Type = Integer32
_FribCfgTimeInterval_Object = MibTableColumn
fribCfgTimeInterval = _FribCfgTimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 2, 1, 1, 6),
    _FribCfgTimeInterval_Type()
)
fribCfgTimeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fribCfgTimeInterval.setStatus("mandatory")
_FribCfgMaxVCs_Type = Integer32
_FribCfgMaxVCs_Object = MibTableColumn
fribCfgMaxVCs = _FribCfgMaxVCs_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 2, 1, 1, 7),
    _FribCfgMaxVCs_Type()
)
fribCfgMaxVCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fribCfgMaxVCs.setStatus("mandatory")
_FribCfgNumberVCs_Type = Integer32
_FribCfgNumberVCs_Object = MibTableColumn
fribCfgNumberVCs = _FribCfgNumberVCs_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 2, 1, 1, 8),
    _FribCfgNumberVCs_Type()
)
fribCfgNumberVCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fribCfgNumberVCs.setStatus("mandatory")
_FribCfgVcAddDLCI_Type = FribDLCI
_FribCfgVcAddDLCI_Object = MibTableColumn
fribCfgVcAddDLCI = _FribCfgVcAddDLCI_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 2, 1, 1, 9),
    _FribCfgVcAddDLCI_Type()
)
fribCfgVcAddDLCI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fribCfgVcAddDLCI.setStatus("mandatory")
_FribCfgVcDelDLCI_Type = FribDLCI
_FribCfgVcDelDLCI_Object = MibTableColumn
fribCfgVcDelDLCI = _FribCfgVcDelDLCI_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 2, 1, 1, 10),
    _FribCfgVcDelDLCI_Type()
)
fribCfgVcDelDLCI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fribCfgVcDelDLCI.setStatus("mandatory")
_FribCfgVcListTable_Object = MibTable
fribCfgVcListTable = _FribCfgVcListTable_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 2, 2)
)
if mibBuilder.loadTexts:
    fribCfgVcListTable.setStatus("mandatory")
_FribCfgVcListEntry_Object = MibTableRow
fribCfgVcListEntry = _FribCfgVcListEntry_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 2, 2, 1)
)
fribCfgVcListEntry.setIndexNames(
    (0, "FRAMEVISIONSTD-MIB", "fribCfgVcListIfIndex"),
    (0, "FRAMEVISIONSTD-MIB", "fribCfgVcListDLCI"),
)
if mibBuilder.loadTexts:
    fribCfgVcListEntry.setStatus("mandatory")
_FribCfgVcListIfIndex_Type = Integer32
_FribCfgVcListIfIndex_Object = MibTableColumn
fribCfgVcListIfIndex = _FribCfgVcListIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 2, 2, 1, 1),
    _FribCfgVcListIfIndex_Type()
)
fribCfgVcListIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fribCfgVcListIfIndex.setStatus("mandatory")
_FribCfgVcListDLCI_Type = FribDLCI
_FribCfgVcListDLCI_Object = MibTableColumn
fribCfgVcListDLCI = _FribCfgVcListDLCI_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 2, 2, 1, 2),
    _FribCfgVcListDLCI_Type()
)
fribCfgVcListDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fribCfgVcListDLCI.setStatus("mandatory")
_FribCfgVcListCIR_Type = Integer32
_FribCfgVcListCIR_Object = MibTableColumn
fribCfgVcListCIR = _FribCfgVcListCIR_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 2, 2, 1, 3),
    _FribCfgVcListCIR_Type()
)
fribCfgVcListCIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fribCfgVcListCIR.setStatus("mandatory")
_FribCfgVcListEIR_Type = Integer32
_FribCfgVcListEIR_Object = MibTableColumn
fribCfgVcListEIR = _FribCfgVcListEIR_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 2, 2, 1, 4),
    _FribCfgVcListEIR_Type()
)
fribCfgVcListEIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fribCfgVcListEIR.setStatus("mandatory")
_FribCfgVcListCreationTime_Type = TimeTicks
_FribCfgVcListCreationTime_Object = MibTableColumn
fribCfgVcListCreationTime = _FribCfgVcListCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 2, 2, 1, 5),
    _FribCfgVcListCreationTime_Type()
)
fribCfgVcListCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fribCfgVcListCreationTime.setStatus("mandatory")
_FribPortMon_ObjectIdentity = ObjectIdentity
fribPortMon = _FribPortMon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 3)
)
_FribPortMonDuration_Type = TimeTicks
_FribPortMonDuration_Object = MibScalar
fribPortMonDuration = _FribPortMonDuration_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 3, 1),
    _FribPortMonDuration_Type()
)
fribPortMonDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fribPortMonDuration.setStatus("mandatory")


class _FribPortMonClearData_Type(Integer32):
    """Custom type fribPortMonClearData based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clearDataIdle", 1),
          ("clearDataStart", 2))
    )


_FribPortMonClearData_Type.__name__ = "Integer32"
_FribPortMonClearData_Object = MibScalar
fribPortMonClearData = _FribPortMonClearData_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 3, 2),
    _FribPortMonClearData_Type()
)
fribPortMonClearData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fribPortMonClearData.setStatus("mandatory")
_FribPortMonTable_Object = MibTable
fribPortMonTable = _FribPortMonTable_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 3, 3)
)
if mibBuilder.loadTexts:
    fribPortMonTable.setStatus("mandatory")
_FribPortMonEntry_Object = MibTableRow
fribPortMonEntry = _FribPortMonEntry_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 3, 3, 1)
)
fribPortMonEntry.setIndexNames(
    (0, "FRAMEVISIONSTD-MIB", "fribPortMonIfIndex"),
)
if mibBuilder.loadTexts:
    fribPortMonEntry.setStatus("mandatory")
_FribPortMonIfIndex_Type = Integer32
_FribPortMonIfIndex_Object = MibTableColumn
fribPortMonIfIndex = _FribPortMonIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 3, 3, 1, 1),
    _FribPortMonIfIndex_Type()
)
fribPortMonIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fribPortMonIfIndex.setStatus("mandatory")
_FribPortMonAvailTime_Type = TimeTicks
_FribPortMonAvailTime_Object = MibTableColumn
fribPortMonAvailTime = _FribPortMonAvailTime_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 3, 3, 1, 2),
    _FribPortMonAvailTime_Type()
)
fribPortMonAvailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fribPortMonAvailTime.setStatus("mandatory")
_FribPortMonTxFrames_Type = Counter32
_FribPortMonTxFrames_Object = MibTableColumn
fribPortMonTxFrames = _FribPortMonTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 3, 3, 1, 3),
    _FribPortMonTxFrames_Type()
)
fribPortMonTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fribPortMonTxFrames.setStatus("mandatory")
_FribPortMonRxFrames_Type = Counter32
_FribPortMonRxFrames_Object = MibTableColumn
fribPortMonRxFrames = _FribPortMonRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 3, 3, 1, 4),
    _FribPortMonRxFrames_Type()
)
fribPortMonRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fribPortMonRxFrames.setStatus("mandatory")
_FribPortMonTxOctets_Type = Counter32
_FribPortMonTxOctets_Object = MibTableColumn
fribPortMonTxOctets = _FribPortMonTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 3, 3, 1, 5),
    _FribPortMonTxOctets_Type()
)
fribPortMonTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fribPortMonTxOctets.setStatus("mandatory")
_FribPortMonRxOctets_Type = Counter32
_FribPortMonRxOctets_Object = MibTableColumn
fribPortMonRxOctets = _FribPortMonRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 3, 3, 1, 6),
    _FribPortMonRxOctets_Type()
)
fribPortMonRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fribPortMonRxOctets.setStatus("mandatory")
_FribPortMonIpMgmtTxFrames_Type = Counter32
_FribPortMonIpMgmtTxFrames_Object = MibTableColumn
fribPortMonIpMgmtTxFrames = _FribPortMonIpMgmtTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 3, 3, 1, 7),
    _FribPortMonIpMgmtTxFrames_Type()
)
fribPortMonIpMgmtTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fribPortMonIpMgmtTxFrames.setStatus("mandatory")
_FribPortMonIpMgmtRxFrames_Type = Counter32
_FribPortMonIpMgmtRxFrames_Object = MibTableColumn
fribPortMonIpMgmtRxFrames = _FribPortMonIpMgmtRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 3, 3, 1, 8),
    _FribPortMonIpMgmtRxFrames_Type()
)
fribPortMonIpMgmtRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fribPortMonIpMgmtRxFrames.setStatus("mandatory")
_FribPortMonIpMgmtTxOctets_Type = Counter32
_FribPortMonIpMgmtTxOctets_Object = MibTableColumn
fribPortMonIpMgmtTxOctets = _FribPortMonIpMgmtTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 3, 3, 1, 9),
    _FribPortMonIpMgmtTxOctets_Type()
)
fribPortMonIpMgmtTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fribPortMonIpMgmtTxOctets.setStatus("mandatory")
_FribPortMonIpMgmtRxOctets_Type = Counter32
_FribPortMonIpMgmtRxOctets_Object = MibTableColumn
fribPortMonIpMgmtRxOctets = _FribPortMonIpMgmtRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 3, 3, 1, 10),
    _FribPortMonIpMgmtRxOctets_Type()
)
fribPortMonIpMgmtRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fribPortMonIpMgmtRxOctets.setStatus("mandatory")
_FribPortMonRxInvalidHdrs_Type = Counter32
_FribPortMonRxInvalidHdrs_Object = MibTableColumn
fribPortMonRxInvalidHdrs = _FribPortMonRxInvalidHdrs_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 3, 3, 1, 11),
    _FribPortMonRxInvalidHdrs_Type()
)
fribPortMonRxInvalidHdrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fribPortMonRxInvalidHdrs.setStatus("mandatory")
_FribPortMonRxHdlcErrors_Type = Counter32
_FribPortMonRxHdlcErrors_Object = MibTableColumn
fribPortMonRxHdlcErrors = _FribPortMonRxHdlcErrors_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 3, 3, 1, 12),
    _FribPortMonRxHdlcErrors_Type()
)
fribPortMonRxHdlcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fribPortMonRxHdlcErrors.setStatus("mandatory")
_FribVcMon_ObjectIdentity = ObjectIdentity
fribVcMon = _FribVcMon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 4)
)
_FribVcStatDuration_Type = TimeTicks
_FribVcStatDuration_Object = MibScalar
fribVcStatDuration = _FribVcStatDuration_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 4, 1),
    _FribVcStatDuration_Type()
)
fribVcStatDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fribVcStatDuration.setStatus("mandatory")


class _FribVcStatClearData_Type(Integer32):
    """Custom type fribVcStatClearData based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clearDataIdle", 1),
          ("clearDataStart", 2))
    )


_FribVcStatClearData_Type.__name__ = "Integer32"
_FribVcStatClearData_Object = MibScalar
fribVcStatClearData = _FribVcStatClearData_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 4, 2),
    _FribVcStatClearData_Type()
)
fribVcStatClearData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fribVcStatClearData.setStatus("mandatory")
_FribVcStatTable_Object = MibTable
fribVcStatTable = _FribVcStatTable_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 4, 3)
)
if mibBuilder.loadTexts:
    fribVcStatTable.setStatus("mandatory")
_FribVcStatEntry_Object = MibTableRow
fribVcStatEntry = _FribVcStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 4, 3, 1)
)
fribVcStatEntry.setIndexNames(
    (0, "FRAMEVISIONSTD-MIB", "fribVcStatIfIndex"),
    (0, "FRAMEVISIONSTD-MIB", "fribVcStatDLCI"),
)
if mibBuilder.loadTexts:
    fribVcStatEntry.setStatus("mandatory")
_FribVcStatIfIndex_Type = Integer32
_FribVcStatIfIndex_Object = MibTableColumn
fribVcStatIfIndex = _FribVcStatIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 4, 3, 1, 1),
    _FribVcStatIfIndex_Type()
)
fribVcStatIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fribVcStatIfIndex.setStatus("mandatory")
_FribVcStatDLCI_Type = Integer32
_FribVcStatDLCI_Object = MibTableColumn
fribVcStatDLCI = _FribVcStatDLCI_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 4, 3, 1, 2),
    _FribVcStatDLCI_Type()
)
fribVcStatDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fribVcStatDLCI.setStatus("mandatory")
_FribVcStatTxFrames_Type = Counter32
_FribVcStatTxFrames_Object = MibTableColumn
fribVcStatTxFrames = _FribVcStatTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 4, 3, 1, 3),
    _FribVcStatTxFrames_Type()
)
fribVcStatTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fribVcStatTxFrames.setStatus("mandatory")
_FribVcStatRxFrames_Type = Counter32
_FribVcStatRxFrames_Object = MibTableColumn
fribVcStatRxFrames = _FribVcStatRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 4, 3, 1, 4),
    _FribVcStatRxFrames_Type()
)
fribVcStatRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fribVcStatRxFrames.setStatus("mandatory")
_FribVcStatTxOctets_Type = Counter32
_FribVcStatTxOctets_Object = MibTableColumn
fribVcStatTxOctets = _FribVcStatTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 4, 3, 1, 5),
    _FribVcStatTxOctets_Type()
)
fribVcStatTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fribVcStatTxOctets.setStatus("mandatory")
_FribVcStatRxOctets_Type = Counter32
_FribVcStatRxOctets_Object = MibTableColumn
fribVcStatRxOctets = _FribVcStatRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 4, 3, 1, 6),
    _FribVcStatRxOctets_Type()
)
fribVcStatRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fribVcStatRxOctets.setStatus("mandatory")
_FribVcStatTxDEs_Type = Counter32
_FribVcStatTxDEs_Object = MibTableColumn
fribVcStatTxDEs = _FribVcStatTxDEs_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 4, 3, 1, 7),
    _FribVcStatTxDEs_Type()
)
fribVcStatTxDEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fribVcStatTxDEs.setStatus("mandatory")
_FribVcStatRxDEs_Type = Counter32
_FribVcStatRxDEs_Object = MibTableColumn
fribVcStatRxDEs = _FribVcStatRxDEs_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 4, 3, 1, 8),
    _FribVcStatRxDEs_Type()
)
fribVcStatRxDEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fribVcStatRxDEs.setStatus("mandatory")
_FribVcStatTxFECNs_Type = Counter32
_FribVcStatTxFECNs_Object = MibTableColumn
fribVcStatTxFECNs = _FribVcStatTxFECNs_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 4, 3, 1, 9),
    _FribVcStatTxFECNs_Type()
)
fribVcStatTxFECNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fribVcStatTxFECNs.setStatus("mandatory")
_FribVcStatRxFECNs_Type = Counter32
_FribVcStatRxFECNs_Object = MibTableColumn
fribVcStatRxFECNs = _FribVcStatRxFECNs_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 4, 3, 1, 10),
    _FribVcStatRxFECNs_Type()
)
fribVcStatRxFECNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fribVcStatRxFECNs.setStatus("mandatory")
_FribVcStatTxBECNs_Type = Counter32
_FribVcStatTxBECNs_Object = MibTableColumn
fribVcStatTxBECNs = _FribVcStatTxBECNs_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 4, 3, 1, 11),
    _FribVcStatTxBECNs_Type()
)
fribVcStatTxBECNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fribVcStatTxBECNs.setStatus("mandatory")
_FribVcStatRxBECNs_Type = Counter32
_FribVcStatRxBECNs_Object = MibTableColumn
fribVcStatRxBECNs = _FribVcStatRxBECNs_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 4, 3, 1, 12),
    _FribVcStatRxBECNs_Type()
)
fribVcStatRxBECNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fribVcStatRxBECNs.setStatus("mandatory")
_FribVcUtilDuration_Type = TimeTicks
_FribVcUtilDuration_Object = MibScalar
fribVcUtilDuration = _FribVcUtilDuration_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 4, 4),
    _FribVcUtilDuration_Type()
)
fribVcUtilDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fribVcUtilDuration.setStatus("mandatory")


class _FribVcUtilClearData_Type(Integer32):
    """Custom type fribVcUtilClearData based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clearDataIdle", 1),
          ("clearDataStart", 2))
    )


_FribVcUtilClearData_Type.__name__ = "Integer32"
_FribVcUtilClearData_Object = MibScalar
fribVcUtilClearData = _FribVcUtilClearData_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 4, 5),
    _FribVcUtilClearData_Type()
)
fribVcUtilClearData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fribVcUtilClearData.setStatus("mandatory")
_FribVcUtilTable_Object = MibTable
fribVcUtilTable = _FribVcUtilTable_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 4, 6)
)
if mibBuilder.loadTexts:
    fribVcUtilTable.setStatus("mandatory")
_FribVcUtilEntry_Object = MibTableRow
fribVcUtilEntry = _FribVcUtilEntry_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 4, 6, 1)
)
fribVcUtilEntry.setIndexNames(
    (0, "FRAMEVISIONSTD-MIB", "fribVcUtilIfIndex"),
    (0, "FRAMEVISIONSTD-MIB", "fribVcUtilDLCI"),
)
if mibBuilder.loadTexts:
    fribVcUtilEntry.setStatus("mandatory")
_FribVcUtilIfIndex_Type = Integer32
_FribVcUtilIfIndex_Object = MibTableColumn
fribVcUtilIfIndex = _FribVcUtilIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 4, 6, 1, 1),
    _FribVcUtilIfIndex_Type()
)
fribVcUtilIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fribVcUtilIfIndex.setStatus("mandatory")
_FribVcUtilDLCI_Type = FribDLCI
_FribVcUtilDLCI_Object = MibTableColumn
fribVcUtilDLCI = _FribVcUtilDLCI_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 4, 6, 1, 2),
    _FribVcUtilDLCI_Type()
)
fribVcUtilDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fribVcUtilDLCI.setStatus("mandatory")
_FribVcUtilCirExceededTx_Type = Counter32
_FribVcUtilCirExceededTx_Object = MibTableColumn
fribVcUtilCirExceededTx = _FribVcUtilCirExceededTx_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 4, 6, 1, 3),
    _FribVcUtilCirExceededTx_Type()
)
fribVcUtilCirExceededTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fribVcUtilCirExceededTx.setStatus("mandatory")
_FribVcUtilCirOctetsExceededTx_Type = Counter32
_FribVcUtilCirOctetsExceededTx_Object = MibTableColumn
fribVcUtilCirOctetsExceededTx = _FribVcUtilCirOctetsExceededTx_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 4, 6, 1, 4),
    _FribVcUtilCirOctetsExceededTx_Type()
)
fribVcUtilCirOctetsExceededTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fribVcUtilCirOctetsExceededTx.setStatus("mandatory")
_FribVcUtilEirExceededTx_Type = Counter32
_FribVcUtilEirExceededTx_Object = MibTableColumn
fribVcUtilEirExceededTx = _FribVcUtilEirExceededTx_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 4, 6, 1, 5),
    _FribVcUtilEirExceededTx_Type()
)
fribVcUtilEirExceededTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fribVcUtilEirExceededTx.setStatus("mandatory")
_FribVcUtilEirOctetsExceededTx_Type = Counter32
_FribVcUtilEirOctetsExceededTx_Object = MibTableColumn
fribVcUtilEirOctetsExceededTx = _FribVcUtilEirOctetsExceededTx_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 4, 6, 1, 6),
    _FribVcUtilEirOctetsExceededTx_Type()
)
fribVcUtilEirOctetsExceededTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fribVcUtilEirOctetsExceededTx.setStatus("mandatory")
_FribFrlm_ObjectIdentity = ObjectIdentity
fribFrlm = _FribFrlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 5)
)
_FribFrlmCfgTable_Object = MibTable
fribFrlmCfgTable = _FribFrlmCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 5, 1)
)
if mibBuilder.loadTexts:
    fribFrlmCfgTable.setStatus("mandatory")
_FribFrlmCfgEntry_Object = MibTableRow
fribFrlmCfgEntry = _FribFrlmCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 5, 1, 1)
)
fribFrlmCfgEntry.setIndexNames(
    (0, "FRAMEVISIONSTD-MIB", "fribFrlmCfgIfIndex"),
)
if mibBuilder.loadTexts:
    fribFrlmCfgEntry.setStatus("mandatory")
_FribFrlmCfgIfIndex_Type = Integer32
_FribFrlmCfgIfIndex_Object = MibTableColumn
fribFrlmCfgIfIndex = _FribFrlmCfgIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 5, 1, 1, 1),
    _FribFrlmCfgIfIndex_Type()
)
fribFrlmCfgIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fribFrlmCfgIfIndex.setStatus("mandatory")
_FribFrlmCfgLastChange_Type = TimeTicks
_FribFrlmCfgLastChange_Object = MibTableColumn
fribFrlmCfgLastChange = _FribFrlmCfgLastChange_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 5, 1, 1, 2),
    _FribFrlmCfgLastChange_Type()
)
fribFrlmCfgLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fribFrlmCfgLastChange.setStatus("mandatory")


class _FribFrlmCfgProtocol_Type(Integer32):
    """Custom type fribFrlmCfgProtocol based on Integer32"""
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
        *(("ansiT1617D", 3),
          ("ccittQ933A", 4),
          ("lmi", 2),
          ("none", 1))
    )


_FribFrlmCfgProtocol_Type.__name__ = "Integer32"
_FribFrlmCfgProtocol_Object = MibTableColumn
fribFrlmCfgProtocol = _FribFrlmCfgProtocol_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 5, 1, 1, 3),
    _FribFrlmCfgProtocol_Type()
)
fribFrlmCfgProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fribFrlmCfgProtocol.setStatus("mandatory")


class _FribFrlmCfgSpoofing_Type(Integer32):
    """Custom type fribFrlmCfgSpoofing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("spoofingDisabled", 2),
          ("spoofingEnabled", 1))
    )


_FribFrlmCfgSpoofing_Type.__name__ = "Integer32"
_FribFrlmCfgSpoofing_Object = MibTableColumn
fribFrlmCfgSpoofing = _FribFrlmCfgSpoofing_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 5, 1, 1, 4),
    _FribFrlmCfgSpoofing_Type()
)
fribFrlmCfgSpoofing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fribFrlmCfgSpoofing.setStatus("mandatory")


class _FribFrlmCfgT391_Type(Integer32):
    """Custom type fribFrlmCfgT391 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_FribFrlmCfgT391_Type.__name__ = "Integer32"
_FribFrlmCfgT391_Object = MibTableColumn
fribFrlmCfgT391 = _FribFrlmCfgT391_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 5, 1, 1, 5),
    _FribFrlmCfgT391_Type()
)
fribFrlmCfgT391.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fribFrlmCfgT391.setStatus("mandatory")


class _FribFrlmCfgN392_Type(Integer32):
    """Custom type fribFrlmCfgN392 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FribFrlmCfgN392_Type.__name__ = "Integer32"
_FribFrlmCfgN392_Object = MibTableColumn
fribFrlmCfgN392 = _FribFrlmCfgN392_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 5, 1, 1, 6),
    _FribFrlmCfgN392_Type()
)
fribFrlmCfgN392.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fribFrlmCfgN392.setStatus("mandatory")


class _FribFrlmCfgN393_Type(Integer32):
    """Custom type fribFrlmCfgN393 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FribFrlmCfgN393_Type.__name__ = "Integer32"
_FribFrlmCfgN393_Object = MibTableColumn
fribFrlmCfgN393 = _FribFrlmCfgN393_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 5, 1, 1, 7),
    _FribFrlmCfgN393_Type()
)
fribFrlmCfgN393.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fribFrlmCfgN393.setStatus("mandatory")


class _FribFrlmCfgSpoofingStatus_Type(Integer32):
    """Custom type fribFrlmCfgSpoofingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("spoofingActive", 2),
          ("spoofingInactive", 1))
    )


_FribFrlmCfgSpoofingStatus_Type.__name__ = "Integer32"
_FribFrlmCfgSpoofingStatus_Object = MibTableColumn
fribFrlmCfgSpoofingStatus = _FribFrlmCfgSpoofingStatus_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 5, 1, 1, 8),
    _FribFrlmCfgSpoofingStatus_Type()
)
fribFrlmCfgSpoofingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fribFrlmCfgSpoofingStatus.setStatus("mandatory")
_FribFrlmPortDuration_Type = TimeTicks
_FribFrlmPortDuration_Object = MibScalar
fribFrlmPortDuration = _FribFrlmPortDuration_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 5, 2),
    _FribFrlmPortDuration_Type()
)
fribFrlmPortDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fribFrlmPortDuration.setStatus("mandatory")


class _FribFrlmPortClearData_Type(Integer32):
    """Custom type fribFrlmPortClearData based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clearDataIdle", 1),
          ("clearDataStart", 2))
    )


_FribFrlmPortClearData_Type.__name__ = "Integer32"
_FribFrlmPortClearData_Object = MibScalar
fribFrlmPortClearData = _FribFrlmPortClearData_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 5, 3),
    _FribFrlmPortClearData_Type()
)
fribFrlmPortClearData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fribFrlmPortClearData.setStatus("mandatory")
_FribFrlmPortTable_Object = MibTable
fribFrlmPortTable = _FribFrlmPortTable_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 5, 4)
)
if mibBuilder.loadTexts:
    fribFrlmPortTable.setStatus("mandatory")
_FribFrlmPortEntry_Object = MibTableRow
fribFrlmPortEntry = _FribFrlmPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 5, 4, 1)
)
fribFrlmPortEntry.setIndexNames(
    (0, "FRAMEVISIONSTD-MIB", "fribFrlmPortIfIndex"),
)
if mibBuilder.loadTexts:
    fribFrlmPortEntry.setStatus("mandatory")
_FribFrlmPortIfIndex_Type = Integer32
_FribFrlmPortIfIndex_Object = MibTableColumn
fribFrlmPortIfIndex = _FribFrlmPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 5, 4, 1, 1),
    _FribFrlmPortIfIndex_Type()
)
fribFrlmPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fribFrlmPortIfIndex.setStatus("mandatory")
_FribFrlmPortSendSeqNumTx_Type = Counter32
_FribFrlmPortSendSeqNumTx_Object = MibTableColumn
fribFrlmPortSendSeqNumTx = _FribFrlmPortSendSeqNumTx_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 5, 4, 1, 2),
    _FribFrlmPortSendSeqNumTx_Type()
)
fribFrlmPortSendSeqNumTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fribFrlmPortSendSeqNumTx.setStatus("mandatory")
_FribFrlmPortSendSeqNumRx_Type = Counter32
_FribFrlmPortSendSeqNumRx_Object = MibTableColumn
fribFrlmPortSendSeqNumRx = _FribFrlmPortSendSeqNumRx_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 5, 4, 1, 3),
    _FribFrlmPortSendSeqNumRx_Type()
)
fribFrlmPortSendSeqNumRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fribFrlmPortSendSeqNumRx.setStatus("mandatory")
_FribFrlmPortReceiveSeqNumTx_Type = Counter32
_FribFrlmPortReceiveSeqNumTx_Object = MibTableColumn
fribFrlmPortReceiveSeqNumTx = _FribFrlmPortReceiveSeqNumTx_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 5, 4, 1, 4),
    _FribFrlmPortReceiveSeqNumTx_Type()
)
fribFrlmPortReceiveSeqNumTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fribFrlmPortReceiveSeqNumTx.setStatus("mandatory")
_FribFrlmPortReceiveSeqNumRx_Type = Counter32
_FribFrlmPortReceiveSeqNumRx_Object = MibTableColumn
fribFrlmPortReceiveSeqNumRx = _FribFrlmPortReceiveSeqNumRx_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 5, 4, 1, 5),
    _FribFrlmPortReceiveSeqNumRx_Type()
)
fribFrlmPortReceiveSeqNumRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fribFrlmPortReceiveSeqNumRx.setStatus("mandatory")
_FribFrlmPortStatusRsp_Type = Counter32
_FribFrlmPortStatusRsp_Object = MibTableColumn
fribFrlmPortStatusRsp = _FribFrlmPortStatusRsp_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 5, 4, 1, 6),
    _FribFrlmPortStatusRsp_Type()
)
fribFrlmPortStatusRsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fribFrlmPortStatusRsp.setStatus("mandatory")
_FribFrlmPortStatusRspMissed_Type = Counter32
_FribFrlmPortStatusRspMissed_Object = MibTableColumn
fribFrlmPortStatusRspMissed = _FribFrlmPortStatusRspMissed_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 5, 4, 1, 7),
    _FribFrlmPortStatusRspMissed_Type()
)
fribFrlmPortStatusRspMissed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fribFrlmPortStatusRspMissed.setStatus("mandatory")
_FribFrlmPortStatusRspSpoofed_Type = Counter32
_FribFrlmPortStatusRspSpoofed_Object = MibTableColumn
fribFrlmPortStatusRspSpoofed = _FribFrlmPortStatusRspSpoofed_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 5, 4, 1, 8),
    _FribFrlmPortStatusRspSpoofed_Type()
)
fribFrlmPortStatusRspSpoofed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fribFrlmPortStatusRspSpoofed.setStatus("mandatory")
_FribFrlmPortStatusFullRsp_Type = Counter32
_FribFrlmPortStatusFullRsp_Object = MibTableColumn
fribFrlmPortStatusFullRsp = _FribFrlmPortStatusFullRsp_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 5, 4, 1, 9),
    _FribFrlmPortStatusFullRsp_Type()
)
fribFrlmPortStatusFullRsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fribFrlmPortStatusFullRsp.setStatus("mandatory")
_FribFrlmPortStatusFullRspMissed_Type = Counter32
_FribFrlmPortStatusFullRspMissed_Object = MibTableColumn
fribFrlmPortStatusFullRspMissed = _FribFrlmPortStatusFullRspMissed_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 5, 4, 1, 10),
    _FribFrlmPortStatusFullRspMissed_Type()
)
fribFrlmPortStatusFullRspMissed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fribFrlmPortStatusFullRspMissed.setStatus("mandatory")
_FribFrlmPortStatusFullRspSpoofed_Type = Counter32
_FribFrlmPortStatusFullRspSpoofed_Object = MibTableColumn
fribFrlmPortStatusFullRspSpoofed = _FribFrlmPortStatusFullRspSpoofed_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 5, 4, 1, 11),
    _FribFrlmPortStatusFullRspSpoofed_Type()
)
fribFrlmPortStatusFullRspSpoofed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fribFrlmPortStatusFullRspSpoofed.setStatus("mandatory")
_FribFrlmStatusDuration_Type = TimeTicks
_FribFrlmStatusDuration_Object = MibScalar
fribFrlmStatusDuration = _FribFrlmStatusDuration_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 5, 5),
    _FribFrlmStatusDuration_Type()
)
fribFrlmStatusDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fribFrlmStatusDuration.setStatus("mandatory")


class _FribFrlmStatusClearData_Type(Integer32):
    """Custom type fribFrlmStatusClearData based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clearDataIdle", 1),
          ("clearDataStart", 2))
    )


_FribFrlmStatusClearData_Type.__name__ = "Integer32"
_FribFrlmStatusClearData_Object = MibScalar
fribFrlmStatusClearData = _FribFrlmStatusClearData_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 5, 6),
    _FribFrlmStatusClearData_Type()
)
fribFrlmStatusClearData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fribFrlmStatusClearData.setStatus("mandatory")
_FribFrlmStatusTable_Object = MibTable
fribFrlmStatusTable = _FribFrlmStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 5, 7)
)
if mibBuilder.loadTexts:
    fribFrlmStatusTable.setStatus("mandatory")
_FribFrlmStatusEntry_Object = MibTableRow
fribFrlmStatusEntry = _FribFrlmStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 5, 7, 1)
)
fribFrlmStatusEntry.setIndexNames(
    (0, "FRAMEVISIONSTD-MIB", "fribVcUtilIfIndex"),
    (0, "FRAMEVISIONSTD-MIB", "fribVcUtilDLCI"),
)
if mibBuilder.loadTexts:
    fribFrlmStatusEntry.setStatus("mandatory")
_FribFrlmStatusIfIndex_Type = Integer32
_FribFrlmStatusIfIndex_Object = MibTableColumn
fribFrlmStatusIfIndex = _FribFrlmStatusIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 5, 7, 1, 1),
    _FribFrlmStatusIfIndex_Type()
)
fribFrlmStatusIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fribFrlmStatusIfIndex.setStatus("mandatory")
_FribFrlmStatusDLCI_Type = FribDLCI
_FribFrlmStatusDLCI_Object = MibTableColumn
fribFrlmStatusDLCI = _FribFrlmStatusDLCI_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 5, 7, 1, 2),
    _FribFrlmStatusDLCI_Type()
)
fribFrlmStatusDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fribFrlmStatusDLCI.setStatus("mandatory")


class _FribFrlmStatusStatus_Type(Integer32):
    """Custom type fribFrlmStatusStatus based on Integer32"""
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
        *(("frlmStatusActive", 3),
          ("frlmStatusDelete", 2),
          ("frlmStatusInactive", 4),
          ("frlmStatusNew", 1),
          ("frlmStatusSpoofed", 5))
    )


_FribFrlmStatusStatus_Type.__name__ = "Integer32"
_FribFrlmStatusStatus_Object = MibTableColumn
fribFrlmStatusStatus = _FribFrlmStatusStatus_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 5, 7, 1, 3),
    _FribFrlmStatusStatus_Type()
)
fribFrlmStatusStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fribFrlmStatusStatus.setStatus("mandatory")
_FribFrlmStatusDownEvents_Type = Counter32
_FribFrlmStatusDownEvents_Object = MibTableColumn
fribFrlmStatusDownEvents = _FribFrlmStatusDownEvents_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 5, 7, 1, 4),
    _FribFrlmStatusDownEvents_Type()
)
fribFrlmStatusDownEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fribFrlmStatusDownEvents.setStatus("mandatory")
_FribFrlmStatusActiveSecs_Type = Counter32
_FribFrlmStatusActiveSecs_Object = MibTableColumn
fribFrlmStatusActiveSecs = _FribFrlmStatusActiveSecs_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 5, 7, 1, 5),
    _FribFrlmStatusActiveSecs_Type()
)
fribFrlmStatusActiveSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fribFrlmStatusActiveSecs.setStatus("mandatory")
_FribFrlmStatusTotalSecs_Type = Counter32
_FribFrlmStatusTotalSecs_Object = MibTableColumn
fribFrlmStatusTotalSecs = _FribFrlmStatusTotalSecs_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 1, 5, 7, 1, 6),
    _FribFrlmStatusTotalSecs_Type()
)
fribFrlmStatusTotalSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fribFrlmStatusTotalSecs.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FRAMEVISIONSTD-MIB",
    **{"FribDLCI": FribDLCI,
       "Counter32": Counter32,
       "framevisionstd": framevisionstd,
       "fribStd": fribStd,
       "fribMibVersion": fribMibVersion,
       "fribMibLastChange": fribMibLastChange,
       "fribCfg": fribCfg,
       "fribCfgTable": fribCfgTable,
       "fribCfgEntry": fribCfgEntry,
       "fribCfgIfIndex": fribCfgIfIndex,
       "fribCfgLastChange": fribCfgLastChange,
       "fribCfgFrameType": fribCfgFrameType,
       "fribCfgAddrOctets": fribCfgAddrOctets,
       "fribCfgFcsBitLength": fribCfgFcsBitLength,
       "fribCfgTimeInterval": fribCfgTimeInterval,
       "fribCfgMaxVCs": fribCfgMaxVCs,
       "fribCfgNumberVCs": fribCfgNumberVCs,
       "fribCfgVcAddDLCI": fribCfgVcAddDLCI,
       "fribCfgVcDelDLCI": fribCfgVcDelDLCI,
       "fribCfgVcListTable": fribCfgVcListTable,
       "fribCfgVcListEntry": fribCfgVcListEntry,
       "fribCfgVcListIfIndex": fribCfgVcListIfIndex,
       "fribCfgVcListDLCI": fribCfgVcListDLCI,
       "fribCfgVcListCIR": fribCfgVcListCIR,
       "fribCfgVcListEIR": fribCfgVcListEIR,
       "fribCfgVcListCreationTime": fribCfgVcListCreationTime,
       "fribPortMon": fribPortMon,
       "fribPortMonDuration": fribPortMonDuration,
       "fribPortMonClearData": fribPortMonClearData,
       "fribPortMonTable": fribPortMonTable,
       "fribPortMonEntry": fribPortMonEntry,
       "fribPortMonIfIndex": fribPortMonIfIndex,
       "fribPortMonAvailTime": fribPortMonAvailTime,
       "fribPortMonTxFrames": fribPortMonTxFrames,
       "fribPortMonRxFrames": fribPortMonRxFrames,
       "fribPortMonTxOctets": fribPortMonTxOctets,
       "fribPortMonRxOctets": fribPortMonRxOctets,
       "fribPortMonIpMgmtTxFrames": fribPortMonIpMgmtTxFrames,
       "fribPortMonIpMgmtRxFrames": fribPortMonIpMgmtRxFrames,
       "fribPortMonIpMgmtTxOctets": fribPortMonIpMgmtTxOctets,
       "fribPortMonIpMgmtRxOctets": fribPortMonIpMgmtRxOctets,
       "fribPortMonRxInvalidHdrs": fribPortMonRxInvalidHdrs,
       "fribPortMonRxHdlcErrors": fribPortMonRxHdlcErrors,
       "fribVcMon": fribVcMon,
       "fribVcStatDuration": fribVcStatDuration,
       "fribVcStatClearData": fribVcStatClearData,
       "fribVcStatTable": fribVcStatTable,
       "fribVcStatEntry": fribVcStatEntry,
       "fribVcStatIfIndex": fribVcStatIfIndex,
       "fribVcStatDLCI": fribVcStatDLCI,
       "fribVcStatTxFrames": fribVcStatTxFrames,
       "fribVcStatRxFrames": fribVcStatRxFrames,
       "fribVcStatTxOctets": fribVcStatTxOctets,
       "fribVcStatRxOctets": fribVcStatRxOctets,
       "fribVcStatTxDEs": fribVcStatTxDEs,
       "fribVcStatRxDEs": fribVcStatRxDEs,
       "fribVcStatTxFECNs": fribVcStatTxFECNs,
       "fribVcStatRxFECNs": fribVcStatRxFECNs,
       "fribVcStatTxBECNs": fribVcStatTxBECNs,
       "fribVcStatRxBECNs": fribVcStatRxBECNs,
       "fribVcUtilDuration": fribVcUtilDuration,
       "fribVcUtilClearData": fribVcUtilClearData,
       "fribVcUtilTable": fribVcUtilTable,
       "fribVcUtilEntry": fribVcUtilEntry,
       "fribVcUtilIfIndex": fribVcUtilIfIndex,
       "fribVcUtilDLCI": fribVcUtilDLCI,
       "fribVcUtilCirExceededTx": fribVcUtilCirExceededTx,
       "fribVcUtilCirOctetsExceededTx": fribVcUtilCirOctetsExceededTx,
       "fribVcUtilEirExceededTx": fribVcUtilEirExceededTx,
       "fribVcUtilEirOctetsExceededTx": fribVcUtilEirOctetsExceededTx,
       "fribFrlm": fribFrlm,
       "fribFrlmCfgTable": fribFrlmCfgTable,
       "fribFrlmCfgEntry": fribFrlmCfgEntry,
       "fribFrlmCfgIfIndex": fribFrlmCfgIfIndex,
       "fribFrlmCfgLastChange": fribFrlmCfgLastChange,
       "fribFrlmCfgProtocol": fribFrlmCfgProtocol,
       "fribFrlmCfgSpoofing": fribFrlmCfgSpoofing,
       "fribFrlmCfgT391": fribFrlmCfgT391,
       "fribFrlmCfgN392": fribFrlmCfgN392,
       "fribFrlmCfgN393": fribFrlmCfgN393,
       "fribFrlmCfgSpoofingStatus": fribFrlmCfgSpoofingStatus,
       "fribFrlmPortDuration": fribFrlmPortDuration,
       "fribFrlmPortClearData": fribFrlmPortClearData,
       "fribFrlmPortTable": fribFrlmPortTable,
       "fribFrlmPortEntry": fribFrlmPortEntry,
       "fribFrlmPortIfIndex": fribFrlmPortIfIndex,
       "fribFrlmPortSendSeqNumTx": fribFrlmPortSendSeqNumTx,
       "fribFrlmPortSendSeqNumRx": fribFrlmPortSendSeqNumRx,
       "fribFrlmPortReceiveSeqNumTx": fribFrlmPortReceiveSeqNumTx,
       "fribFrlmPortReceiveSeqNumRx": fribFrlmPortReceiveSeqNumRx,
       "fribFrlmPortStatusRsp": fribFrlmPortStatusRsp,
       "fribFrlmPortStatusRspMissed": fribFrlmPortStatusRspMissed,
       "fribFrlmPortStatusRspSpoofed": fribFrlmPortStatusRspSpoofed,
       "fribFrlmPortStatusFullRsp": fribFrlmPortStatusFullRsp,
       "fribFrlmPortStatusFullRspMissed": fribFrlmPortStatusFullRspMissed,
       "fribFrlmPortStatusFullRspSpoofed": fribFrlmPortStatusFullRspSpoofed,
       "fribFrlmStatusDuration": fribFrlmStatusDuration,
       "fribFrlmStatusClearData": fribFrlmStatusClearData,
       "fribFrlmStatusTable": fribFrlmStatusTable,
       "fribFrlmStatusEntry": fribFrlmStatusEntry,
       "fribFrlmStatusIfIndex": fribFrlmStatusIfIndex,
       "fribFrlmStatusDLCI": fribFrlmStatusDLCI,
       "fribFrlmStatusStatus": fribFrlmStatusStatus,
       "fribFrlmStatusDownEvents": fribFrlmStatusDownEvents,
       "fribFrlmStatusActiveSecs": fribFrlmStatusActiveSecs,
       "fribFrlmStatusTotalSecs": fribFrlmStatusTotalSecs}
)
