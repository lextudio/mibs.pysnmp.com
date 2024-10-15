# SNMP MIB module (CXBOPIO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CXBOPIO-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:20:07 2024
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

(Alias,
 cxBOPIO) = mibBuilder.importSymbols(
    "CXProduct-SMI",
    "Alias",
    "cxBOPIO")

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

_BopSapOprTable_Object = MibTable
bopSapOprTable = _BopSapOprTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 1)
)
if mibBuilder.loadTexts:
    bopSapOprTable.setStatus("mandatory")
_BopSapOprEntry_Object = MibTableRow
bopSapOprEntry = _BopSapOprEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 1, 1)
)
bopSapOprEntry.setIndexNames(
    (0, "CXBOPIO-MIB", "bopSapOprNumber"),
)
if mibBuilder.loadTexts:
    bopSapOprEntry.setStatus("mandatory")
_BopSapOprNumber_Type = Integer32
_BopSapOprNumber_Object = MibTableColumn
bopSapOprNumber = _BopSapOprNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 1, 1, 1),
    _BopSapOprNumber_Type()
)
bopSapOprNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bopSapOprNumber.setStatus("mandatory")
_BopSapOprAlias_Type = Alias
_BopSapOprAlias_Object = MibTableColumn
bopSapOprAlias = _BopSapOprAlias_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 1, 1, 2),
    _BopSapOprAlias_Type()
)
bopSapOprAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bopSapOprAlias.setStatus("mandatory")


class _BopSapOprProtocol_Type(Integer32):
    """Custom type bopSapOprProtocol based on Integer32"""
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
        *(("borroughs", 3),
          ("bsc3270", 2),
          ("bsc3780", 5),
          ("hdlc", 1),
          ("sperry", 4))
    )


_BopSapOprProtocol_Type.__name__ = "Integer32"
_BopSapOprProtocol_Object = MibTableColumn
bopSapOprProtocol = _BopSapOprProtocol_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 1, 1, 3),
    _BopSapOprProtocol_Type()
)
bopSapOprProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bopSapOprProtocol.setStatus("mandatory")


class _BopSapOprPortClockSource_Type(Integer32):
    """Custom type bopSapOprPortClockSource based on Integer32"""
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
        *(("external", 2),
          ("internal", 1),
          ("slave", 4),
          ("split", 3))
    )


_BopSapOprPortClockSource_Type.__name__ = "Integer32"
_BopSapOprPortClockSource_Object = MibTableColumn
bopSapOprPortClockSource = _BopSapOprPortClockSource_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 1, 1, 5),
    _BopSapOprPortClockSource_Type()
)
bopSapOprPortClockSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bopSapOprPortClockSource.setStatus("mandatory")


class _BopSapOprPortSpeed_Type(Integer32):
    """Custom type bopSapOprPortSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(375, 2048000),
    )


_BopSapOprPortSpeed_Type.__name__ = "Integer32"
_BopSapOprPortSpeed_Object = MibTableColumn
bopSapOprPortSpeed = _BopSapOprPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 1, 1, 6),
    _BopSapOprPortSpeed_Type()
)
bopSapOprPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bopSapOprPortSpeed.setStatus("mandatory")


class _BopSapOprPortDuplex_Type(Integer32):
    """Custom type bopSapOprPortDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("full", 2),
          ("half", 1))
    )


_BopSapOprPortDuplex_Type.__name__ = "Integer32"
_BopSapOprPortDuplex_Object = MibTableColumn
bopSapOprPortDuplex = _BopSapOprPortDuplex_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 1, 1, 7),
    _BopSapOprPortDuplex_Type()
)
bopSapOprPortDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bopSapOprPortDuplex.setStatus("mandatory")


class _BopSapOprPortMaxFrameSize_Type(Integer32):
    """Custom type bopSapOprPortMaxFrameSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 9000),
    )


_BopSapOprPortMaxFrameSize_Type.__name__ = "Integer32"
_BopSapOprPortMaxFrameSize_Object = MibTableColumn
bopSapOprPortMaxFrameSize = _BopSapOprPortMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 1, 1, 8),
    _BopSapOprPortMaxFrameSize_Type()
)
bopSapOprPortMaxFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bopSapOprPortMaxFrameSize.setStatus("mandatory")


class _BopSapOprPortDataEncoding_Type(Integer32):
    """Custom type bopSapOprPortDataEncoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nrz", 1),
          ("nrzi-mark", 2),
          ("nrzi-space", 3))
    )


_BopSapOprPortDataEncoding_Type.__name__ = "Integer32"
_BopSapOprPortDataEncoding_Object = MibTableColumn
bopSapOprPortDataEncoding = _BopSapOprPortDataEncoding_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 1, 1, 9),
    _BopSapOprPortDataEncoding_Type()
)
bopSapOprPortDataEncoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bopSapOprPortDataEncoding.setStatus("mandatory")


class _BopSapOprPortIdleCondition_Type(Integer32):
    """Custom type bopSapOprPortIdleCondition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("as400", 3),
          ("flags", 1),
          ("marks", 2))
    )


_BopSapOprPortIdleCondition_Type.__name__ = "Integer32"
_BopSapOprPortIdleCondition_Object = MibTableColumn
bopSapOprPortIdleCondition = _BopSapOprPortIdleCondition_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 1, 1, 10),
    _BopSapOprPortIdleCondition_Type()
)
bopSapOprPortIdleCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bopSapOprPortIdleCondition.setStatus("mandatory")


class _BopSapOprPortPreAmbleLength_Type(Integer32):
    """Custom type bopSapOprPortPreAmbleLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_BopSapOprPortPreAmbleLength_Type.__name__ = "Integer32"
_BopSapOprPortPreAmbleLength_Object = MibTableColumn
bopSapOprPortPreAmbleLength = _BopSapOprPortPreAmbleLength_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 1, 1, 11),
    _BopSapOprPortPreAmbleLength_Type()
)
bopSapOprPortPreAmbleLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bopSapOprPortPreAmbleLength.setStatus("mandatory")


class _BopSapOprPortFlagSharing_Type(Integer32):
    """Custom type bopSapOprPortFlagSharing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BopSapOprPortFlagSharing_Type.__name__ = "Integer32"
_BopSapOprPortFlagSharing_Object = MibTableColumn
bopSapOprPortFlagSharing = _BopSapOprPortFlagSharing_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 1, 1, 12),
    _BopSapOprPortFlagSharing_Type()
)
bopSapOprPortFlagSharing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bopSapOprPortFlagSharing.setStatus("obsolete")


class _BopSapOprPortFilterMask_Type(Integer32):
    """Custom type bopSapOprPortFilterMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BopSapOprPortFilterMask_Type.__name__ = "Integer32"
_BopSapOprPortFilterMask_Object = MibTableColumn
bopSapOprPortFilterMask = _BopSapOprPortFilterMask_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 1, 1, 13),
    _BopSapOprPortFilterMask_Type()
)
bopSapOprPortFilterMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bopSapOprPortFilterMask.setStatus("obsolete")


class _BopSapOprPortFilterAddress1_Type(Integer32):
    """Custom type bopSapOprPortFilterAddress1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BopSapOprPortFilterAddress1_Type.__name__ = "Integer32"
_BopSapOprPortFilterAddress1_Object = MibTableColumn
bopSapOprPortFilterAddress1 = _BopSapOprPortFilterAddress1_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 1, 1, 14),
    _BopSapOprPortFilterAddress1_Type()
)
bopSapOprPortFilterAddress1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bopSapOprPortFilterAddress1.setStatus("obsolete")


class _BopSapOprPortFilterAddress2_Type(Integer32):
    """Custom type bopSapOprPortFilterAddress2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BopSapOprPortFilterAddress2_Type.__name__ = "Integer32"
_BopSapOprPortFilterAddress2_Object = MibTableColumn
bopSapOprPortFilterAddress2 = _BopSapOprPortFilterAddress2_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 1, 1, 15),
    _BopSapOprPortFilterAddress2_Type()
)
bopSapOprPortFilterAddress2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bopSapOprPortFilterAddress2.setStatus("obsolete")


class _BopSapOprPortFilterAddress3_Type(Integer32):
    """Custom type bopSapOprPortFilterAddress3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BopSapOprPortFilterAddress3_Type.__name__ = "Integer32"
_BopSapOprPortFilterAddress3_Object = MibTableColumn
bopSapOprPortFilterAddress3 = _BopSapOprPortFilterAddress3_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 1, 1, 16),
    _BopSapOprPortFilterAddress3_Type()
)
bopSapOprPortFilterAddress3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bopSapOprPortFilterAddress3.setStatus("obsolete")


class _BopSapOprPortFilterAddress4_Type(Integer32):
    """Custom type bopSapOprPortFilterAddress4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BopSapOprPortFilterAddress4_Type.__name__ = "Integer32"
_BopSapOprPortFilterAddress4_Object = MibTableColumn
bopSapOprPortFilterAddress4 = _BopSapOprPortFilterAddress4_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 1, 1, 17),
    _BopSapOprPortFilterAddress4_Type()
)
bopSapOprPortFilterAddress4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bopSapOprPortFilterAddress4.setStatus("obsolete")


class _BopSapOprPortCrc_Type(Integer32):
    """Custom type bopSapOprPortCrc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("crc-32", 2),
          ("crc-ccitt", 1))
    )


_BopSapOprPortCrc_Type.__name__ = "Integer32"
_BopSapOprPortCrc_Object = MibTableColumn
bopSapOprPortCrc = _BopSapOprPortCrc_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 1, 1, 18),
    _BopSapOprPortCrc_Type()
)
bopSapOprPortCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bopSapOprPortCrc.setStatus("obsolete")


class _BopSapOprPortDtrUpTimer_Type(Integer32):
    """Custom type bopSapOprPortDtrUpTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BopSapOprPortDtrUpTimer_Type.__name__ = "Integer32"
_BopSapOprPortDtrUpTimer_Object = MibTableColumn
bopSapOprPortDtrUpTimer = _BopSapOprPortDtrUpTimer_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 1, 1, 19),
    _BopSapOprPortDtrUpTimer_Type()
)
bopSapOprPortDtrUpTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bopSapOprPortDtrUpTimer.setStatus("mandatory")


