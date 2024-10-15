# SNMP MIB module (SHIVA-FP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SHIVA-FP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:51:25 2024
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

(fastpath,) = mibBuilder.importSymbols(
    "SHIVA-MIB",
    "fastpath")

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

_FpBuffer_ObjectIdentity = ObjectIdentity
fpBuffer = _FpBuffer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 166, 2, 1, 1)
)
_BufferSize_Type = Integer32
_BufferSize_Object = MibScalar
bufferSize = _BufferSize_Object(
    (1, 3, 6, 1, 4, 1, 166, 2, 1, 1, 1),
    _BufferSize_Type()
)
bufferSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferSize.setStatus("mandatory")
_BufferAvail_Type = Integer32
_BufferAvail_Object = MibScalar
bufferAvail = _BufferAvail_Object(
    (1, 3, 6, 1, 4, 1, 166, 2, 1, 1, 2),
    _BufferAvail_Type()
)
bufferAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferAvail.setStatus("mandatory")
_BufferDrops_Type = Counter32
_BufferDrops_Object = MibScalar
bufferDrops = _BufferDrops_Object(
    (1, 3, 6, 1, 4, 1, 166, 2, 1, 1, 3),
    _BufferDrops_Type()
)
bufferDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferDrops.setStatus("mandatory")
_BufferTypeTable_Object = MibTable
bufferTypeTable = _BufferTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 166, 2, 1, 1, 4)
)
if mibBuilder.loadTexts:
    bufferTypeTable.setStatus("mandatory")
_BufferTypeEntry_Object = MibTableRow
bufferTypeEntry = _BufferTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 166, 2, 1, 1, 4, 1)
)
bufferTypeEntry.setIndexNames(
    (0, "SHIVA-FP-MIB", "bufferTypeIndex"),
)
if mibBuilder.loadTexts:
    bufferTypeEntry.setStatus("mandatory")
_BufferTypeIndex_Type = Integer32
_BufferTypeIndex_Object = MibTableColumn
bufferTypeIndex = _BufferTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 166, 2, 1, 1, 4, 1, 1),
    _BufferTypeIndex_Type()
)
bufferTypeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferTypeIndex.setStatus("mandatory")


