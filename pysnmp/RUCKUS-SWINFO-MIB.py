# SNMP MIB module (RUCKUS-SWINFO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RUCKUS-SWINFO-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:48:44 2024
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

(ruckusCommonSwInfoModule,) = mibBuilder.importSymbols(
    "RUCKUS-ROOT-MIB",
    "ruckusCommonSwInfoModule")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

(DateAndTime,
 DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ruckusSwInfoMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 3, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuckusSwInfoObjects_ObjectIdentity = ObjectIdentity
ruckusSwInfoObjects = _RuckusSwInfoObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 3, 1, 1)
)
_RuckusSwInfo_ObjectIdentity = ObjectIdentity
ruckusSwInfo = _RuckusSwInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 3, 1, 1, 1)
)
_RuckusSwRevTable_Object = MibTable
ruckusSwRevTable = _RuckusSwRevTable_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 3, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ruckusSwRevTable.setStatus("current")
_RuckusSwRevEntry_Object = MibTableRow
ruckusSwRevEntry = _RuckusSwRevEntry_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 3, 1, 1, 1, 1, 1)
)
ruckusSwRevEntry.setIndexNames(
    (0, "RUCKUS-SWINFO-MIB", "ruckusSwRevIndex"),
)
if mibBuilder.loadTexts:
    ruckusSwRevEntry.setStatus("current")


class _RuckusSwRevIndex_Type(Integer32):
    """Custom type ruckusSwRevIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_RuckusSwRevIndex_Type.__name__ = "Integer32"
_RuckusSwRevIndex_Object = MibTableColumn
ruckusSwRevIndex = _RuckusSwRevIndex_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 3, 1, 1, 1, 1, 1, 1),
    _RuckusSwRevIndex_Type()
)
ruckusSwRevIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruckusSwRevIndex.setStatus("current")


class _RuckusSwRevName_Type(DisplayString):
    """Custom type ruckusSwRevName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RuckusSwRevName_Type.__name__ = "DisplayString"
_RuckusSwRevName_Object = MibTableColumn
ruckusSwRevName = _RuckusSwRevName_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 3, 1, 1, 1, 1, 1, 2),
    _RuckusSwRevName_Type()
)
ruckusSwRevName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSwRevName.setStatus("current")


class _RuckusSwRevision_Type(DisplayString):
    """Custom type ruckusSwRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuckusSwRevision_Type.__name__ = "DisplayString"
_RuckusSwRevision_Object = MibTableColumn
ruckusSwRevision = _RuckusSwRevision_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 3, 1, 1, 1, 1, 1, 3),
    _RuckusSwRevision_Type()
)
ruckusSwRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSwRevision.setStatus("current")
_RuckusSwRevSize_Type = Unsigned32
_RuckusSwRevSize_Object = MibTableColumn
ruckusSwRevSize = _RuckusSwRevSize_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 3, 1, 1, 1, 1, 1, 4),
    _RuckusSwRevSize_Type()
)
ruckusSwRevSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSwRevSize.setStatus("current")


class _RuckusSwRevStatus_Type(Integer32):
    """Custom type ruckusSwRevStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_RuckusSwRevStatus_Type.__name__ = "Integer32"
_RuckusSwRevStatus_Object = MibTableColumn
ruckusSwRevStatus = _RuckusSwRevStatus_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 3, 1, 1, 1, 1, 1, 5),
    _RuckusSwRevStatus_Type()
)
ruckusSwRevStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSwRevStatus.setStatus("current")
_RuckusSwInfoEvents_ObjectIdentity = ObjectIdentity
ruckusSwInfoEvents = _RuckusSwInfoEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 3, 1, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUCKUS-SWINFO-MIB",
    **{"ruckusSwInfoMIB": ruckusSwInfoMIB,
       "ruckusSwInfoObjects": ruckusSwInfoObjects,
       "ruckusSwInfo": ruckusSwInfo,
       "ruckusSwRevTable": ruckusSwRevTable,
       "ruckusSwRevEntry": ruckusSwRevEntry,
       "ruckusSwRevIndex": ruckusSwRevIndex,
       "ruckusSwRevName": ruckusSwRevName,
       "ruckusSwRevision": ruckusSwRevision,
       "ruckusSwRevSize": ruckusSwRevSize,
       "ruckusSwRevStatus": ruckusSwRevStatus,
       "ruckusSwInfoEvents": ruckusSwInfoEvents}
)
