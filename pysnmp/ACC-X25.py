# SNMP MIB module (ACC-X25) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACC-X25
# Produced by pysmi-1.5.4 at Mon Oct 14 20:33:11 2024
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
 NotificationType,
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
    "NotificationType",
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

_AccX25_ObjectIdentity = ObjectIdentity
accX25 = _AccX25_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17)
)
_AccX25AtTable_Object = MibTable
accX25AtTable = _AccX25AtTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 1)
)
if mibBuilder.loadTexts:
    accX25AtTable.setStatus("mandatory")
_AccX25AtEntry_Object = MibTableRow
accX25AtEntry = _AccX25AtEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 1, 1)
)
accX25AtEntry.setIndexNames(
    (0, "ACC-X25", "accX25AtIfIndex"),
    (0, "ACC-X25", "accX25AtIpAddress"),
)
if mibBuilder.loadTexts:
    accX25AtEntry.setStatus("mandatory")
_AccX25AtIfIndex_Type = Integer32
_AccX25AtIfIndex_Object = MibTableColumn
accX25AtIfIndex = _AccX25AtIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 1, 1, 1),
    _AccX25AtIfIndex_Type()
)
accX25AtIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25AtIfIndex.setStatus("mandatory")
_AccX25AtIpAddress_Type = IpAddress
_AccX25AtIpAddress_Object = MibTableColumn
accX25AtIpAddress = _AccX25AtIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 1, 1, 2),
    _AccX25AtIpAddress_Type()
)
accX25AtIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25AtIpAddress.setStatus("mandatory")
_AccX25AtNetInOutAddr_Type = DisplayString
_AccX25AtNetInOutAddr_Object = MibTableColumn
accX25AtNetInOutAddr = _AccX25AtNetInOutAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 1, 1, 3),
    _AccX25AtNetInOutAddr_Type()
)
accX25AtNetInOutAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25AtNetInOutAddr.setStatus("mandatory")
_AccX25AtNetInAddr_Type = DisplayString
_AccX25AtNetInAddr_Object = MibTableColumn
accX25AtNetInAddr = _AccX25AtNetInAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 1, 1, 4),
    _AccX25AtNetInAddr_Type()
)
accX25AtNetInAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25AtNetInAddr.setStatus("mandatory")


class _AccX25AtNetFacIndex_Type(Integer32):
    """Custom type accX25AtNetFacIndex based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AccX25AtNetFacIndex_Type.__name__ = "Integer32"
_AccX25AtNetFacIndex_Object = MibTableColumn
accX25AtNetFacIndex = _AccX25AtNetFacIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 1, 1, 5),
    _AccX25AtNetFacIndex_Type()
)
accX25AtNetFacIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25AtNetFacIndex.setStatus("mandatory")
_AccX25SubnetParmTable_Object = MibTable
accX25SubnetParmTable = _AccX25SubnetParmTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 2)
)
if mibBuilder.loadTexts:
    accX25SubnetParmTable.setStatus("mandatory")
_AccX25SubnetParmEntry_Object = MibTableRow
accX25SubnetParmEntry = _AccX25SubnetParmEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 2, 1)
)
accX25SubnetParmEntry.setIndexNames(
    (0, "ACC-X25", "accX25SubnetAddr"),
)
if mibBuilder.loadTexts:
    accX25SubnetParmEntry.setStatus("mandatory")
_AccX25SubnetAddr_Type = IpAddress
_AccX25SubnetAddr_Object = MibTableColumn
accX25SubnetAddr = _AccX25SubnetAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 2, 1, 1),
    _AccX25SubnetAddr_Type()
)
accX25SubnetAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25SubnetAddr.setStatus("mandatory")


class _AccX25Facility_Type(Integer32):
    """Custom type accX25Facility based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("std", 2))
    )


_AccX25Facility_Type.__name__ = "Integer32"
_AccX25Facility_Object = MibTableColumn
accX25Facility = _AccX25Facility_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 2, 1, 2),
    _AccX25Facility_Type()
)
accX25Facility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25Facility.setStatus("mandatory")


class _AccX25PktNegot_Type(Integer32):
    """Custom type accX25PktNegot based on Integer32"""
    defaultValue = 0


_AccX25PktNegot_Object = MibTableColumn
accX25PktNegot = _AccX25PktNegot_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 2, 1, 3),
    _AccX25PktNegot_Type()
)
accX25PktNegot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25PktNegot.setStatus("mandatory")


class _AccX25WindowNegot_Type(Integer32):
    """Custom type accX25WindowNegot based on Integer32"""
    defaultValue = 0


_AccX25WindowNegot_Object = MibTableColumn
accX25WindowNegot = _AccX25WindowNegot_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 2, 1, 4),
    _AccX25WindowNegot_Type()
)
accX25WindowNegot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25WindowNegot.setStatus("mandatory")
_AccX25PortParmTable_Object = MibTable
accX25PortParmTable = _AccX25PortParmTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 3)
)
if mibBuilder.loadTexts:
    accX25PortParmTable.setStatus("mandatory")
_AccX25PortParmEntry_Object = MibTableRow
accX25PortParmEntry = _AccX25PortParmEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 3, 1)
)
accX25PortParmEntry.setIndexNames(
    (0, "ACC-X25", "accX25PortParmIndex"),
)
if mibBuilder.loadTexts:
    accX25PortParmEntry.setStatus("mandatory")
_AccX25PortParmIndex_Type = Integer32
_AccX25PortParmIndex_Object = MibTableColumn
accX25PortParmIndex = _AccX25PortParmIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 3, 1, 1),
    _AccX25PortParmIndex_Type()
)
accX25PortParmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25PortParmIndex.setStatus("mandatory")


class _AccX25AddrMode_Type(Integer32):
    """Custom type accX25AddrMode based on Integer32"""
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
        *(("bfe", 3),
          ("ddn", 2),
          ("table", 1))
    )


_AccX25AddrMode_Type.__name__ = "Integer32"
_AccX25AddrMode_Object = MibTableColumn
accX25AddrMode = _AccX25AddrMode_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 3, 1, 2),
    _AccX25AddrMode_Type()
)
accX25AddrMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25AddrMode.setStatus("mandatory")


class _AccX25PktSize_Type(Integer32):
    """Custom type accX25PktSize based on Integer32"""
    defaultValue = 128


_AccX25PktSize_Object = MibTableColumn
accX25PktSize = _AccX25PktSize_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 3, 1, 3),
    _AccX25PktSize_Type()
)
accX25PktSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25PktSize.setStatus("mandatory")


class _AccX25PktWind_Type(Integer32):
    """Custom type accX25PktWind based on Integer32"""
    defaultValue = 2


_AccX25PktWind_Object = MibTableColumn
accX25PktWind = _AccX25PktWind_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 3, 1, 4),
    _AccX25PktWind_Type()
)
accX25PktWind.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25PktWind.setStatus("mandatory")


class _AccX25SvcNumber_Type(Integer32):
    """Custom type accX25SvcNumber based on Integer32"""
    defaultValue = 256


_AccX25SvcNumber_Object = MibTableColumn
accX25SvcNumber = _AccX25SvcNumber_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 3, 1, 5),
    _AccX25SvcNumber_Type()
)
accX25SvcNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25SvcNumber.setStatus("mandatory")


class _AccX25SvcBase_Type(Integer32):
    """Custom type accX25SvcBase based on Integer32"""
    defaultValue = 1


_AccX25SvcBase_Object = MibTableColumn
accX25SvcBase = _AccX25SvcBase_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 3, 1, 6),
    _AccX25SvcBase_Type()
)
accX25SvcBase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25SvcBase.setStatus("mandatory")


class _AccX25ExtendClr_Type(Integer32):
    """Custom type accX25ExtendClr based on Integer32"""
    defaultValue = 2

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


_AccX25ExtendClr_Type.__name__ = "Integer32"
_AccX25ExtendClr_Object = MibTableColumn
accX25ExtendClr = _AccX25ExtendClr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 3, 1, 7),
    _AccX25ExtendClr_Type()
)
accX25ExtendClr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25ExtendClr.setStatus("mandatory")