class _BopSapOprPortTxWindow_Type(Integer32):
    """Custom type bopSapOprPortTxWindow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_BopSapOprPortTxWindow_Type.__name__ = "Integer32"
_BopSapOprPortTxWindow_Object = MibTableColumn
bopSapOprPortTxWindow = _BopSapOprPortTxWindow_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 1, 1, 20),
    _BopSapOprPortTxWindow_Type()
)
bopSapOprPortTxWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bopSapOprPortTxWindow.setStatus("mandatory")


class _BopSapOprPortDialMode_Type(Integer32):
    """Custom type bopSapOprPortDialMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dial-in-only", 1),
          ("dial-in-out", 3),
          ("dial-out-only", 2))
    )


_BopSapOprPortDialMode_Type.__name__ = "Integer32"
_BopSapOprPortDialMode_Object = MibTableColumn
bopSapOprPortDialMode = _BopSapOprPortDialMode_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 1, 1, 21),
    _BopSapOprPortDialMode_Type()
)
bopSapOprPortDialMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bopSapOprPortDialMode.setStatus("mandatory")


class _BopSapOprPortLoopback_Type(Integer32):
    """Custom type bopSapOprPortLoopback based on Integer32"""
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
        *(("both", 4),
          ("isdn-uif-external", 8),
          ("isdn-uif-framer", 7),
          ("isdn-uif-idl2", 6),
          ("isdn-uif-uif", 5),
          ("local", 2),
          ("none", 1),
          ("remote", 3))
    )


_BopSapOprPortLoopback_Type.__name__ = "Integer32"
_BopSapOprPortLoopback_Object = MibTableColumn
bopSapOprPortLoopback = _BopSapOprPortLoopback_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 1, 1, 28),
    _BopSapOprPortLoopback_Type()
)
bopSapOprPortLoopback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bopSapOprPortLoopback.setStatus("mandatory")


class _BopSapOprPortSignalSamplingPeriod_Type(Integer32):
    """Custom type bopSapOprPortSignalSamplingPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 100),
    )


_BopSapOprPortSignalSamplingPeriod_Type.__name__ = "Integer32"
_BopSapOprPortSignalSamplingPeriod_Object = MibTableColumn
bopSapOprPortSignalSamplingPeriod = _BopSapOprPortSignalSamplingPeriod_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 1, 1, 29),
    _BopSapOprPortSignalSamplingPeriod_Type()
)
bopSapOprPortSignalSamplingPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bopSapOprPortSignalSamplingPeriod.setStatus("mandatory")


class _BopSapOprPortDcdDtrSignalSamples_Type(Integer32):
    """Custom type bopSapOprPortDcdDtrSignalSamples based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_BopSapOprPortDcdDtrSignalSamples_Type.__name__ = "Integer32"
_BopSapOprPortDcdDtrSignalSamples_Object = MibTableColumn
bopSapOprPortDcdDtrSignalSamples = _BopSapOprPortDcdDtrSignalSamples_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 1, 1, 30),
    _BopSapOprPortDcdDtrSignalSamples_Type()
)
bopSapOprPortDcdDtrSignalSamples.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bopSapOprPortDcdDtrSignalSamples.setStatus("mandatory")


class _BopSapOprPortCtsRtsSignalSamples_Type(Integer32):
    """Custom type bopSapOprPortCtsRtsSignalSamples based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_BopSapOprPortCtsRtsSignalSamples_Type.__name__ = "Integer32"
_BopSapOprPortCtsRtsSignalSamples_Object = MibTableColumn
bopSapOprPortCtsRtsSignalSamples = _BopSapOprPortCtsRtsSignalSamples_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 1, 1, 31),
    _BopSapOprPortCtsRtsSignalSamples_Type()
)
bopSapOprPortCtsRtsSignalSamples.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bopSapOprPortCtsRtsSignalSamples.setStatus("mandatory")


class _BopSapOprPortDsrDrsSignalSamples_Type(Integer32):
    """Custom type bopSapOprPortDsrDrsSignalSamples based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_BopSapOprPortDsrDrsSignalSamples_Type.__name__ = "Integer32"
_BopSapOprPortDsrDrsSignalSamples_Object = MibTableColumn
bopSapOprPortDsrDrsSignalSamples = _BopSapOprPortDsrDrsSignalSamples_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 1, 1, 32),
    _BopSapOprPortDsrDrsSignalSamples_Type()
)
bopSapOprPortDsrDrsSignalSamples.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bopSapOprPortDsrDrsSignalSamples.setStatus("mandatory")


class _BopSapOprPortTmLlSignalSamples_Type(Integer32):
    """Custom type bopSapOprPortTmLlSignalSamples based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_BopSapOprPortTmLlSignalSamples_Type.__name__ = "Integer32"
_BopSapOprPortTmLlSignalSamples_Object = MibTableColumn
bopSapOprPortTmLlSignalSamples = _BopSapOprPortTmLlSignalSamples_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 1, 1, 33),
    _BopSapOprPortTmLlSignalSamples_Type()
)
bopSapOprPortTmLlSignalSamples.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bopSapOprPortTmLlSignalSamples.setStatus("mandatory")


class _BopSapOprPortRiRlSignalSamples_Type(Integer32):
    """Custom type bopSapOprPortRiRlSignalSamples based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_BopSapOprPortRiRlSignalSamples_Type.__name__ = "Integer32"
_BopSapOprPortRiRlSignalSamples_Object = MibTableColumn
bopSapOprPortRiRlSignalSamples = _BopSapOprPortRiRlSignalSamples_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 1, 1, 34),
    _BopSapOprPortRiRlSignalSamples_Type()
)
bopSapOprPortRiRlSignalSamples.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bopSapOprPortRiRlSignalSamples.setStatus("mandatory")


class _BopSapOprPortStatisticsTimer_Type(Integer32):
    """Custom type bopSapOprPortStatisticsTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_BopSapOprPortStatisticsTimer_Type.__name__ = "Integer32"
_BopSapOprPortStatisticsTimer_Object = MibTableColumn
bopSapOprPortStatisticsTimer = _BopSapOprPortStatisticsTimer_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 1, 1, 35),
    _BopSapOprPortStatisticsTimer_Type()
)
bopSapOprPortStatisticsTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bopSapOprPortStatisticsTimer.setStatus("mandatory")


class _BopSapOprPortCarrierAction_Type(Integer32):
    """Custom type bopSapOprPortCarrierAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BopSapOprPortCarrierAction_Type.__name__ = "Integer32"
_BopSapOprPortCarrierAction_Object = MibTableColumn
bopSapOprPortCarrierAction = _BopSapOprPortCarrierAction_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 1, 1, 36),
    _BopSapOprPortCarrierAction_Type()
)
bopSapOprPortCarrierAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bopSapOprPortCarrierAction.setStatus("mandatory")


class _BopSapOprPortDataGenerator_Type(Integer32):
    """Custom type bopSapOprPortDataGenerator based on Integer32"""
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
        *(("disabled", 1),
          ("enabled", 2),
          ("enabled-verify", 3),
          ("retrigger", 4))
    )


_BopSapOprPortDataGenerator_Type.__name__ = "Integer32"
_BopSapOprPortDataGenerator_Object = MibTableColumn
bopSapOprPortDataGenerator = _BopSapOprPortDataGenerator_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 1, 1, 37),
    _BopSapOprPortDataGenerator_Type()
)
bopSapOprPortDataGenerator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bopSapOprPortDataGenerator.setStatus("mandatory")


class _BopSapOprPortGenFrames_Type(Integer32):
    """Custom type bopSapOprPortGenFrames based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BopSapOprPortGenFrames_Type.__name__ = "Integer32"
_BopSapOprPortGenFrames_Object = MibTableColumn
bopSapOprPortGenFrames = _BopSapOprPortGenFrames_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 1, 1, 38),
    _BopSapOprPortGenFrames_Type()
)
bopSapOprPortGenFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bopSapOprPortGenFrames.setStatus("mandatory")


class _BopSapOprPortGenFrameSize_Type(Integer32):
    """Custom type bopSapOprPortGenFrameSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 65535),
    )


_BopSapOprPortGenFrameSize_Type.__name__ = "Integer32"
_BopSapOprPortGenFrameSize_Object = MibTableColumn
bopSapOprPortGenFrameSize = _BopSapOprPortGenFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 1, 1, 39),
    _BopSapOprPortGenFrameSize_Type()
)
bopSapOprPortGenFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bopSapOprPortGenFrameSize.setStatus("mandatory")


class _BopSapOprPortGenFrameHeader_Type(Integer32):
    """Custom type bopSapOprPortGenFrameHeader based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BopSapOprPortGenFrameHeader_Type.__name__ = "Integer32"
_BopSapOprPortGenFrameHeader_Object = MibTableColumn
bopSapOprPortGenFrameHeader = _BopSapOprPortGenFrameHeader_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 1, 1, 40),
    _BopSapOprPortGenFrameHeader_Type()
)
bopSapOprPortGenFrameHeader.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bopSapOprPortGenFrameHeader.setStatus("mandatory")


class _BopSapOprPortThreshBandwidth_Type(Integer32):
    """Custom type bopSapOprPortThreshBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BopSapOprPortThreshBandwidth_Type.__name__ = "Integer32"
_BopSapOprPortThreshBandwidth_Object = MibTableColumn
bopSapOprPortThreshBandwidth = _BopSapOprPortThreshBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 1, 1, 41),
    _BopSapOprPortThreshBandwidth_Type()
)
bopSapOprPortThreshBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bopSapOprPortThreshBandwidth.setStatus("mandatory")


class _BopSapOprPortActualSpeed_Type(Integer32):
    """Custom type bopSapOprPortActualSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(375, 2048000),
    )


_BopSapOprPortActualSpeed_Type.__name__ = "Integer32"
_BopSapOprPortActualSpeed_Object = MibTableColumn
bopSapOprPortActualSpeed = _BopSapOprPortActualSpeed_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 1, 1, 42),
    _BopSapOprPortActualSpeed_Type()
)
bopSapOprPortActualSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bopSapOprPortActualSpeed.setStatus("mandatory")


class _BopSapOprCodeSet_Type(Integer32):
    """Custom type bopSapOprCodeSet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ascii", 2),
          ("ebcdic", 1))
    )


