# SNMP MIB module (CXLANIOGEN-PORT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CXLANIOGEN-PORT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:20:34 2024
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

(cxLanIoPort,) = mibBuilder.importSymbols(
    "CXProduct-SMI",
    "cxLanIoPort")

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



class PhysAddress(OctetString):
    """Custom type PhysAddress based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CxLanIoGenPortTable_Object = MibTable
cxLanIoGenPortTable = _CxLanIoGenPortTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 10, 2)
)
if mibBuilder.loadTexts:
    cxLanIoGenPortTable.setStatus("mandatory")
_CxLanIoGenPortEntry_Object = MibTableRow
cxLanIoGenPortEntry = _CxLanIoGenPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 10, 2, 1)
)
cxLanIoGenPortEntry.setIndexNames(
    (0, "CXLANIOGEN-PORT-MIB", "cxLanIoGenPortIndex"),
)
if mibBuilder.loadTexts:
    cxLanIoGenPortEntry.setStatus("mandatory")
_CxLanIoGenPortIndex_Type = Integer32
_CxLanIoGenPortIndex_Object = MibTableColumn
cxLanIoGenPortIndex = _CxLanIoGenPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 10, 2, 1, 1),
    _CxLanIoGenPortIndex_Type()
)
cxLanIoGenPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxLanIoGenPortIndex.setStatus("mandatory")
_CxLanIoGenMacAddrSrc_Type = PhysAddress
_CxLanIoGenMacAddrSrc_Object = MibTableColumn
cxLanIoGenMacAddrSrc = _CxLanIoGenMacAddrSrc_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 10, 2, 1, 2),
    _CxLanIoGenMacAddrSrc_Type()
)
cxLanIoGenMacAddrSrc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxLanIoGenMacAddrSrc.setStatus("mandatory")
_CxLanIoGenMacAddrDst_Type = PhysAddress
_CxLanIoGenMacAddrDst_Object = MibTableColumn
cxLanIoGenMacAddrDst = _CxLanIoGenMacAddrDst_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 10, 2, 1, 3),
    _CxLanIoGenMacAddrDst_Type()
)
cxLanIoGenMacAddrDst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxLanIoGenMacAddrDst.setStatus("mandatory")


class _CxLanIoGenType_Type(Integer32):
    """Custom type cxLanIoGenType based on Integer32"""
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
        *(("disabled", 2),
          ("internalLoopbackLevel1", 3),
          ("internalLoopbackLevel2", 4),
          ("invalid", 1),
          ("noLoopbackFrameForward", 6),
          ("noLoopbackFrameVerify", 5))
    )


_CxLanIoGenType_Type.__name__ = "Integer32"
_CxLanIoGenType_Object = MibTableColumn
cxLanIoGenType = _CxLanIoGenType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 10, 2, 1, 4),
    _CxLanIoGenType_Type()
)
cxLanIoGenType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxLanIoGenType.setStatus("mandatory")


class _CxLanIoGenDelay_Type(Integer32):
    """Custom type cxLanIoGenDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CxLanIoGenDelay_Type.__name__ = "Integer32"
_CxLanIoGenDelay_Object = MibTableColumn
cxLanIoGenDelay = _CxLanIoGenDelay_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 10, 2, 1, 5),
    _CxLanIoGenDelay_Type()
)
cxLanIoGenDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxLanIoGenDelay.setStatus("mandatory")


class _CxLanIoGenFrameSize_Type(Integer32):
    """Custom type cxLanIoGenFrameSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 4096),
    )


_CxLanIoGenFrameSize_Type.__name__ = "Integer32"
_CxLanIoGenFrameSize_Object = MibTableColumn
cxLanIoGenFrameSize = _CxLanIoGenFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 10, 2, 1, 6),
    _CxLanIoGenFrameSize_Type()
)
cxLanIoGenFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxLanIoGenFrameSize.setStatus("mandatory")


class _CxLanIoGenStatus_Type(Integer32):
    """Custom type cxLanIoGenStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("internalLoopbackLevel1", 3),
          ("internalLoopbackLevel2", 4),
          ("noLoopbackFrameForward", 6),
          ("noLoopbackFrameVerify", 5))
    )


_CxLanIoGenStatus_Type.__name__ = "Integer32"
_CxLanIoGenStatus_Object = MibTableColumn
cxLanIoGenStatus = _CxLanIoGenStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 10, 2, 1, 7),
    _CxLanIoGenStatus_Type()
)
cxLanIoGenStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxLanIoGenStatus.setStatus("mandatory")
_CxLanIoGenRxError_Type = Counter32
_CxLanIoGenRxError_Object = MibTableColumn
cxLanIoGenRxError = _CxLanIoGenRxError_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 10, 2, 1, 8),
    _CxLanIoGenRxError_Type()
)
cxLanIoGenRxError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxLanIoGenRxError.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CXLANIOGEN-PORT-MIB",
    **{"PhysAddress": PhysAddress,
       "cxLanIoGenPortTable": cxLanIoGenPortTable,
       "cxLanIoGenPortEntry": cxLanIoGenPortEntry,
       "cxLanIoGenPortIndex": cxLanIoGenPortIndex,
       "cxLanIoGenMacAddrSrc": cxLanIoGenMacAddrSrc,
       "cxLanIoGenMacAddrDst": cxLanIoGenMacAddrDst,
       "cxLanIoGenType": cxLanIoGenType,
       "cxLanIoGenDelay": cxLanIoGenDelay,
       "cxLanIoGenFrameSize": cxLanIoGenFrameSize,
       "cxLanIoGenStatus": cxLanIoGenStatus,
       "cxLanIoGenRxError": cxLanIoGenRxError}
)
