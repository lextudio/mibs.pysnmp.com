# SNMP MIB module (ACC-FLASH) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACC-FLASH
# Produced by pysmi-1.5.4 at Mon Oct 14 20:32:15 2024
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

(DisplayString,
 IfIndex,
 RowStatus,
 SmdsAddress,
 accBRG) = mibBuilder.importSymbols(
    "ACC-MIB",
    "DisplayString",
    "IfIndex",
    "RowStatus",
    "SmdsAddress",
    "accBRG")

(accTrapLogSeqNum,) = mibBuilder.importSymbols(
    "ACC-SYSTEM",
    "accTrapLogSeqNum")

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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AccBridge_ObjectIdentity = ObjectIdentity
accBridge = _AccBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4)
)


class _AccBrFdbTimeout_Type(Integer32):
    """Custom type accBrFdbTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 65535),
    )


_AccBrFdbTimeout_Type.__name__ = "Integer32"
_AccBrFdbTimeout_Object = MibScalar
accBrFdbTimeout = _AccBrFdbTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 1),
    _AccBrFdbTimeout_Type()
)
accBrFdbTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBrFdbTimeout.setStatus("mandatory")


class _AccBrFdbLearnMode_Type(Integer32):
    """Custom type accBrFdbLearnMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_AccBrFdbLearnMode_Type.__name__ = "Integer32"
_AccBrFdbLearnMode_Object = MibScalar
accBrFdbLearnMode = _AccBrFdbLearnMode_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 2),
    _AccBrFdbLearnMode_Type()
)
accBrFdbLearnMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBrFdbLearnMode.setStatus("mandatory")
_AccBrFdbRamCurrSize_Type = Integer32
_AccBrFdbRamCurrSize_Object = MibScalar
accBrFdbRamCurrSize = _AccBrFdbRamCurrSize_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 3),
    _AccBrFdbRamCurrSize_Type()
)
accBrFdbRamCurrSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBrFdbRamCurrSize.setStatus("mandatory")


class _AccBrFdbRamMaxSize_Type(Integer32):
    """Custom type accBrFdbRamMaxSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 1024),
    )


_AccBrFdbRamMaxSize_Type.__name__ = "Integer32"
_AccBrFdbRamMaxSize_Object = MibScalar
accBrFdbRamMaxSize = _AccBrFdbRamMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 5),
    _AccBrFdbRamMaxSize_Type()
)
accBrFdbRamMaxSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBrFdbRamMaxSize.setStatus("mandatory")
_AccBrFdbNvmMaxSize_Type = Integer32
_AccBrFdbNvmMaxSize_Object = MibScalar
accBrFdbNvmMaxSize = _AccBrFdbNvmMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 6),
    _AccBrFdbNvmMaxSize_Type()
)
accBrFdbNvmMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBrFdbNvmMaxSize.setStatus("mandatory")
_AccBrFdbTable_Object = MibTable
accBrFdbTable = _AccBrFdbTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 7)
)
if mibBuilder.loadTexts:
    accBrFdbTable.setStatus("mandatory")
_AccBrFdbEntry_Object = MibTableRow
accBrFdbEntry = _AccBrFdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 7, 1)
)
accBrFdbEntry.setIndexNames(
    (0, "ACC-FLASH", "accBrFdbEntMacAddr"),
)
if mibBuilder.loadTexts:
    accBrFdbEntry.setStatus("mandatory")
_AccBrFdbEntMacAddr_Type = OctetString
_AccBrFdbEntMacAddr_Object = MibTableColumn
accBrFdbEntMacAddr = _AccBrFdbEntMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 7, 1, 1),
    _AccBrFdbEntMacAddr_Type()
)
accBrFdbEntMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBrFdbEntMacAddr.setStatus("mandatory")


class _AccBrFdbEntDisp_Type(Integer32):
    """Custom type accBrFdbEntDisp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discard", 2),
          ("flood", 1),
          ("forward", 0))
    )