class _AccX25ExtendSeq_Type(Integer32):
    """Custom type accX25ExtendSeq based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("extended", 2),
          ("normal", 1))
    )


_AccX25ExtendSeq_Type.__name__ = "Integer32"
_AccX25ExtendSeq_Object = MibTableColumn
accX25ExtendSeq = _AccX25ExtendSeq_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 3, 1, 8),
    _AccX25ExtendSeq_Type()
)
accX25ExtendSeq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25ExtendSeq.setStatus("mandatory")


class _AccX25IdleMin_Type(TimeTicks):
    """Custom type accX25IdleMin based on TimeTicks"""
    defaultValue = 30000


_AccX25IdleMin_Object = MibTableColumn
accX25IdleMin = _AccX25IdleMin_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 3, 1, 9),
    _AccX25IdleMin_Type()
)
accX25IdleMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25IdleMin.setStatus("mandatory")


class _AccX25IdleMax_Type(TimeTicks):
    """Custom type accX25IdleMax based on TimeTicks"""
    defaultValue = 180000


_AccX25IdleMax_Object = MibTableColumn
accX25IdleMax = _AccX25IdleMax_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 3, 1, 10),
    _AccX25IdleMax_Type()
)
accX25IdleMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25IdleMax.setStatus("mandatory")


class _AccX25IdleScale_Type(TimeTicks):
    """Custom type accX25IdleScale based on TimeTicks"""
    defaultValue = 1000


_AccX25IdleScale_Object = MibTableColumn
accX25IdleScale = _AccX25IdleScale_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 3, 1, 11),
    _AccX25IdleScale_Type()
)
accX25IdleScale.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25IdleScale.setStatus("mandatory")


class _AccX25SvcMax_Type(Integer32):
    """Custom type accX25SvcMax based on Integer32"""
    defaultValue = 1


_AccX25SvcMax_Object = MibTableColumn
accX25SvcMax = _AccX25SvcMax_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 3, 1, 12),
    _AccX25SvcMax_Type()
)
accX25SvcMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25SvcMax.setStatus("mandatory")


class _AccX25SvcLimit_Type(Integer32):
    """Custom type accX25SvcLimit based on Integer32"""
    defaultValue = 256


_AccX25SvcLimit_Object = MibTableColumn
accX25SvcLimit = _AccX25SvcLimit_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 3, 1, 13),
    _AccX25SvcLimit_Type()
)
accX25SvcLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25SvcLimit.setStatus("mandatory")


class _AccX25OpenThresh_Type(Integer32):
    """Custom type accX25OpenThresh based on Integer32"""
    defaultValue = 3


_AccX25OpenThresh_Object = MibTableColumn
accX25OpenThresh = _AccX25OpenThresh_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 3, 1, 14),
    _AccX25OpenThresh_Type()
)
accX25OpenThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25OpenThresh.setStatus("mandatory")


class _AccX25SvcMin_Type(Integer32):
    """Custom type accX25SvcMin based on Integer32"""
    defaultValue = 0


_AccX25SvcMin_Object = MibTableColumn
accX25SvcMin = _AccX25SvcMin_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 3, 1, 15),
    _AccX25SvcMin_Type()
)
accX25SvcMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25SvcMin.setStatus("mandatory")


class _AccX25SvcDelay_Type(Integer32):
    """Custom type accX25SvcDelay based on Integer32"""
    defaultValue = 5


_AccX25SvcDelay_Object = MibTableColumn
accX25SvcDelay = _AccX25SvcDelay_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 3, 1, 16),
    _AccX25SvcDelay_Type()
)
accX25SvcDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25SvcDelay.setStatus("mandatory")


class _AccX25InitBackoff_Type(Integer32):
    """Custom type accX25InitBackoff based on Integer32"""
    defaultValue = 15


_AccX25InitBackoff_Object = MibTableColumn
accX25InitBackoff = _AccX25InitBackoff_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 3, 1, 17),
    _AccX25InitBackoff_Type()
)
accX25InitBackoff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25InitBackoff.setStatus("mandatory")


class _AccX25MaxBackoff_Type(Integer32):
    """Custom type accX25MaxBackoff based on Integer32"""
    defaultValue = 86400


_AccX25MaxBackoff_Object = MibTableColumn
accX25MaxBackoff = _AccX25MaxBackoff_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 3, 1, 18),
    _AccX25MaxBackoff_Type()
)
accX25MaxBackoff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25MaxBackoff.setStatus("mandatory")


class _AccX25OurAddress_Type(DisplayString):
    """Custom type accX25OurAddress based on DisplayString"""
    defaultHexValue = "0"


_AccX25OurAddress_Object = MibTableColumn
accX25OurAddress = _AccX25OurAddress_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 3, 1, 19),
    _AccX25OurAddress_Type()
)
accX25OurAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25OurAddress.setStatus("mandatory")


class _AccX25PvcBase_Type(Integer32):
    """Custom type accX25PvcBase based on Integer32"""
    defaultValue = 0


_AccX25PvcBase_Object = MibTableColumn
accX25PvcBase = _AccX25PvcBase_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 3, 1, 20),
    _AccX25PvcBase_Type()
)
accX25PvcBase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25PvcBase.setStatus("mandatory")


class _AccX25PvcNumber_Type(Integer32):
    """Custom type accX25PvcNumber based on Integer32"""
    defaultValue = 0


_AccX25PvcNumber_Object = MibTableColumn
accX25PvcNumber = _AccX25PvcNumber_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 3, 1, 21),
    _AccX25PvcNumber_Type()
)
accX25PvcNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25PvcNumber.setStatus("mandatory")


class _AccX25Tx0Timer_Type(TimeTicks):
    """Custom type accX25Tx0Timer based on TimeTicks"""
    defaultValue = 18000


_AccX25Tx0Timer_Object = MibTableColumn
accX25Tx0Timer = _AccX25Tx0Timer_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 3, 1, 22),
    _AccX25Tx0Timer_Type()
)
accX25Tx0Timer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25Tx0Timer.setStatus("mandatory")


class _AccX25Tx1Timer_Type(TimeTicks):
    """Custom type accX25Tx1Timer based on TimeTicks"""
    defaultValue = 20000


_AccX25Tx1Timer_Object = MibTableColumn
accX25Tx1Timer = _AccX25Tx1Timer_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 3, 1, 23),
    _AccX25Tx1Timer_Type()
)
accX25Tx1Timer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25Tx1Timer.setStatus("mandatory")


class _AccX25Tx2Timer_Type(TimeTicks):
    """Custom type accX25Tx2Timer based on TimeTicks"""
    defaultValue = 18000


_AccX25Tx2Timer_Object = MibTableColumn
accX25Tx2Timer = _AccX25Tx2Timer_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 3, 1, 24),
    _AccX25Tx2Timer_Type()
)
accX25Tx2Timer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25Tx2Timer.setStatus("mandatory")


class _AccX25Tx3Timer_Type(TimeTicks):
    """Custom type accX25Tx3Timer based on TimeTicks"""
    defaultValue = 18000


_AccX25Tx3Timer_Object = MibTableColumn
accX25Tx3Timer = _AccX25Tx3Timer_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 3, 1, 25),
    _AccX25Tx3Timer_Type()
)
accX25Tx3Timer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25Tx3Timer.setStatus("mandatory")


class _AccX25PortEventSeverityLevel_Type(Integer32):
    """Custom type accX25PortEventSeverityLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_AccX25PortEventSeverityLevel_Type.__name__ = "Integer32"
_AccX25PortEventSeverityLevel_Object = MibTableColumn
accX25PortEventSeverityLevel = _AccX25PortEventSeverityLevel_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 3, 1, 26),
    _AccX25PortEventSeverityLevel_Type()
)
accX25PortEventSeverityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25PortEventSeverityLevel.setStatus("mandatory")
_AccX25PktStatTable_Object = MibTable
accX25PktStatTable = _AccX25PktStatTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 4)
)
if mibBuilder.loadTexts:
    accX25PktStatTable.setStatus("mandatory")
_AccX25PktStatEntry_Object = MibTableRow
accX25PktStatEntry = _AccX25PktStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 4, 1)
)
accX25PktStatEntry.setIndexNames(
    (0, "ACC-X25", "accX25PktIndex"),
)
if mibBuilder.loadTexts:
    accX25PktStatEntry.setStatus("mandatory")