class _BufferTypeType_Type(Integer32):
    """Custom type bufferTypeType based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("arp", 5),
          ("data", 6),
          ("erbf", 7),
          ("etbf", 8),
          ("ethernet", 4),
          ("free", 2),
          ("localtalk", 3),
          ("malloc", 9),
          ("other", 1),
          ("serial", 10),
          ("tokenring", 11))
    )


_BufferTypeType_Type.__name__ = "Integer32"
_BufferTypeType_Object = MibTableColumn
bufferTypeType = _BufferTypeType_Object(
    (1, 3, 6, 1, 4, 1, 166, 2, 1, 1, 4, 1, 2),
    _BufferTypeType_Type()
)
bufferTypeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferTypeType.setStatus("mandatory")
_BufferTypeDescr_Type = DisplayString
_BufferTypeDescr_Object = MibTableColumn
bufferTypeDescr = _BufferTypeDescr_Object(
    (1, 3, 6, 1, 4, 1, 166, 2, 1, 1, 4, 1, 3),
    _BufferTypeDescr_Type()
)
bufferTypeDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferTypeDescr.setStatus("mandatory")
_BufferTypeCount_Type = Integer32
_BufferTypeCount_Object = MibTableColumn
bufferTypeCount = _BufferTypeCount_Object(
    (1, 3, 6, 1, 4, 1, 166, 2, 1, 1, 4, 1, 4),
    _BufferTypeCount_Type()
)
bufferTypeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferTypeCount.setStatus("mandatory")
_BufferTypeDrops_Type = Integer32
_BufferTypeDrops_Object = MibTableColumn
bufferTypeDrops = _BufferTypeDrops_Object(
    (1, 3, 6, 1, 4, 1, 166, 2, 1, 1, 4, 1, 5),
    _BufferTypeDrops_Type()
)
bufferTypeDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferTypeDrops.setStatus("mandatory")
_BufferTypeRequests_Type = Integer32
_BufferTypeRequests_Object = MibTableColumn
bufferTypeRequests = _BufferTypeRequests_Object(
    (1, 3, 6, 1, 4, 1, 166, 2, 1, 1, 4, 1, 6),
    _BufferTypeRequests_Type()
)
bufferTypeRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferTypeRequests.setStatus("mandatory")
_BufferTypeMaximum_Type = Integer32
_BufferTypeMaximum_Object = MibTableColumn
bufferTypeMaximum = _BufferTypeMaximum_Object(
    (1, 3, 6, 1, 4, 1, 166, 2, 1, 1, 4, 1, 7),
    _BufferTypeMaximum_Type()
)
bufferTypeMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferTypeMaximum.setStatus("mandatory")
_FpConf_ObjectIdentity = ObjectIdentity
fpConf = _FpConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 166, 2, 1, 2)
)
_ConfReboot_Type = TimeTicks
_ConfReboot_Object = MibScalar
confReboot = _ConfReboot_Object(
    (1, 3, 6, 1, 4, 1, 166, 2, 1, 2, 1),
    _ConfReboot_Type()
)
confReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    confReboot.setStatus("mandatory")


class _ConfCheckSum_Type(Integer32):
    """Custom type confCheckSum based on Integer32"""
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


_ConfCheckSum_Type.__name__ = "Integer32"
_ConfCheckSum_Object = MibScalar
confCheckSum = _ConfCheckSum_Object(
    (1, 3, 6, 1, 4, 1, 166, 2, 1, 2, 2),
    _ConfCheckSum_Type()
)
confCheckSum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    confCheckSum.setStatus("mandatory")


class _CodeCheckSum_Type(Integer32):
    """Custom type codeCheckSum based on Integer32"""
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


_CodeCheckSum_Type.__name__ = "Integer32"
_CodeCheckSum_Object = MibScalar
codeCheckSum = _CodeCheckSum_Object(
    (1, 3, 6, 1, 4, 1, 166, 2, 1, 2, 3),
    _CodeCheckSum_Type()
)
codeCheckSum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    codeCheckSum.setStatus("mandatory")
_PromVersion_Type = Integer32
_PromVersion_Object = MibScalar
promVersion = _PromVersion_Object(
    (1, 3, 6, 1, 4, 1, 166, 2, 1, 2, 4),
    _PromVersion_Type()
)
promVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promVersion.setStatus("mandatory")
_HwStatus_Type = Integer32
_HwStatus_Object = MibScalar
hwStatus = _HwStatus_Object(
    (1, 3, 6, 1, 4, 1, 166, 2, 1, 2, 5),
    _HwStatus_Type()
)
hwStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStatus.setStatus("mandatory")


class _ConfWhyReboot_Type(Integer32):
    """Custom type confWhyReboot based on Integer32"""
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
        *(("config", 5),
          ("firmware", 3),
          ("hardware", 2),
          ("other", 1),
          ("software", 4))
    )


_ConfWhyReboot_Type.__name__ = "Integer32"
_ConfWhyReboot_Object = MibScalar
confWhyReboot = _ConfWhyReboot_Object(
    (1, 3, 6, 1, 4, 1, 166, 2, 1, 2, 6),
    _ConfWhyReboot_Type()
)
confWhyReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    confWhyReboot.setStatus("mandatory")
_ConfWhoReboot_Type = DisplayString
_ConfWhoReboot_Object = MibScalar
confWhoReboot = _ConfWhoReboot_Object(
    (1, 3, 6, 1, 4, 1, 166, 2, 1, 2, 7),
    _ConfWhoReboot_Type()
)
confWhoReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    confWhoReboot.setStatus("mandatory")
_ConfRebootComment_Type = DisplayString
_ConfRebootComment_Object = MibScalar
confRebootComment = _ConfRebootComment_Object(
    (1, 3, 6, 1, 4, 1, 166, 2, 1, 2, 8),
    _ConfRebootComment_Type()
)
confRebootComment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    confRebootComment.setStatus("mandatory")


class _ConfHowReboot_Type(Integer32):
    """Custom type confHowReboot based on Integer32"""
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
        *(("bstrap", 7),
          ("cold", 1),
          ("dl", 6),
          ("ramdl", 3),
          ("reset", 4),
          ("romdl", 5),
          ("warm", 2))
    )


_ConfHowReboot_Type.__name__ = "Integer32"
_ConfHowReboot_Object = MibScalar
confHowReboot = _ConfHowReboot_Object(
    (1, 3, 6, 1, 4, 1, 166, 2, 1, 2, 9),
    _ConfHowReboot_Type()
)
confHowReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    confHowReboot.setStatus("mandatory")
_ConfSerialNum_Type = Integer32
_ConfSerialNum_Object = MibScalar
confSerialNum = _ConfSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 166, 2, 1, 2, 10),
    _ConfSerialNum_Type()
)
confSerialNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    confSerialNum.setStatus("mandatory")
_K_star_ObjectIdentity = ObjectIdentity
k_star = _K_star_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 166, 2, 1, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SHIVA-FP-MIB",
    **{"fpBuffer": fpBuffer,
       "bufferSize": bufferSize,
       "bufferAvail": bufferAvail,
       "bufferDrops": bufferDrops,
       "bufferTypeTable": bufferTypeTable,
       "bufferTypeEntry": bufferTypeEntry,
       "bufferTypeIndex": bufferTypeIndex,
       "bufferTypeType": bufferTypeType,
       "bufferTypeDescr": bufferTypeDescr,
       "bufferTypeCount": bufferTypeCount,
       "bufferTypeDrops": bufferTypeDrops,
       "bufferTypeRequests": bufferTypeRequests,
       "bufferTypeMaximum": bufferTypeMaximum,
       "fpConf": fpConf,
       "confReboot": confReboot,
       "confCheckSum": confCheckSum,
       "codeCheckSum": codeCheckSum,
       "promVersion": promVersion,
       "hwStatus": hwStatus,
       "confWhyReboot": confWhyReboot,
       "confWhoReboot": confWhoReboot,
       "confRebootComment": confRebootComment,
       "confHowReboot": confHowReboot,
       "confSerialNum": confSerialNum,
       "k-star": k_star}
)
