# SNMP MIB module (XYLO-TRAPOBJECTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XYLO-TRAPOBJECTS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:19:36 2024
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

(anxTrapHostInfo,
 callmgmtTrapObj,
 genericTrapObj,
 modemTrapObj,
 wanTrapObj) = mibBuilder.importSymbols(
    "XYLO-MIB-SMI",
    "anxTrapHostInfo",
    "callmgmtTrapObj",
    "genericTrapObj",
    "modemTrapObj",
    "wanTrapObj")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _AnxTrapHostMax_Type(Integer32):
    """Custom type anxTrapHostMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_AnxTrapHostMax_Type.__name__ = "Integer32"
_AnxTrapHostMax_Object = MibScalar
anxTrapHostMax = _AnxTrapHostMax_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 10, 1),
    _AnxTrapHostMax_Type()
)
anxTrapHostMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anxTrapHostMax.setStatus("mandatory")


class _AnxTrapHostCurEnt_Type(Integer32):
    """Custom type anxTrapHostCurEnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_AnxTrapHostCurEnt_Type.__name__ = "Integer32"
_AnxTrapHostCurEnt_Object = MibScalar
anxTrapHostCurEnt = _AnxTrapHostCurEnt_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 10, 2),
    _AnxTrapHostCurEnt_Type()
)
anxTrapHostCurEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anxTrapHostCurEnt.setStatus("mandatory")


class _AnxTrapHostNext_Type(Integer32):
    """Custom type anxTrapHostNext based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_AnxTrapHostNext_Type.__name__ = "Integer32"
_AnxTrapHostNext_Object = MibScalar
anxTrapHostNext = _AnxTrapHostNext_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 10, 3),
    _AnxTrapHostNext_Type()
)
anxTrapHostNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anxTrapHostNext.setStatus("mandatory")
_AnxTrapHostTable_Object = MibTable
anxTrapHostTable = _AnxTrapHostTable_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 10, 4)
)
if mibBuilder.loadTexts:
    anxTrapHostTable.setStatus("mandatory")
_AnxTrapHostEntry_Object = MibTableRow
anxTrapHostEntry = _AnxTrapHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 10, 4, 1)
)
anxTrapHostEntry.setIndexNames(
    (0, "XYLO-TRAPOBJECTS-MIB", "anxTrapHostIndex"),
)
if mibBuilder.loadTexts:
    anxTrapHostEntry.setStatus("mandatory")


class _AnxTrapHostIndex_Type(Integer32):
    """Custom type anxTrapHostIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AnxTrapHostIndex_Type.__name__ = "Integer32"
_AnxTrapHostIndex_Object = MibTableColumn
anxTrapHostIndex = _AnxTrapHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 10, 4, 1, 1),
    _AnxTrapHostIndex_Type()
)
anxTrapHostIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anxTrapHostIndex.setStatus("mandatory")


class _AnxTrapHostStatus_Type(Integer32):
    """Custom type anxTrapHostStatus based on Integer32"""
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
        *(("create", 5),
          ("delete", 4),
          ("ignore", 3),
          ("other", 1),
          ("valid", 2))
    )


_AnxTrapHostStatus_Type.__name__ = "Integer32"
_AnxTrapHostStatus_Object = MibTableColumn
anxTrapHostStatus = _AnxTrapHostStatus_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 10, 4, 1, 2),
    _AnxTrapHostStatus_Type()
)
anxTrapHostStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxTrapHostStatus.setStatus("mandatory")


class _AnxTrapHostAddrType_Type(Integer32):
    """Custom type anxTrapHostAddrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ip", 1)
    )


_AnxTrapHostAddrType_Type.__name__ = "Integer32"
_AnxTrapHostAddrType_Object = MibTableColumn
anxTrapHostAddrType = _AnxTrapHostAddrType_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 10, 4, 1, 3),
    _AnxTrapHostAddrType_Type()
)
anxTrapHostAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxTrapHostAddrType.setStatus("mandatory")
_AnxTrapHostNetAddr_Type = OctetString
_AnxTrapHostNetAddr_Object = MibTableColumn
anxTrapHostNetAddr = _AnxTrapHostNetAddr_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 10, 4, 1, 4),
    _AnxTrapHostNetAddr_Type()
)
anxTrapHostNetAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxTrapHostNetAddr.setStatus("mandatory")


class _AnxTrapHostComm_Type(OctetString):
    """Custom type anxTrapHostComm based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_AnxTrapHostComm_Type.__name__ = "OctetString"