_AccX25PktIndex_Type = Integer32
_AccX25PktIndex_Object = MibTableColumn
accX25PktIndex = _AccX25PktIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 4, 1, 1),
    _AccX25PktIndex_Type()
)
accX25PktIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25PktIndex.setStatus("mandatory")
_AccX25RcvDiags_Type = Counter32
_AccX25RcvDiags_Object = MibTableColumn
accX25RcvDiags = _AccX25RcvDiags_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 4, 1, 2),
    _AccX25RcvDiags_Type()
)
accX25RcvDiags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25RcvDiags.setStatus("mandatory")
_AccX25RcvRestartReqs_Type = Counter32
_AccX25RcvRestartReqs_Object = MibTableColumn
accX25RcvRestartReqs = _AccX25RcvRestartReqs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 4, 1, 3),
    _AccX25RcvRestartReqs_Type()
)
accX25RcvRestartReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25RcvRestartReqs.setStatus("mandatory")
_AccX25RcvRestartConfs_Type = Counter32
_AccX25RcvRestartConfs_Object = MibTableColumn
accX25RcvRestartConfs = _AccX25RcvRestartConfs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 4, 1, 4),
    _AccX25RcvRestartConfs_Type()
)
accX25RcvRestartConfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25RcvRestartConfs.setStatus("mandatory")
_AccX25RcvCallReqs_Type = Counter32
_AccX25RcvCallReqs_Object = MibTableColumn
accX25RcvCallReqs = _AccX25RcvCallReqs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 4, 1, 5),
    _AccX25RcvCallReqs_Type()
)
accX25RcvCallReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25RcvCallReqs.setStatus("mandatory")
_AccX25RcvCallAccs_Type = Counter32
_AccX25RcvCallAccs_Object = MibTableColumn
accX25RcvCallAccs = _AccX25RcvCallAccs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 4, 1, 6),
    _AccX25RcvCallAccs_Type()
)
accX25RcvCallAccs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25RcvCallAccs.setStatus("mandatory")
_AccX25RcvClrReqs_Type = Counter32
_AccX25RcvClrReqs_Object = MibTableColumn
accX25RcvClrReqs = _AccX25RcvClrReqs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 4, 1, 7),
    _AccX25RcvClrReqs_Type()
)
accX25RcvClrReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25RcvClrReqs.setStatus("mandatory")
_AccX25RcvClrConfs_Type = Counter32
_AccX25RcvClrConfs_Object = MibTableColumn
accX25RcvClrConfs = _AccX25RcvClrConfs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 4, 1, 8),
    _AccX25RcvClrConfs_Type()
)
accX25RcvClrConfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25RcvClrConfs.setStatus("mandatory")
_AccX25RcvResetReqs_Type = Counter32
_AccX25RcvResetReqs_Object = MibTableColumn
accX25RcvResetReqs = _AccX25RcvResetReqs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 4, 1, 9),
    _AccX25RcvResetReqs_Type()
)
accX25RcvResetReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25RcvResetReqs.setStatus("mandatory")
_AccX25RcvResetConfs_Type = Counter32
_AccX25RcvResetConfs_Object = MibTableColumn
accX25RcvResetConfs = _AccX25RcvResetConfs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 4, 1, 10),
    _AccX25RcvResetConfs_Type()
)
accX25RcvResetConfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25RcvResetConfs.setStatus("mandatory")
_AccX25RcvInts_Type = Counter32
_AccX25RcvInts_Object = MibTableColumn
accX25RcvInts = _AccX25RcvInts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 4, 1, 11),
    _AccX25RcvInts_Type()
)
accX25RcvInts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25RcvInts.setStatus("mandatory")
_AccX25RcvIntConfs_Type = Counter32
_AccX25RcvIntConfs_Object = MibTableColumn
accX25RcvIntConfs = _AccX25RcvIntConfs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 4, 1, 12),
    _AccX25RcvIntConfs_Type()
)
accX25RcvIntConfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25RcvIntConfs.setStatus("mandatory")
_AccX25RcvRRs_Type = Counter32
_AccX25RcvRRs_Object = MibTableColumn
accX25RcvRRs = _AccX25RcvRRs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 4, 1, 13),
    _AccX25RcvRRs_Type()
)
accX25RcvRRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25RcvRRs.setStatus("mandatory")
_AccX25RcvRNRs_Type = Counter32
_AccX25RcvRNRs_Object = MibTableColumn
accX25RcvRNRs = _AccX25RcvRNRs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 4, 1, 14),
    _AccX25RcvRNRs_Type()
)
accX25RcvRNRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25RcvRNRs.setStatus("mandatory")
_AccX25RcvDatas_Type = Counter32
_AccX25RcvDatas_Object = MibTableColumn
accX25RcvDatas = _AccX25RcvDatas_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 4, 1, 15),
    _AccX25RcvDatas_Type()
)
accX25RcvDatas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25RcvDatas.setStatus("mandatory")
_AccX25XmtDiags_Type = Counter32
_AccX25XmtDiags_Object = MibTableColumn
accX25XmtDiags = _AccX25XmtDiags_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 4, 1, 16),
    _AccX25XmtDiags_Type()
)
accX25XmtDiags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25XmtDiags.setStatus("mandatory")
_AccX25XmtRestartReqs_Type = Counter32
_AccX25XmtRestartReqs_Object = MibTableColumn
accX25XmtRestartReqs = _AccX25XmtRestartReqs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 4, 1, 17),
    _AccX25XmtRestartReqs_Type()
)
accX25XmtRestartReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25XmtRestartReqs.setStatus("mandatory")
_AccX25XmtRestartConfs_Type = Counter32
_AccX25XmtRestartConfs_Object = MibTableColumn
accX25XmtRestartConfs = _AccX25XmtRestartConfs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 4, 1, 18),
    _AccX25XmtRestartConfs_Type()
)
accX25XmtRestartConfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25XmtRestartConfs.setStatus("mandatory")
_AccX25XmtCallReqs_Type = Counter32
_AccX25XmtCallReqs_Object = MibTableColumn
accX25XmtCallReqs = _AccX25XmtCallReqs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 4, 1, 19),
    _AccX25XmtCallReqs_Type()
)
accX25XmtCallReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25XmtCallReqs.setStatus("mandatory")
_AccX25XmtCallAccs_Type = Counter32
_AccX25XmtCallAccs_Object = MibTableColumn
accX25XmtCallAccs = _AccX25XmtCallAccs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 4, 1, 20),
    _AccX25XmtCallAccs_Type()
)
accX25XmtCallAccs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25XmtCallAccs.setStatus("mandatory")
_AccX25XmtClrReqs_Type = Counter32
_AccX25XmtClrReqs_Object = MibTableColumn
accX25XmtClrReqs = _AccX25XmtClrReqs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 4, 1, 21),
    _AccX25XmtClrReqs_Type()
)
accX25XmtClrReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25XmtClrReqs.setStatus("mandatory")
_AccX25XmtClrConfs_Type = Counter32
_AccX25XmtClrConfs_Object = MibTableColumn
accX25XmtClrConfs = _AccX25XmtClrConfs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 4, 1, 22),
    _AccX25XmtClrConfs_Type()
)
accX25XmtClrConfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25XmtClrConfs.setStatus("mandatory")
_AccX25XmtResetReqs_Type = Counter32
_AccX25XmtResetReqs_Object = MibTableColumn
accX25XmtResetReqs = _AccX25XmtResetReqs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 4, 1, 23),
    _AccX25XmtResetReqs_Type()
)
accX25XmtResetReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25XmtResetReqs.setStatus("mandatory")
_AccX25XmtResetConfs_Type = Counter32
_AccX25XmtResetConfs_Object = MibTableColumn
accX25XmtResetConfs = _AccX25XmtResetConfs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 4, 1, 24),
    _AccX25XmtResetConfs_Type()
)
accX25XmtResetConfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25XmtResetConfs.setStatus("mandatory")
_AccX25XmtInts_Type = Counter32
_AccX25XmtInts_Object = MibTableColumn
accX25XmtInts = _AccX25XmtInts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 4, 1, 25),
    _AccX25XmtInts_Type()
)
accX25XmtInts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25XmtInts.setStatus("mandatory")
_AccX25XmtIntConfs_Type = Counter32
_AccX25XmtIntConfs_Object = MibTableColumn
accX25XmtIntConfs = _AccX25XmtIntConfs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 4, 1, 26),
    _AccX25XmtIntConfs_Type()
)
accX25XmtIntConfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25XmtIntConfs.setStatus("mandatory")
_AccX25XmtRRs_Type = Counter32
_AccX25XmtRRs_Object = MibTableColumn
accX25XmtRRs = _AccX25XmtRRs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 4, 1, 27),
    _AccX25XmtRRs_Type()
)
accX25XmtRRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25XmtRRs.setStatus("mandatory")
_AccX25XmtRNRs_Type = Counter32
_AccX25XmtRNRs_Object = MibTableColumn
accX25XmtRNRs = _AccX25XmtRNRs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 4, 1, 28),
    _AccX25XmtRNRs_Type()
)
accX25XmtRNRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25XmtRNRs.setStatus("mandatory")
_AccX25XmtDatas_Type = Counter32
_AccX25XmtDatas_Object = MibTableColumn
accX25XmtDatas = _AccX25XmtDatas_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 4, 1, 29),
    _AccX25XmtDatas_Type()
)
accX25XmtDatas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25XmtDatas.setStatus("mandatory")
_AccX25OpenSvcCounts_Type = Counter32
_AccX25OpenSvcCounts_Object = MibTableColumn
accX25OpenSvcCounts = _AccX25OpenSvcCounts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 4, 1, 30),
    _AccX25OpenSvcCounts_Type()
)
accX25OpenSvcCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25OpenSvcCounts.setStatus("mandatory")
_AccX25OptFacTable_Object = MibTable
accX25OptFacTable = _AccX25OptFacTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 5)
)
if mibBuilder.loadTexts:
    accX25OptFacTable.setStatus("mandatory")
_AccX25OptFacEntry_Object = MibTableRow
accX25OptFacEntry = _AccX25OptFacEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 5, 1)
)
accX25OptFacEntry.setIndexNames(
    (0, "ACC-X25", "accX25OptFacIndex"),
)
if mibBuilder.loadTexts:
    accX25OptFacEntry.setStatus("mandatory")
_AccX25OptFacIndex_Type = Integer32
_AccX25OptFacIndex_Object = MibTableColumn
accX25OptFacIndex = _AccX25OptFacIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 5, 1, 1),
    _AccX25OptFacIndex_Type()
)
accX25OptFacIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25OptFacIndex.setStatus("mandatory")
_AccX25OptFacString_Type = OctetString
_AccX25OptFacString_Object = MibTableColumn
accX25OptFacString = _AccX25OptFacString_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 5, 1, 2),
    _AccX25OptFacString_Type()
)
accX25OptFacString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25OptFacString.setStatus("mandatory")
_AccX25PvcAddrTable_Object = MibTable
accX25PvcAddrTable = _AccX25PvcAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 6)
)
if mibBuilder.loadTexts:
    accX25PvcAddrTable.setStatus("mandatory")
_AccX25PvcAddrEntry_Object = MibTableRow
accX25PvcAddrEntry = _AccX25PvcAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 6, 1)
)
accX25PvcAddrEntry.setIndexNames(
    (0, "ACC-X25", "accX25PvcLine"),
    (0, "ACC-X25", "accX25PvcAddrLcid"),
)
if mibBuilder.loadTexts:
    accX25PvcAddrEntry.setStatus("mandatory")
_AccX25PvcLine_Type = Integer32
_AccX25PvcLine_Object = MibTableColumn
accX25PvcLine = _AccX25PvcLine_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 6, 1, 1),
    _AccX25PvcLine_Type()
)
accX25PvcLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25PvcLine.setStatus("mandatory")
_AccX25PvcAddrLcid_Type = Integer32
_AccX25PvcAddrLcid_Object = MibTableColumn
accX25PvcAddrLcid = _AccX25PvcAddrLcid_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 6, 1, 2),
    _AccX25PvcAddrLcid_Type()
)
accX25PvcAddrLcid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25PvcAddrLcid.setStatus("mandatory")
_AccX25PvcAddrString_Type = DisplayString
_AccX25PvcAddrString_Object = MibTableColumn
accX25PvcAddrString = _AccX25PvcAddrString_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 6, 1, 3),
    _AccX25PvcAddrString_Type()
)
accX25PvcAddrString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25PvcAddrString.setStatus("mandatory")


class _AccX25PvcProtocol_Type(Integer32):
    """Custom type accX25PvcProtocol based on Integer32"""
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
        *(("appletalk", 2),
          ("bridging", 6),
          ("decnet", 3),
          ("idp", 4),
          ("ip", 1),
          ("ipx", 5),
          ("sourcerouting", 7))
    )