_BopSapOprCodeSet_Type.__name__ = "Integer32"
_BopSapOprCodeSet_Object = MibTableColumn
bopSapOprCodeSet = _BopSapOprCodeSet_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 1, 1, 43),
    _BopSapOprCodeSet_Type()
)
bopSapOprCodeSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bopSapOprCodeSet.setStatus("mandatory")


class _BopSapOprParity_Type(Integer32):
    """Custom type bopSapOprParity based on Integer32"""
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
        *(("even", 3),
          ("mark", 5),
          ("none", 1),
          ("odd", 2),
          ("space", 4))
    )


_BopSapOprParity_Type.__name__ = "Integer32"
_BopSapOprParity_Object = MibTableColumn
bopSapOprParity = _BopSapOprParity_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 1, 1, 44),
    _BopSapOprParity_Type()
)
bopSapOprParity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bopSapOprParity.setStatus("mandatory")


class _BopOprPortTrap_Type(Integer32):
    """Custom type bopOprPortTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BopOprPortTrap_Type.__name__ = "Integer32"
_BopOprPortTrap_Object = MibTableColumn
bopOprPortTrap = _BopOprPortTrap_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 1, 1, 47),
    _BopOprPortTrap_Type()
)
bopOprPortTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bopOprPortTrap.setStatus("mandatory")


class _BopOprTxClockTrap_Type(Integer32):
    """Custom type bopOprTxClockTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BopOprTxClockTrap_Type.__name__ = "Integer32"
_BopOprTxClockTrap_Object = MibTableColumn
bopOprTxClockTrap = _BopOprTxClockTrap_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 1, 1, 48),
    _BopOprTxClockTrap_Type()
)
bopOprTxClockTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bopOprTxClockTrap.setStatus("mandatory")


class _BopOprControlLine_Type(Integer32):
    """Custom type bopOprControlLine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("forceDown", 1),
          ("forceReset", 3),
          ("forceUp", 2))
    )


_BopOprControlLine_Type.__name__ = "Integer32"
_BopOprControlLine_Object = MibTableColumn
bopOprControlLine = _BopOprControlLine_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 1, 1, 52),
    _BopOprControlLine_Type()
)
bopOprControlLine.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    bopOprControlLine.setStatus("mandatory")


class _BopOprControlStats_Type(Integer32):
    """Custom type bopOprControlStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clearSapStats", 1)
    )


_BopOprControlStats_Type.__name__ = "Integer32"
_BopOprControlStats_Object = MibTableColumn
bopOprControlStats = _BopOprControlStats_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 1, 1, 53),
    _BopOprControlStats_Type()
)
bopOprControlStats.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    bopOprControlStats.setStatus("mandatory")


class _BopStatOprPortType_Type(Integer32):
    """Custom type bopStatOprPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dce", 3),
          ("dte", 2),
          ("unknown", 1))
    )


_BopStatOprPortType_Type.__name__ = "Integer32"
_BopStatOprPortType_Object = MibTableColumn
bopStatOprPortType = _BopStatOprPortType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 1, 1, 55),
    _BopStatOprPortType_Type()
)
bopStatOprPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bopStatOprPortType.setStatus("mandatory")


class _BopStatOprPortInterfaceType_Type(Integer32):
    """Custom type bopStatOprPortInterfaceType based on Integer32"""
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
        *(("dds", 6),
          ("rs232d", 2),
          ("uif", 7),
          ("unknown", 1),
          ("v34", 5),
          ("v35", 3),
          ("v36", 8),
          ("x21", 4))
    )


_BopStatOprPortInterfaceType_Type.__name__ = "Integer32"
_BopStatOprPortInterfaceType_Object = MibTableColumn
bopStatOprPortInterfaceType = _BopStatOprPortInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 1, 1, 56),
    _BopStatOprPortInterfaceType_Type()
)
bopStatOprPortInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bopStatOprPortInterfaceType.setStatus("mandatory")


class _BopStatOprPortState_Type(Integer32):
    """Custom type bopStatOprPortState based on Integer32"""
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
        *(("portDown", 2),
          ("portDownBadConfiguration", 4),
          ("portOutOfOrder", 5),
          ("portShutDown", 3),
          ("portUp", 1))
    )


_BopStatOprPortState_Type.__name__ = "Integer32"
_BopStatOprPortState_Object = MibTableColumn
bopStatOprPortState = _BopStatOprPortState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 1, 1, 57),
    _BopStatOprPortState_Type()
)
bopStatOprPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bopStatOprPortState.setStatus("mandatory")


class _BopStatOprTxClockState_Type(Integer32):
    """Custom type bopStatOprTxClockState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("txClockDown", 1),
          ("txClockUp", 2))
    )


_BopStatOprTxClockState_Type.__name__ = "Integer32"
_BopStatOprTxClockState_Object = MibTableColumn
bopStatOprTxClockState = _BopStatOprTxClockState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 1, 1, 61),
    _BopStatOprTxClockState_Type()
)
bopStatOprTxClockState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bopStatOprTxClockState.setStatus("mandatory")


class _BopStatOprDCDState_Type(Integer32):
    """Custom type bopStatOprDCDState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 3),
          ("inactive", 2),
          ("unknown", 1))
    )


_BopStatOprDCDState_Type.__name__ = "Integer32"
_BopStatOprDCDState_Object = MibTableColumn
bopStatOprDCDState = _BopStatOprDCDState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 1, 1, 62),
    _BopStatOprDCDState_Type()
)
bopStatOprDCDState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bopStatOprDCDState.setStatus("mandatory")


class _BopStatOprDTRState_Type(Integer32):
    """Custom type bopStatOprDTRState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 3),
          ("inactive", 2),
          ("unknown", 1))
    )


_BopStatOprDTRState_Type.__name__ = "Integer32"
_BopStatOprDTRState_Object = MibTableColumn
bopStatOprDTRState = _BopStatOprDTRState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 1, 1, 63),
    _BopStatOprDTRState_Type()
)
bopStatOprDTRState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bopStatOprDTRState.setStatus("mandatory")


class _BopStatOprRTSState_Type(Integer32):
    """Custom type bopStatOprRTSState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 3),
          ("inactive", 2),
          ("unknown", 1))
    )


_BopStatOprRTSState_Type.__name__ = "Integer32"
_BopStatOprRTSState_Object = MibTableColumn
bopStatOprRTSState = _BopStatOprRTSState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 1, 1, 64),
    _BopStatOprRTSState_Type()
)
bopStatOprRTSState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bopStatOprRTSState.setStatus("mandatory")


class _BopStatOprCTSState_Type(Integer32):
    """Custom type bopStatOprCTSState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 3),
          ("inactive", 2),
          ("unknown", 1))
    )


_BopStatOprCTSState_Type.__name__ = "Integer32"
_BopStatOprCTSState_Object = MibTableColumn
bopStatOprCTSState = _BopStatOprCTSState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 1, 1, 65),
    _BopStatOprCTSState_Type()
)
bopStatOprCTSState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bopStatOprCTSState.setStatus("mandatory")


class _BopStatOprDSRState_Type(Integer32):
    """Custom type bopStatOprDSRState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 3),
          ("inactive", 2),
          ("unknown", 1))
    )


_BopStatOprDSRState_Type.__name__ = "Integer32"
_BopStatOprDSRState_Object = MibTableColumn
bopStatOprDSRState = _BopStatOprDSRState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 1, 1, 66),
    _BopStatOprDSRState_Type()
)
bopStatOprDSRState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bopStatOprDSRState.setStatus("mandatory")


class _BopStatOprDRSState_Type(Integer32):
    """Custom type bopStatOprDRSState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 3),
          ("inactive", 2),
          ("unknown", 1))
    )


_BopStatOprDRSState_Type.__name__ = "Integer32"
_BopStatOprDRSState_Object = MibTableColumn
bopStatOprDRSState = _BopStatOprDRSState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 1, 1, 67),
    _BopStatOprDRSState_Type()
)
bopStatOprDRSState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bopStatOprDRSState.setStatus("mandatory")


class _BopStatOprTMState_Type(Integer32):
    """Custom type bopStatOprTMState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 3),
          ("inactive", 2),
          ("unknown", 1))
    )


_BopStatOprTMState_Type.__name__ = "Integer32"
_BopStatOprTMState_Object = MibTableColumn
bopStatOprTMState = _BopStatOprTMState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 1, 1, 68),
    _BopStatOprTMState_Type()
)
bopStatOprTMState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bopStatOprTMState.setStatus("mandatory")


class _BopStatOprLLState_Type(Integer32):
    """Custom type bopStatOprLLState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 3),
          ("inactive", 2),
          ("unknown", 1))
    )


_BopStatOprLLState_Type.__name__ = "Integer32"
_BopStatOprLLState_Object = MibTableColumn
bopStatOprLLState = _BopStatOprLLState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 1, 1, 69),
    _BopStatOprLLState_Type()
)
bopStatOprLLState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bopStatOprLLState.setStatus("mandatory")


class _BopStatOprRIState_Type(Integer32):
    """Custom type bopStatOprRIState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 3),
          ("inactive", 2),
          ("unknown", 1))
    )


_BopStatOprRIState_Type.__name__ = "Integer32"
_BopStatOprRIState_Object = MibTableColumn
bopStatOprRIState = _BopStatOprRIState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 1, 1, 70),
    _BopStatOprRIState_Type()
)
bopStatOprRIState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bopStatOprRIState.setStatus("mandatory")


class _BopStatOprRLState_Type(Integer32):
    """Custom type bopStatOprRLState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 3),
          ("inactive", 2),
          ("unknown", 1))
    )


