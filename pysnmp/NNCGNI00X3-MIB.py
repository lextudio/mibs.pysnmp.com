# SNMP MIB module (NNCGNI00X3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NNCGNI00X3-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:28:25 2024
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

(nncExtNetSynch,) = mibBuilder.importSymbols(
    "NNCGNI00X1-SMI",
    "nncExtNetSynch")

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



class NsCandidateIndex(Integer32):
    """Custom type NsCandidateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )





class PortIndex(Integer32):
    """Custom type PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )





class NsSourcePriority(Integer32):
    """Custom type NsSourcePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )





class NsRecoveryKind(Integer32):
    """Custom type NsRecoveryKind based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 2),
          ("manual", 1),
          ("timed", 3))
    )





class NsRecoveryTime(Integer32):
    """Custom type NsRecoveryTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1800),
    )





class NsThreshold(Integer32):
    """Custom type NsThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )





class NsOperStatus(Integer32):
    """Custom type NsOperStatus based on Integer32"""
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
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("acquiring", 14),
          ("autoRecovery", 8),
          ("cannotLock", 9),
          ("current", 3),
          ("disabled", 1),
          ("enabled", 10),
          ("failed", 5),
          ("illegalState", 11),
          ("notReady", 7),
          ("ready", 2),
          ("shutDown", 6),
          ("timedRecovery", 4),
          ("unavailable", 13),
          ("undefinedSource", 12))
    )





class NsAdminStatus(Integer32):
    """Custom type NsAdminStatus based on Integer32"""
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
        *(("deselect", 4),
          ("disable", 2),
          ("enable", 1),
          ("select", 3))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NncExtNsCurrentSource_Type = NsCandidateIndex
_NncExtNsCurrentSource_Object = MibScalar
nncExtNsCurrentSource = _NncExtNsCurrentSource_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 7, 1),
    _NncExtNsCurrentSource_Type()
)
nncExtNsCurrentSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtNsCurrentSource.setStatus("mandatory")
_NncExtNsCurrentClass_Type = NsSourcePriority
_NncExtNsCurrentClass_Object = MibScalar
nncExtNsCurrentClass = _NncExtNsCurrentClass_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 7, 2),
    _NncExtNsCurrentClass_Type()
)
nncExtNsCurrentClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtNsCurrentClass.setStatus("mandatory")
_NncExtNsCandidateTable_Object = MibTable
nncExtNsCandidateTable = _NncExtNsCandidateTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 7, 3)
)
if mibBuilder.loadTexts:
    nncExtNsCandidateTable.setStatus("mandatory")
_NncExtNsCandidateEntry_Object = MibTableRow
nncExtNsCandidateEntry = _NncExtNsCandidateEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 7, 3, 1)
)
nncExtNsCandidateEntry.setIndexNames(
    (0, "NNCGNI00X3-MIB", "nncExtNsCandidateIndex"),
)
if mibBuilder.loadTexts:
    nncExtNsCandidateEntry.setStatus("mandatory")
_NncExtNsCandidateIndex_Type = NsCandidateIndex
_NncExtNsCandidateIndex_Object = MibTableColumn
nncExtNsCandidateIndex = _NncExtNsCandidateIndex_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 7, 3, 1, 1),
    _NncExtNsCandidateIndex_Type()
)
nncExtNsCandidateIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtNsCandidateIndex.setStatus("mandatory")
_NncExtNsCandidateSource_Type = PortIndex
_NncExtNsCandidateSource_Object = MibTableColumn
nncExtNsCandidateSource = _NncExtNsCandidateSource_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 7, 3, 1, 2),
    _NncExtNsCandidateSource_Type()
)
nncExtNsCandidateSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nncExtNsCandidateSource.setStatus("mandatory")
_NncExtNsCandidatePriority_Type = NsSourcePriority
_NncExtNsCandidatePriority_Object = MibTableColumn
nncExtNsCandidatePriority = _NncExtNsCandidatePriority_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 7, 3, 1, 3),
    _NncExtNsCandidatePriority_Type()
)
nncExtNsCandidatePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nncExtNsCandidatePriority.setStatus("mandatory")