_AnxTrapHostComm_Object = MibTableColumn
anxTrapHostComm = _AnxTrapHostComm_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 10, 4, 1, 5),
    _AnxTrapHostComm_Type()
)
anxTrapHostComm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxTrapHostComm.setStatus("mandatory")


class _AnxTrapHostAgeTime_Type(Integer32):
    """Custom type anxTrapHostAgeTime based on Integer32"""
    defaultValue = 0


_AnxTrapHostAgeTime_Object = MibTableColumn
anxTrapHostAgeTime = _AnxTrapHostAgeTime_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 10, 4, 1, 6),
    _AnxTrapHostAgeTime_Type()
)
anxTrapHostAgeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxTrapHostAgeTime.setStatus("mandatory")
_AnxTrapHostPortNumber_Type = Integer32
_AnxTrapHostPortNumber_Object = MibTableColumn
anxTrapHostPortNumber = _AnxTrapHostPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 10, 4, 1, 7),
    _AnxTrapHostPortNumber_Type()
)
anxTrapHostPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxTrapHostPortNumber.setStatus("mandatory")


class _AnxTrapHostGrouping_Type(Integer32):
    """Custom type anxTrapHostGrouping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AnxTrapHostGrouping_Type.__name__ = "Integer32"
_AnxTrapHostGrouping_Object = MibTableColumn
anxTrapHostGrouping = _AnxTrapHostGrouping_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 10, 4, 1, 8),
    _AnxTrapHostGrouping_Type()
)
anxTrapHostGrouping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxTrapHostGrouping.setStatus("mandatory")


class _AnxTrapUserName_Type(DisplayString):
    """Custom type anxTrapUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AnxTrapUserName_Type.__name__ = "DisplayString"
_AnxTrapUserName_Object = MibScalar
anxTrapUserName = _AnxTrapUserName_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 10, 5),
    _AnxTrapUserName_Type()
)
anxTrapUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anxTrapUserName.setStatus("mandatory")
_AnxTrapPortIndex_Type = Integer32
_AnxTrapPortIndex_Object = MibScalar
anxTrapPortIndex = _AnxTrapPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 10, 6),
    _AnxTrapPortIndex_Type()
)
anxTrapPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anxTrapPortIndex.setStatus("mandatory")


class _AnxTrapPortType_Type(Integer32):
    """Custom type anxTrapPortType based on Integer32"""
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
        *(("async", 1),
          ("dialout", 4),
          ("ethernet", 5),
          ("rfc", 6),
          ("sync", 2),
          ("virtual", 3))
    )


_AnxTrapPortType_Type.__name__ = "Integer32"
_AnxTrapPortType_Object = MibScalar
anxTrapPortType = _AnxTrapPortType_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 10, 7),
    _AnxTrapPortType_Type()
)
anxTrapPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anxTrapPortType.setStatus("mandatory")
_AnxTrapInetAddr_Type = IpAddress
_AnxTrapInetAddr_Object = MibScalar
anxTrapInetAddr = _AnxTrapInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 10, 8),
    _AnxTrapInetAddr_Type()
)
anxTrapInetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anxTrapInetAddr.setStatus("mandatory")


class _AnxTrapAttackErrcode_Type(Integer32):
    """Custom type anxTrapAttackErrcode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("maxThreshold", 1),
          ("timeThreshold", 2))
    )


_AnxTrapAttackErrcode_Type.__name__ = "Integer32"
_AnxTrapAttackErrcode_Object = MibScalar
anxTrapAttackErrcode = _AnxTrapAttackErrcode_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 10, 9),
    _AnxTrapAttackErrcode_Type()
)
anxTrapAttackErrcode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anxTrapAttackErrcode.setStatus("mandatory")


class _AnxTrapAttackErrmsg_Type(DisplayString):
    """Custom type anxTrapAttackErrmsg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AnxTrapAttackErrmsg_Type.__name__ = "DisplayString"
_AnxTrapAttackErrmsg_Object = MibScalar
anxTrapAttackErrmsg = _AnxTrapAttackErrmsg_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 10, 10),
    _AnxTrapAttackErrmsg_Type()
)
anxTrapAttackErrmsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anxTrapAttackErrmsg.setStatus("mandatory")