_BopStatOprRLState_Type.__name__ = "Integer32"
_BopStatOprRLState_Object = MibTableColumn
bopStatOprRLState = _BopStatOprRLState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 1, 1, 71),
    _BopStatOprRLState_Type()
)
bopStatOprRLState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bopStatOprRLState.setStatus("mandatory")
_BopStatOprTxFrames_Type = Counter32
_BopStatOprTxFrames_Object = MibTableColumn
bopStatOprTxFrames = _BopStatOprTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 1, 1, 75),
    _BopStatOprTxFrames_Type()
)
bopStatOprTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bopStatOprTxFrames.setStatus("mandatory")
_BopStatOprRxFrames_Type = Counter32
_BopStatOprRxFrames_Object = MibTableColumn
bopStatOprRxFrames = _BopStatOprRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 1, 1, 76),
    _BopStatOprRxFrames_Type()
)
bopStatOprRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bopStatOprRxFrames.setStatus("mandatory")
_BopStatOprLocalLoopbackFrames_Type = Counter32
_BopStatOprLocalLoopbackFrames_Object = MibTableColumn
bopStatOprLocalLoopbackFrames = _BopStatOprLocalLoopbackFrames_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 1, 1, 77),
    _BopStatOprLocalLoopbackFrames_Type()
)
bopStatOprLocalLoopbackFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bopStatOprLocalLoopbackFrames.setStatus("mandatory")
_BopStatOprTxBps_Type = Counter32
_BopStatOprTxBps_Object = MibTableColumn
bopStatOprTxBps = _BopStatOprTxBps_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 1, 1, 78),
    _BopStatOprTxBps_Type()
)
bopStatOprTxBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bopStatOprTxBps.setStatus("mandatory")
_BopStatOprRxBps_Type = Counter32
_BopStatOprRxBps_Object = MibTableColumn
bopStatOprRxBps = _BopStatOprRxBps_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 1, 1, 79),
    _BopStatOprRxBps_Type()
)
bopStatOprRxBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bopStatOprRxBps.setStatus("mandatory")
_BopStatOprTxBpsMax_Type = Counter32
_BopStatOprTxBpsMax_Object = MibTableColumn
bopStatOprTxBpsMax = _BopStatOprTxBpsMax_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 1, 1, 80),
    _BopStatOprTxBpsMax_Type()
)
bopStatOprTxBpsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bopStatOprTxBpsMax.setStatus("mandatory")
_BopStatOprRxBpsMax_Type = Counter32
_BopStatOprRxBpsMax_Object = MibTableColumn
bopStatOprRxBpsMax = _BopStatOprRxBpsMax_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 1, 1, 81),
    _BopStatOprRxBpsMax_Type()
)
bopStatOprRxBpsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bopStatOprRxBpsMax.setStatus("mandatory")
_BopStatOprTxFps_Type = Counter32
_BopStatOprTxFps_Object = MibTableColumn
bopStatOprTxFps = _BopStatOprTxFps_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 1, 1, 82),
    _BopStatOprTxFps_Type()
)
bopStatOprTxFps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bopStatOprTxFps.setStatus("mandatory")
_BopStatOprRxFps_Type = Counter32
_BopStatOprRxFps_Object = MibTableColumn
bopStatOprRxFps = _BopStatOprRxFps_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 1, 1, 83),
    _BopStatOprRxFps_Type()
)
bopStatOprRxFps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bopStatOprRxFps.setStatus("mandatory")
_BopStatOprTxFpsMax_Type = Counter32
_BopStatOprTxFpsMax_Object = MibTableColumn
bopStatOprTxFpsMax = _BopStatOprTxFpsMax_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 1, 1, 84),
    _BopStatOprTxFpsMax_Type()
)
bopStatOprTxFpsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bopStatOprTxFpsMax.setStatus("mandatory")
_BopStatOprRxFpsMax_Type = Counter32
_BopStatOprRxFpsMax_Object = MibTableColumn
bopStatOprRxFpsMax = _BopStatOprRxFpsMax_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 1, 1, 85),
    _BopStatOprRxFpsMax_Type()
)
bopStatOprRxFpsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bopStatOprRxFpsMax.setStatus("mandatory")
_BopStatOprTxUnderrunFrames_Type = Counter32
_BopStatOprTxUnderrunFrames_Object = MibTableColumn
bopStatOprTxUnderrunFrames = _BopStatOprTxUnderrunFrames_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 1, 1, 86),
    _BopStatOprTxUnderrunFrames_Type()
)
bopStatOprTxUnderrunFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bopStatOprTxUnderrunFrames.setStatus("mandatory")
_BopStatOprTxCtsLostFrames_Type = Counter32
_BopStatOprTxCtsLostFrames_Object = MibTableColumn
bopStatOprTxCtsLostFrames = _BopStatOprTxCtsLostFrames_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 1, 1, 87),
    _BopStatOprTxCtsLostFrames_Type()
)
bopStatOprTxCtsLostFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bopStatOprTxCtsLostFrames.setStatus("mandatory")
_BopStatOprTxBadStateDiscards_Type = Counter32
_BopStatOprTxBadStateDiscards_Object = MibTableColumn
bopStatOprTxBadStateDiscards = _BopStatOprTxBadStateDiscards_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 1, 1, 88),
    _BopStatOprTxBadStateDiscards_Type()
)
bopStatOprTxBadStateDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bopStatOprTxBadStateDiscards.setStatus("mandatory")
_BopStatOprTxResetDiscards_Type = Counter32
_BopStatOprTxResetDiscards_Object = MibTableColumn
bopStatOprTxResetDiscards = _BopStatOprTxResetDiscards_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 1, 1, 89),
    _BopStatOprTxResetDiscards_Type()
)
bopStatOprTxResetDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bopStatOprTxResetDiscards.setStatus("mandatory")
_BopStatOprTxSysCongestionDiscards_Type = Counter32
_BopStatOprTxSysCongestionDiscards_Object = MibTableColumn
bopStatOprTxSysCongestionDiscards = _BopStatOprTxSysCongestionDiscards_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 1, 1, 90),
    _BopStatOprTxSysCongestionDiscards_Type()
)
bopStatOprTxSysCongestionDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bopStatOprTxSysCongestionDiscards.setStatus("mandatory")
_BopStatOprTxInvWinDiscards_Type = Counter32
_BopStatOprTxInvWinDiscards_Object = MibTableColumn
bopStatOprTxInvWinDiscards = _BopStatOprTxInvWinDiscards_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 1, 1, 91),
    _BopStatOprTxInvWinDiscards_Type()
)
bopStatOprTxInvWinDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bopStatOprTxInvWinDiscards.setStatus("mandatory")
_BopStatOprTxInvRLpbkWinDiscards_Type = Counter32
_BopStatOprTxInvRLpbkWinDiscards_Object = MibTableColumn
bopStatOprTxInvRLpbkWinDiscards = _BopStatOprTxInvRLpbkWinDiscards_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 1, 1, 92),
    _BopStatOprTxInvRLpbkWinDiscards_Type()
)
bopStatOprTxInvRLpbkWinDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bopStatOprTxInvRLpbkWinDiscards.setStatus("mandatory")
_BopStatOprRxBadCrcFrames_Type = Counter32
_BopStatOprRxBadCrcFrames_Object = MibTableColumn
bopStatOprRxBadCrcFrames = _BopStatOprRxBadCrcFrames_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 1, 1, 98),
    _BopStatOprRxBadCrcFrames_Type()
)
bopStatOprRxBadCrcFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bopStatOprRxBadCrcFrames.setStatus("mandatory")
_BopStatOprRxAbortedFrames_Type = Counter32
_BopStatOprRxAbortedFrames_Object = MibTableColumn
bopStatOprRxAbortedFrames = _BopStatOprRxAbortedFrames_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 1, 1, 99),
    _BopStatOprRxAbortedFrames_Type()
)
bopStatOprRxAbortedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bopStatOprRxAbortedFrames.setStatus("mandatory")
_BopStatOprRxNonIntegralBitFrames_Type = Counter32
_BopStatOprRxNonIntegralBitFrames_Object = MibTableColumn
bopStatOprRxNonIntegralBitFrames = _BopStatOprRxNonIntegralBitFrames_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 1, 1, 100),
    _BopStatOprRxNonIntegralBitFrames_Type()
)
bopStatOprRxNonIntegralBitFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bopStatOprRxNonIntegralBitFrames.setStatus("mandatory")
_BopStatOprRxLongFrames_Type = Counter32
_BopStatOprRxLongFrames_Object = MibTableColumn
bopStatOprRxLongFrames = _BopStatOprRxLongFrames_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 1, 1, 101),
    _BopStatOprRxLongFrames_Type()
)
bopStatOprRxLongFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bopStatOprRxLongFrames.setStatus("mandatory")
_BopStatOprRxOverrunFrames_Type = Counter32
_BopStatOprRxOverrunFrames_Object = MibTableColumn
bopStatOprRxOverrunFrames = _BopStatOprRxOverrunFrames_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 1, 1, 102),
    _BopStatOprRxOverrunFrames_Type()
)
bopStatOprRxOverrunFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bopStatOprRxOverrunFrames.setStatus("mandatory")
_BopStatOprRxCdLostFrames_Type = Counter32
_BopStatOprRxCdLostFrames_Object = MibTableColumn
bopStatOprRxCdLostFrames = _BopStatOprRxCdLostFrames_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 1, 1, 103),
    _BopStatOprRxCdLostFrames_Type()
)
bopStatOprRxCdLostFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bopStatOprRxCdLostFrames.setStatus("mandatory")
_BopStatOprRxBadStateDiscards_Type = Counter32
_BopStatOprRxBadStateDiscards_Object = MibTableColumn
bopStatOprRxBadStateDiscards = _BopStatOprRxBadStateDiscards_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 1, 1, 104),
    _BopStatOprRxBadStateDiscards_Type()
)
bopStatOprRxBadStateDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bopStatOprRxBadStateDiscards.setStatus("mandatory")
_BopStatOprRxBusyDiscards_Type = Counter32
_BopStatOprRxBusyDiscards_Object = MibTableColumn
bopStatOprRxBusyDiscards = _BopStatOprRxBusyDiscards_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 1, 1, 105),
    _BopStatOprRxBusyDiscards_Type()
)
bopStatOprRxBusyDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bopStatOprRxBusyDiscards.setStatus("mandatory")
_BopStatOprPortStateChanges_Type = Counter32
_BopStatOprPortStateChanges_Object = MibTableColumn
bopStatOprPortStateChanges = _BopStatOprPortStateChanges_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 1, 1, 109),
    _BopStatOprPortStateChanges_Type()
)
bopStatOprPortStateChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bopStatOprPortStateChanges.setStatus("mandatory")
_BopStatOprTxClockStateChanges_Type = Counter32
_BopStatOprTxClockStateChanges_Object = MibTableColumn
bopStatOprTxClockStateChanges = _BopStatOprTxClockStateChanges_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 1, 1, 110),
    _BopStatOprTxClockStateChanges_Type()
)
bopStatOprTxClockStateChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bopStatOprTxClockStateChanges.setStatus("mandatory")
_BopStatOprDCDStateChanges_Type = Counter32
_BopStatOprDCDStateChanges_Object = MibTableColumn
bopStatOprDCDStateChanges = _BopStatOprDCDStateChanges_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 1, 1, 111),
    _BopStatOprDCDStateChanges_Type()
)
bopStatOprDCDStateChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bopStatOprDCDStateChanges.setStatus("mandatory")
_BopStatOprDTRStateChanges_Type = Counter32
_BopStatOprDTRStateChanges_Object = MibTableColumn
bopStatOprDTRStateChanges = _BopStatOprDTRStateChanges_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 1, 1, 112),
    _BopStatOprDTRStateChanges_Type()
)
bopStatOprDTRStateChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bopStatOprDTRStateChanges.setStatus("mandatory")
_BopStatOprRTSStateChanges_Type = Counter32
_BopStatOprRTSStateChanges_Object = MibTableColumn
bopStatOprRTSStateChanges = _BopStatOprRTSStateChanges_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 1, 1, 113),
    _BopStatOprRTSStateChanges_Type()
)
bopStatOprRTSStateChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bopStatOprRTSStateChanges.setStatus("mandatory")
_BopStatOprCTSStateChanges_Type = Counter32
_BopStatOprCTSStateChanges_Object = MibTableColumn
bopStatOprCTSStateChanges = _BopStatOprCTSStateChanges_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 1, 1, 114),
    _BopStatOprCTSStateChanges_Type()
)
bopStatOprCTSStateChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bopStatOprCTSStateChanges.setStatus("mandatory")
_BopStatOprDSRStateChanges_Type = Counter32
_BopStatOprDSRStateChanges_Object = MibTableColumn
bopStatOprDSRStateChanges = _BopStatOprDSRStateChanges_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 1, 1, 115),
    _BopStatOprDSRStateChanges_Type()
)
bopStatOprDSRStateChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bopStatOprDSRStateChanges.setStatus("mandatory")
_BopStatOprDRSStateChanges_Type = Counter32
_BopStatOprDRSStateChanges_Object = MibTableColumn
bopStatOprDRSStateChanges = _BopStatOprDRSStateChanges_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 1, 1, 116),
    _BopStatOprDRSStateChanges_Type()
)
bopStatOprDRSStateChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bopStatOprDRSStateChanges.setStatus("mandatory")
_BopStatOprTMStateChanges_Type = Counter32
_BopStatOprTMStateChanges_Object = MibTableColumn
bopStatOprTMStateChanges = _BopStatOprTMStateChanges_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 1, 1, 117),
    _BopStatOprTMStateChanges_Type()
)
bopStatOprTMStateChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bopStatOprTMStateChanges.setStatus("mandatory")
_BopStatOprLLStateChanges_Type = Counter32
_BopStatOprLLStateChanges_Object = MibTableColumn
bopStatOprLLStateChanges = _BopStatOprLLStateChanges_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 1, 1, 118),
    _BopStatOprLLStateChanges_Type()
)
bopStatOprLLStateChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bopStatOprLLStateChanges.setStatus("mandatory")
_BopStatOprRIStateChanges_Type = Counter32
_BopStatOprRIStateChanges_Object = MibTableColumn
bopStatOprRIStateChanges = _BopStatOprRIStateChanges_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 1, 1, 119),
    _BopStatOprRIStateChanges_Type()
)
bopStatOprRIStateChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bopStatOprRIStateChanges.setStatus("mandatory")
_BopStatOprRLStateChanges_Type = Counter32
_BopStatOprRLStateChanges_Object = MibTableColumn
bopStatOprRLStateChanges = _BopStatOprRLStateChanges_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 1, 1, 120),
    _BopStatOprRLStateChanges_Type()
)
bopStatOprRLStateChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bopStatOprRLStateChanges.setStatus("mandatory")
_BopStatOprPortResets_Type = Counter32
_BopStatOprPortResets_Object = MibTableColumn
bopStatOprPortResets = _BopStatOprPortResets_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 1, 1, 121),
    _BopStatOprPortResets_Type()
)
bopStatOprPortResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bopStatOprPortResets.setStatus("mandatory")
_BopStatOprRxGenError_Type = Counter32
_BopStatOprRxGenError_Object = MibTableColumn
bopStatOprRxGenError = _BopStatOprRxGenError_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 1, 1, 123),
    _BopStatOprRxGenError_Type()
)
bopStatOprRxGenError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bopStatOprRxGenError.setStatus("mandatory")
_BopSapAdmTable_Object = MibTable
bopSapAdmTable = _BopSapAdmTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 2)
)
if mibBuilder.loadTexts:
    bopSapAdmTable.setStatus("mandatory")