_AccBrFdbEntDisp_Type.__name__ = "Integer32"
_AccBrFdbEntDisp_Object = MibTableColumn
accBrFdbEntDisp = _AccBrFdbEntDisp_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 7, 1, 2),
    _AccBrFdbEntDisp_Type()
)
accBrFdbEntDisp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBrFdbEntDisp.setStatus("mandatory")
_AccBrFdbEntPort_Type = Integer32
_AccBrFdbEntPort_Object = MibTableColumn
accBrFdbEntPort = _AccBrFdbEntPort_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 7, 1, 3),
    _AccBrFdbEntPort_Type()
)
accBrFdbEntPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBrFdbEntPort.setStatus("mandatory")
_AccBrFdbEntTimer_Type = Integer32
_AccBrFdbEntTimer_Object = MibTableColumn
accBrFdbEntTimer = _AccBrFdbEntTimer_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 7, 1, 4),
    _AccBrFdbEntTimer_Type()
)
accBrFdbEntTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBrFdbEntTimer.setStatus("mandatory")
_AccBrFpTable_Object = MibTable
accBrFpTable = _AccBrFpTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 8)
)
if mibBuilder.loadTexts:
    accBrFpTable.setStatus("mandatory")
_AccBrFpEntry_Object = MibTableRow
accBrFpEntry = _AccBrFpEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 8, 1)
)
accBrFpEntry.setIndexNames(
    (0, "ACC-FLASH", "accBrFpIndex"),
)
if mibBuilder.loadTexts:
    accBrFpEntry.setStatus("mandatory")
_AccBrFpIndex_Type = Integer32
_AccBrFpIndex_Object = MibTableColumn
accBrFpIndex = _AccBrFpIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 8, 1, 1),
    _AccBrFpIndex_Type()
)
accBrFpIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBrFpIndex.setStatus("mandatory")


class _AccBrFpProt_Type(Integer32):
    """Custom type accBrFpProt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AccBrFpProt_Type.__name__ = "Integer32"
_AccBrFpProt_Object = MibTableColumn
accBrFpProt = _AccBrFpProt_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 8, 1, 2),
    _AccBrFpProt_Type()
)
accBrFpProt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBrFpProt.setStatus("mandatory")


class _AccBrFpPrio_Type(Integer32):
    """Custom type accBrFpPrio based on Integer32"""
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
        *(("discard", 0),
          ("high", 3),
          ("low", 1),
          ("normal", 2))
    )


_AccBrFpPrio_Type.__name__ = "Integer32"
_AccBrFpPrio_Object = MibTableColumn
accBrFpPrio = _AccBrFpPrio_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 8, 1, 3),
    _AccBrFpPrio_Type()
)
accBrFpPrio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBrFpPrio.setStatus("mandatory")


class _AccBrFpPriDefault_Type(Integer32):
    """Custom type accBrFpPriDefault based on Integer32"""
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
        *(("discard", 0),
          ("high", 3),
          ("low", 1),
          ("normal", 2))
    )


_AccBrFpPriDefault_Type.__name__ = "Integer32"
_AccBrFpPriDefault_Object = MibScalar
accBrFpPriDefault = _AccBrFpPriDefault_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 9),
    _AccBrFpPriDefault_Type()
)
accBrFpPriDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBrFpPriDefault.setStatus("mandatory")


class _AccBrNumPorts_Type(Integer32):
    """Custom type accBrNumPorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 16),
    )


_AccBrNumPorts_Type.__name__ = "Integer32"
_AccBrNumPorts_Object = MibScalar
accBrNumPorts = _AccBrNumPorts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 10),
    _AccBrNumPorts_Type()
)
accBrNumPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBrNumPorts.setStatus("mandatory")