_AccX25PvcProtocol_Type.__name__ = "Integer32"
_AccX25PvcProtocol_Object = MibTableColumn
accX25PvcProtocol = _AccX25PvcProtocol_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 6, 1, 4),
    _AccX25PvcProtocol_Type()
)
accX25PvcProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25PvcProtocol.setStatus("mandatory")
_AccX25Switch_ObjectIdentity = ObjectIdentity
accX25Switch = _AccX25Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 8)
)


class _AccX25SwitchStatus_Type(Integer32):
    """Custom type accX25SwitchStatus based on Integer32"""
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


_AccX25SwitchStatus_Type.__name__ = "Integer32"
_AccX25SwitchStatus_Object = MibScalar
accX25SwitchStatus = _AccX25SwitchStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 8, 1),
    _AccX25SwitchStatus_Type()
)
accX25SwitchStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25SwitchStatus.setStatus("mandatory")
_AccX25SwitchConnections_Type = Gauge32
_AccX25SwitchConnections_Object = MibScalar
accX25SwitchConnections = _AccX25SwitchConnections_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 8, 2),
    _AccX25SwitchConnections_Type()
)
accX25SwitchConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25SwitchConnections.setStatus("mandatory")
_AccX25SwitchCallSucceeds_Type = Counter32
_AccX25SwitchCallSucceeds_Object = MibScalar
accX25SwitchCallSucceeds = _AccX25SwitchCallSucceeds_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 8, 3),
    _AccX25SwitchCallSucceeds_Type()
)
accX25SwitchCallSucceeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25SwitchCallSucceeds.setStatus("mandatory")
_AccX25SwitchCallFails_Type = Counter32
_AccX25SwitchCallFails_Object = MibScalar
accX25SwitchCallFails = _AccX25SwitchCallFails_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 8, 4),
    _AccX25SwitchCallFails_Type()
)
accX25SwitchCallFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25SwitchCallFails.setStatus("mandatory")
_AccX25SwitchConnTable_Object = MibTable
accX25SwitchConnTable = _AccX25SwitchConnTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 8, 5)
)
if mibBuilder.loadTexts:
    accX25SwitchConnTable.setStatus("mandatory")
_AccX25SwitchConnEntry_Object = MibTableRow
accX25SwitchConnEntry = _AccX25SwitchConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 8, 5, 1)
)
accX25SwitchConnEntry.setIndexNames(
    (0, "ACC-X25", "accX25SwitchConnCallingIfIndex"),
    (0, "ACC-X25", "accX25SwitchConnCallingIndex"),
)
if mibBuilder.loadTexts:
    accX25SwitchConnEntry.setStatus("mandatory")
_AccX25SwitchConnCallingIfIndex_Type = Integer32
_AccX25SwitchConnCallingIfIndex_Object = MibTableColumn
accX25SwitchConnCallingIfIndex = _AccX25SwitchConnCallingIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 8, 5, 1, 1),
    _AccX25SwitchConnCallingIfIndex_Type()
)
accX25SwitchConnCallingIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25SwitchConnCallingIfIndex.setStatus("mandatory")
_AccX25SwitchConnCallingIndex_Type = Integer32
_AccX25SwitchConnCallingIndex_Object = MibTableColumn
accX25SwitchConnCallingIndex = _AccX25SwitchConnCallingIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 8, 5, 1, 2),
    _AccX25SwitchConnCallingIndex_Type()
)
accX25SwitchConnCallingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25SwitchConnCallingIndex.setStatus("mandatory")


class _AccX25SwitchConnCallingType_Type(Integer32):
    """Custom type accX25SwitchConnCallingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("tcp", 3),
          ("x25", 2))
    )


_AccX25SwitchConnCallingType_Type.__name__ = "Integer32"
_AccX25SwitchConnCallingType_Object = MibTableColumn
accX25SwitchConnCallingType = _AccX25SwitchConnCallingType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 8, 5, 1, 3),
    _AccX25SwitchConnCallingType_Type()
)
accX25SwitchConnCallingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25SwitchConnCallingType.setStatus("mandatory")
_AccX25SwitchConnCallingX121Addr_Type = OctetString
_AccX25SwitchConnCallingX121Addr_Object = MibTableColumn
accX25SwitchConnCallingX121Addr = _AccX25SwitchConnCallingX121Addr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 8, 5, 1, 4),
    _AccX25SwitchConnCallingX121Addr_Type()
)
accX25SwitchConnCallingX121Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25SwitchConnCallingX121Addr.setStatus("mandatory")
_AccX25SwitchConnCallingPkts_Type = Counter32
_AccX25SwitchConnCallingPkts_Object = MibTableColumn
accX25SwitchConnCallingPkts = _AccX25SwitchConnCallingPkts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 8, 5, 1, 5),
    _AccX25SwitchConnCallingPkts_Type()
)
accX25SwitchConnCallingPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25SwitchConnCallingPkts.setStatus("mandatory")
_AccX25SwitchConnCallingOctets_Type = Counter32
_AccX25SwitchConnCallingOctets_Object = MibTableColumn
accX25SwitchConnCallingOctets = _AccX25SwitchConnCallingOctets_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 8, 5, 1, 6),
    _AccX25SwitchConnCallingOctets_Type()
)
accX25SwitchConnCallingOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25SwitchConnCallingOctets.setStatus("mandatory")
_AccX25SwitchConnCalledIfIndex_Type = Integer32
_AccX25SwitchConnCalledIfIndex_Object = MibTableColumn
accX25SwitchConnCalledIfIndex = _AccX25SwitchConnCalledIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 8, 5, 1, 7),
    _AccX25SwitchConnCalledIfIndex_Type()
)
accX25SwitchConnCalledIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25SwitchConnCalledIfIndex.setStatus("mandatory")
_AccX25SwitchConnCalledIndex_Type = Integer32
_AccX25SwitchConnCalledIndex_Object = MibTableColumn
accX25SwitchConnCalledIndex = _AccX25SwitchConnCalledIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 8, 5, 1, 8),
    _AccX25SwitchConnCalledIndex_Type()
)
accX25SwitchConnCalledIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25SwitchConnCalledIndex.setStatus("mandatory")


class _AccX25SwitchConnCalledType_Type(Integer32):
    """Custom type accX25SwitchConnCalledType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("tcp", 3),
          ("x25", 2))
    )


_AccX25SwitchConnCalledType_Type.__name__ = "Integer32"
_AccX25SwitchConnCalledType_Object = MibTableColumn
accX25SwitchConnCalledType = _AccX25SwitchConnCalledType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 8, 5, 1, 9),
    _AccX25SwitchConnCalledType_Type()
)
accX25SwitchConnCalledType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25SwitchConnCalledType.setStatus("mandatory")
_AccX25SwitchConnCalledX121Addr_Type = OctetString
_AccX25SwitchConnCalledX121Addr_Object = MibTableColumn
accX25SwitchConnCalledX121Addr = _AccX25SwitchConnCalledX121Addr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 8, 5, 1, 10),
    _AccX25SwitchConnCalledX121Addr_Type()
)
accX25SwitchConnCalledX121Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25SwitchConnCalledX121Addr.setStatus("mandatory")
_AccX25SwitchConnCalledPkts_Type = Counter32
_AccX25SwitchConnCalledPkts_Object = MibTableColumn
accX25SwitchConnCalledPkts = _AccX25SwitchConnCalledPkts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 8, 5, 1, 11),
    _AccX25SwitchConnCalledPkts_Type()
)
accX25SwitchConnCalledPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25SwitchConnCalledPkts.setStatus("mandatory")
_AccX25SwitchConnCalledOctets_Type = Counter32
_AccX25SwitchConnCalledOctets_Object = MibTableColumn
accX25SwitchConnCalledOctets = _AccX25SwitchConnCalledOctets_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 8, 5, 1, 12),
    _AccX25SwitchConnCalledOctets_Type()
)
accX25SwitchConnCalledOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25SwitchConnCalledOctets.setStatus("mandatory")


class _AccX25SwitchConnState_Type(Integer32):
    """Custom type accX25SwitchConnState based on Integer32"""
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
        *(("calling", 2),
          ("clearing", 3),
          ("open", 1),
          ("resetting", 4))
    )


_AccX25SwitchConnState_Type.__name__ = "Integer32"
_AccX25SwitchConnState_Object = MibTableColumn
accX25SwitchConnState = _AccX25SwitchConnState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 8, 5, 1, 13),
    _AccX25SwitchConnState_Type()
)
accX25SwitchConnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25SwitchConnState.setStatus("mandatory")
_AccX25SwitchAddrTransTable_Object = MibTable
accX25SwitchAddrTransTable = _AccX25SwitchAddrTransTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 8, 6)
)
if mibBuilder.loadTexts:
    accX25SwitchAddrTransTable.setStatus("mandatory")
_AccX25SwitchAddrTransEntry_Object = MibTableRow
accX25SwitchAddrTransEntry = _AccX25SwitchAddrTransEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 8, 6, 1)
)
accX25SwitchAddrTransEntry.setIndexNames(
    (0, "ACC-X25", "accX25SwitchAddrTransIfIndex"),
    (0, "ACC-X25", "accX25SwitchAddrTransDir"),
    (0, "ACC-X25", "accX25SwitchAddrTransType"),
    (0, "ACC-X25", "accX25SwitchAddrTransPattern"),
)
if mibBuilder.loadTexts:
    accX25SwitchAddrTransEntry.setStatus("mandatory")
_AccX25SwitchAddrTransIfIndex_Type = Integer32
_AccX25SwitchAddrTransIfIndex_Object = MibTableColumn
accX25SwitchAddrTransIfIndex = _AccX25SwitchAddrTransIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 8, 6, 1, 1),
    _AccX25SwitchAddrTransIfIndex_Type()
)
accX25SwitchAddrTransIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25SwitchAddrTransIfIndex.setStatus("mandatory")