_BopSapAdmEntry_Object = MibTableRow
bopSapAdmEntry = _BopSapAdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 2, 1)
)
bopSapAdmEntry.setIndexNames(
    (0, "CXBOPIO-MIB", "bopSapAdmNumber"),
)
if mibBuilder.loadTexts:
    bopSapAdmEntry.setStatus("mandatory")
_BopSapAdmNumber_Type = Integer32
_BopSapAdmNumber_Object = MibTableColumn
bopSapAdmNumber = _BopSapAdmNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 2, 1, 1),
    _BopSapAdmNumber_Type()
)
bopSapAdmNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bopSapAdmNumber.setStatus("mandatory")
_BopSapAdmAlias_Type = Alias
_BopSapAdmAlias_Object = MibTableColumn
bopSapAdmAlias = _BopSapAdmAlias_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 2, 1, 2),
    _BopSapAdmAlias_Type()
)
bopSapAdmAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bopSapAdmAlias.setStatus("mandatory")


class _BopSapAdmProtocol_Type(Integer32):
    """Custom type bopSapAdmProtocol based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("aircat", 6),
          ("borroughs", 3),
          ("bsc3270", 2),
          ("bsc3780", 5),
          ("hdlc", 1),
          ("sperry", 4))
    )


_BopSapAdmProtocol_Type.__name__ = "Integer32"
_BopSapAdmProtocol_Object = MibTableColumn
bopSapAdmProtocol = _BopSapAdmProtocol_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 2, 1, 3),
    _BopSapAdmProtocol_Type()
)
bopSapAdmProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bopSapAdmProtocol.setStatus("mandatory")


class _BopSapAdmPortClockSource_Type(Integer32):
    """Custom type bopSapAdmPortClockSource based on Integer32"""
    defaultValue = 2

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
        *(("external", 2),
          ("internal", 1),
          ("slave", 4),
          ("split", 3))
    )


_BopSapAdmPortClockSource_Type.__name__ = "Integer32"
_BopSapAdmPortClockSource_Object = MibTableColumn
bopSapAdmPortClockSource = _BopSapAdmPortClockSource_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 2, 1, 5),
    _BopSapAdmPortClockSource_Type()
)
bopSapAdmPortClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bopSapAdmPortClockSource.setStatus("mandatory")


class _BopSapAdmPortSpeed_Type(Integer32):
    """Custom type bopSapAdmPortSpeed based on Integer32"""
    defaultValue = 64000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(375, 2048000),
    )


_BopSapAdmPortSpeed_Type.__name__ = "Integer32"
_BopSapAdmPortSpeed_Object = MibTableColumn
bopSapAdmPortSpeed = _BopSapAdmPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 2, 1, 6),
    _BopSapAdmPortSpeed_Type()
)
bopSapAdmPortSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bopSapAdmPortSpeed.setStatus("mandatory")


class _BopSapAdmPortDuplex_Type(Integer32):
    """Custom type bopSapAdmPortDuplex based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("full", 2),
          ("half", 1))
    )


_BopSapAdmPortDuplex_Type.__name__ = "Integer32"
_BopSapAdmPortDuplex_Object = MibTableColumn
bopSapAdmPortDuplex = _BopSapAdmPortDuplex_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 2, 1, 7),
    _BopSapAdmPortDuplex_Type()
)
bopSapAdmPortDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bopSapAdmPortDuplex.setStatus("mandatory")


class _BopSapAdmPortMaxFrameSize_Type(Integer32):
    """Custom type bopSapAdmPortMaxFrameSize based on Integer32"""
    defaultValue = 1600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 9000),
    )


_BopSapAdmPortMaxFrameSize_Type.__name__ = "Integer32"
_BopSapAdmPortMaxFrameSize_Object = MibTableColumn
bopSapAdmPortMaxFrameSize = _BopSapAdmPortMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 2, 1, 8),
    _BopSapAdmPortMaxFrameSize_Type()
)
bopSapAdmPortMaxFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bopSapAdmPortMaxFrameSize.setStatus("mandatory")


class _BopSapAdmPortDataEncoding_Type(Integer32):
    """Custom type bopSapAdmPortDataEncoding based on Integer32"""
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
        *(("nrz", 1),
          ("nrzi-mark", 2),
          ("nrzi-space", 3))
    )


_BopSapAdmPortDataEncoding_Type.__name__ = "Integer32"
_BopSapAdmPortDataEncoding_Object = MibTableColumn
bopSapAdmPortDataEncoding = _BopSapAdmPortDataEncoding_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 2, 1, 9),
    _BopSapAdmPortDataEncoding_Type()
)
bopSapAdmPortDataEncoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bopSapAdmPortDataEncoding.setStatus("mandatory")