class _AnxTrapDbErrcode_Type(Integer32):
    """Custom type anxTrapDbErrcode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("protect-error", 3),
          ("read-error", 1),
          ("write-error", 2))
    )


_AnxTrapDbErrcode_Type.__name__ = "Integer32"
_AnxTrapDbErrcode_Object = MibScalar
anxTrapDbErrcode = _AnxTrapDbErrcode_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 10, 11),
    _AnxTrapDbErrcode_Type()
)
anxTrapDbErrcode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anxTrapDbErrcode.setStatus("mandatory")


class _AnxTrapDbErrmsg_Type(DisplayString):
    """Custom type anxTrapDbErrmsg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AnxTrapDbErrmsg_Type.__name__ = "DisplayString"
_AnxTrapDbErrmsg_Object = MibScalar
anxTrapDbErrmsg = _AnxTrapDbErrmsg_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 10, 12),
    _AnxTrapDbErrmsg_Type()
)
anxTrapDbErrmsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anxTrapDbErrmsg.setStatus("mandatory")


class _TrapModemMsg_Type(DisplayString):
    """Custom type trapModemMsg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_TrapModemMsg_Type.__name__ = "DisplayString"
_TrapModemMsg_Object = MibScalar
trapModemMsg = _TrapModemMsg_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 10, 13),
    _TrapModemMsg_Type()
)
trapModemMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapModemMsg.setStatus("mandatory")


class _OperImageModemImage_Type(DisplayString):
    """Custom type operImageModemImage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_OperImageModemImage_Type.__name__ = "DisplayString"
_OperImageModemImage_Object = MibScalar
operImageModemImage = _OperImageModemImage_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 10, 14),
    _OperImageModemImage_Type()
)
operImageModemImage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operImageModemImage.setStatus("mandatory")


class _WanVersion_Type(DisplayString):
    """Custom type wanVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_WanVersion_Type.__name__ = "DisplayString"
_WanVersion_Object = MibScalar
wanVersion = _WanVersion_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 10, 15),
    _WanVersion_Type()
)
wanVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanVersion.setStatus("mandatory")


class _TrapAfdMsg_Type(DisplayString):
    """Custom type trapAfdMsg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_TrapAfdMsg_Type.__name__ = "DisplayString"
_TrapAfdMsg_Object = MibScalar
trapAfdMsg = _TrapAfdMsg_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 10, 18),
    _TrapAfdMsg_Type()
)
trapAfdMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapAfdMsg.setStatus("mandatory")


class _WanBpvThreshold_Type(Integer32):
    """Custom type wanBpvThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WanBpvThreshold_Type.__name__ = "Integer32"
_WanBpvThreshold_Object = MibScalar
wanBpvThreshold = _WanBpvThreshold_Object(
    (1, 3, 6, 1, 4, 1, 15, 100, 1, 1, 1),
    _WanBpvThreshold_Type()
)
wanBpvThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanBpvThreshold.setStatus("mandatory")


class _WanOofThreshold_Type(Integer32):
    """Custom type wanOofThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WanOofThreshold_Type.__name__ = "Integer32"
_WanOofThreshold_Object = MibScalar
wanOofThreshold = _WanOofThreshold_Object(
    (1, 3, 6, 1, 4, 1, 15, 100, 1, 1, 2),
    _WanOofThreshold_Type()
)
wanOofThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanOofThreshold.setStatus("mandatory")


class _WanEsThreshold_Type(Integer32):
    """Custom type wanEsThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WanEsThreshold_Type.__name__ = "Integer32"
_WanEsThreshold_Object = MibScalar
wanEsThreshold = _WanEsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 15, 100, 1, 1, 3),
    _WanEsThreshold_Type()
)
wanEsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanEsThreshold.setStatus("mandatory")


class _WanCvThreshold_Type(Integer32):
    """Custom type wanCvThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WanCvThreshold_Type.__name__ = "Integer32"
_WanCvThreshold_Object = MibScalar
wanCvThreshold = _WanCvThreshold_Object(
    (1, 3, 6, 1, 4, 1, 15, 100, 1, 1, 4),
    _WanCvThreshold_Type()
)
wanCvThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanCvThreshold.setStatus("mandatory")


class _WanEsfThreshold_Type(Integer32):
    """Custom type wanEsfThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WanEsfThreshold_Type.__name__ = "Integer32"
_WanEsfThreshold_Object = MibScalar
wanEsfThreshold = _WanEsfThreshold_Object(
    (1, 3, 6, 1, 4, 1, 15, 100, 1, 1, 5),
    _WanEsfThreshold_Type()
)
wanEsfThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanEsfThreshold.setStatus("mandatory")


class _WanSesThreshold_Type(Integer32):
    """Custom type wanSesThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WanSesThreshold_Type.__name__ = "Integer32"
