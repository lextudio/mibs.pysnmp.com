# SNMP MIB module (CADANT-CMTS-PC-EVENTMSG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CADANT-CMTS-PC-EVENTMSG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:52:44 2024
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

(cadPCMibObjects,) = mibBuilder.importSymbols(
    "CADANT-CMTS-PACKETCABLE-MIB",
    "cadPCMibObjects")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

cadEvMsgMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 5)
)
cadEvMsgMIB.setRevisions(
        ("2007-10-24 00:00",
         "2005-05-23 00:00",
         "2003-02-05 00:00",
         "2002-12-27 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class TimeOfDay(OctetString, TextualConvention):
    status = "current"
    displayHint = "1d:1d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )



# MIB Managed Objects in the order of their OIDs

_CadEvMsgMibBase_ObjectIdentity = ObjectIdentity
cadEvMsgMibBase = _CadEvMsgMibBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 5, 1)
)


class _CadEvMsgElementType_Type(Unsigned32):
    """Custom type cadEvMsgElementType based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_CadEvMsgElementType_Type.__name__ = "Unsigned32"
_CadEvMsgElementType_Object = MibScalar
cadEvMsgElementType = _CadEvMsgElementType_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 5, 1, 1),
    _CadEvMsgElementType_Type()
)
cadEvMsgElementType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadEvMsgElementType.setStatus("current")


class _CadEvMsgElementId_Type(Unsigned32):
    """Custom type cadEvMsgElementId based on Unsigned32"""
    defaultValue = 100000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_CadEvMsgElementId_Type.__name__ = "Unsigned32"
_CadEvMsgElementId_Object = MibScalar
cadEvMsgElementId = _CadEvMsgElementId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 5, 1, 2),
    _CadEvMsgElementId_Type()
)
cadEvMsgElementId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadEvMsgElementId.setStatus("current")


class _CadEvMsgMaxAge_Type(Unsigned32):
    """Custom type cadEvMsgMaxAge based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_CadEvMsgMaxAge_Type.__name__ = "Unsigned32"
_CadEvMsgMaxAge_Object = MibScalar
cadEvMsgMaxAge = _CadEvMsgMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 5, 1, 3),
    _CadEvMsgMaxAge_Type()
)
cadEvMsgMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadEvMsgMaxAge.setStatus("current")
if mibBuilder.loadTexts:
    cadEvMsgMaxAge.setUnits("minutes")


class _CadEvMsgRetransTimer_Type(Unsigned32):
    """Custom type cadEvMsgRetransTimer based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10000),
    )


_CadEvMsgRetransTimer_Type.__name__ = "Unsigned32"
_CadEvMsgRetransTimer_Object = MibScalar
cadEvMsgRetransTimer = _CadEvMsgRetransTimer_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 5, 1, 4),
    _CadEvMsgRetransTimer_Type()
)
cadEvMsgRetransTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadEvMsgRetransTimer.setStatus("current")
if mibBuilder.loadTexts:
    cadEvMsgRetransTimer.setUnits("milliseconds")


class _CadEvMsgMaxRetry_Type(Unsigned32):
    """Custom type cadEvMsgMaxRetry based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_CadEvMsgMaxRetry_Type.__name__ = "Unsigned32"
_CadEvMsgMaxRetry_Object = MibScalar
cadEvMsgMaxRetry = _CadEvMsgMaxRetry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 5, 1, 5),
    _CadEvMsgMaxRetry_Type()
)
cadEvMsgMaxRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadEvMsgMaxRetry.setStatus("current")