class _AccX25SwitchAddrTransDir_Type(Integer32):
    """Custom type accX25SwitchAddrTransDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("outbound", 2))
    )


_AccX25SwitchAddrTransDir_Type.__name__ = "Integer32"
_AccX25SwitchAddrTransDir_Object = MibTableColumn
accX25SwitchAddrTransDir = _AccX25SwitchAddrTransDir_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 8, 6, 1, 2),
    _AccX25SwitchAddrTransDir_Type()
)
accX25SwitchAddrTransDir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25SwitchAddrTransDir.setStatus("mandatory")


class _AccX25SwitchAddrTransType_Type(Integer32):
    """Custom type accX25SwitchAddrTransType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("called", 1),
          ("calling", 2))
    )


_AccX25SwitchAddrTransType_Type.__name__ = "Integer32"
_AccX25SwitchAddrTransType_Object = MibTableColumn
accX25SwitchAddrTransType = _AccX25SwitchAddrTransType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 8, 6, 1, 3),
    _AccX25SwitchAddrTransType_Type()
)
accX25SwitchAddrTransType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25SwitchAddrTransType.setStatus("mandatory")
_AccX25SwitchAddrTransPattern_Type = DisplayString
_AccX25SwitchAddrTransPattern_Object = MibTableColumn
accX25SwitchAddrTransPattern = _AccX25SwitchAddrTransPattern_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 8, 6, 1, 4),
    _AccX25SwitchAddrTransPattern_Type()
)
accX25SwitchAddrTransPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25SwitchAddrTransPattern.setStatus("mandatory")
_AccX25SwitchAddrTransReplace_Type = DisplayString
_AccX25SwitchAddrTransReplace_Object = MibTableColumn
accX25SwitchAddrTransReplace = _AccX25SwitchAddrTransReplace_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 8, 6, 1, 5),
    _AccX25SwitchAddrTransReplace_Type()
)
accX25SwitchAddrTransReplace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25SwitchAddrTransReplace.setStatus("mandatory")


class _AccX25SwitchAddrTransStatus_Type(Integer32):
    """Custom type accX25SwitchAddrTransStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_AccX25SwitchAddrTransStatus_Type.__name__ = "Integer32"
_AccX25SwitchAddrTransStatus_Object = MibTableColumn
accX25SwitchAddrTransStatus = _AccX25SwitchAddrTransStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 8, 6, 1, 6),
    _AccX25SwitchAddrTransStatus_Type()
)
accX25SwitchAddrTransStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25SwitchAddrTransStatus.setStatus("mandatory")
_AccX25SwitchRouteTable_Object = MibTable
accX25SwitchRouteTable = _AccX25SwitchRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 8, 7)
)
if mibBuilder.loadTexts:
    accX25SwitchRouteTable.setStatus("mandatory")
_AccX25SwitchRouteEntry_Object = MibTableRow
accX25SwitchRouteEntry = _AccX25SwitchRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 8, 7, 1)
)
accX25SwitchRouteEntry.setIndexNames(
    (0, "ACC-X25", "accX25SwitchRoutePattern"),
)
if mibBuilder.loadTexts:
    accX25SwitchRouteEntry.setStatus("mandatory")
_AccX25SwitchRoutePattern_Type = OctetString
_AccX25SwitchRoutePattern_Object = MibTableColumn
accX25SwitchRoutePattern = _AccX25SwitchRoutePattern_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 8, 7, 1, 1),
    _AccX25SwitchRoutePattern_Type()
)
accX25SwitchRoutePattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25SwitchRoutePattern.setStatus("mandatory")
_AccX25SwitchRouteIfIndex_Type = Integer32
_AccX25SwitchRouteIfIndex_Object = MibTableColumn
accX25SwitchRouteIfIndex = _AccX25SwitchRouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 8, 7, 1, 2),
    _AccX25SwitchRouteIfIndex_Type()
)
accX25SwitchRouteIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25SwitchRouteIfIndex.setStatus("mandatory")


class _AccX25SwitchRouteStatus_Type(Integer32):
    """Custom type accX25SwitchRouteStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_AccX25SwitchRouteStatus_Type.__name__ = "Integer32"
_AccX25SwitchRouteStatus_Object = MibTableColumn
accX25SwitchRouteStatus = _AccX25SwitchRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 8, 7, 1, 3),
    _AccX25SwitchRouteStatus_Type()
)
accX25SwitchRouteStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25SwitchRouteStatus.setStatus("mandatory")
_AccX25SwitchExtRtTable_Object = MibTable
accX25SwitchExtRtTable = _AccX25SwitchExtRtTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 8, 8)
)
if mibBuilder.loadTexts:
    accX25SwitchExtRtTable.setStatus("mandatory")
_AccX25SwitchExtRtEntry_Object = MibTableRow
accX25SwitchExtRtEntry = _AccX25SwitchExtRtEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 8, 8, 1)
)
accX25SwitchExtRtEntry.setIndexNames(
    (0, "ACC-X25", "accX25SwitchExtRtIndex"),
)
if mibBuilder.loadTexts:
    accX25SwitchExtRtEntry.setStatus("mandatory")
_AccX25SwitchExtRtIndex_Type = Integer32
_AccX25SwitchExtRtIndex_Object = MibTableColumn
accX25SwitchExtRtIndex = _AccX25SwitchExtRtIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 8, 8, 1, 1),
    _AccX25SwitchExtRtIndex_Type()
)
accX25SwitchExtRtIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25SwitchExtRtIndex.setStatus("mandatory")
_AccX25SwitchExtRtIfIn_Type = Integer32
_AccX25SwitchExtRtIfIn_Object = MibTableColumn
accX25SwitchExtRtIfIn = _AccX25SwitchExtRtIfIn_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 8, 8, 1, 2),
    _AccX25SwitchExtRtIfIn_Type()
)
accX25SwitchExtRtIfIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25SwitchExtRtIfIn.setStatus("mandatory")
_AccX25SwitchExtRtAddr_Type = OctetString
_AccX25SwitchExtRtAddr_Object = MibTableColumn
accX25SwitchExtRtAddr = _AccX25SwitchExtRtAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 8, 8, 1, 3),
    _AccX25SwitchExtRtAddr_Type()
)
accX25SwitchExtRtAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25SwitchExtRtAddr.setStatus("mandatory")
_AccX25SwitchExtRtCUD_Type = OctetString
_AccX25SwitchExtRtCUD_Object = MibTableColumn
accX25SwitchExtRtCUD = _AccX25SwitchExtRtCUD_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 8, 8, 1, 4),
    _AccX25SwitchExtRtCUD_Type()
)
accX25SwitchExtRtCUD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25SwitchExtRtCUD.setStatus("mandatory")


class _AccX25SwitchExtRtDisp_Type(Integer32):
    """Custom type accX25SwitchExtRtDisp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("local", 2),
          ("reject", 3),
          ("switch", 1))
    )


_AccX25SwitchExtRtDisp_Type.__name__ = "Integer32"
_AccX25SwitchExtRtDisp_Object = MibTableColumn
accX25SwitchExtRtDisp = _AccX25SwitchExtRtDisp_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 8, 8, 1, 5),
    _AccX25SwitchExtRtDisp_Type()
)
accX25SwitchExtRtDisp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25SwitchExtRtDisp.setStatus("mandatory")
_AccX25SwitchExtRtIfOut_Type = Integer32
_AccX25SwitchExtRtIfOut_Object = MibTableColumn
accX25SwitchExtRtIfOut = _AccX25SwitchExtRtIfOut_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 8, 8, 1, 6),
    _AccX25SwitchExtRtIfOut_Type()
)
accX25SwitchExtRtIfOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25SwitchExtRtIfOut.setStatus("mandatory")


class _AccX25SwitchExtRtStatus_Type(Integer32):
    """Custom type accX25SwitchExtRtStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_AccX25SwitchExtRtStatus_Type.__name__ = "Integer32"
_AccX25SwitchExtRtStatus_Object = MibTableColumn
accX25SwitchExtRtStatus = _AccX25SwitchExtRtStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 8, 8, 1, 7),
    _AccX25SwitchExtRtStatus_Type()
)
accX25SwitchExtRtStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25SwitchExtRtStatus.setStatus("mandatory")
_AccX25EventLogSize_Type = Integer32
_AccX25EventLogSize_Object = MibScalar
accX25EventLogSize = _AccX25EventLogSize_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 9),
    _AccX25EventLogSize_Type()
)
accX25EventLogSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25EventLogSize.setStatus("mandatory")
_AccX25EventTable_Object = MibTable
accX25EventTable = _AccX25EventTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 10)
)
if mibBuilder.loadTexts:
    accX25EventTable.setStatus("mandatory")
_AccX25EventEntry_Object = MibTableRow
accX25EventEntry = _AccX25EventEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 10, 1)
)
accX25EventEntry.setIndexNames(
    (0, "ACC-X25", "accX25EventSeq"),
)
if mibBuilder.loadTexts:
    accX25EventEntry.setStatus("mandatory")
