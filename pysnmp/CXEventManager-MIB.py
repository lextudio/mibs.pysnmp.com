# SNMP MIB module (CXEventManager-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CXEventManager-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:20:22 2024
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

(cxEventManager,) = mibBuilder.importSymbols(
    "CXProduct-SMI",
    "cxEventManager")

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



class _CxEvmLoggingCPU_Type(Integer32):
    """Custom type cxEvmLoggingCPU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_CxEvmLoggingCPU_Type.__name__ = "Integer32"
_CxEvmLoggingCPU_Object = MibScalar
cxEvmLoggingCPU = _CxEvmLoggingCPU_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 17, 1),
    _CxEvmLoggingCPU_Type()
)
cxEvmLoggingCPU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxEvmLoggingCPU.setStatus("mandatory")


class _CxEvmTriggerFunction_Type(Integer32):
    """Custom type cxEvmTriggerFunction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CxEvmTriggerFunction_Type.__name__ = "Integer32"
_CxEvmTriggerFunction_Object = MibScalar
cxEvmTriggerFunction = _CxEvmTriggerFunction_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 17, 2),
    _CxEvmTriggerFunction_Type()
)
cxEvmTriggerFunction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxEvmTriggerFunction.setStatus("mandatory")


class _CxEvmTrigDestSelector_Type(Integer32):
    """Custom type cxEvmTrigDestSelector based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CxEvmTrigDestSelector_Type.__name__ = "Integer32"
_CxEvmTrigDestSelector_Object = MibScalar
cxEvmTrigDestSelector = _CxEvmTrigDestSelector_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 17, 3),
    _CxEvmTrigDestSelector_Type()
)
cxEvmTrigDestSelector.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxEvmTrigDestSelector.setStatus("mandatory")


class _CxEvmTrigDestSapId_Type(Integer32):
    """Custom type cxEvmTrigDestSapId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CxEvmTrigDestSapId_Type.__name__ = "Integer32"
_CxEvmTrigDestSapId_Object = MibScalar
cxEvmTrigDestSapId = _CxEvmTrigDestSapId_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 17, 4),
    _CxEvmTrigDestSapId_Type()
)
cxEvmTrigDestSapId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxEvmTrigDestSapId.setStatus("mandatory")


class _CxEvmTrigArgument1_Type(Integer32):
    """Custom type cxEvmTrigArgument1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CxEvmTrigArgument1_Type.__name__ = "Integer32"
_CxEvmTrigArgument1_Object = MibScalar
cxEvmTrigArgument1 = _CxEvmTrigArgument1_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 17, 5),
    _CxEvmTrigArgument1_Type()
)
cxEvmTrigArgument1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxEvmTrigArgument1.setStatus("mandatory")


class _CxEvmTrigArgument2_Type(Integer32):
    """Custom type cxEvmTrigArgument2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CxEvmTrigArgument2_Type.__name__ = "Integer32"
_CxEvmTrigArgument2_Object = MibScalar
cxEvmTrigArgument2 = _CxEvmTrigArgument2_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 17, 6),
    _CxEvmTrigArgument2_Type()
)
cxEvmTrigArgument2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxEvmTrigArgument2.setStatus("mandatory")


class _CxEvmTrigDestCPU_Type(Integer32):
    """Custom type cxEvmTrigDestCPU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_CxEvmTrigDestCPU_Type.__name__ = "Integer32"
_CxEvmTrigDestCPU_Object = MibScalar
cxEvmTrigDestCPU = _CxEvmTrigDestCPU_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 17, 7),
    _CxEvmTrigDestCPU_Type()
)
cxEvmTrigDestCPU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxEvmTrigDestCPU.setStatus("mandatory")
_CxEvmLogFileTable_Object = MibTable
cxEvmLogFileTable = _CxEvmLogFileTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 17, 8)
)
if mibBuilder.loadTexts:
    cxEvmLogFileTable.setStatus("mandatory")
_CxEvmLogFileEntry_Object = MibTableRow
cxEvmLogFileEntry = _CxEvmLogFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 17, 8, 1)
)
cxEvmLogFileEntry.setIndexNames(
    (0, "CXEventManager-MIB", "cxEvmLogFileId"),
)
if mibBuilder.loadTexts:
    cxEvmLogFileEntry.setStatus("mandatory")


class _CxEvmLogFileId_Type(Integer32):
    """Custom type cxEvmLogFileId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_CxEvmLogFileId_Type.__name__ = "Integer32"