class _CadEvMsgMaxBatchSize_Type(Unsigned32):
    """Custom type cadEvMsgMaxBatchSize based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_CadEvMsgMaxBatchSize_Type.__name__ = "Unsigned32"
_CadEvMsgMaxBatchSize_Object = MibScalar
cadEvMsgMaxBatchSize = _CadEvMsgMaxBatchSize_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 5, 1, 6),
    _CadEvMsgMaxBatchSize_Type()
)
cadEvMsgMaxBatchSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadEvMsgMaxBatchSize.setStatus("current")


class _CadEvMsgEnableFlag_Type(TruthValue):
    """Custom type cadEvMsgEnableFlag based on TruthValue"""


_CadEvMsgEnableFlag_Object = MibScalar
cadEvMsgEnableFlag = _CadEvMsgEnableFlag_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 5, 1, 7),
    _CadEvMsgEnableFlag_Type()
)
cadEvMsgEnableFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadEvMsgEnableFlag.setStatus("current")
_CadEvMsgTransTimeTable_Object = MibTable
cadEvMsgTransTimeTable = _CadEvMsgTransTimeTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 5, 2)
)
if mibBuilder.loadTexts:
    cadEvMsgTransTimeTable.setStatus("current")
_CadEvMsgTransTimeEntry_Object = MibTableRow
cadEvMsgTransTimeEntry = _CadEvMsgTransTimeEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 5, 2, 1)
)
cadEvMsgTransTimeEntry.setIndexNames(
    (0, "CADANT-CMTS-PC-EVENTMSG-MIB", "cadEvMsgTransTimeIdx"),
)
if mibBuilder.loadTexts:
    cadEvMsgTransTimeEntry.setStatus("current")


class _CadEvMsgTransTimeIdx_Type(Unsigned32):
    """Custom type cadEvMsgTransTimeIdx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_CadEvMsgTransTimeIdx_Type.__name__ = "Unsigned32"
_CadEvMsgTransTimeIdx_Object = MibTableColumn
cadEvMsgTransTimeIdx = _CadEvMsgTransTimeIdx_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 5, 2, 1, 1),
    _CadEvMsgTransTimeIdx_Type()
)
cadEvMsgTransTimeIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadEvMsgTransTimeIdx.setStatus("current")


class _CadEvMsgTransTOD_Type(TimeOfDay):
    """Custom type cadEvMsgTransTOD based on TimeOfDay"""
    defaultValue = OctetString("00:00")


_CadEvMsgTransTOD_Object = MibTableColumn
cadEvMsgTransTOD = _CadEvMsgTransTOD_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 5, 2, 1, 2),
    _CadEvMsgTransTOD_Type()
)
cadEvMsgTransTOD.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadEvMsgTransTOD.setStatus("current")
_CadEvMsgTransTimeStatus_Type = RowStatus
_CadEvMsgTransTimeStatus_Object = MibTableColumn
cadEvMsgTransTimeStatus = _CadEvMsgTransTimeStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 5, 2, 1, 3),
    _CadEvMsgTransTimeStatus_Type()
)
cadEvMsgTransTimeStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadEvMsgTransTimeStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CADANT-CMTS-PC-EVENTMSG-MIB",
    **{"TimeOfDay": TimeOfDay,
       "cadEvMsgMIB": cadEvMsgMIB,
       "cadEvMsgMibBase": cadEvMsgMibBase,
       "cadEvMsgElementType": cadEvMsgElementType,
       "cadEvMsgElementId": cadEvMsgElementId,
       "cadEvMsgMaxAge": cadEvMsgMaxAge,
       "cadEvMsgRetransTimer": cadEvMsgRetransTimer,
       "cadEvMsgMaxRetry": cadEvMsgMaxRetry,
       "cadEvMsgMaxBatchSize": cadEvMsgMaxBatchSize,
       "cadEvMsgEnableFlag": cadEvMsgEnableFlag,
       "cadEvMsgTransTimeTable": cadEvMsgTransTimeTable,
       "cadEvMsgTransTimeEntry": cadEvMsgTransTimeEntry,
       "cadEvMsgTransTimeIdx": cadEvMsgTransTimeIdx,
       "cadEvMsgTransTOD": cadEvMsgTransTOD,
       "cadEvMsgTransTimeStatus": cadEvMsgTransTimeStatus}
)