_AccX25EventSeq_Type = Integer32
_AccX25EventSeq_Object = MibTableColumn
accX25EventSeq = _AccX25EventSeq_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 10, 1, 1),
    _AccX25EventSeq_Type()
)
accX25EventSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25EventSeq.setStatus("mandatory")
_AccX25EventLine_Type = Integer32
_AccX25EventLine_Object = MibTableColumn
accX25EventLine = _AccX25EventLine_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 10, 1, 2),
    _AccX25EventLine_Type()
)
accX25EventLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25EventLine.setStatus("mandatory")
_AccX25EventLCID_Type = Integer32
_AccX25EventLCID_Object = MibTableColumn
accX25EventLCID = _AccX25EventLCID_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 10, 1, 3),
    _AccX25EventLCID_Type()
)
accX25EventLCID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25EventLCID.setStatus("mandatory")
_AccX25EventUpTime_Type = TimeTicks
_AccX25EventUpTime_Object = MibTableColumn
accX25EventUpTime = _AccX25EventUpTime_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 10, 1, 4),
    _AccX25EventUpTime_Type()
)
accX25EventUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25EventUpTime.setStatus("mandatory")
_AccX25EventCode_Type = OctetString
_AccX25EventCode_Object = MibTableColumn
accX25EventCode = _AccX25EventCode_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 10, 1, 5),
    _AccX25EventCode_Type()
)
accX25EventCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25EventCode.setStatus("mandatory")
_AccX25EventCause_Type = Integer32
_AccX25EventCause_Object = MibTableColumn
accX25EventCause = _AccX25EventCause_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 10, 1, 6),
    _AccX25EventCause_Type()
)
accX25EventCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25EventCause.setStatus("mandatory")
_AccX25EventDiag_Type = Integer32
_AccX25EventDiag_Object = MibTableColumn
accX25EventDiag = _AccX25EventDiag_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 10, 1, 7),
    _AccX25EventDiag_Type()
)
accX25EventDiag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25EventDiag.setStatus("mandatory")
_AccX25EventProtocol_Type = Integer32
_AccX25EventProtocol_Object = MibTableColumn
accX25EventProtocol = _AccX25EventProtocol_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 10, 1, 8),
    _AccX25EventProtocol_Type()
)
accX25EventProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25EventProtocol.setStatus("mandatory")
_AccX25EventPacket_Type = OctetString
_AccX25EventPacket_Object = MibTableColumn
accX25EventPacket = _AccX25EventPacket_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 10, 1, 9),
    _AccX25EventPacket_Type()
)
accX25EventPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25EventPacket.setStatus("mandatory")
_AccX25CircuitTable_Object = MibTable
accX25CircuitTable = _AccX25CircuitTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 11)
)
if mibBuilder.loadTexts:
    accX25CircuitTable.setStatus("mandatory")
_AccX25CircuitEntry_Object = MibTableRow
accX25CircuitEntry = _AccX25CircuitEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 11, 1)
)
accX25CircuitEntry.setIndexNames(
    (0, "ACC-X25", "accX25CircuitLine"),
    (0, "ACC-X25", "accX25CircuitLCID"),
)
if mibBuilder.loadTexts:
    accX25CircuitEntry.setStatus("mandatory")
_AccX25CircuitLine_Type = Integer32
_AccX25CircuitLine_Object = MibTableColumn
accX25CircuitLine = _AccX25CircuitLine_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 11, 1, 1),
    _AccX25CircuitLine_Type()
)
accX25CircuitLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25CircuitLine.setStatus("mandatory")


class _AccX25CircuitLCID_Type(Integer32):
    """Custom type accX25CircuitLCID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AccX25CircuitLCID_Type.__name__ = "Integer32"
_AccX25CircuitLCID_Object = MibTableColumn
accX25CircuitLCID = _AccX25CircuitLCID_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 11, 1, 2),
    _AccX25CircuitLCID_Type()
)
accX25CircuitLCID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25CircuitLCID.setStatus("mandatory")


class _AccX25CircuitType_Type(Integer32):
    """Custom type accX25CircuitType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("incoming", 1),
          ("outgoing", 2),
          ("pvc", 3))
    )


_AccX25CircuitType_Type.__name__ = "Integer32"
_AccX25CircuitType_Object = MibTableColumn
accX25CircuitType = _AccX25CircuitType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 11, 1, 3),
    _AccX25CircuitType_Type()
)
accX25CircuitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25CircuitType.setStatus("mandatory")
_AccX25CircuitRemoteAddr_Type = OctetString
_AccX25CircuitRemoteAddr_Object = MibTableColumn
accX25CircuitRemoteAddr = _AccX25CircuitRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 11, 1, 4),
    _AccX25CircuitRemoteAddr_Type()
)
accX25CircuitRemoteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25CircuitRemoteAddr.setStatus("mandatory")
_AccX25CircuitLocalAddr_Type = OctetString
_AccX25CircuitLocalAddr_Object = MibTableColumn
accX25CircuitLocalAddr = _AccX25CircuitLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 11, 1, 5),
    _AccX25CircuitLocalAddr_Type()
)
accX25CircuitLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25CircuitLocalAddr.setStatus("mandatory")


class _AccX25CircuitState_Type(Integer32):
    """Custom type accX25CircuitState based on Integer32"""
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
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("d1-flow-ctl-rdy", 4),
          ("d2-dte-reset-req", 5),
          ("d3-dxe-reset-ind", 6),
          ("p1-ready", 1),
          ("p2-dte-call-req", 2),
          ("p3-dxe-inc-call", 3),
          ("p5-call-collision", 7),
          ("p6-dte-clr-req", 8),
          ("p7-dxe-clr-ind", 9),
          ("pvc", 12),
          ("r2-dte-restart-req", 10),
          ("r3-dxe-restart-ind", 11))
    )


_AccX25CircuitState_Type.__name__ = "Integer32"
_AccX25CircuitState_Object = MibTableColumn
accX25CircuitState = _AccX25CircuitState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 11, 1, 6),
    _AccX25CircuitState_Type()
)
accX25CircuitState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25CircuitState.setStatus("mandatory")
_AccX25CircuitPktTimer_Type = Integer32
_AccX25CircuitPktTimer_Object = MibTableColumn
accX25CircuitPktTimer = _AccX25CircuitPktTimer_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 11, 1, 7),
    _AccX25CircuitPktTimer_Type()
)
accX25CircuitPktTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25CircuitPktTimer.setStatus("mandatory")
_AccX25CircuitPktRetry_Type = Integer32
_AccX25CircuitPktRetry_Object = MibTableColumn
accX25CircuitPktRetry = _AccX25CircuitPktRetry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 11, 1, 8),
    _AccX25CircuitPktRetry_Type()
)
accX25CircuitPktRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25CircuitPktRetry.setStatus("mandatory")
_AccX25Xot_ObjectIdentity = ObjectIdentity
accX25Xot = _AccX25Xot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 12)
)
_AccX25XotParmTable_Object = MibTable
accX25XotParmTable = _AccX25XotParmTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 12, 1)
)
if mibBuilder.loadTexts:
    accX25XotParmTable.setStatus("mandatory")
_AccX25XotParmEntry_Object = MibTableRow
accX25XotParmEntry = _AccX25XotParmEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 12, 1, 1)
)
accX25XotParmEntry.setIndexNames(
    (0, "ACC-X25", "accX25XotParmLine"),
)
if mibBuilder.loadTexts:
    accX25XotParmEntry.setStatus("mandatory")
_AccX25XotParmLine_Type = Integer32
_AccX25XotParmLine_Object = MibTableColumn
accX25XotParmLine = _AccX25XotParmLine_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 12, 1, 1, 1),
    _AccX25XotParmLine_Type()
)
accX25XotParmLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25XotParmLine.setStatus("mandatory")
_AccX25XotParmIpAddress_Type = IpAddress
_AccX25XotParmIpAddress_Object = MibTableColumn
accX25XotParmIpAddress = _AccX25XotParmIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 12, 1, 1, 2),
    _AccX25XotParmIpAddress_Type()
)
accX25XotParmIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25XotParmIpAddress.setStatus("mandatory")
_AccX25XotParmMsgLevel_Type = Integer32
_AccX25XotParmMsgLevel_Object = MibTableColumn
accX25XotParmMsgLevel = _AccX25XotParmMsgLevel_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 12, 1, 1, 3),
    _AccX25XotParmMsgLevel_Type()
)
accX25XotParmMsgLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25XotParmMsgLevel.setStatus("mandatory")
_AccX25XotConnTable_Object = MibTable
accX25XotConnTable = _AccX25XotConnTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 12, 2)
)
if mibBuilder.loadTexts:
    accX25XotConnTable.setStatus("mandatory")
_AccX25XotConnEntry_Object = MibTableRow
accX25XotConnEntry = _AccX25XotConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 12, 2, 1)
)
accX25XotConnEntry.setIndexNames(
    (0, "ACC-X25", "accX25XotConnLine"),
    (0, "ACC-X25", "accX25XotConnLcn"),
)
if mibBuilder.loadTexts:
    accX25XotConnEntry.setStatus("mandatory")
_AccX25XotConnLine_Type = Integer32
_AccX25XotConnLine_Object = MibTableColumn
accX25XotConnLine = _AccX25XotConnLine_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 12, 2, 1, 1),
    _AccX25XotConnLine_Type()
)
accX25XotConnLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25XotConnLine.setStatus("mandatory")
_AccX25XotConnLcn_Type = Integer32
_AccX25XotConnLcn_Object = MibTableColumn
accX25XotConnLcn = _AccX25XotConnLcn_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 12, 2, 1, 2),
    _AccX25XotConnLcn_Type()
)
accX25XotConnLcn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25XotConnLcn.setStatus("mandatory")