class _AccBrCompress_Type(Integer32):
    """Custom type accBrCompress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_AccBrCompress_Type.__name__ = "Integer32"
_AccBrCompress_Object = MibScalar
accBrCompress = _AccBrCompress_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 11),
    _AccBrCompress_Type()
)
accBrCompress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBrCompress.setStatus("mandatory")
_AccBrPortFRTable_Object = MibTable
accBrPortFRTable = _AccBrPortFRTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 13)
)
if mibBuilder.loadTexts:
    accBrPortFRTable.setStatus("mandatory")
_AccBrPortFREntry_Object = MibTableRow
accBrPortFREntry = _AccBrPortFREntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 13, 1)
)
accBrPortFREntry.setIndexNames(
    (0, "ACC-FLASH", "accBrPortFRport"),
)
if mibBuilder.loadTexts:
    accBrPortFREntry.setStatus("mandatory")
_AccBrPortFRport_Type = Integer32
_AccBrPortFRport_Object = MibTableColumn
accBrPortFRport = _AccBrPortFRport_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 13, 1, 1),
    _AccBrPortFRport_Type()
)
accBrPortFRport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBrPortFRport.setStatus("mandatory")
_AccBrPortFRdlci_Type = Integer32
_AccBrPortFRdlci_Object = MibTableColumn
accBrPortFRdlci = _AccBrPortFRdlci_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 13, 1, 2),
    _AccBrPortFRdlci_Type()
)
accBrPortFRdlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBrPortFRdlci.setStatus("mandatory")
_AccBrPortX25Table_Object = MibTable
accBrPortX25Table = _AccBrPortX25Table_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 14)
)
if mibBuilder.loadTexts:
    accBrPortX25Table.setStatus("mandatory")
_AccBrPortX25Entry_Object = MibTableRow
accBrPortX25Entry = _AccBrPortX25Entry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 14, 1)
)
accBrPortX25Entry.setIndexNames(
    (0, "ACC-FLASH", "accBrPortX25port"),
)
if mibBuilder.loadTexts:
    accBrPortX25Entry.setStatus("mandatory")
_AccBrPortX25port_Type = Integer32
_AccBrPortX25port_Object = MibTableColumn
accBrPortX25port = _AccBrPortX25port_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 14, 1, 1),
    _AccBrPortX25port_Type()
)
accBrPortX25port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBrPortX25port.setStatus("mandatory")
_AccBrPortX25addr1_Type = Integer32
_AccBrPortX25addr1_Object = MibTableColumn
accBrPortX25addr1 = _AccBrPortX25addr1_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 14, 1, 2),
    _AccBrPortX25addr1_Type()
)
accBrPortX25addr1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBrPortX25addr1.setStatus("mandatory")
_AccBrPortX25addr2_Type = Integer32
_AccBrPortX25addr2_Object = MibTableColumn
accBrPortX25addr2 = _AccBrPortX25addr2_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 14, 1, 3),
    _AccBrPortX25addr2_Type()
)
accBrPortX25addr2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBrPortX25addr2.setStatus("mandatory")
_AccBrPortX25idleTime_Type = Integer32
_AccBrPortX25idleTime_Object = MibTableColumn
accBrPortX25idleTime = _AccBrPortX25idleTime_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 14, 1, 4),
    _AccBrPortX25idleTime_Type()
)
accBrPortX25idleTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBrPortX25idleTime.setStatus("mandatory")
_AccBrPortX25pktNegot_Type = Integer32
_AccBrPortX25pktNegot_Object = MibTableColumn
accBrPortX25pktNegot = _AccBrPortX25pktNegot_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 14, 1, 5),
    _AccBrPortX25pktNegot_Type()
)
accBrPortX25pktNegot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBrPortX25pktNegot.setStatus("mandatory")
_AccBrPortX25windowNegot_Type = Integer32
_AccBrPortX25windowNegot_Object = MibTableColumn
accBrPortX25windowNegot = _AccBrPortX25windowNegot_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 14, 1, 6),
    _AccBrPortX25windowNegot_Type()
)
accBrPortX25windowNegot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBrPortX25windowNegot.setStatus("mandatory")


class _AccBrPortX25FacIndex_Type(Integer32):
    """Custom type accBrPortX25FacIndex based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AccBrPortX25FacIndex_Type.__name__ = "Integer32"
_AccBrPortX25FacIndex_Object = MibTableColumn
accBrPortX25FacIndex = _AccBrPortX25FacIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 14, 1, 7),
    _AccBrPortX25FacIndex_Type()
)
accBrPortX25FacIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBrPortX25FacIndex.setStatus("mandatory")


