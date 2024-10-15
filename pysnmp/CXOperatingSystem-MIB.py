# SNMP MIB module (CXOperatingSystem-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CXOperatingSystem-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:20:44 2024
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

(cxOperatingSystem,) = mibBuilder.importSymbols(
    "CXProduct-SMI",
    "cxOperatingSystem")

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

_CxOsParameter_ObjectIdentity = ObjectIdentity
cxOsParameter = _CxOsParameter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 5, 1)
)


class _CxOsNbBufs_Type(Integer32):
    """Custom type cxOsNbBufs based on Integer32"""
    defaultValue = 1200


_CxOsNbBufs_Object = MibScalar
cxOsNbBufs = _CxOsNbBufs_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 5, 1, 1),
    _CxOsNbBufs_Type()
)
cxOsNbBufs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxOsNbBufs.setStatus("mandatory")


class _CxOsBufSize_Type(Integer32):
    """Custom type cxOsBufSize based on Integer32"""
    defaultValue = 292


_CxOsBufSize_Object = MibScalar
cxOsBufSize = _CxOsBufSize_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 5, 1, 2),
    _CxOsBufSize_Type()
)
cxOsBufSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxOsBufSize.setStatus("mandatory")
_CxOsNbBufsAvail_Type = Integer32
_CxOsNbBufsAvail_Object = MibScalar
cxOsNbBufsAvail = _CxOsNbBufsAvail_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 5, 1, 3),
    _CxOsNbBufsAvail_Type()
)
cxOsNbBufsAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxOsNbBufsAvail.setStatus("mandatory")
_CxOsNbBufsFree_Type = Integer32
_CxOsNbBufsFree_Object = MibScalar
cxOsNbBufsFree = _CxOsNbBufsFree_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 5, 1, 4),
    _CxOsNbBufsFree_Type()
)
cxOsNbBufsFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxOsNbBufsFree.setStatus("mandatory")


class _CxOsNbSystemMsg_Type(Integer32):
    """Custom type cxOsNbSystemMsg based on Integer32"""
    defaultValue = 1320


_CxOsNbSystemMsg_Object = MibScalar
cxOsNbSystemMsg = _CxOsNbSystemMsg_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 5, 1, 16),
    _CxOsNbSystemMsg_Type()
)
cxOsNbSystemMsg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxOsNbSystemMsg.setStatus("mandatory")
_CxOsNbSystemMsgFree_Type = Integer32
_CxOsNbSystemMsgFree_Object = MibScalar
cxOsNbSystemMsgFree = _CxOsNbSystemMsgFree_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 5, 1, 17),
    _CxOsNbSystemMsgFree_Type()
)
cxOsNbSystemMsgFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxOsNbSystemMsgFree.setStatus("mandatory")


class _CxOsOptions_Type(Integer32):
    """Custom type cxOsOptions based on Integer32"""
    defaultValue = 7

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
        *(("data", 1),
          ("data-inst", 3),
          ("inst", 2),
          ("none", 8),
          ("p-data", 5),
          ("p-data-inst", 7),
          ("p-inst", 6),
          ("pipeline", 4))
    )


_CxOsOptions_Type.__name__ = "Integer32"
_CxOsOptions_Object = MibScalar
cxOsOptions = _CxOsOptions_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 5, 1, 18),
    _CxOsOptions_Type()
)
cxOsOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxOsOptions.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CXOperatingSystem-MIB",
    **{"cxOsParameter": cxOsParameter,
       "cxOsNbBufs": cxOsNbBufs,
       "cxOsBufSize": cxOsBufSize,
       "cxOsNbBufsAvail": cxOsNbBufsAvail,
       "cxOsNbBufsFree": cxOsNbBufsFree,
       "cxOsNbSystemMsg": cxOsNbSystemMsg,
       "cxOsNbSystemMsgFree": cxOsNbSystemMsgFree,
       "cxOsOptions": cxOsOptions}
)