class _AccX25XotConnState_Type(Integer32):
    """Custom type accX25XotConnState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              9,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26)
        )
    )
    namedValues = NamedValues(
        *(("clearProcActive", 2),
          ("clearProcComplete", 3),
          ("connected", 18),
          ("destInterfaceNotUp", 20),
          ("destInterfaceNotX25", 21),
          ("destPvcCfgMismatch", 23),
          ("flowControlMismatch", 24),
          ("flowControlValuesNotSupported", 25),
          ("noDestInterface", 19),
          ("noDestPvc", 22),
          ("pvcSetupProtocolError", 26),
          ("tcpCongested", 4),
          ("tcpConnInProgress", 16),
          ("tcpConnRefused", 9),
          ("waitCallConfirm", 1),
          ("waitPvcSetupConfirm", 17))
    )


_AccX25XotConnState_Type.__name__ = "Integer32"
_AccX25XotConnState_Object = MibTableColumn
accX25XotConnState = _AccX25XotConnState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 12, 2, 1, 3),
    _AccX25XotConnState_Type()
)
accX25XotConnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25XotConnState.setStatus("mandatory")


class _AccX25XotConnType_Type(Integer32):
    """Custom type accX25XotConnType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("incoming", 1),
          ("outgoing", 2),
          ("pvc", 3))
    )


_AccX25XotConnType_Type.__name__ = "Integer32"
_AccX25XotConnType_Object = MibTableColumn
accX25XotConnType = _AccX25XotConnType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 12, 2, 1, 4),
    _AccX25XotConnType_Type()
)
accX25XotConnType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25XotConnType.setStatus("mandatory")
_AccX25XotConnIpAddress_Type = IpAddress
_AccX25XotConnIpAddress_Object = MibTableColumn
accX25XotConnIpAddress = _AccX25XotConnIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 12, 2, 1, 5),
    _AccX25XotConnIpAddress_Type()
)
accX25XotConnIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25XotConnIpAddress.setStatus("mandatory")
_AccX25XotConnTcpPortNumber_Type = Integer32
_AccX25XotConnTcpPortNumber_Object = MibTableColumn
accX25XotConnTcpPortNumber = _AccX25XotConnTcpPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 12, 2, 1, 6),
    _AccX25XotConnTcpPortNumber_Type()
)
accX25XotConnTcpPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25XotConnTcpPortNumber.setStatus("mandatory")
_AccX25XotConnRemoteIpAddress_Type = IpAddress
_AccX25XotConnRemoteIpAddress_Object = MibTableColumn
accX25XotConnRemoteIpAddress = _AccX25XotConnRemoteIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 12, 2, 1, 7),
    _AccX25XotConnRemoteIpAddress_Type()
)
accX25XotConnRemoteIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25XotConnRemoteIpAddress.setStatus("mandatory")
_AccX25XotConnRemoteTCPPortNumber_Type = Integer32
_AccX25XotConnRemoteTCPPortNumber_Object = MibTableColumn
accX25XotConnRemoteTCPPortNumber = _AccX25XotConnRemoteTCPPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 12, 2, 1, 8),
    _AccX25XotConnRemoteTCPPortNumber_Type()
)
accX25XotConnRemoteTCPPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25XotConnRemoteTCPPortNumber.setStatus("mandatory")
_AccX25XotConnRcvEncaps_Type = Counter32
_AccX25XotConnRcvEncaps_Object = MibTableColumn
accX25XotConnRcvEncaps = _AccX25XotConnRcvEncaps_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 12, 2, 1, 9),
    _AccX25XotConnRcvEncaps_Type()
)
accX25XotConnRcvEncaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25XotConnRcvEncaps.setStatus("mandatory")
_AccX25XotConnXmtEncaps_Type = Counter32
_AccX25XotConnXmtEncaps_Object = MibTableColumn
accX25XotConnXmtEncaps = _AccX25XotConnXmtEncaps_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 12, 2, 1, 10),
    _AccX25XotConnXmtEncaps_Type()
)
accX25XotConnXmtEncaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25XotConnXmtEncaps.setStatus("mandatory")
_AccX25XotStatsTable_Object = MibTable
accX25XotStatsTable = _AccX25XotStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 12, 4)
)
if mibBuilder.loadTexts:
    accX25XotStatsTable.setStatus("mandatory")
_AccX25XotStatsEntry_Object = MibTableRow
accX25XotStatsEntry = _AccX25XotStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 12, 4, 1)
)
accX25XotStatsEntry.setIndexNames(
    (0, "ACC-X25", "accX25XotStatsLine"),
)
if mibBuilder.loadTexts:
    accX25XotStatsEntry.setStatus("mandatory")