class _AccBrMode_Type(Integer32):
    """Custom type accBrMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bridging", 1),
          ("off", 2),
          ("passive", 3))
    )


_AccBrMode_Type.__name__ = "Integer32"
_AccBrMode_Object = MibScalar
accBrMode = _AccBrMode_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 15),
    _AccBrMode_Type()
)
accBrMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBrMode.setStatus("mandatory")


class _AccBrFilterMode_Type(Integer32):
    """Custom type accBrFilterMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_AccBrFilterMode_Type.__name__ = "Integer32"
_AccBrFilterMode_Object = MibScalar
accBrFilterMode = _AccBrFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 16),
    _AccBrFilterMode_Type()
)
accBrFilterMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBrFilterMode.setStatus("mandatory")


class _AccBrFilterDefault_Type(Integer32):
    """Custom type accBrFilterDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discard", 2),
          ("forward", 1))
    )


_AccBrFilterDefault_Type.__name__ = "Integer32"
_AccBrFilterDefault_Object = MibScalar
accBrFilterDefault = _AccBrFilterDefault_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 17),
    _AccBrFilterDefault_Type()
)
accBrFilterDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBrFilterDefault.setStatus("mandatory")
_AccBrFilterTable_Object = MibTable
accBrFilterTable = _AccBrFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 18)
)
if mibBuilder.loadTexts:
    accBrFilterTable.setStatus("deprecated")
_AccBrFilterEntry_Object = MibTableRow
accBrFilterEntry = _AccBrFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 18, 1)
)
accBrFilterEntry.setIndexNames(
    (0, "ACC-FLASH", "accBrFilterEntDstMacAddr"),
    (0, "ACC-FLASH", "accBrFilterEntSrcMacAddr"),
    (0, "ACC-FLASH", "accBrFilterEntPort"),
    (0, "ACC-FLASH", "accBrFilterEntLogicalOp"),
    (0, "ACC-FLASH", "accBrFilterEntProtocol"),
)
if mibBuilder.loadTexts:
    accBrFilterEntry.setStatus("deprecated")
_AccBrFilterEntDstMacAddr_Type = OctetString
_AccBrFilterEntDstMacAddr_Object = MibTableColumn
accBrFilterEntDstMacAddr = _AccBrFilterEntDstMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 18, 1, 1),
    _AccBrFilterEntDstMacAddr_Type()
)
accBrFilterEntDstMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBrFilterEntDstMacAddr.setStatus("deprecated")
_AccBrFilterEntSrcMacAddr_Type = OctetString
_AccBrFilterEntSrcMacAddr_Object = MibTableColumn
accBrFilterEntSrcMacAddr = _AccBrFilterEntSrcMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 18, 1, 2),
    _AccBrFilterEntSrcMacAddr_Type()
)
accBrFilterEntSrcMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBrFilterEntSrcMacAddr.setStatus("deprecated")


class _AccBrFilterEntDisp_Type(Integer32):
    """Custom type accBrFilterEntDisp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discard", 2),
          ("forward", 1))
    )


_AccBrFilterEntDisp_Type.__name__ = "Integer32"
_AccBrFilterEntDisp_Object = MibTableColumn
accBrFilterEntDisp = _AccBrFilterEntDisp_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 18, 1, 3),
    _AccBrFilterEntDisp_Type()
)
accBrFilterEntDisp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBrFilterEntDisp.setStatus("deprecated")
_AccBrFilterEntPort_Type = Integer32
_AccBrFilterEntPort_Object = MibTableColumn
accBrFilterEntPort = _AccBrFilterEntPort_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 18, 1, 4),
    _AccBrFilterEntPort_Type()
)
accBrFilterEntPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBrFilterEntPort.setStatus("deprecated")


