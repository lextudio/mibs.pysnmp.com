# SNMP MIB module (ExpandAccelerator-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ExpandAccelerator-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:43:17 2024
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



class Enumerator00(Integer32):
    """Custom type Enumerator00 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )





class Enumerator01(Integer32):
    """Custom type Enumerator01 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("hdlc", 1),
          ("ppp", 0))
    )





class Enumerator02(Integer32):
    """Custom type Enumerator02 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 0))
    )





class Enumerator03(Integer32):
    """Custom type Enumerator03 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )





class Enumerator04(Integer32):
    """Custom type Enumerator04 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("hdlc", 1),
          ("ppp", 0))
    )





class Enumerator05(Integer32):
    """Custom type Enumerator05 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("off", 1),
          ("on", 0))
    )





class Enumerator06(Integer32):
    """Custom type Enumerator06 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("bit-16", 0),
          ("bit-32", 1))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Expand_ObjectIdentity = ObjectIdentity
expand = _Expand_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3405)
)
_Accelerator_ObjectIdentity = ObjectIdentity
accelerator = _Accelerator_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3405, 1)
)
_Acc4000_ObjectIdentity = ObjectIdentity
acc4000 = _Acc4000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3405, 1, 1)
)
_Accelerator_4000_series_Type = Unsigned32
_Accelerator_4000_series_Object = MibScalar
accelerator_4000_series = _Accelerator_4000_series_Object(
    (1, 3, 6, 1, 4, 1, 3405, 1, 1, 1),
    _Accelerator_4000_series_Type()
)
accelerator_4000_series.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accelerator_4000_series.setStatus("mandatory")
_Details_ObjectIdentity = ObjectIdentity
details = _Details_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3405, 1, 1, 2)
)
_DetailsInterfaceTable_Object = MibTable
detailsInterfaceTable = _DetailsInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 3405, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    detailsInterfaceTable.setStatus("mandatory")
_DetailsInterfaceEntry_Object = MibTableRow
detailsInterfaceEntry = _DetailsInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 3405, 1, 1, 2, 1, 1)
)
detailsInterfaceEntry.setIndexNames(
    (0, "ExpandAccelerator-MIB", "interfaceName"),
)
if mibBuilder.loadTexts:
    detailsInterfaceEntry.setStatus("mandatory")
_InterfaceName_Type = OctetString
_InterfaceName_Object = MibTableColumn
interfaceName = _InterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 3405, 1, 1, 2, 1, 1, 1),
    _InterfaceName_Type()
)
interfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceName.setStatus("mandatory")
_InterfaceStatus_Type = Enumerator00
_InterfaceStatus_Object = MibTableColumn
interfaceStatus = _InterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 3405, 1, 1, 2, 1, 1, 2),
    _InterfaceStatus_Type()
)
interfaceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceStatus.setStatus("mandatory")
_InterfaceCloackRate_Type = Integer32
_InterfaceCloackRate_Object = MibTableColumn
interfaceCloackRate = _InterfaceCloackRate_Object(
    (1, 3, 6, 1, 4, 1, 3405, 1, 1, 2, 1, 1, 3),
    _InterfaceCloackRate_Type()
)
interfaceCloackRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceCloackRate.setStatus("mandatory")
_InterfaceQueueMode_Type = Enumerator01
_InterfaceQueueMode_Object = MibTableColumn
interfaceQueueMode = _InterfaceQueueMode_Object(
    (1, 3, 6, 1, 4, 1, 3405, 1, 1, 2, 1, 1, 4),
    _InterfaceQueueMode_Type()
)
interfaceQueueMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceQueueMode.setStatus("mandatory")
_InterfaceFifoSystemLimits_Type = Unsigned32
_InterfaceFifoSystemLimits_Object = MibTableColumn
interfaceFifoSystemLimits = _InterfaceFifoSystemLimits_Object(
    (1, 3, 6, 1, 4, 1, 3405, 1, 1, 2, 1, 1, 5),
    _InterfaceFifoSystemLimits_Type()
)
interfaceFifoSystemLimits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceFifoSystemLimits.setStatus("mandatory")
_InterfaceFairQueueSystemLimits_Type = Unsigned32
_InterfaceFairQueueSystemLimits_Object = MibTableColumn
interfaceFairQueueSystemLimits = _InterfaceFairQueueSystemLimits_Object(
    (1, 3, 6, 1, 4, 1, 3405, 1, 1, 2, 1, 1, 6),
    _InterfaceFairQueueSystemLimits_Type()
)
interfaceFairQueueSystemLimits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceFairQueueSystemLimits.setStatus("mandatory")
_InterfaceFairQueueSessionLimits_Type = Unsigned32
_InterfaceFairQueueSessionLimits_Object = MibTableColumn
interfaceFairQueueSessionLimits = _InterfaceFairQueueSessionLimits_Object(
    (1, 3, 6, 1, 4, 1, 3405, 1, 1, 2, 1, 1, 7),
    _InterfaceFairQueueSessionLimits_Type()
)
interfaceFairQueueSessionLimits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceFairQueueSessionLimits.setStatus("mandatory")
_InterfaceIgnoreDCD_Type = Enumerator02
_InterfaceIgnoreDCD_Object = MibTableColumn
interfaceIgnoreDCD = _InterfaceIgnoreDCD_Object(
    (1, 3, 6, 1, 4, 1, 3405, 1, 1, 2, 1, 1, 8),
    _InterfaceIgnoreDCD_Type()
)
interfaceIgnoreDCD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceIgnoreDCD.setStatus("mandatory")
_InterfaceBandwidth_Type = Unsigned32
_InterfaceBandwidth_Object = MibTableColumn
interfaceBandwidth = _InterfaceBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 3405, 1, 1, 2, 1, 1, 9),
    _InterfaceBandwidth_Type()
)
interfaceBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceBandwidth.setStatus("mandatory")
_InterfaceCountersPeriod_Type = Unsigned32
_InterfaceCountersPeriod_Object = MibTableColumn
interfaceCountersPeriod = _InterfaceCountersPeriod_Object(
    (1, 3, 6, 1, 4, 1, 3405, 1, 1, 2, 1, 1, 10),
    _InterfaceCountersPeriod_Type()
)
interfaceCountersPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceCountersPeriod.setStatus("mandatory")
_InterfaceProtocolType_Type = Enumerator04
_InterfaceProtocolType_Object = MibTableColumn
interfaceProtocolType = _InterfaceProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 3405, 1, 1, 2, 1, 1, 11),
    _InterfaceProtocolType_Type()
)
interfaceProtocolType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceProtocolType.setStatus("mandatory")
_InterfaceDCDMode_Type = Enumerator05
_InterfaceDCDMode_Object = MibTableColumn
interfaceDCDMode = _InterfaceDCDMode_Object(
    (1, 3, 6, 1, 4, 1, 3405, 1, 1, 2, 1, 1, 12),
    _InterfaceDCDMode_Type()
)
interfaceDCDMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceDCDMode.setStatus("mandatory")
_InterfaceCRCMode_Type = Enumerator06
_InterfaceCRCMode_Object = MibTableColumn
interfaceCRCMode = _InterfaceCRCMode_Object(
    (1, 3, 6, 1, 4, 1, 3405, 1, 1, 2, 1, 1, 13),
    _InterfaceCRCMode_Type()
)
interfaceCRCMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceCRCMode.setStatus("mandatory")
_Statistics_ObjectIdentity = ObjectIdentity
statistics = _Statistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3405, 1, 1, 3)
)
_StatInterfaceTable_Object = MibTable
statInterfaceTable = _StatInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    statInterfaceTable.setStatus("mandatory")
_StatInterfaceEntry_Object = MibTableRow
statInterfaceEntry = _StatInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1)
)
statInterfaceEntry.setIndexNames(
    (0, "ExpandAccelerator-MIB", "interfaceName"),
)
if mibBuilder.loadTexts:
    statInterfaceEntry.setStatus("mandatory")
_InterfaceName2_Type = OctetString
_InterfaceName2_Object = MibScalar
interfaceName2 = _InterfaceName2_Object(
    (1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 1),
    _InterfaceName2_Type()
)
interfaceName2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceName2.setStatus("mandatory")
_SystemUpInBytes_Low_Type = Unsigned32
_SystemUpInBytes_Low_Object = MibScalar
systemUpInBytes_Low = _SystemUpInBytes_Low_Object(
    (1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 2),
    _SystemUpInBytes_Low_Type()
)
systemUpInBytes_Low.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemUpInBytes_Low.setStatus("mandatory")
_SystemUpInBytes_High_Type = Unsigned32
_SystemUpInBytes_High_Object = MibScalar
systemUpInBytes_High = _SystemUpInBytes_High_Object(
    (1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 3),
    _SystemUpInBytes_High_Type()
)
systemUpInBytes_High.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemUpInBytes_High.setStatus("mandatory")
_SystemUpInBytes_String_Type = OctetString
_SystemUpInBytes_String_Object = MibScalar
systemUpInBytes_String = _SystemUpInBytes_String_Object(
    (1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 4),
    _SystemUpInBytes_String_Type()
)
systemUpInBytes_String.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemUpInBytes_String.setStatus("mandatory")
_SystemUpInPackets_Low_Type = Unsigned32
_SystemUpInPackets_Low_Object = MibScalar
systemUpInPackets_Low = _SystemUpInPackets_Low_Object(
    (1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 5),
    _SystemUpInPackets_Low_Type()
)
systemUpInPackets_Low.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemUpInPackets_Low.setStatus("mandatory")
_SystemUpInPackets_High_Type = Unsigned32
_SystemUpInPackets_High_Object = MibScalar
systemUpInPackets_High = _SystemUpInPackets_High_Object(
    (1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 6),
    _SystemUpInPackets_High_Type()
)
systemUpInPackets_High.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemUpInPackets_High.setStatus("mandatory")
_SystemUpInPackets_String_Type = OctetString
_SystemUpInPackets_String_Object = MibScalar
systemUpInPackets_String = _SystemUpInPackets_String_Object(
    (1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 7),
    _SystemUpInPackets_String_Type()
)
systemUpInPackets_String.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemUpInPackets_String.setStatus("mandatory")
_SystemUpOutBytes_Low_Type = Unsigned32
_SystemUpOutBytes_Low_Object = MibScalar
systemUpOutBytes_Low = _SystemUpOutBytes_Low_Object(
    (1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 8),
    _SystemUpOutBytes_Low_Type()
)
systemUpOutBytes_Low.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemUpOutBytes_Low.setStatus("mandatory")
_SystemUpOutBytes_High_Type = Unsigned32
_SystemUpOutBytes_High_Object = MibScalar
systemUpOutBytes_High = _SystemUpOutBytes_High_Object(
    (1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 9),
    _SystemUpOutBytes_High_Type()
)
systemUpOutBytes_High.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemUpOutBytes_High.setStatus("mandatory")
_SystemUpOutBytes_String_Type = OctetString
_SystemUpOutBytes_String_Object = MibScalar
systemUpOutBytes_String = _SystemUpOutBytes_String_Object(
    (1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 10),
    _SystemUpOutBytes_String_Type()
)
systemUpOutBytes_String.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemUpOutBytes_String.setStatus("mandatory")
_SystemUpOutPackets_Low_Type = Unsigned32
_SystemUpOutPackets_Low_Object = MibScalar
systemUpOutPackets_Low = _SystemUpOutPackets_Low_Object(
    (1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 11),
    _SystemUpOutPackets_Low_Type()
)
systemUpOutPackets_Low.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemUpOutPackets_Low.setStatus("mandatory")
_SystemUpOutPackets_High_Type = Unsigned32
_SystemUpOutPackets_High_Object = MibScalar
systemUpOutPackets_High = _SystemUpOutPackets_High_Object(
    (1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 12),
    _SystemUpOutPackets_High_Type()
)
systemUpOutPackets_High.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemUpOutPackets_High.setStatus("mandatory")
_SystemUpOutPackets_String_Type = OctetString
_SystemUpOutPackets_String_Object = MibScalar
systemUpOutPackets_String = _SystemUpOutPackets_String_Object(
    (1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 13),
    _SystemUpOutPackets_String_Type()
)
systemUpOutPackets_String.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemUpOutPackets_String.setStatus("mandatory")
_SystemUpDroppedBytes_Low_Type = Unsigned32
_SystemUpDroppedBytes_Low_Object = MibScalar
systemUpDroppedBytes_Low = _SystemUpDroppedBytes_Low_Object(
    (1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 14),
    _SystemUpDroppedBytes_Low_Type()
)
systemUpDroppedBytes_Low.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemUpDroppedBytes_Low.setStatus("mandatory")
_SystemUpDroppedBytes_High_Type = Unsigned32
_SystemUpDroppedBytes_High_Object = MibScalar
systemUpDroppedBytes_High = _SystemUpDroppedBytes_High_Object(
    (1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 15),
    _SystemUpDroppedBytes_High_Type()
)
systemUpDroppedBytes_High.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemUpDroppedBytes_High.setStatus("mandatory")
_SystemUpDroppedBytes_String_Type = OctetString
_SystemUpDroppedBytes_String_Object = MibScalar
systemUpDroppedBytes_String = _SystemUpDroppedBytes_String_Object(
    (1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 16),
    _SystemUpDroppedBytes_String_Type()
)
systemUpDroppedBytes_String.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemUpDroppedBytes_String.setStatus("mandatory")
_SystemUpDroppedPackets_Low_Type = Unsigned32
_SystemUpDroppedPackets_Low_Object = MibScalar
systemUpDroppedPackets_Low = _SystemUpDroppedPackets_Low_Object(
    (1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 17),
    _SystemUpDroppedPackets_Low_Type()
)
systemUpDroppedPackets_Low.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemUpDroppedPackets_Low.setStatus("mandatory")
_SystemUpDroppedPackets_High_Type = Unsigned32
_SystemUpDroppedPackets_High_Object = MibScalar
systemUpDroppedPackets_High = _SystemUpDroppedPackets_High_Object(
    (1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 18),
    _SystemUpDroppedPackets_High_Type()
)
systemUpDroppedPackets_High.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemUpDroppedPackets_High.setStatus("mandatory")
_SystemUpDroppedPackets_String_Type = OctetString
_SystemUpDroppedPackets_String_Object = MibScalar
systemUpDroppedPackets_String = _SystemUpDroppedPackets_String_Object(
    (1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 19),
    _SystemUpDroppedPackets_String_Type()
)
systemUpDroppedPackets_String.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemUpDroppedPackets_String.setStatus("mandatory")
_SystemUpOverrunPackets_Low_Type = Unsigned32
_SystemUpOverrunPackets_Low_Object = MibScalar
systemUpOverrunPackets_Low = _SystemUpOverrunPackets_Low_Object(
    (1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 20),
    _SystemUpOverrunPackets_Low_Type()
)
systemUpOverrunPackets_Low.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemUpOverrunPackets_Low.setStatus("mandatory")
_SystemUpOverrunPackets_High_Type = Unsigned32
_SystemUpOverrunPackets_High_Object = MibScalar
systemUpOverrunPackets_High = _SystemUpOverrunPackets_High_Object(
    (1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 21),
    _SystemUpOverrunPackets_High_Type()
)
systemUpOverrunPackets_High.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemUpOverrunPackets_High.setStatus("mandatory")
_SystemUpOverrunPackets_String_Type = OctetString
_SystemUpOverrunPackets_String_Object = MibScalar
systemUpOverrunPackets_String = _SystemUpOverrunPackets_String_Object(
    (1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 22),
    _SystemUpOverrunPackets_String_Type()
)
systemUpOverrunPackets_String.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemUpOverrunPackets_String.setStatus("mandatory")
_SystemUpCrcErrors_Low_Type = Unsigned32
_SystemUpCrcErrors_Low_Object = MibScalar
systemUpCrcErrors_Low = _SystemUpCrcErrors_Low_Object(
    (1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 23),
    _SystemUpCrcErrors_Low_Type()
)
systemUpCrcErrors_Low.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemUpCrcErrors_Low.setStatus("mandatory")
_SystemUpCrcErrors_High_Type = Unsigned32
_SystemUpCrcErrors_High_Object = MibScalar
systemUpCrcErrors_High = _SystemUpCrcErrors_High_Object(
    (1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 24),
    _SystemUpCrcErrors_High_Type()
)
systemUpCrcErrors_High.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemUpCrcErrors_High.setStatus("mandatory")
_SystemUpCrcErrors_String_Type = OctetString
_SystemUpCrcErrors_String_Object = MibScalar
systemUpCrcErrors_String = _SystemUpCrcErrors_String_Object(
    (1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 25),
    _SystemUpCrcErrors_String_Type()
)
systemUpCrcErrors_String.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemUpCrcErrors_String.setStatus("mandatory")
_ClearCountersInBytes_Low_Type = Unsigned32
_ClearCountersInBytes_Low_Object = MibScalar
clearCountersInBytes_Low = _ClearCountersInBytes_Low_Object(
    (1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 26),
    _ClearCountersInBytes_Low_Type()
)
clearCountersInBytes_Low.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clearCountersInBytes_Low.setStatus("mandatory")
_ClearCountersInBytes_High_Type = Unsigned32
_ClearCountersInBytes_High_Object = MibScalar
clearCountersInBytes_High = _ClearCountersInBytes_High_Object(
    (1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 27),
    _ClearCountersInBytes_High_Type()
)
clearCountersInBytes_High.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clearCountersInBytes_High.setStatus("mandatory")
_ClearCountersInBytes_String_Type = OctetString
_ClearCountersInBytes_String_Object = MibScalar
clearCountersInBytes_String = _ClearCountersInBytes_String_Object(
    (1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 28),
    _ClearCountersInBytes_String_Type()
)
clearCountersInBytes_String.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clearCountersInBytes_String.setStatus("mandatory")
_ClearCountersInPackets_Low_Type = Unsigned32
_ClearCountersInPackets_Low_Object = MibScalar
clearCountersInPackets_Low = _ClearCountersInPackets_Low_Object(
    (1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 29),
    _ClearCountersInPackets_Low_Type()
)
clearCountersInPackets_Low.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clearCountersInPackets_Low.setStatus("mandatory")
_ClearCountersInPackets_High_Type = Unsigned32
_ClearCountersInPackets_High_Object = MibScalar
clearCountersInPackets_High = _ClearCountersInPackets_High_Object(
    (1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 30),
    _ClearCountersInPackets_High_Type()
)
clearCountersInPackets_High.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clearCountersInPackets_High.setStatus("mandatory")
_ClearCountersInPackets_String_Type = OctetString
_ClearCountersInPackets_String_Object = MibScalar
clearCountersInPackets_String = _ClearCountersInPackets_String_Object(
    (1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 31),
    _ClearCountersInPackets_String_Type()
)
clearCountersInPackets_String.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clearCountersInPackets_String.setStatus("mandatory")
_ClearCountersOutBytes_Low_Type = Unsigned32
_ClearCountersOutBytes_Low_Object = MibScalar
clearCountersOutBytes_Low = _ClearCountersOutBytes_Low_Object(
    (1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 32),
    _ClearCountersOutBytes_Low_Type()
)
clearCountersOutBytes_Low.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clearCountersOutBytes_Low.setStatus("mandatory")
_ClearCountersOutBytes_High_Type = Unsigned32
_ClearCountersOutBytes_High_Object = MibScalar
clearCountersOutBytes_High = _ClearCountersOutBytes_High_Object(
    (1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 33),
    _ClearCountersOutBytes_High_Type()
)
clearCountersOutBytes_High.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clearCountersOutBytes_High.setStatus("mandatory")
_ClearCountersOutBytes_String_Type = OctetString
_ClearCountersOutBytes_String_Object = MibScalar
clearCountersOutBytes_String = _ClearCountersOutBytes_String_Object(
    (1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 34),
    _ClearCountersOutBytes_String_Type()
)
clearCountersOutBytes_String.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clearCountersOutBytes_String.setStatus("mandatory")
_ClearCountersOutPackets_Low_Type = Unsigned32
_ClearCountersOutPackets_Low_Object = MibScalar
clearCountersOutPackets_Low = _ClearCountersOutPackets_Low_Object(
    (1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 35),
    _ClearCountersOutPackets_Low_Type()
)
clearCountersOutPackets_Low.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clearCountersOutPackets_Low.setStatus("mandatory")
_ClearCountersOutPackets_High_Type = Unsigned32
_ClearCountersOutPackets_High_Object = MibScalar
clearCountersOutPackets_High = _ClearCountersOutPackets_High_Object(
    (1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 36),
    _ClearCountersOutPackets_High_Type()
)
clearCountersOutPackets_High.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clearCountersOutPackets_High.setStatus("mandatory")
_ClearCountersOutPackets_String_Type = OctetString
_ClearCountersOutPackets_String_Object = MibScalar
clearCountersOutPackets_String = _ClearCountersOutPackets_String_Object(
    (1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 37),
    _ClearCountersOutPackets_String_Type()
)
clearCountersOutPackets_String.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clearCountersOutPackets_String.setStatus("mandatory")
_ClearCountersDroppedBytes_Low_Type = Unsigned32
_ClearCountersDroppedBytes_Low_Object = MibScalar
clearCountersDroppedBytes_Low = _ClearCountersDroppedBytes_Low_Object(
    (1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 38),
    _ClearCountersDroppedBytes_Low_Type()
)
clearCountersDroppedBytes_Low.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clearCountersDroppedBytes_Low.setStatus("mandatory")
_ClearCountersDroppedBytes_High_Type = Unsigned32
_ClearCountersDroppedBytes_High_Object = MibScalar
clearCountersDroppedBytes_High = _ClearCountersDroppedBytes_High_Object(
    (1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 39),
    _ClearCountersDroppedBytes_High_Type()
)
clearCountersDroppedBytes_High.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clearCountersDroppedBytes_High.setStatus("mandatory")
_ClearCountersDroppedBytes_String_Type = OctetString
_ClearCountersDroppedBytes_String_Object = MibScalar
clearCountersDroppedBytes_String = _ClearCountersDroppedBytes_String_Object(
    (1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 40),
    _ClearCountersDroppedBytes_String_Type()
)
clearCountersDroppedBytes_String.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clearCountersDroppedBytes_String.setStatus("mandatory")
_ClearCountersDroppedPackets_Low_Type = Unsigned32
_ClearCountersDroppedPackets_Low_Object = MibScalar
clearCountersDroppedPackets_Low = _ClearCountersDroppedPackets_Low_Object(
    (1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 41),
    _ClearCountersDroppedPackets_Low_Type()
)
clearCountersDroppedPackets_Low.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clearCountersDroppedPackets_Low.setStatus("mandatory")
_ClearCountersDroppedPackets_High_Type = Unsigned32
_ClearCountersDroppedPackets_High_Object = MibScalar
clearCountersDroppedPackets_High = _ClearCountersDroppedPackets_High_Object(
    (1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 42),
    _ClearCountersDroppedPackets_High_Type()
)
clearCountersDroppedPackets_High.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clearCountersDroppedPackets_High.setStatus("mandatory")
_ClearCountersDroppedPackets_String_Type = OctetString
_ClearCountersDroppedPackets_String_Object = MibScalar
clearCountersDroppedPackets_String = _ClearCountersDroppedPackets_String_Object(
    (1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 43),
    _ClearCountersDroppedPackets_String_Type()
)
clearCountersDroppedPackets_String.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clearCountersDroppedPackets_String.setStatus("mandatory")
_ClearCountersOverrunPackets_Low_Type = Unsigned32
_ClearCountersOverrunPackets_Low_Object = MibScalar
clearCountersOverrunPackets_Low = _ClearCountersOverrunPackets_Low_Object(
    (1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 44),
    _ClearCountersOverrunPackets_Low_Type()
)
clearCountersOverrunPackets_Low.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clearCountersOverrunPackets_Low.setStatus("mandatory")
_ClearCountersOverrunPackets_High_Type = Unsigned32
_ClearCountersOverrunPackets_High_Object = MibScalar
clearCountersOverrunPackets_High = _ClearCountersOverrunPackets_High_Object(
    (1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 45),
    _ClearCountersOverrunPackets_High_Type()
)
clearCountersOverrunPackets_High.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clearCountersOverrunPackets_High.setStatus("mandatory")
_ClearCountersOverrunPackets_String_Type = OctetString
_ClearCountersOverrunPackets_String_Object = MibScalar
clearCountersOverrunPackets_String = _ClearCountersOverrunPackets_String_Object(
    (1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 46),
    _ClearCountersOverrunPackets_String_Type()
)
clearCountersOverrunPackets_String.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clearCountersOverrunPackets_String.setStatus("mandatory")
_ClearCountersCrcErrors_Low_Type = Unsigned32
_ClearCountersCrcErrors_Low_Object = MibScalar
clearCountersCrcErrors_Low = _ClearCountersCrcErrors_Low_Object(
    (1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 47),
    _ClearCountersCrcErrors_Low_Type()
)
clearCountersCrcErrors_Low.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clearCountersCrcErrors_Low.setStatus("mandatory")
_ClearCountersCrcErrors_High_Type = Unsigned32
_ClearCountersCrcErrors_High_Object = MibScalar
clearCountersCrcErrors_High = _ClearCountersCrcErrors_High_Object(
    (1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 48),
    _ClearCountersCrcErrors_High_Type()
)
clearCountersCrcErrors_High.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clearCountersCrcErrors_High.setStatus("mandatory")
_ClearCountersCrcErrors_String_Type = OctetString
_ClearCountersCrcErrors_String_Object = MibScalar
clearCountersCrcErrors_String = _ClearCountersCrcErrors_String_Object(
    (1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 49),
    _ClearCountersCrcErrors_String_Type()
)
clearCountersCrcErrors_String.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clearCountersCrcErrors_String.setStatus("mandatory")
_CountersPeriodBytesInPerSec_Type = Unsigned32
_CountersPeriodBytesInPerSec_Object = MibTableColumn
countersPeriodBytesInPerSec = _CountersPeriodBytesInPerSec_Object(
    (1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 50),
    _CountersPeriodBytesInPerSec_Type()
)
countersPeriodBytesInPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    countersPeriodBytesInPerSec.setStatus("mandatory")
_CountersPeriodPacketsInPerSec_Type = Unsigned32
_CountersPeriodPacketsInPerSec_Object = MibTableColumn
countersPeriodPacketsInPerSec = _CountersPeriodPacketsInPerSec_Object(
    (1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 51),
    _CountersPeriodPacketsInPerSec_Type()
)
countersPeriodPacketsInPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    countersPeriodPacketsInPerSec.setStatus("mandatory")
_CountersPeriodBytesOutPerSec_Type = Unsigned32
_CountersPeriodBytesOutPerSec_Object = MibTableColumn
countersPeriodBytesOutPerSec = _CountersPeriodBytesOutPerSec_Object(
    (1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 52),
    _CountersPeriodBytesOutPerSec_Type()
)
countersPeriodBytesOutPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    countersPeriodBytesOutPerSec.setStatus("mandatory")
_CountersPeriodPacketsOutPerSec_Type = Unsigned32
_CountersPeriodPacketsOutPerSec_Object = MibTableColumn
countersPeriodPacketsOutPerSec = _CountersPeriodPacketsOutPerSec_Object(
    (1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 53),
    _CountersPeriodPacketsOutPerSec_Type()
)
countersPeriodPacketsOutPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    countersPeriodPacketsOutPerSec.setStatus("mandatory")
_CountersPeriodDroppedBytes_Type = Unsigned32
_CountersPeriodDroppedBytes_Object = MibTableColumn
countersPeriodDroppedBytes = _CountersPeriodDroppedBytes_Object(
    (1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 54),
    _CountersPeriodDroppedBytes_Type()
)
countersPeriodDroppedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    countersPeriodDroppedBytes.setStatus("mandatory")
_CountersPeriodDroppedPackets_Type = Unsigned32
_CountersPeriodDroppedPackets_Object = MibTableColumn
countersPeriodDroppedPackets = _CountersPeriodDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 55),
    _CountersPeriodDroppedPackets_Type()
)
countersPeriodDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    countersPeriodDroppedPackets.setStatus("mandatory")
_CountersPeriodOverrunPackets_Type = Unsigned32
_CountersPeriodOverrunPackets_Object = MibTableColumn
countersPeriodOverrunPackets = _CountersPeriodOverrunPackets_Object(
    (1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 56),
    _CountersPeriodOverrunPackets_Type()
)
countersPeriodOverrunPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    countersPeriodOverrunPackets.setStatus("mandatory")
_CountersPeriodCrcErrors_Type = Unsigned32
_CountersPeriodCrcErrors_Object = MibTableColumn
countersPeriodCrcErrors = _CountersPeriodCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 3405, 1, 1, 3, 1, 1, 57),
    _CountersPeriodCrcErrors_Type()
)
countersPeriodCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    countersPeriodCrcErrors.setStatus("mandatory")
_Acceleration_ObjectIdentity = ObjectIdentity
acceleration = _Acceleration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3405, 1, 1, 4)
)
_Local_ObjectIdentity = ObjectIdentity
local = _Local_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3405, 1, 1, 4, 1)
)
_AclSystemUp_Type = Unsigned32
_AclSystemUp_Object = MibScalar
aclSystemUp = _AclSystemUp_Object(
    (1, 3, 6, 1, 4, 1, 3405, 1, 1, 4, 1, 1),
    _AclSystemUp_Type()
)
aclSystemUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclSystemUp.setStatus("mandatory")
_AclSinceClear_Type = Unsigned32
_AclSinceClear_Object = MibScalar
aclSinceClear = _AclSinceClear_Object(
    (1, 3, 6, 1, 4, 1, 3405, 1, 1, 4, 1, 2),
    _AclSinceClear_Type()
)
aclSinceClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclSinceClear.setStatus("mandatory")
_AclLastPeriod_Type = Unsigned32
_AclLastPeriod_Object = MibScalar
aclLastPeriod = _AclLastPeriod_Object(
    (1, 3, 6, 1, 4, 1, 3405, 1, 1, 4, 1, 3),
    _AclLastPeriod_Type()
)
aclLastPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclLastPeriod.setStatus("mandatory")
_Remote_ObjectIdentity = ObjectIdentity
remote = _Remote_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3405, 1, 1, 4, 2)
)
_AcrSystemUp_Type = Unsigned32
_AcrSystemUp_Object = MibScalar
acrSystemUp = _AcrSystemUp_Object(
    (1, 3, 6, 1, 4, 1, 3405, 1, 1, 4, 2, 1),
    _AcrSystemUp_Type()
)
acrSystemUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acrSystemUp.setStatus("mandatory")
_AcrSinceClear_Type = Unsigned32
_AcrSinceClear_Object = MibScalar
acrSinceClear = _AcrSinceClear_Object(
    (1, 3, 6, 1, 4, 1, 3405, 1, 1, 4, 2, 2),
    _AcrSinceClear_Type()
)
acrSinceClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acrSinceClear.setStatus("mandatory")
_AcrLastPeriod_Type = Unsigned32
_AcrLastPeriod_Object = MibScalar
acrLastPeriod = _AcrLastPeriod_Object(
    (1, 3, 6, 1, 4, 1, 3405, 1, 1, 4, 2, 3),
    _AcrLastPeriod_Type()
)
acrLastPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acrLastPeriod.setStatus("mandatory")
_AccPeriod_Type = Unsigned32
_AccPeriod_Object = MibScalar
accPeriod = _AccPeriod_Object(
    (1, 3, 6, 1, 4, 1, 3405, 1, 1, 4, 3),
    _AccPeriod_Type()
)
accPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPeriod.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ExpandAccelerator-MIB",
    **{"Enumerator00": Enumerator00,
       "Enumerator01": Enumerator01,
       "Enumerator02": Enumerator02,
       "Enumerator03": Enumerator03,
       "Enumerator04": Enumerator04,
       "Enumerator05": Enumerator05,
       "Enumerator06": Enumerator06,
       "expand": expand,
       "accelerator": accelerator,
       "acc4000": acc4000,
       "accelerator-4000-series": accelerator_4000_series,
       "details": details,
       "detailsInterfaceTable": detailsInterfaceTable,
       "detailsInterfaceEntry": detailsInterfaceEntry,
       "interfaceName": interfaceName,
       "interfaceStatus": interfaceStatus,
       "interfaceCloackRate": interfaceCloackRate,
       "interfaceQueueMode": interfaceQueueMode,
       "interfaceFifoSystemLimits": interfaceFifoSystemLimits,
       "interfaceFairQueueSystemLimits": interfaceFairQueueSystemLimits,
       "interfaceFairQueueSessionLimits": interfaceFairQueueSessionLimits,
       "interfaceIgnoreDCD": interfaceIgnoreDCD,
       "interfaceBandwidth": interfaceBandwidth,
       "interfaceCountersPeriod": interfaceCountersPeriod,
       "interfaceProtocolType": interfaceProtocolType,
       "interfaceDCDMode": interfaceDCDMode,
       "interfaceCRCMode": interfaceCRCMode,
       "statistics": statistics,
       "statInterfaceTable": statInterfaceTable,
       "statInterfaceEntry": statInterfaceEntry,
       "interfaceName2": interfaceName2,
       "systemUpInBytes-Low": systemUpInBytes_Low,
       "systemUpInBytes-High": systemUpInBytes_High,
       "systemUpInBytes-String": systemUpInBytes_String,
       "systemUpInPackets-Low": systemUpInPackets_Low,
       "systemUpInPackets-High": systemUpInPackets_High,
       "systemUpInPackets-String": systemUpInPackets_String,
       "systemUpOutBytes-Low": systemUpOutBytes_Low,
       "systemUpOutBytes-High": systemUpOutBytes_High,
       "systemUpOutBytes-String": systemUpOutBytes_String,
       "systemUpOutPackets-Low": systemUpOutPackets_Low,
       "systemUpOutPackets-High": systemUpOutPackets_High,
       "systemUpOutPackets-String": systemUpOutPackets_String,
       "systemUpDroppedBytes-Low": systemUpDroppedBytes_Low,
       "systemUpDroppedBytes-High": systemUpDroppedBytes_High,
       "systemUpDroppedBytes-String": systemUpDroppedBytes_String,
       "systemUpDroppedPackets-Low": systemUpDroppedPackets_Low,
       "systemUpDroppedPackets-High": systemUpDroppedPackets_High,
       "systemUpDroppedPackets-String": systemUpDroppedPackets_String,
       "systemUpOverrunPackets-Low": systemUpOverrunPackets_Low,
       "systemUpOverrunPackets-High": systemUpOverrunPackets_High,
       "systemUpOverrunPackets-String": systemUpOverrunPackets_String,
       "systemUpCrcErrors-Low": systemUpCrcErrors_Low,
       "systemUpCrcErrors-High": systemUpCrcErrors_High,
       "systemUpCrcErrors-String": systemUpCrcErrors_String,
       "clearCountersInBytes-Low": clearCountersInBytes_Low,
       "clearCountersInBytes-High": clearCountersInBytes_High,
       "clearCountersInBytes-String": clearCountersInBytes_String,
       "clearCountersInPackets-Low": clearCountersInPackets_Low,
       "clearCountersInPackets-High": clearCountersInPackets_High,
       "clearCountersInPackets-String": clearCountersInPackets_String,
       "clearCountersOutBytes-Low": clearCountersOutBytes_Low,
       "clearCountersOutBytes-High": clearCountersOutBytes_High,
       "clearCountersOutBytes-String": clearCountersOutBytes_String,
       "clearCountersOutPackets-Low": clearCountersOutPackets_Low,
       "clearCountersOutPackets-High": clearCountersOutPackets_High,
       "clearCountersOutPackets-String": clearCountersOutPackets_String,
       "clearCountersDroppedBytes-Low": clearCountersDroppedBytes_Low,
       "clearCountersDroppedBytes-High": clearCountersDroppedBytes_High,
       "clearCountersDroppedBytes-String": clearCountersDroppedBytes_String,
       "clearCountersDroppedPackets-Low": clearCountersDroppedPackets_Low,
       "clearCountersDroppedPackets-High": clearCountersDroppedPackets_High,
       "clearCountersDroppedPackets-String": clearCountersDroppedPackets_String,
       "clearCountersOverrunPackets-Low": clearCountersOverrunPackets_Low,
       "clearCountersOverrunPackets-High": clearCountersOverrunPackets_High,
       "clearCountersOverrunPackets-String": clearCountersOverrunPackets_String,
       "clearCountersCrcErrors-Low": clearCountersCrcErrors_Low,
       "clearCountersCrcErrors-High": clearCountersCrcErrors_High,
       "clearCountersCrcErrors-String": clearCountersCrcErrors_String,
       "countersPeriodBytesInPerSec": countersPeriodBytesInPerSec,
       "countersPeriodPacketsInPerSec": countersPeriodPacketsInPerSec,
       "countersPeriodBytesOutPerSec": countersPeriodBytesOutPerSec,
       "countersPeriodPacketsOutPerSec": countersPeriodPacketsOutPerSec,
       "countersPeriodDroppedBytes": countersPeriodDroppedBytes,
       "countersPeriodDroppedPackets": countersPeriodDroppedPackets,
       "countersPeriodOverrunPackets": countersPeriodOverrunPackets,
       "countersPeriodCrcErrors": countersPeriodCrcErrors,
       "acceleration": acceleration,
       "local": local,
       "aclSystemUp": aclSystemUp,
       "aclSinceClear": aclSinceClear,
       "aclLastPeriod": aclLastPeriod,
       "remote": remote,
       "acrSystemUp": acrSystemUp,
       "acrSinceClear": acrSinceClear,
       "acrLastPeriod": acrLastPeriod,
       "accPeriod": accPeriod}
)