class _NncExtNsCandidateRecoveryKind_Type(Integer32):
    """Custom type nncExtNsCandidateRecoveryKind based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 2),
          ("manual", 1),
          ("timed", 3))
    )


_NncExtNsCandidateRecoveryKind_Type.__name__ = "Integer32"
_NncExtNsCandidateRecoveryKind_Object = MibTableColumn
nncExtNsCandidateRecoveryKind = _NncExtNsCandidateRecoveryKind_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 7, 3, 1, 4),
    _NncExtNsCandidateRecoveryKind_Type()
)
nncExtNsCandidateRecoveryKind.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nncExtNsCandidateRecoveryKind.setStatus("mandatory")
_NncExtNsCandidateRecoveryTime_Type = NsRecoveryTime
_NncExtNsCandidateRecoveryTime_Object = MibTableColumn
nncExtNsCandidateRecoveryTime = _NncExtNsCandidateRecoveryTime_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 7, 3, 1, 5),
    _NncExtNsCandidateRecoveryTime_Type()
)
nncExtNsCandidateRecoveryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nncExtNsCandidateRecoveryTime.setStatus("mandatory")
_NncExtNsCandidateFailureThreshold_Type = NsThreshold
_NncExtNsCandidateFailureThreshold_Object = MibTableColumn
nncExtNsCandidateFailureThreshold = _NncExtNsCandidateFailureThreshold_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 7, 3, 1, 6),
    _NncExtNsCandidateFailureThreshold_Type()
)
nncExtNsCandidateFailureThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nncExtNsCandidateFailureThreshold.setStatus("mandatory")


class _NncExtNsCandidateAdminStatus_Type(Integer32):
    """Custom type nncExtNsCandidateAdminStatus based on Integer32"""
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
        *(("deselect", 4),
          ("disable", 2),
          ("enable", 1),
          ("select", 3))
    )


_NncExtNsCandidateAdminStatus_Type.__name__ = "Integer32"
_NncExtNsCandidateAdminStatus_Object = MibTableColumn
nncExtNsCandidateAdminStatus = _NncExtNsCandidateAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 7, 3, 1, 7),
    _NncExtNsCandidateAdminStatus_Type()
)
nncExtNsCandidateAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nncExtNsCandidateAdminStatus.setStatus("mandatory")


class _NncExtNsCandidateOperStatus_Type(Integer32):
    """Custom type nncExtNsCandidateOperStatus based on Integer32"""
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
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("acquiring", 14),
          ("autoRecovery", 8),
          ("cannotLock", 9),
          ("current", 3),
          ("disabled", 1),
          ("enabled", 10),
          ("failed", 5),
          ("illegalState", 11),
          ("notReady", 7),
          ("ready", 2),
          ("shutDown", 6),
          ("timedRecovery", 4),
          ("unavailable", 13),
          ("undefinedSource", 12))
    )


_NncExtNsCandidateOperStatus_Type.__name__ = "Integer32"
_NncExtNsCandidateOperStatus_Object = MibTableColumn
nncExtNsCandidateOperStatus = _NncExtNsCandidateOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 7, 3, 1, 8),
    _NncExtNsCandidateOperStatus_Type()
)
nncExtNsCandidateOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtNsCandidateOperStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NNCGNI00X3-MIB",
    **{"NsCandidateIndex": NsCandidateIndex,
       "PortIndex": PortIndex,
       "NsSourcePriority": NsSourcePriority,
       "NsRecoveryKind": NsRecoveryKind,
       "NsRecoveryTime": NsRecoveryTime,
       "NsThreshold": NsThreshold,
       "NsOperStatus": NsOperStatus,
       "NsAdminStatus": NsAdminStatus,
       "nncExtNsCurrentSource": nncExtNsCurrentSource,
       "nncExtNsCurrentClass": nncExtNsCurrentClass,
       "nncExtNsCandidateTable": nncExtNsCandidateTable,
       "nncExtNsCandidateEntry": nncExtNsCandidateEntry,
       "nncExtNsCandidateIndex": nncExtNsCandidateIndex,
       "nncExtNsCandidateSource": nncExtNsCandidateSource,
       "nncExtNsCandidatePriority": nncExtNsCandidatePriority,
       "nncExtNsCandidateRecoveryKind": nncExtNsCandidateRecoveryKind,
       "nncExtNsCandidateRecoveryTime": nncExtNsCandidateRecoveryTime,
       "nncExtNsCandidateFailureThreshold": nncExtNsCandidateFailureThreshold,
       "nncExtNsCandidateAdminStatus": nncExtNsCandidateAdminStatus,
       "nncExtNsCandidateOperStatus": nncExtNsCandidateOperStatus}
)