class _AccBrFilterEntLogicalOp_Type(Integer32):
    """Custom type accBrFilterEntLogicalOp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("any", 1),
          ("equal", 2),
          ("notequal", 3))
    )


_AccBrFilterEntLogicalOp_Type.__name__ = "Integer32"
_AccBrFilterEntLogicalOp_Object = MibTableColumn
accBrFilterEntLogicalOp = _AccBrFilterEntLogicalOp_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 18, 1, 5),
    _AccBrFilterEntLogicalOp_Type()
)
accBrFilterEntLogicalOp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBrFilterEntLogicalOp.setStatus("deprecated")
_AccBrFilterEntProtocol_Type = OctetString
_AccBrFilterEntProtocol_Object = MibTableColumn
accBrFilterEntProtocol = _AccBrFilterEntProtocol_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 18, 1, 6),
    _AccBrFilterEntProtocol_Type()
)
accBrFilterEntProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBrFilterEntProtocol.setStatus("deprecated")
_AccBrFilterDiscards_Type = Integer32
_AccBrFilterDiscards_Object = MibTableColumn
accBrFilterDiscards = _AccBrFilterDiscards_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 18, 1, 7),
    _AccBrFilterDiscards_Type()
)
accBrFilterDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBrFilterDiscards.setStatus("deprecated")
_AccBrFilterEntries_Type = Integer32
_AccBrFilterEntries_Object = MibTableColumn
accBrFilterEntries = _AccBrFilterEntries_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 18, 1, 8),
    _AccBrFilterEntries_Type()
)
accBrFilterEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBrFilterEntries.setStatus("deprecated")
_AccBrFiltIITable_Object = MibTable
accBrFiltIITable = _AccBrFiltIITable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 19)
)
if mibBuilder.loadTexts:
    accBrFiltIITable.setStatus("mandatory")
_AccBrFiltIIEntry_Object = MibTableRow
accBrFiltIIEntry = _AccBrFiltIIEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 19, 1)
)
accBrFiltIIEntry.setIndexNames(
    (0, "ACC-FLASH", "accBrFiltIIEntDstMacAddr"),
    (0, "ACC-FLASH", "accBrFiltIIEntDstMacAddrMask"),
    (0, "ACC-FLASH", "accBrFiltIIEntSrcMacAddr"),
    (0, "ACC-FLASH", "accBrFiltIIEntSrcMacAddrMask"),
    (0, "ACC-FLASH", "accBrFiltIIEntPort"),
    (0, "ACC-FLASH", "accBrFiltIIEntLogicalOp"),
    (0, "ACC-FLASH", "accBrFiltIIEntProtocol"),
)
if mibBuilder.loadTexts:
    accBrFiltIIEntry.setStatus("mandatory")
_AccBrFiltIIEntDstMacAddr_Type = OctetString
_AccBrFiltIIEntDstMacAddr_Object = MibTableColumn
accBrFiltIIEntDstMacAddr = _AccBrFiltIIEntDstMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 19, 1, 1),
    _AccBrFiltIIEntDstMacAddr_Type()
)
accBrFiltIIEntDstMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBrFiltIIEntDstMacAddr.setStatus("mandatory")
_AccBrFiltIIEntSrcMacAddr_Type = OctetString
_AccBrFiltIIEntSrcMacAddr_Object = MibTableColumn
accBrFiltIIEntSrcMacAddr = _AccBrFiltIIEntSrcMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 19, 1, 2),
    _AccBrFiltIIEntSrcMacAddr_Type()
)
accBrFiltIIEntSrcMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBrFiltIIEntSrcMacAddr.setStatus("mandatory")


class _AccBrFiltIIEntDisp_Type(Integer32):
    """Custom type accBrFiltIIEntDisp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discard", 2),
          ("forward", 1))
    )


_AccBrFiltIIEntDisp_Type.__name__ = "Integer32"
_AccBrFiltIIEntDisp_Object = MibTableColumn
accBrFiltIIEntDisp = _AccBrFiltIIEntDisp_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 19, 1, 3),
    _AccBrFiltIIEntDisp_Type()
)
accBrFiltIIEntDisp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBrFiltIIEntDisp.setStatus("mandatory")
_AccBrFiltIIEntPort_Type = Integer32
_AccBrFiltIIEntPort_Object = MibTableColumn
accBrFiltIIEntPort = _AccBrFiltIIEntPort_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 19, 1, 4),
    _AccBrFiltIIEntPort_Type()
)
accBrFiltIIEntPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBrFiltIIEntPort.setStatus("mandatory")