class _BopSapAdmPortIdleCondition_Type(Integer32):
    """Custom type bopSapAdmPortIdleCondition based on Integer32"""
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
        *(("as400", 3),
          ("flags", 1),
          ("marks", 2))
    )


_BopSapAdmPortIdleCondition_Type.__name__ = "Integer32"
_BopSapAdmPortIdleCondition_Object = MibTableColumn
bopSapAdmPortIdleCondition = _BopSapAdmPortIdleCondition_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 2, 1, 10),
    _BopSapAdmPortIdleCondition_Type()
)
bopSapAdmPortIdleCondition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bopSapAdmPortIdleCondition.setStatus("mandatory")


class _BopSapAdmPortPreAmbleLength_Type(Integer32):
    """Custom type bopSapAdmPortPreAmbleLength based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_BopSapAdmPortPreAmbleLength_Type.__name__ = "Integer32"
_BopSapAdmPortPreAmbleLength_Object = MibTableColumn
bopSapAdmPortPreAmbleLength = _BopSapAdmPortPreAmbleLength_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 2, 1, 11),
    _BopSapAdmPortPreAmbleLength_Type()
)
bopSapAdmPortPreAmbleLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bopSapAdmPortPreAmbleLength.setStatus("mandatory")


class _BopSapAdmPortFlagSharing_Type(Integer32):
    """Custom type bopSapAdmPortFlagSharing based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BopSapAdmPortFlagSharing_Type.__name__ = "Integer32"
_BopSapAdmPortFlagSharing_Object = MibTableColumn
bopSapAdmPortFlagSharing = _BopSapAdmPortFlagSharing_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 2, 1, 12),
    _BopSapAdmPortFlagSharing_Type()
)
bopSapAdmPortFlagSharing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bopSapAdmPortFlagSharing.setStatus("obsolete")


class _BopSapAdmPortFilterMask_Type(Integer32):
    """Custom type bopSapAdmPortFilterMask based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BopSapAdmPortFilterMask_Type.__name__ = "Integer32"
_BopSapAdmPortFilterMask_Object = MibTableColumn
bopSapAdmPortFilterMask = _BopSapAdmPortFilterMask_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 2, 1, 13),
    _BopSapAdmPortFilterMask_Type()
)
bopSapAdmPortFilterMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bopSapAdmPortFilterMask.setStatus("obsolete")


class _BopSapAdmPortFilterAddress1_Type(Integer32):
    """Custom type bopSapAdmPortFilterAddress1 based on Integer32"""
    defaultValue = 126

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BopSapAdmPortFilterAddress1_Type.__name__ = "Integer32"
_BopSapAdmPortFilterAddress1_Object = MibTableColumn
bopSapAdmPortFilterAddress1 = _BopSapAdmPortFilterAddress1_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 2, 1, 14),
    _BopSapAdmPortFilterAddress1_Type()
)
bopSapAdmPortFilterAddress1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bopSapAdmPortFilterAddress1.setStatus("obsolete")


class _BopSapAdmPortFilterAddress2_Type(Integer32):
    """Custom type bopSapAdmPortFilterAddress2 based on Integer32"""
    defaultValue = 126

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BopSapAdmPortFilterAddress2_Type.__name__ = "Integer32"
_BopSapAdmPortFilterAddress2_Object = MibTableColumn
bopSapAdmPortFilterAddress2 = _BopSapAdmPortFilterAddress2_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 2, 1, 15),
    _BopSapAdmPortFilterAddress2_Type()
)
bopSapAdmPortFilterAddress2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bopSapAdmPortFilterAddress2.setStatus("obsolete")


class _BopSapAdmPortFilterAddress3_Type(Integer32):
    """Custom type bopSapAdmPortFilterAddress3 based on Integer32"""
    defaultValue = 126

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BopSapAdmPortFilterAddress3_Type.__name__ = "Integer32"
_BopSapAdmPortFilterAddress3_Object = MibTableColumn
bopSapAdmPortFilterAddress3 = _BopSapAdmPortFilterAddress3_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 2, 1, 16),
    _BopSapAdmPortFilterAddress3_Type()
)
bopSapAdmPortFilterAddress3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bopSapAdmPortFilterAddress3.setStatus("obsolete")


class _BopSapAdmPortFilterAddress4_Type(Integer32):
    """Custom type bopSapAdmPortFilterAddress4 based on Integer32"""
    defaultValue = 126

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BopSapAdmPortFilterAddress4_Type.__name__ = "Integer32"
_BopSapAdmPortFilterAddress4_Object = MibTableColumn
bopSapAdmPortFilterAddress4 = _BopSapAdmPortFilterAddress4_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 2, 1, 17),
    _BopSapAdmPortFilterAddress4_Type()
)
bopSapAdmPortFilterAddress4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bopSapAdmPortFilterAddress4.setStatus("obsolete")


class _BopSapAdmPortCrc_Type(Integer32):
    """Custom type bopSapAdmPortCrc based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("crc-32", 2),
          ("crc-ccitt", 1))
    )


_BopSapAdmPortCrc_Type.__name__ = "Integer32"
_BopSapAdmPortCrc_Object = MibTableColumn
bopSapAdmPortCrc = _BopSapAdmPortCrc_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 2, 1, 18),
    _BopSapAdmPortCrc_Type()
)
bopSapAdmPortCrc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bopSapAdmPortCrc.setStatus("obsolete")


class _BopSapAdmPortDtrUpTimer_Type(Integer32):
    """Custom type bopSapAdmPortDtrUpTimer based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BopSapAdmPortDtrUpTimer_Type.__name__ = "Integer32"
_BopSapAdmPortDtrUpTimer_Object = MibTableColumn
bopSapAdmPortDtrUpTimer = _BopSapAdmPortDtrUpTimer_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 2, 1, 19),
    _BopSapAdmPortDtrUpTimer_Type()
)
bopSapAdmPortDtrUpTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bopSapAdmPortDtrUpTimer.setStatus("mandatory")


class _BopSapAdmPortTxWindow_Type(Integer32):
    """Custom type bopSapAdmPortTxWindow based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_BopSapAdmPortTxWindow_Type.__name__ = "Integer32"
_BopSapAdmPortTxWindow_Object = MibTableColumn
bopSapAdmPortTxWindow = _BopSapAdmPortTxWindow_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 2, 1, 20),
    _BopSapAdmPortTxWindow_Type()
)
bopSapAdmPortTxWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bopSapAdmPortTxWindow.setStatus("mandatory")


class _BopSapAdmPortThreshBandwidth_Type(Integer32):
    """Custom type bopSapAdmPortThreshBandwidth based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BopSapAdmPortThreshBandwidth_Type.__name__ = "Integer32"
_BopSapAdmPortThreshBandwidth_Object = MibTableColumn
bopSapAdmPortThreshBandwidth = _BopSapAdmPortThreshBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 2, 1, 21),
    _BopSapAdmPortThreshBandwidth_Type()
)
bopSapAdmPortThreshBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bopSapAdmPortThreshBandwidth.setStatus("mandatory")


class _BopSapAdmPortDialMode_Type(Integer32):
    """Custom type bopSapAdmPortDialMode based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dial-in-only", 1),
          ("dial-in-out", 3),
          ("dial-out-only", 2))
    )


_BopSapAdmPortDialMode_Type.__name__ = "Integer32"
_BopSapAdmPortDialMode_Object = MibTableColumn
bopSapAdmPortDialMode = _BopSapAdmPortDialMode_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 2, 1, 22),
    _BopSapAdmPortDialMode_Type()
)
bopSapAdmPortDialMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bopSapAdmPortDialMode.setStatus("mandatory")


class _BopSapAdmPortLoopback_Type(Integer32):
    """Custom type bopSapAdmPortLoopback based on Integer32"""
    defaultValue = 1

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
        *(("both", 4),
          ("isdn-uif-external", 8),
          ("isdn-uif-framer", 7),
          ("isdn-uif-idl2", 6),
          ("isdn-uif-uif", 5),
          ("local", 2),
          ("none", 1),
          ("remote", 3))
    )


_BopSapAdmPortLoopback_Type.__name__ = "Integer32"
_BopSapAdmPortLoopback_Object = MibTableColumn
bopSapAdmPortLoopback = _BopSapAdmPortLoopback_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 2, 1, 28),
    _BopSapAdmPortLoopback_Type()
)
bopSapAdmPortLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bopSapAdmPortLoopback.setStatus("mandatory")


class _BopSapAdmPortSignalSamplingPeriod_Type(Integer32):
    """Custom type bopSapAdmPortSignalSamplingPeriod based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 100),
    )


_BopSapAdmPortSignalSamplingPeriod_Type.__name__ = "Integer32"
_BopSapAdmPortSignalSamplingPeriod_Object = MibTableColumn
bopSapAdmPortSignalSamplingPeriod = _BopSapAdmPortSignalSamplingPeriod_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 2, 1, 29),
    _BopSapAdmPortSignalSamplingPeriod_Type()
)
bopSapAdmPortSignalSamplingPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bopSapAdmPortSignalSamplingPeriod.setStatus("mandatory")


class _BopSapAdmPortDcdDtrSignalSamples_Type(Integer32):
    """Custom type bopSapAdmPortDcdDtrSignalSamples based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_BopSapAdmPortDcdDtrSignalSamples_Type.__name__ = "Integer32"
_BopSapAdmPortDcdDtrSignalSamples_Object = MibTableColumn
bopSapAdmPortDcdDtrSignalSamples = _BopSapAdmPortDcdDtrSignalSamples_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 2, 1, 30),
    _BopSapAdmPortDcdDtrSignalSamples_Type()
)
bopSapAdmPortDcdDtrSignalSamples.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bopSapAdmPortDcdDtrSignalSamples.setStatus("mandatory")


