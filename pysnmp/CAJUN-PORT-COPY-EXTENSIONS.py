# SNMP MIB module (CAJUN-PORT-COPY-EXTENSIONS) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CAJUN-PORT-COPY-EXTENSIONS
# Produced by pysmi-1.5.4 at Mon Oct 14 20:53:22 2024
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

(lsg,) = mibBuilder.importSymbols(
    "AVAYAGEN-MIB",
    "lsg")

(portCopyEntry,) = mibBuilder.importSymbols(
    "SMON-MIB",
    "portCopyEntry")

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

cjnPortCopyExtensions = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 5)
)


# Types definitions



class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CjnPortCopyTable_Object = MibTable
cjnPortCopyTable = _CjnPortCopyTable_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 5, 1)
)
if mibBuilder.loadTexts:
    cjnPortCopyTable.setStatus("current")
_CjnPortCopyEntry_Object = MibTableRow
cjnPortCopyEntry = _CjnPortCopyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 5, 1, 1)
)
if mibBuilder.loadTexts:
    cjnPortCopyEntry.setStatus("current")
_CjnPortCopyChannel_Type = Integer32
_CjnPortCopyChannel_Object = MibTableColumn
cjnPortCopyChannel = _CjnPortCopyChannel_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 5, 1, 1, 1),
    _CjnPortCopyChannel_Type()
)
cjnPortCopyChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnPortCopyChannel.setStatus("current")


class _CjnPortCopySamplingMode_Type(Integer32):
    """Custom type cjnPortCopySamplingMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("always", 1),
          ("disabled", 0),
          ("periodic", 2))
    )


_CjnPortCopySamplingMode_Type.__name__ = "Integer32"
_CjnPortCopySamplingMode_Object = MibTableColumn
cjnPortCopySamplingMode = _CjnPortCopySamplingMode_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 5, 1, 1, 2),
    _CjnPortCopySamplingMode_Type()
)
cjnPortCopySamplingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnPortCopySamplingMode.setStatus("current")
_CjnPortCopyMaxPacketsPerSecond_Type = Integer32
_CjnPortCopyMaxPacketsPerSecond_Object = MibTableColumn
cjnPortCopyMaxPacketsPerSecond = _CjnPortCopyMaxPacketsPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 5, 1, 1, 3),
    _CjnPortCopyMaxPacketsPerSecond_Type()
)
cjnPortCopyMaxPacketsPerSecond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnPortCopyMaxPacketsPerSecond.setStatus("current")
_CjnPortCopySAFilter_Type = MacAddress
_CjnPortCopySAFilter_Object = MibTableColumn
cjnPortCopySAFilter = _CjnPortCopySAFilter_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 5, 1, 1, 4),
    _CjnPortCopySAFilter_Type()
)
cjnPortCopySAFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnPortCopySAFilter.setStatus("current")
_CjnPortCopyDAFilter_Type = MacAddress
_CjnPortCopyDAFilter_Object = MibTableColumn
cjnPortCopyDAFilter = _CjnPortCopyDAFilter_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 5, 1, 1, 5),
    _CjnPortCopyDAFilter_Type()
)
cjnPortCopyDAFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnPortCopyDAFilter.setStatus("current")


class _CjnPortCopyFilter_Type(Integer32):
    """Custom type cjnPortCopyFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("da", 2),
          ("disabled", 0),
          ("sa", 1))
    )


_CjnPortCopyFilter_Type.__name__ = "Integer32"
_CjnPortCopyFilter_Object = MibTableColumn
cjnPortCopyFilter = _CjnPortCopyFilter_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 5, 1, 1, 6),
    _CjnPortCopyFilter_Type()
)
cjnPortCopyFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnPortCopyFilter.setStatus("current")
portCopyEntry.registerAugmentions(
    ("CAJUN-PORT-COPY-EXTENSIONS",
     "cjnPortCopyEntry")
)
cjnPortCopyEntry.setIndexNames(*portCopyEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CAJUN-PORT-COPY-EXTENSIONS",
    **{"MacAddress": MacAddress,
       "cjnPortCopyExtensions": cjnPortCopyExtensions,
       "cjnPortCopyTable": cjnPortCopyTable,
       "cjnPortCopyEntry": cjnPortCopyEntry,
       "cjnPortCopyChannel": cjnPortCopyChannel,
       "cjnPortCopySamplingMode": cjnPortCopySamplingMode,
       "cjnPortCopyMaxPacketsPerSecond": cjnPortCopyMaxPacketsPerSecond,
       "cjnPortCopySAFilter": cjnPortCopySAFilter,
       "cjnPortCopyDAFilter": cjnPortCopyDAFilter,
       "cjnPortCopyFilter": cjnPortCopyFilter}
)