class _AccBrFiltIIEntLogicalOp_Type(Integer32):
    """Custom type accBrFiltIIEntLogicalOp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("any", 1),
          ("equal", 2),
          ("notequal", 3))
    )


_AccBrFiltIIEntLogicalOp_Type.__name__ = "Integer32"
_AccBrFiltIIEntLogicalOp_Object = MibTableColumn
accBrFiltIIEntLogicalOp = _AccBrFiltIIEntLogicalOp_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 19, 1, 5),
    _AccBrFiltIIEntLogicalOp_Type()
)
accBrFiltIIEntLogicalOp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBrFiltIIEntLogicalOp.setStatus("mandatory")
_AccBrFiltIIEntProtocol_Type = Integer32
_AccBrFiltIIEntProtocol_Object = MibTableColumn
accBrFiltIIEntProtocol = _AccBrFiltIIEntProtocol_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 19, 1, 6),
    _AccBrFiltIIEntProtocol_Type()
)
accBrFiltIIEntProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBrFiltIIEntProtocol.setStatus("mandatory")
_AccBrFiltIIEntDstMacAddrMask_Type = OctetString
_AccBrFiltIIEntDstMacAddrMask_Object = MibTableColumn
accBrFiltIIEntDstMacAddrMask = _AccBrFiltIIEntDstMacAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 19, 1, 7),
    _AccBrFiltIIEntDstMacAddrMask_Type()
)
accBrFiltIIEntDstMacAddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBrFiltIIEntDstMacAddrMask.setStatus("mandatory")
_AccBrFiltIIEntSrcMacAddrMask_Type = OctetString
_AccBrFiltIIEntSrcMacAddrMask_Object = MibTableColumn
accBrFiltIIEntSrcMacAddrMask = _AccBrFiltIIEntSrcMacAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 19, 1, 8),
    _AccBrFiltIIEntSrcMacAddrMask_Type()
)
accBrFiltIIEntSrcMacAddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBrFiltIIEntSrcMacAddrMask.setStatus("mandatory")
_AccBrFiltIIEntStatus_Type = Integer32
_AccBrFiltIIEntStatus_Object = MibTableColumn
accBrFiltIIEntStatus = _AccBrFiltIIEntStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 19, 1, 9),
    _AccBrFiltIIEntStatus_Type()
)
accBrFiltIIEntStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBrFiltIIEntStatus.setStatus("mandatory")
_AccBrFiltIIDiscards_Type = Integer32
_AccBrFiltIIDiscards_Object = MibScalar
accBrFiltIIDiscards = _AccBrFiltIIDiscards_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 20),
    _AccBrFiltIIDiscards_Type()
)
accBrFiltIIDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBrFiltIIDiscards.setStatus("mandatory")
_AccBrFiltIIEntries_Type = Integer32
_AccBrFiltIIEntries_Object = MibScalar
accBrFiltIIEntries = _AccBrFiltIIEntries_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 21),
    _AccBrFiltIIEntries_Type()
)
accBrFiltIIEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBrFiltIIEntries.setStatus("mandatory")
_AccBrFiltPatternTable_Object = MibTable
accBrFiltPatternTable = _AccBrFiltPatternTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 22)
)
if mibBuilder.loadTexts:
    accBrFiltPatternTable.setStatus("mandatory")
_AccBrFiltPatternEntry_Object = MibTableRow
accBrFiltPatternEntry = _AccBrFiltPatternEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 22, 1)
)
accBrFiltPatternEntry.setIndexNames(
    (0, "ACC-FLASH", "accBrFiltPatternIndex"),
)
if mibBuilder.loadTexts:
    accBrFiltPatternEntry.setStatus("mandatory")
_AccBrFiltPatternIndex_Type = Integer32
_AccBrFiltPatternIndex_Object = MibTableColumn
accBrFiltPatternIndex = _AccBrFiltPatternIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 22, 1, 1),
    _AccBrFiltPatternIndex_Type()
)
accBrFiltPatternIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBrFiltPatternIndex.setStatus("mandatory")
_AccBrFiltPatternPort_Type = Integer32
_AccBrFiltPatternPort_Object = MibTableColumn
accBrFiltPatternPort = _AccBrFiltPatternPort_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 22, 1, 2),
    _AccBrFiltPatternPort_Type()
)
accBrFiltPatternPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBrFiltPatternPort.setStatus("mandatory")


class _AccBrFiltPatternPath_Type(Integer32):
    """Custom type accBrFiltPatternPath based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("in", 1),
          ("out", 2))
    )


