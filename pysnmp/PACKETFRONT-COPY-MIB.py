# SNMP MIB module (PACKETFRONT-COPY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PACKETFRONT-COPY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:36:04 2024
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

(pfExperiment,) = mibBuilder.importSymbols(
    "PACKETFRONT-SMI",
    "pfExperiment")

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

pfCopy = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 3, 2)
)
pfCopy.setRevisions(
        ("2011-01-11 17:35",
         "2009-03-23 11:17",
         "2008-09-10 15:38")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PfCopyNextState_Type = Unsigned32
_PfCopyNextState_Object = MibScalar
pfCopyNextState = _PfCopyNextState_Object(
    (1, 3, 6, 1, 4, 1, 9303, 3, 2, 1),
    _PfCopyNextState_Type()
)
pfCopyNextState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfCopyNextState.setStatus("current")
_PfCopyTable_Object = MibTable
pfCopyTable = _PfCopyTable_Object(
    (1, 3, 6, 1, 4, 1, 9303, 3, 2, 2)
)
if mibBuilder.loadTexts:
    pfCopyTable.setStatus("current")
_PfCopyEntry_Object = MibTableRow
pfCopyEntry = _PfCopyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9303, 3, 2, 2, 1)
)
pfCopyEntry.setIndexNames(
    (0, "PACKETFRONT-COPY-MIB", "pfCopyIndex"),
)
if mibBuilder.loadTexts:
    pfCopyEntry.setStatus("current")
_PfCopyIndex_Type = Unsigned32
_PfCopyIndex_Object = MibTableColumn
pfCopyIndex = _PfCopyIndex_Object(
    (1, 3, 6, 1, 4, 1, 9303, 3, 2, 2, 1, 1),
    _PfCopyIndex_Type()
)
pfCopyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfCopyIndex.setStatus("current")


class _PfCopySource_Type(DisplayString):
    """Custom type pfCopySource based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PfCopySource_Type.__name__ = "DisplayString"
_PfCopySource_Object = MibTableColumn
pfCopySource = _PfCopySource_Object(
    (1, 3, 6, 1, 4, 1, 9303, 3, 2, 2, 1, 2),
    _PfCopySource_Type()
)
pfCopySource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pfCopySource.setStatus("current")


class _PfCopyDestination_Type(DisplayString):
    """Custom type pfCopyDestination based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PfCopyDestination_Type.__name__ = "DisplayString"
_PfCopyDestination_Object = MibTableColumn
pfCopyDestination = _PfCopyDestination_Object(
    (1, 3, 6, 1, 4, 1, 9303, 3, 2, 2, 1, 3),
    _PfCopyDestination_Type()
)
pfCopyDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pfCopyDestination.setStatus("current")


class _PfCopyStatus_Type(Integer32):
    """Custom type pfCopyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("destroy", 3),
          ("failed", 6),
          ("finished", 7),
          ("init", 4),
          ("inprogress", 5),
          ("notused", 0),
          ("start", 1),
          ("stop", 2))
    )


_PfCopyStatus_Type.__name__ = "Integer32"
_PfCopyStatus_Object = MibTableColumn
pfCopyStatus = _PfCopyStatus_Object(
    (1, 3, 6, 1, 4, 1, 9303, 3, 2, 2, 1, 4),
    _PfCopyStatus_Type()
)
pfCopyStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pfCopyStatus.setStatus("current")


class _PfCopyError_Type(DisplayString):
    """Custom type pfCopyError based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PfCopyError_Type.__name__ = "DisplayString"
_PfCopyError_Object = MibTableColumn
pfCopyError = _PfCopyError_Object(
    (1, 3, 6, 1, 4, 1, 9303, 3, 2, 2, 1, 5),
    _PfCopyError_Type()
)
pfCopyError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfCopyError.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PACKETFRONT-COPY-MIB",
    **{"pfCopy": pfCopy,
       "pfCopyNextState": pfCopyNextState,
       "pfCopyTable": pfCopyTable,
       "pfCopyEntry": pfCopyEntry,
       "pfCopyIndex": pfCopyIndex,
       "pfCopySource": pfCopySource,
       "pfCopyDestination": pfCopyDestination,
       "pfCopyStatus": pfCopyStatus,
       "pfCopyError": pfCopyError}
)