_WanSesThreshold_Object = MibScalar
wanSesThreshold = _WanSesThreshold_Object(
    (1, 3, 6, 1, 4, 1, 15, 100, 1, 1, 6),
    _WanSesThreshold_Type()
)
wanSesThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanSesThreshold.setStatus("mandatory")


class _WanUasThreshold_Type(Integer32):
    """Custom type wanUasThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WanUasThreshold_Type.__name__ = "Integer32"
_WanUasThreshold_Object = MibScalar
wanUasThreshold = _WanUasThreshold_Object(
    (1, 3, 6, 1, 4, 1, 15, 100, 1, 1, 7),
    _WanUasThreshold_Type()
)
wanUasThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanUasThreshold.setStatus("mandatory")


class _WanBesThreshold_Type(Integer32):
    """Custom type wanBesThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WanBesThreshold_Type.__name__ = "Integer32"
_WanBesThreshold_Object = MibScalar
wanBesThreshold = _WanBesThreshold_Object(
    (1, 3, 6, 1, 4, 1, 15, 100, 1, 1, 8),
    _WanBesThreshold_Type()
)
wanBesThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanBesThreshold.setStatus("mandatory")


class _WanLofcThreshold_Type(Integer32):
    """Custom type wanLofcThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WanLofcThreshold_Type.__name__ = "Integer32"
_WanLofcThreshold_Object = MibScalar
wanLofcThreshold = _WanLofcThreshold_Object(
    (1, 3, 6, 1, 4, 1, 15, 100, 1, 1, 9),
    _WanLofcThreshold_Type()
)
wanLofcThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanLofcThreshold.setStatus("mandatory")


class _WanCssThreshold_Type(Integer32):
    """Custom type wanCssThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WanCssThreshold_Type.__name__ = "Integer32"
_WanCssThreshold_Object = MibScalar
wanCssThreshold = _WanCssThreshold_Object(
    (1, 3, 6, 1, 4, 1, 15, 100, 1, 1, 10),
    _WanCssThreshold_Type()
)
wanCssThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanCssThreshold.setStatus("mandatory")


class _Ds0ErrorThreshold_Type(Integer32):
    """Custom type ds0ErrorThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Ds0ErrorThreshold_Type.__name__ = "Integer32"
_Ds0ErrorThreshold_Object = MibScalar
ds0ErrorThreshold = _Ds0ErrorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 15, 100, 1, 1, 11),
    _Ds0ErrorThreshold_Type()
)
ds0ErrorThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds0ErrorThreshold.setStatus("mandatory")


class _MdmErrorTrapThresh_Type(Integer32):
    """Custom type mdmErrorTrapThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MdmErrorTrapThresh_Type.__name__ = "Integer32"
_MdmErrorTrapThresh_Object = MibScalar
mdmErrorTrapThresh = _MdmErrorTrapThresh_Object(
    (1, 3, 6, 1, 4, 1, 15, 100, 1, 2, 1),
    _MdmErrorTrapThresh_Type()
)
mdmErrorTrapThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmErrorTrapThresh.setStatus("mandatory")


class _CallBeginTrapObj_Type(Integer32):
    """Custom type callBeginTrapObj based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_CallBeginTrapObj_Type.__name__ = "Integer32"
_CallBeginTrapObj_Object = MibScalar
callBeginTrapObj = _CallBeginTrapObj_Object(
    (1, 3, 6, 1, 4, 1, 15, 100, 1, 3, 1),
    _CallBeginTrapObj_Type()
)
callBeginTrapObj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    callBeginTrapObj.setStatus("mandatory")


class _CallEndTrapThresh_Type(Integer32):
    """Custom type callEndTrapThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CallEndTrapThresh_Type.__name__ = "Integer32"
_CallEndTrapThresh_Object = MibScalar
callEndTrapThresh = _CallEndTrapThresh_Object(
    (1, 3, 6, 1, 4, 1, 15, 100, 1, 3, 2),
    _CallEndTrapThresh_Type()
)
callEndTrapThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    callEndTrapThresh.setStatus("mandatory")