_AccBrFiltPatternPath_Type.__name__ = "Integer32"
_AccBrFiltPatternPath_Object = MibTableColumn
accBrFiltPatternPath = _AccBrFiltPatternPath_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 22, 1, 3),
    _AccBrFiltPatternPath_Type()
)
accBrFiltPatternPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBrFiltPatternPath.setStatus("mandatory")
_AccBrFiltPatternByteOff_Type = Integer32
_AccBrFiltPatternByteOff_Object = MibTableColumn
accBrFiltPatternByteOff = _AccBrFiltPatternByteOff_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 22, 1, 4),
    _AccBrFiltPatternByteOff_Type()
)
accBrFiltPatternByteOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBrFiltPatternByteOff.setStatus("mandatory")
_AccBrFiltPatternMask_Type = OctetString
_AccBrFiltPatternMask_Object = MibTableColumn
accBrFiltPatternMask = _AccBrFiltPatternMask_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 22, 1, 5),
    _AccBrFiltPatternMask_Type()
)
accBrFiltPatternMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBrFiltPatternMask.setStatus("mandatory")
_AccBrFiltPatternCompVal_Type = OctetString
_AccBrFiltPatternCompVal_Object = MibTableColumn
accBrFiltPatternCompVal = _AccBrFiltPatternCompVal_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 22, 1, 6),
    _AccBrFiltPatternCompVal_Type()
)
accBrFiltPatternCompVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBrFiltPatternCompVal.setStatus("mandatory")


class _AccBrFiltPatternDisp_Type(Integer32):
    """Custom type accBrFiltPatternDisp based on Integer32"""
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
        *(("discard", 1),
          ("high", 4),
          ("low", 2),
          ("normal", 3))
    )


_AccBrFiltPatternDisp_Type.__name__ = "Integer32"
_AccBrFiltPatternDisp_Object = MibTableColumn
accBrFiltPatternDisp = _AccBrFiltPatternDisp_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 22, 1, 7),
    _AccBrFiltPatternDisp_Type()
)
accBrFiltPatternDisp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBrFiltPatternDisp.setStatus("mandatory")
_AccBrFiltPatternHitCount_Type = Integer32
_AccBrFiltPatternHitCount_Object = MibTableColumn
accBrFiltPatternHitCount = _AccBrFiltPatternHitCount_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 22, 1, 8),
    _AccBrFiltPatternHitCount_Type()
)
accBrFiltPatternHitCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBrFiltPatternHitCount.setStatus("mandatory")
_AccBrFiltPatternStatus_Type = Integer32
_AccBrFiltPatternStatus_Object = MibTableColumn
accBrFiltPatternStatus = _AccBrFiltPatternStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 22, 1, 9),
    _AccBrFiltPatternStatus_Type()
)
accBrFiltPatternStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBrFiltPatternStatus.setStatus("mandatory")