class _BopSapAdmPortCtsRtsSignalSamples_Type(Integer32):
    """Custom type bopSapAdmPortCtsRtsSignalSamples based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_BopSapAdmPortCtsRtsSignalSamples_Type.__name__ = "Integer32"
_BopSapAdmPortCtsRtsSignalSamples_Object = MibTableColumn
bopSapAdmPortCtsRtsSignalSamples = _BopSapAdmPortCtsRtsSignalSamples_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 2, 1, 31),
    _BopSapAdmPortCtsRtsSignalSamples_Type()
)
bopSapAdmPortCtsRtsSignalSamples.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bopSapAdmPortCtsRtsSignalSamples.setStatus("mandatory")


class _BopSapAdmPortDsrDrsSignalSamples_Type(Integer32):
    """Custom type bopSapAdmPortDsrDrsSignalSamples based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_BopSapAdmPortDsrDrsSignalSamples_Type.__name__ = "Integer32"
_BopSapAdmPortDsrDrsSignalSamples_Object = MibTableColumn
bopSapAdmPortDsrDrsSignalSamples = _BopSapAdmPortDsrDrsSignalSamples_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 2, 1, 32),
    _BopSapAdmPortDsrDrsSignalSamples_Type()
)
bopSapAdmPortDsrDrsSignalSamples.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bopSapAdmPortDsrDrsSignalSamples.setStatus("mandatory")


class _BopSapAdmPortTmLlSignalSamples_Type(Integer32):
    """Custom type bopSapAdmPortTmLlSignalSamples based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_BopSapAdmPortTmLlSignalSamples_Type.__name__ = "Integer32"
_BopSapAdmPortTmLlSignalSamples_Object = MibTableColumn
bopSapAdmPortTmLlSignalSamples = _BopSapAdmPortTmLlSignalSamples_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 2, 1, 33),
    _BopSapAdmPortTmLlSignalSamples_Type()
)
bopSapAdmPortTmLlSignalSamples.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bopSapAdmPortTmLlSignalSamples.setStatus("mandatory")


class _BopSapAdmPortRiRlSignalSamples_Type(Integer32):
    """Custom type bopSapAdmPortRiRlSignalSamples based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_BopSapAdmPortRiRlSignalSamples_Type.__name__ = "Integer32"
_BopSapAdmPortRiRlSignalSamples_Object = MibTableColumn
bopSapAdmPortRiRlSignalSamples = _BopSapAdmPortRiRlSignalSamples_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 2, 1, 34),
    _BopSapAdmPortRiRlSignalSamples_Type()
)
bopSapAdmPortRiRlSignalSamples.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bopSapAdmPortRiRlSignalSamples.setStatus("mandatory")


class _BopSapAdmPortStatisticsTimer_Type(Integer32):
    """Custom type bopSapAdmPortStatisticsTimer based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_BopSapAdmPortStatisticsTimer_Type.__name__ = "Integer32"
_BopSapAdmPortStatisticsTimer_Object = MibTableColumn
bopSapAdmPortStatisticsTimer = _BopSapAdmPortStatisticsTimer_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 2, 1, 35),
    _BopSapAdmPortStatisticsTimer_Type()
)
bopSapAdmPortStatisticsTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bopSapAdmPortStatisticsTimer.setStatus("mandatory")


class _BopSapAdmPortCarrierAction_Type(Integer32):
    """Custom type bopSapAdmPortCarrierAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BopSapAdmPortCarrierAction_Type.__name__ = "Integer32"
_BopSapAdmPortCarrierAction_Object = MibTableColumn
bopSapAdmPortCarrierAction = _BopSapAdmPortCarrierAction_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 2, 1, 36),
    _BopSapAdmPortCarrierAction_Type()
)
bopSapAdmPortCarrierAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bopSapAdmPortCarrierAction.setStatus("mandatory")


class _BopSapAdmPortDataGenerator_Type(Integer32):
    """Custom type bopSapAdmPortDataGenerator based on Integer32"""
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
        *(("disabled", 1),
          ("enabled", 2),
          ("enabled-verify", 3))
    )


_BopSapAdmPortDataGenerator_Type.__name__ = "Integer32"
_BopSapAdmPortDataGenerator_Object = MibTableColumn
bopSapAdmPortDataGenerator = _BopSapAdmPortDataGenerator_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 2, 1, 37),
    _BopSapAdmPortDataGenerator_Type()
)
bopSapAdmPortDataGenerator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bopSapAdmPortDataGenerator.setStatus("mandatory")


class _BopSapAdmPortGenFrames_Type(Integer32):
    """Custom type bopSapAdmPortGenFrames based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BopSapAdmPortGenFrames_Type.__name__ = "Integer32"
_BopSapAdmPortGenFrames_Object = MibTableColumn
bopSapAdmPortGenFrames = _BopSapAdmPortGenFrames_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 2, 1, 38),
    _BopSapAdmPortGenFrames_Type()
)
bopSapAdmPortGenFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bopSapAdmPortGenFrames.setStatus("mandatory")


class _BopSapAdmPortGenFrameSize_Type(Integer32):
    """Custom type bopSapAdmPortGenFrameSize based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 65535),
    )


_BopSapAdmPortGenFrameSize_Type.__name__ = "Integer32"
_BopSapAdmPortGenFrameSize_Object = MibTableColumn
bopSapAdmPortGenFrameSize = _BopSapAdmPortGenFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 2, 1, 39),
    _BopSapAdmPortGenFrameSize_Type()
)
bopSapAdmPortGenFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bopSapAdmPortGenFrameSize.setStatus("mandatory")


class _BopSapAdmPortGenFrameHeader_Type(Integer32):
    """Custom type bopSapAdmPortGenFrameHeader based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BopSapAdmPortGenFrameHeader_Type.__name__ = "Integer32"
_BopSapAdmPortGenFrameHeader_Object = MibTableColumn
bopSapAdmPortGenFrameHeader = _BopSapAdmPortGenFrameHeader_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 2, 1, 40),
    _BopSapAdmPortGenFrameHeader_Type()
)
bopSapAdmPortGenFrameHeader.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bopSapAdmPortGenFrameHeader.setStatus("mandatory")


class _BopSapAdmCodeSet_Type(Integer32):
    """Custom type bopSapAdmCodeSet based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ascii", 3),
          ("ebcdic", 2),
          ("other", 1))
    )


_BopSapAdmCodeSet_Type.__name__ = "Integer32"
_BopSapAdmCodeSet_Object = MibTableColumn
bopSapAdmCodeSet = _BopSapAdmCodeSet_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 2, 1, 45),
    _BopSapAdmCodeSet_Type()
)
bopSapAdmCodeSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bopSapAdmCodeSet.setStatus("mandatory")


class _BopSapAdmParity_Type(Integer32):
    """Custom type bopSapAdmParity based on Integer32"""
    defaultValue = 1

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
        *(("even", 3),
          ("mark", 5),
          ("none", 1),
          ("odd", 2),
          ("space", 4))
    )


_BopSapAdmParity_Type.__name__ = "Integer32"
_BopSapAdmParity_Object = MibTableColumn
bopSapAdmParity = _BopSapAdmParity_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 2, 1, 46),
    _BopSapAdmParity_Type()
)
bopSapAdmParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bopSapAdmParity.setStatus("mandatory")


class _BopAdmPortTrap_Type(Integer32):
    """Custom type bopAdmPortTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BopAdmPortTrap_Type.__name__ = "Integer32"
_BopAdmPortTrap_Object = MibTableColumn
bopAdmPortTrap = _BopAdmPortTrap_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 2, 1, 47),
    _BopAdmPortTrap_Type()
)
bopAdmPortTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bopAdmPortTrap.setStatus("mandatory")


class _BopAdmTxClockTrap_Type(Integer32):
    """Custom type bopAdmTxClockTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BopAdmTxClockTrap_Type.__name__ = "Integer32"
_BopAdmTxClockTrap_Object = MibTableColumn
bopAdmTxClockTrap = _BopAdmTxClockTrap_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 2, 1, 48),
    _BopAdmTxClockTrap_Type()
)
bopAdmTxClockTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bopAdmTxClockTrap.setStatus("mandatory")


class _BopMibLevel_Type(Integer32):
    """Custom type bopMibLevel based on Integer32"""
    defaultValue = 0


_BopMibLevel_Object = MibScalar
bopMibLevel = _BopMibLevel_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 3),
    _BopMibLevel_Type()
)
bopMibLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bopMibLevel.setStatus("mandatory")

# Managed Objects groups


# Notification objects

bopPortStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 0, 1)
)
bopPortStatusChange.setObjects(
      *(("CXBOPIO-MIB", "bopSapOprNumber"),
        ("CXBOPIO-MIB", "bopStatOprPortState"))
)
if mibBuilder.loadTexts:
    bopPortStatusChange.setStatus(
        ""
    )

bopTxClockStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36, 0, 2)
)
bopTxClockStatusChange.setObjects(
      *(("CXBOPIO-MIB", "bopSapOprNumber"),
        ("CXBOPIO-MIB", "bopStatOprTxClockState"))
)
if mibBuilder.loadTexts:
    bopTxClockStatusChange.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CXBOPIO-MIB",
    **{"bopPortStatusChange": bopPortStatusChange,
       "bopTxClockStatusChange": bopTxClockStatusChange,
       "bopSapOprTable": bopSapOprTable,
       "bopSapOprEntry": bopSapOprEntry,
       "bopSapOprNumber": bopSapOprNumber,
       "bopSapOprAlias": bopSapOprAlias,
       "bopSapOprProtocol": bopSapOprProtocol,
       "bopSapOprPortClockSource": bopSapOprPortClockSource,
       "bopSapOprPortSpeed": bopSapOprPortSpeed,
       "bopSapOprPortDuplex": bopSapOprPortDuplex,
       "bopSapOprPortMaxFrameSize": bopSapOprPortMaxFrameSize,
       "bopSapOprPortDataEncoding": bopSapOprPortDataEncoding,
       "bopSapOprPortIdleCondition": bopSapOprPortIdleCondition,
       "bopSapOprPortPreAmbleLength": bopSapOprPortPreAmbleLength,
       "bopSapOprPortFlagSharing": bopSapOprPortFlagSharing,
       "bopSapOprPortFilterMask": bopSapOprPortFilterMask,
       "bopSapOprPortFilterAddress1": bopSapOprPortFilterAddress1,
       "bopSapOprPortFilterAddress2": bopSapOprPortFilterAddress2,
       "bopSapOprPortFilterAddress3": bopSapOprPortFilterAddress3,
       "bopSapOprPortFilterAddress4": bopSapOprPortFilterAddress4,
       "bopSapOprPortCrc": bopSapOprPortCrc,
       "bopSapOprPortDtrUpTimer": bopSapOprPortDtrUpTimer,
       "bopSapOprPortTxWindow": bopSapOprPortTxWindow,
       "bopSapOprPortDialMode": bopSapOprPortDialMode,
       "bopSapOprPortLoopback": bopSapOprPortLoopback,
       "bopSapOprPortSignalSamplingPeriod": bopSapOprPortSignalSamplingPeriod,
       "bopSapOprPortDcdDtrSignalSamples": bopSapOprPortDcdDtrSignalSamples,
       "bopSapOprPortCtsRtsSignalSamples": bopSapOprPortCtsRtsSignalSamples,
       "bopSapOprPortDsrDrsSignalSamples": bopSapOprPortDsrDrsSignalSamples,
       "bopSapOprPortTmLlSignalSamples": bopSapOprPortTmLlSignalSamples,
       "bopSapOprPortRiRlSignalSamples": bopSapOprPortRiRlSignalSamples,
       "bopSapOprPortStatisticsTimer": bopSapOprPortStatisticsTimer,
       "bopSapOprPortCarrierAction": bopSapOprPortCarrierAction,
       "bopSapOprPortDataGenerator": bopSapOprPortDataGenerator,
       "bopSapOprPortGenFrames": bopSapOprPortGenFrames,
       "bopSapOprPortGenFrameSize": bopSapOprPortGenFrameSize,
       "bopSapOprPortGenFrameHeader": bopSapOprPortGenFrameHeader,
       "bopSapOprPortThreshBandwidth": bopSapOprPortThreshBandwidth,
       "bopSapOprPortActualSpeed": bopSapOprPortActualSpeed,
       "bopSapOprCodeSet": bopSapOprCodeSet,
       "bopSapOprParity": bopSapOprParity,
       "bopOprPortTrap": bopOprPortTrap,
       "bopOprTxClockTrap": bopOprTxClockTrap,
       "bopOprControlLine": bopOprControlLine,
       "bopOprControlStats": bopOprControlStats,
       "bopStatOprPortType": bopStatOprPortType,
       "bopStatOprPortInterfaceType": bopStatOprPortInterfaceType,
       "bopStatOprPortState": bopStatOprPortState,
       "bopStatOprTxClockState": bopStatOprTxClockState,
       "bopStatOprDCDState": bopStatOprDCDState,
       "bopStatOprDTRState": bopStatOprDTRState,
       "bopStatOprRTSState": bopStatOprRTSState,
       "bopStatOprCTSState": bopStatOprCTSState,
       "bopStatOprDSRState": bopStatOprDSRState,
       "bopStatOprDRSState": bopStatOprDRSState,
       "bopStatOprTMState": bopStatOprTMState,
       "bopStatOprLLState": bopStatOprLLState,
       "bopStatOprRIState": bopStatOprRIState,
       "bopStatOprRLState": bopStatOprRLState,
       "bopStatOprTxFrames": bopStatOprTxFrames,
       "bopStatOprRxFrames": bopStatOprRxFrames,
       "bopStatOprLocalLoopbackFrames": bopStatOprLocalLoopbackFrames,
       "bopStatOprTxBps": bopStatOprTxBps,
       "bopStatOprRxBps": bopStatOprRxBps,
       "bopStatOprTxBpsMax": bopStatOprTxBpsMax,
       "bopStatOprRxBpsMax": bopStatOprRxBpsMax,
       "bopStatOprTxFps": bopStatOprTxFps,
       "bopStatOprRxFps": bopStatOprRxFps,
       "bopStatOprTxFpsMax": bopStatOprTxFpsMax,
       "bopStatOprRxFpsMax": bopStatOprRxFpsMax,
       "bopStatOprTxUnderrunFrames": bopStatOprTxUnderrunFrames,
       "bopStatOprTxCtsLostFrames": bopStatOprTxCtsLostFrames,
       "bopStatOprTxBadStateDiscards": bopStatOprTxBadStateDiscards,
       "bopStatOprTxResetDiscards": bopStatOprTxResetDiscards,
       "bopStatOprTxSysCongestionDiscards": bopStatOprTxSysCongestionDiscards,
       "bopStatOprTxInvWinDiscards": bopStatOprTxInvWinDiscards,
       "bopStatOprTxInvRLpbkWinDiscards": bopStatOprTxInvRLpbkWinDiscards,
       "bopStatOprRxBadCrcFrames": bopStatOprRxBadCrcFrames,
       "bopStatOprRxAbortedFrames": bopStatOprRxAbortedFrames,
       "bopStatOprRxNonIntegralBitFrames": bopStatOprRxNonIntegralBitFrames,
       "bopStatOprRxLongFrames": bopStatOprRxLongFrames,
       "bopStatOprRxOverrunFrames": bopStatOprRxOverrunFrames,
       "bopStatOprRxCdLostFrames": bopStatOprRxCdLostFrames,
       "bopStatOprRxBadStateDiscards": bopStatOprRxBadStateDiscards,
       "bopStatOprRxBusyDiscards": bopStatOprRxBusyDiscards,
       "bopStatOprPortStateChanges": bopStatOprPortStateChanges,
       "bopStatOprTxClockStateChanges": bopStatOprTxClockStateChanges,
       "bopStatOprDCDStateChanges": bopStatOprDCDStateChanges,
       "bopStatOprDTRStateChanges": bopStatOprDTRStateChanges,
       "bopStatOprRTSStateChanges": bopStatOprRTSStateChanges,
       "bopStatOprCTSStateChanges": bopStatOprCTSStateChanges,
       "bopStatOprDSRStateChanges": bopStatOprDSRStateChanges,
       "bopStatOprDRSStateChanges": bopStatOprDRSStateChanges,
       "bopStatOprTMStateChanges": bopStatOprTMStateChanges,
       "bopStatOprLLStateChanges": bopStatOprLLStateChanges,
       "bopStatOprRIStateChanges": bopStatOprRIStateChanges,
       "bopStatOprRLStateChanges": bopStatOprRLStateChanges,
       "bopStatOprPortResets": bopStatOprPortResets,
       "bopStatOprRxGenError": bopStatOprRxGenError,
       "bopSapAdmTable": bopSapAdmTable,
       "bopSapAdmEntry": bopSapAdmEntry,
       "bopSapAdmNumber": bopSapAdmNumber,
       "bopSapAdmAlias": bopSapAdmAlias,
       "bopSapAdmProtocol": bopSapAdmProtocol,
       "bopSapAdmPortClockSource": bopSapAdmPortClockSource,
       "bopSapAdmPortSpeed": bopSapAdmPortSpeed,
       "bopSapAdmPortDuplex": bopSapAdmPortDuplex,
       "bopSapAdmPortMaxFrameSize": bopSapAdmPortMaxFrameSize,
       "bopSapAdmPortDataEncoding": bopSapAdmPortDataEncoding,
       "bopSapAdmPortIdleCondition": bopSapAdmPortIdleCondition,
       "bopSapAdmPortPreAmbleLength": bopSapAdmPortPreAmbleLength,
       "bopSapAdmPortFlagSharing": bopSapAdmPortFlagSharing,
       "bopSapAdmPortFilterMask": bopSapAdmPortFilterMask,
       "bopSapAdmPortFilterAddress1": bopSapAdmPortFilterAddress1,
       "bopSapAdmPortFilterAddress2": bopSapAdmPortFilterAddress2,
       "bopSapAdmPortFilterAddress3": bopSapAdmPortFilterAddress3,
       "bopSapAdmPortFilterAddress4": bopSapAdmPortFilterAddress4,
       "bopSapAdmPortCrc": bopSapAdmPortCrc,
       "bopSapAdmPortDtrUpTimer": bopSapAdmPortDtrUpTimer,
       "bopSapAdmPortTxWindow": bopSapAdmPortTxWindow,
       "bopSapAdmPortThreshBandwidth": bopSapAdmPortThreshBandwidth,
       "bopSapAdmPortDialMode": bopSapAdmPortDialMode,
       "bopSapAdmPortLoopback": bopSapAdmPortLoopback,
       "bopSapAdmPortSignalSamplingPeriod": bopSapAdmPortSignalSamplingPeriod,
       "bopSapAdmPortDcdDtrSignalSamples": bopSapAdmPortDcdDtrSignalSamples,
       "bopSapAdmPortCtsRtsSignalSamples": bopSapAdmPortCtsRtsSignalSamples,
       "bopSapAdmPortDsrDrsSignalSamples": bopSapAdmPortDsrDrsSignalSamples,
       "bopSapAdmPortTmLlSignalSamples": bopSapAdmPortTmLlSignalSamples,
       "bopSapAdmPortRiRlSignalSamples": bopSapAdmPortRiRlSignalSamples,
       "bopSapAdmPortStatisticsTimer": bopSapAdmPortStatisticsTimer,
       "bopSapAdmPortCarrierAction": bopSapAdmPortCarrierAction,
       "bopSapAdmPortDataGenerator": bopSapAdmPortDataGenerator,
       "bopSapAdmPortGenFrames": bopSapAdmPortGenFrames,
       "bopSapAdmPortGenFrameSize": bopSapAdmPortGenFrameSize,
       "bopSapAdmPortGenFrameHeader": bopSapAdmPortGenFrameHeader,
       "bopSapAdmCodeSet": bopSapAdmCodeSet,
       "bopSapAdmParity": bopSapAdmParity,
       "bopAdmPortTrap": bopAdmPortTrap,
       "bopAdmTxClockTrap": bopAdmTxClockTrap,
       "bopMibLevel": bopMibLevel}
)