_CxEvmLogFileId_Object = MibTableColumn
cxEvmLogFileId = _CxEvmLogFileId_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 17, 8, 1, 1),
    _CxEvmLogFileId_Type()
)
cxEvmLogFileId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxEvmLogFileId.setStatus("mandatory")


class _CxEvmLogFileRowStatus_Type(Integer32):
    """Custom type cxEvmLogFileRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_CxEvmLogFileRowStatus_Type.__name__ = "Integer32"
_CxEvmLogFileRowStatus_Object = MibTableColumn
cxEvmLogFileRowStatus = _CxEvmLogFileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 17, 8, 1, 2),
    _CxEvmLogFileRowStatus_Type()
)
cxEvmLogFileRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxEvmLogFileRowStatus.setStatus("mandatory")
_CxEvmLogFileMaxSize_Type = Integer32
_CxEvmLogFileMaxSize_Object = MibTableColumn
cxEvmLogFileMaxSize = _CxEvmLogFileMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 17, 8, 1, 3),
    _CxEvmLogFileMaxSize_Type()
)
cxEvmLogFileMaxSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxEvmLogFileMaxSize.setStatus("mandatory")
_CxEvmLogFileCurSize_Type = Integer32
_CxEvmLogFileCurSize_Object = MibTableColumn
cxEvmLogFileCurSize = _CxEvmLogFileCurSize_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 17, 8, 1, 4),
    _CxEvmLogFileCurSize_Type()
)
cxEvmLogFileCurSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxEvmLogFileCurSize.setStatus("mandatory")


class _CxEvmLogFileCPUFilter_Type(OctetString):
    """Custom type cxEvmLogFileCPUFilter based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_CxEvmLogFileCPUFilter_Type.__name__ = "OctetString"
_CxEvmLogFileCPUFilter_Object = MibTableColumn
cxEvmLogFileCPUFilter = _CxEvmLogFileCPUFilter_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 17, 8, 1, 5),
    _CxEvmLogFileCPUFilter_Type()
)
cxEvmLogFileCPUFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxEvmLogFileCPUFilter.setStatus("mandatory")


class _CxEvmLogFileEvLogFilter_Type(OctetString):
    """Custom type cxEvmLogFileEvLogFilter based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_CxEvmLogFileEvLogFilter_Type.__name__ = "OctetString"
_CxEvmLogFileEvLogFilter_Object = MibTableColumn
cxEvmLogFileEvLogFilter = _CxEvmLogFileEvLogFilter_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 17, 8, 1, 6),
    _CxEvmLogFileEvLogFilter_Type()
)
cxEvmLogFileEvLogFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxEvmLogFileEvLogFilter.setStatus("mandatory")


class _CxEvmLogFileEvTrapFilter_Type(OctetString):
    """Custom type cxEvmLogFileEvTrapFilter based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_CxEvmLogFileEvTrapFilter_Type.__name__ = "OctetString"
_CxEvmLogFileEvTrapFilter_Object = MibTableColumn
cxEvmLogFileEvTrapFilter = _CxEvmLogFileEvTrapFilter_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 17, 8, 1, 7),
    _CxEvmLogFileEvTrapFilter_Type()
)
cxEvmLogFileEvTrapFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxEvmLogFileEvTrapFilter.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CXEventManager-MIB",
    **{"cxEvmLoggingCPU": cxEvmLoggingCPU,
       "cxEvmTriggerFunction": cxEvmTriggerFunction,
       "cxEvmTrigDestSelector": cxEvmTrigDestSelector,
       "cxEvmTrigDestSapId": cxEvmTrigDestSapId,
       "cxEvmTrigArgument1": cxEvmTrigArgument1,
       "cxEvmTrigArgument2": cxEvmTrigArgument2,
       "cxEvmTrigDestCPU": cxEvmTrigDestCPU,
       "cxEvmLogFileTable": cxEvmLogFileTable,
       "cxEvmLogFileEntry": cxEvmLogFileEntry,
       "cxEvmLogFileId": cxEvmLogFileId,
       "cxEvmLogFileRowStatus": cxEvmLogFileRowStatus,
       "cxEvmLogFileMaxSize": cxEvmLogFileMaxSize,
       "cxEvmLogFileCurSize": cxEvmLogFileCurSize,
       "cxEvmLogFileCPUFilter": cxEvmLogFileCPUFilter,
       "cxEvmLogFileEvLogFilter": cxEvmLogFileEvLogFilter,
       "cxEvmLogFileEvTrapFilter": cxEvmLogFileEvTrapFilter}
)