_AccX25XotStatsLine_Type = Integer32
_AccX25XotStatsLine_Object = MibTableColumn
accX25XotStatsLine = _AccX25XotStatsLine_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 12, 4, 1, 1),
    _AccX25XotStatsLine_Type()
)
accX25XotStatsLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25XotStatsLine.setStatus("mandatory")
_AccX25XotStatsTotalConnections_Type = Counter32
_AccX25XotStatsTotalConnections_Object = MibTableColumn
accX25XotStatsTotalConnections = _AccX25XotStatsTotalConnections_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 12, 4, 1, 2),
    _AccX25XotStatsTotalConnections_Type()
)
accX25XotStatsTotalConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25XotStatsTotalConnections.setStatus("mandatory")
_AccX25XotStatsActiveConnections_Type = Gauge32
_AccX25XotStatsActiveConnections_Object = MibTableColumn
accX25XotStatsActiveConnections = _AccX25XotStatsActiveConnections_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 12, 4, 1, 3),
    _AccX25XotStatsActiveConnections_Type()
)
accX25XotStatsActiveConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25XotStatsActiveConnections.setStatus("mandatory")
_AccX25XotStatsRcvInvalids_Type = Counter32
_AccX25XotStatsRcvInvalids_Object = MibTableColumn
accX25XotStatsRcvInvalids = _AccX25XotStatsRcvInvalids_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 12, 4, 1, 4),
    _AccX25XotStatsRcvInvalids_Type()
)
accX25XotStatsRcvInvalids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25XotStatsRcvInvalids.setStatus("mandatory")
_AccX25XotStatsGenClearReqs_Type = Counter32
_AccX25XotStatsGenClearReqs_Object = MibTableColumn
accX25XotStatsGenClearReqs = _AccX25XotStatsGenClearReqs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 12, 4, 1, 5),
    _AccX25XotStatsGenClearReqs_Type()
)
accX25XotStatsGenClearReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25XotStatsGenClearReqs.setStatus("mandatory")
_AccX25XotStatsGenResetReqs_Type = Counter32
_AccX25XotStatsGenResetReqs_Object = MibTableColumn
accX25XotStatsGenResetReqs = _AccX25XotStatsGenResetReqs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 12, 4, 1, 6),
    _AccX25XotStatsGenResetReqs_Type()
)
accX25XotStatsGenResetReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25XotStatsGenResetReqs.setStatus("mandatory")
_AccX25XotStatsGenPvcSetups_Type = Counter32
_AccX25XotStatsGenPvcSetups_Object = MibTableColumn
accX25XotStatsGenPvcSetups = _AccX25XotStatsGenPvcSetups_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 12, 4, 1, 7),
    _AccX25XotStatsGenPvcSetups_Type()
)
accX25XotStatsGenPvcSetups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25XotStatsGenPvcSetups.setStatus("mandatory")
_AccX25XotStatsRcvValids_Type = Counter32
_AccX25XotStatsRcvValids_Object = MibTableColumn
accX25XotStatsRcvValids = _AccX25XotStatsRcvValids_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 12, 4, 1, 8),
    _AccX25XotStatsRcvValids_Type()
)
accX25XotStatsRcvValids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25XotStatsRcvValids.setStatus("mandatory")
_AccX25XotStatsXmtTotals_Type = Counter32
_AccX25XotStatsXmtTotals_Object = MibTableColumn
accX25XotStatsXmtTotals = _AccX25XotStatsXmtTotals_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 12, 4, 1, 9),
    _AccX25XotStatsXmtTotals_Type()
)
accX25XotStatsXmtTotals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25XotStatsXmtTotals.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACC-X25",
    **{"accX25": accX25,
       "accX25AtTable": accX25AtTable,
       "accX25AtEntry": accX25AtEntry,
       "accX25AtIfIndex": accX25AtIfIndex,
       "accX25AtIpAddress": accX25AtIpAddress,
       "accX25AtNetInOutAddr": accX25AtNetInOutAddr,
       "accX25AtNetInAddr": accX25AtNetInAddr,
       "accX25AtNetFacIndex": accX25AtNetFacIndex,
       "accX25SubnetParmTable": accX25SubnetParmTable,
       "accX25SubnetParmEntry": accX25SubnetParmEntry,
       "accX25SubnetAddr": accX25SubnetAddr,
       "accX25Facility": accX25Facility,
       "accX25PktNegot": accX25PktNegot,
       "accX25WindowNegot": accX25WindowNegot,
       "accX25PortParmTable": accX25PortParmTable,
       "accX25PortParmEntry": accX25PortParmEntry,
       "accX25PortParmIndex": accX25PortParmIndex,
       "accX25AddrMode": accX25AddrMode,
       "accX25PktSize": accX25PktSize,
       "accX25PktWind": accX25PktWind,
       "accX25SvcNumber": accX25SvcNumber,
       "accX25SvcBase": accX25SvcBase,
       "accX25ExtendClr": accX25ExtendClr,
       "accX25ExtendSeq": accX25ExtendSeq,
       "accX25IdleMin": accX25IdleMin,
       "accX25IdleMax": accX25IdleMax,
       "accX25IdleScale": accX25IdleScale,
       "accX25SvcMax": accX25SvcMax,
       "accX25SvcLimit": accX25SvcLimit,
       "accX25OpenThresh": accX25OpenThresh,
       "accX25SvcMin": accX25SvcMin,
       "accX25SvcDelay": accX25SvcDelay,
       "accX25InitBackoff": accX25InitBackoff,
       "accX25MaxBackoff": accX25MaxBackoff,
       "accX25OurAddress": accX25OurAddress,
       "accX25PvcBase": accX25PvcBase,
       "accX25PvcNumber": accX25PvcNumber,
       "accX25Tx0Timer": accX25Tx0Timer,
       "accX25Tx1Timer": accX25Tx1Timer,
       "accX25Tx2Timer": accX25Tx2Timer,
       "accX25Tx3Timer": accX25Tx3Timer,
       "accX25PortEventSeverityLevel": accX25PortEventSeverityLevel,
       "accX25PktStatTable": accX25PktStatTable,
       "accX25PktStatEntry": accX25PktStatEntry,
       "accX25PktIndex": accX25PktIndex,
       "accX25RcvDiags": accX25RcvDiags,
       "accX25RcvRestartReqs": accX25RcvRestartReqs,
       "accX25RcvRestartConfs": accX25RcvRestartConfs,
       "accX25RcvCallReqs": accX25RcvCallReqs,
       "accX25RcvCallAccs": accX25RcvCallAccs,
       "accX25RcvClrReqs": accX25RcvClrReqs,
       "accX25RcvClrConfs": accX25RcvClrConfs,
       "accX25RcvResetReqs": accX25RcvResetReqs,
       "accX25RcvResetConfs": accX25RcvResetConfs,
       "accX25RcvInts": accX25RcvInts,
       "accX25RcvIntConfs": accX25RcvIntConfs,
       "accX25RcvRRs": accX25RcvRRs,
       "accX25RcvRNRs": accX25RcvRNRs,
       "accX25RcvDatas": accX25RcvDatas,
       "accX25XmtDiags": accX25XmtDiags,
       "accX25XmtRestartReqs": accX25XmtRestartReqs,
       "accX25XmtRestartConfs": accX25XmtRestartConfs,
       "accX25XmtCallReqs": accX25XmtCallReqs,
       "accX25XmtCallAccs": accX25XmtCallAccs,
       "accX25XmtClrReqs": accX25XmtClrReqs,
       "accX25XmtClrConfs": accX25XmtClrConfs,
       "accX25XmtResetReqs": accX25XmtResetReqs,
       "accX25XmtResetConfs": accX25XmtResetConfs,
       "accX25XmtInts": accX25XmtInts,
       "accX25XmtIntConfs": accX25XmtIntConfs,
       "accX25XmtRRs": accX25XmtRRs,
       "accX25XmtRNRs": accX25XmtRNRs,
       "accX25XmtDatas": accX25XmtDatas,
       "accX25OpenSvcCounts": accX25OpenSvcCounts,
       "accX25OptFacTable": accX25OptFacTable,
       "accX25OptFacEntry": accX25OptFacEntry,
       "accX25OptFacIndex": accX25OptFacIndex,
       "accX25OptFacString": accX25OptFacString,
       "accX25PvcAddrTable": accX25PvcAddrTable,
       "accX25PvcAddrEntry": accX25PvcAddrEntry,
       "accX25PvcLine": accX25PvcLine,
       "accX25PvcAddrLcid": accX25PvcAddrLcid,
       "accX25PvcAddrString": accX25PvcAddrString,
       "accX25PvcProtocol": accX25PvcProtocol,
       "accX25Switch": accX25Switch,
       "accX25SwitchStatus": accX25SwitchStatus,
       "accX25SwitchConnections": accX25SwitchConnections,
       "accX25SwitchCallSucceeds": accX25SwitchCallSucceeds,
       "accX25SwitchCallFails": accX25SwitchCallFails,
       "accX25SwitchConnTable": accX25SwitchConnTable,
       "accX25SwitchConnEntry": accX25SwitchConnEntry,
       "accX25SwitchConnCallingIfIndex": accX25SwitchConnCallingIfIndex,
       "accX25SwitchConnCallingIndex": accX25SwitchConnCallingIndex,
       "accX25SwitchConnCallingType": accX25SwitchConnCallingType,
       "accX25SwitchConnCallingX121Addr": accX25SwitchConnCallingX121Addr,
       "accX25SwitchConnCallingPkts": accX25SwitchConnCallingPkts,
       "accX25SwitchConnCallingOctets": accX25SwitchConnCallingOctets,
       "accX25SwitchConnCalledIfIndex": accX25SwitchConnCalledIfIndex,
       "accX25SwitchConnCalledIndex": accX25SwitchConnCalledIndex,
       "accX25SwitchConnCalledType": accX25SwitchConnCalledType,
       "accX25SwitchConnCalledX121Addr": accX25SwitchConnCalledX121Addr,
       "accX25SwitchConnCalledPkts": accX25SwitchConnCalledPkts,
       "accX25SwitchConnCalledOctets": accX25SwitchConnCalledOctets,
       "accX25SwitchConnState": accX25SwitchConnState,
       "accX25SwitchAddrTransTable": accX25SwitchAddrTransTable,
       "accX25SwitchAddrTransEntry": accX25SwitchAddrTransEntry,
       "accX25SwitchAddrTransIfIndex": accX25SwitchAddrTransIfIndex,
       "accX25SwitchAddrTransDir": accX25SwitchAddrTransDir,
       "accX25SwitchAddrTransType": accX25SwitchAddrTransType,
       "accX25SwitchAddrTransPattern": accX25SwitchAddrTransPattern,
       "accX25SwitchAddrTransReplace": accX25SwitchAddrTransReplace,
       "accX25SwitchAddrTransStatus": accX25SwitchAddrTransStatus,
       "accX25SwitchRouteTable": accX25SwitchRouteTable,
       "accX25SwitchRouteEntry": accX25SwitchRouteEntry,
       "accX25SwitchRoutePattern": accX25SwitchRoutePattern,
       "accX25SwitchRouteIfIndex": accX25SwitchRouteIfIndex,
       "accX25SwitchRouteStatus": accX25SwitchRouteStatus,
       "accX25SwitchExtRtTable": accX25SwitchExtRtTable,
       "accX25SwitchExtRtEntry": accX25SwitchExtRtEntry,
       "accX25SwitchExtRtIndex": accX25SwitchExtRtIndex,
       "accX25SwitchExtRtIfIn": accX25SwitchExtRtIfIn,
       "accX25SwitchExtRtAddr": accX25SwitchExtRtAddr,
       "accX25SwitchExtRtCUD": accX25SwitchExtRtCUD,
       "accX25SwitchExtRtDisp": accX25SwitchExtRtDisp,
       "accX25SwitchExtRtIfOut": accX25SwitchExtRtIfOut,
       "accX25SwitchExtRtStatus": accX25SwitchExtRtStatus,
       "accX25EventLogSize": accX25EventLogSize,
       "accX25EventTable": accX25EventTable,
       "accX25EventEntry": accX25EventEntry,
       "accX25EventSeq": accX25EventSeq,
       "accX25EventLine": accX25EventLine,
       "accX25EventLCID": accX25EventLCID,
       "accX25EventUpTime": accX25EventUpTime,
       "accX25EventCode": accX25EventCode,
       "accX25EventCause": accX25EventCause,
       "accX25EventDiag": accX25EventDiag,
       "accX25EventProtocol": accX25EventProtocol,
       "accX25EventPacket": accX25EventPacket,
       "accX25CircuitTable": accX25CircuitTable,
       "accX25CircuitEntry": accX25CircuitEntry,
       "accX25CircuitLine": accX25CircuitLine,
       "accX25CircuitLCID": accX25CircuitLCID,
       "accX25CircuitType": accX25CircuitType,
       "accX25CircuitRemoteAddr": accX25CircuitRemoteAddr,
       "accX25CircuitLocalAddr": accX25CircuitLocalAddr,
       "accX25CircuitState": accX25CircuitState,
       "accX25CircuitPktTimer": accX25CircuitPktTimer,
       "accX25CircuitPktRetry": accX25CircuitPktRetry,
       "accX25Xot": accX25Xot,
       "accX25XotParmTable": accX25XotParmTable,
       "accX25XotParmEntry": accX25XotParmEntry,
       "accX25XotParmLine": accX25XotParmLine,
       "accX25XotParmIpAddress": accX25XotParmIpAddress,
       "accX25XotParmMsgLevel": accX25XotParmMsgLevel,
       "accX25XotConnTable": accX25XotConnTable,
       "accX25XotConnEntry": accX25XotConnEntry,
       "accX25XotConnLine": accX25XotConnLine,
       "accX25XotConnLcn": accX25XotConnLcn,
       "accX25XotConnState": accX25XotConnState,
       "accX25XotConnType": accX25XotConnType,
       "accX25XotConnIpAddress": accX25XotConnIpAddress,
       "accX25XotConnTcpPortNumber": accX25XotConnTcpPortNumber,
       "accX25XotConnRemoteIpAddress": accX25XotConnRemoteIpAddress,
       "accX25XotConnRemoteTCPPortNumber": accX25XotConnRemoteTCPPortNumber,
       "accX25XotConnRcvEncaps": accX25XotConnRcvEncaps,
       "accX25XotConnXmtEncaps": accX25XotConnXmtEncaps,
       "accX25XotStatsTable": accX25XotStatsTable,
       "accX25XotStatsEntry": accX25XotStatsEntry,
       "accX25XotStatsLine": accX25XotStatsLine,
       "accX25XotStatsTotalConnections": accX25XotStatsTotalConnections,
       "accX25XotStatsActiveConnections": accX25XotStatsActiveConnections,
       "accX25XotStatsRcvInvalids": accX25XotStatsRcvInvalids,
       "accX25XotStatsGenClearReqs": accX25XotStatsGenClearReqs,
       "accX25XotStatsGenResetReqs": accX25XotStatsGenResetReqs,
       "accX25XotStatsGenPvcSetups": accX25XotStatsGenPvcSetups,
       "accX25XotStatsRcvValids": accX25XotStatsRcvValids,
       "accX25XotStatsXmtTotals": accX25XotStatsXmtTotals}
)