class _AccFdbWhichAddr_Type(Integer32):
    """Custom type accFdbWhichAddr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("destination", 1),
          ("source", 2))
    )


_AccFdbWhichAddr_Type.__name__ = "Integer32"
_AccFdbWhichAddr_Object = MibScalar
accFdbWhichAddr = _AccFdbWhichAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 23),
    _AccFdbWhichAddr_Type()
)
accFdbWhichAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accFdbWhichAddr.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACC-FLASH",
    **{"accBridge": accBridge,
       "accBrFdbTimeout": accBrFdbTimeout,
       "accBrFdbLearnMode": accBrFdbLearnMode,
       "accBrFdbRamCurrSize": accBrFdbRamCurrSize,
       "accBrFdbRamMaxSize": accBrFdbRamMaxSize,
       "accBrFdbNvmMaxSize": accBrFdbNvmMaxSize,
       "accBrFdbTable": accBrFdbTable,
       "accBrFdbEntry": accBrFdbEntry,
       "accBrFdbEntMacAddr": accBrFdbEntMacAddr,
       "accBrFdbEntDisp": accBrFdbEntDisp,
       "accBrFdbEntPort": accBrFdbEntPort,
       "accBrFdbEntTimer": accBrFdbEntTimer,
       "accBrFpTable": accBrFpTable,
       "accBrFpEntry": accBrFpEntry,
       "accBrFpIndex": accBrFpIndex,
       "accBrFpProt": accBrFpProt,
       "accBrFpPrio": accBrFpPrio,
       "accBrFpPriDefault": accBrFpPriDefault,
       "accBrNumPorts": accBrNumPorts,
       "accBrCompress": accBrCompress,
       "accBrPortFRTable": accBrPortFRTable,
       "accBrPortFREntry": accBrPortFREntry,
       "accBrPortFRport": accBrPortFRport,
       "accBrPortFRdlci": accBrPortFRdlci,
       "accBrPortX25Table": accBrPortX25Table,
       "accBrPortX25Entry": accBrPortX25Entry,
       "accBrPortX25port": accBrPortX25port,
       "accBrPortX25addr1": accBrPortX25addr1,
       "accBrPortX25addr2": accBrPortX25addr2,
       "accBrPortX25idleTime": accBrPortX25idleTime,
       "accBrPortX25pktNegot": accBrPortX25pktNegot,
       "accBrPortX25windowNegot": accBrPortX25windowNegot,
       "accBrPortX25FacIndex": accBrPortX25FacIndex,
       "accBrMode": accBrMode,
       "accBrFilterMode": accBrFilterMode,
       "accBrFilterDefault": accBrFilterDefault,
       "accBrFilterTable": accBrFilterTable,
       "accBrFilterEntry": accBrFilterEntry,
       "accBrFilterEntDstMacAddr": accBrFilterEntDstMacAddr,
       "accBrFilterEntSrcMacAddr": accBrFilterEntSrcMacAddr,
       "accBrFilterEntDisp": accBrFilterEntDisp,
       "accBrFilterEntPort": accBrFilterEntPort,
       "accBrFilterEntLogicalOp": accBrFilterEntLogicalOp,
       "accBrFilterEntProtocol": accBrFilterEntProtocol,
       "accBrFilterDiscards": accBrFilterDiscards,
       "accBrFilterEntries": accBrFilterEntries,
       "accBrFiltIITable": accBrFiltIITable,
       "accBrFiltIIEntry": accBrFiltIIEntry,
       "accBrFiltIIEntDstMacAddr": accBrFiltIIEntDstMacAddr,
       "accBrFiltIIEntSrcMacAddr": accBrFiltIIEntSrcMacAddr,
       "accBrFiltIIEntDisp": accBrFiltIIEntDisp,
       "accBrFiltIIEntPort": accBrFiltIIEntPort,
       "accBrFiltIIEntLogicalOp": accBrFiltIIEntLogicalOp,
       "accBrFiltIIEntProtocol": accBrFiltIIEntProtocol,
       "accBrFiltIIEntDstMacAddrMask": accBrFiltIIEntDstMacAddrMask,
       "accBrFiltIIEntSrcMacAddrMask": accBrFiltIIEntSrcMacAddrMask,
       "accBrFiltIIEntStatus": accBrFiltIIEntStatus,
       "accBrFiltIIDiscards": accBrFiltIIDiscards,
       "accBrFiltIIEntries": accBrFiltIIEntries,
       "accBrFiltPatternTable": accBrFiltPatternTable,
       "accBrFiltPatternEntry": accBrFiltPatternEntry,
       "accBrFiltPatternIndex": accBrFiltPatternIndex,
       "accBrFiltPatternPort": accBrFiltPatternPort,
       "accBrFiltPatternPath": accBrFiltPatternPath,
       "accBrFiltPatternByteOff": accBrFiltPatternByteOff,
       "accBrFiltPatternMask": accBrFiltPatternMask,
       "accBrFiltPatternCompVal": accBrFiltPatternCompVal,
       "accBrFiltPatternDisp": accBrFiltPatternDisp,
       "accBrFiltPatternHitCount": accBrFiltPatternHitCount,
       "accBrFiltPatternStatus": accBrFiltPatternStatus,
       "accFdbWhichAddr": accFdbWhichAddr}
)