class _UnexpectDisconnectTrapThresh_Type(Integer32):
    """Custom type unexpectDisconnectTrapThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_UnexpectDisconnectTrapThresh_Type.__name__ = "Integer32"
_UnexpectDisconnectTrapThresh_Object = MibScalar
unexpectDisconnectTrapThresh = _UnexpectDisconnectTrapThresh_Object(
    (1, 3, 6, 1, 4, 1, 15, 100, 1, 3, 3),
    _UnexpectDisconnectTrapThresh_Type()
)
unexpectDisconnectTrapThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unexpectDisconnectTrapThresh.setStatus("mandatory")


class _ForcedCallDisconnectTrapThresh_Type(Integer32):
    """Custom type forcedCallDisconnectTrapThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ForcedCallDisconnectTrapThresh_Type.__name__ = "Integer32"
_ForcedCallDisconnectTrapThresh_Object = MibScalar
forcedCallDisconnectTrapThresh = _ForcedCallDisconnectTrapThresh_Object(
    (1, 3, 6, 1, 4, 1, 15, 100, 1, 3, 4),
    _ForcedCallDisconnectTrapThresh_Type()
)
forcedCallDisconnectTrapThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    forcedCallDisconnectTrapThresh.setStatus("mandatory")


class _DiallnkTrpEna_Type(Integer32):
    """Custom type diallnkTrpEna based on Integer32"""
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


_DiallnkTrpEna_Type.__name__ = "Integer32"
_DiallnkTrpEna_Object = MibScalar
diallnkTrpEna = _DiallnkTrpEna_Object(
    (1, 3, 6, 1, 4, 1, 15, 100, 1, 4, 1),
    _DiallnkTrpEna_Type()
)
diallnkTrpEna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diallnkTrpEna.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XYLO-TRAPOBJECTS-MIB",
    **{"anxTrapHostMax": anxTrapHostMax,
       "anxTrapHostCurEnt": anxTrapHostCurEnt,
       "anxTrapHostNext": anxTrapHostNext,
       "anxTrapHostTable": anxTrapHostTable,
       "anxTrapHostEntry": anxTrapHostEntry,
       "anxTrapHostIndex": anxTrapHostIndex,
       "anxTrapHostStatus": anxTrapHostStatus,
       "anxTrapHostAddrType": anxTrapHostAddrType,
       "anxTrapHostNetAddr": anxTrapHostNetAddr,
       "anxTrapHostComm": anxTrapHostComm,
       "anxTrapHostAgeTime": anxTrapHostAgeTime,
       "anxTrapHostPortNumber": anxTrapHostPortNumber,
       "anxTrapHostGrouping": anxTrapHostGrouping,
       "anxTrapUserName": anxTrapUserName,
       "anxTrapPortIndex": anxTrapPortIndex,
       "anxTrapPortType": anxTrapPortType,
       "anxTrapInetAddr": anxTrapInetAddr,
       "anxTrapAttackErrcode": anxTrapAttackErrcode,
       "anxTrapAttackErrmsg": anxTrapAttackErrmsg,
       "anxTrapDbErrcode": anxTrapDbErrcode,
       "anxTrapDbErrmsg": anxTrapDbErrmsg,
       "trapModemMsg": trapModemMsg,
       "operImageModemImage": operImageModemImage,
       "wanVersion": wanVersion,
       "trapAfdMsg": trapAfdMsg,
       "wanBpvThreshold": wanBpvThreshold,
       "wanOofThreshold": wanOofThreshold,
       "wanEsThreshold": wanEsThreshold,
       "wanCvThreshold": wanCvThreshold,
       "wanEsfThreshold": wanEsfThreshold,
       "wanSesThreshold": wanSesThreshold,
       "wanUasThreshold": wanUasThreshold,
       "wanBesThreshold": wanBesThreshold,
       "wanLofcThreshold": wanLofcThreshold,
       "wanCssThreshold": wanCssThreshold,
       "ds0ErrorThreshold": ds0ErrorThreshold,
       "mdmErrorTrapThresh": mdmErrorTrapThresh,
       "callBeginTrapObj": callBeginTrapObj,
       "callEndTrapThresh": callEndTrapThresh,
       "unexpectDisconnectTrapThresh": unexpectDisconnectTrapThresh,
       "forcedCallDisconnectTrapThresh": forcedCallDisconnectTrapThresh,
       "diallnkTrpEna": diallnkTrpEna}
)
