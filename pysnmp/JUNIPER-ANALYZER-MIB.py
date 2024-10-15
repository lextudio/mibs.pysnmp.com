# SNMP MIB module (JUNIPER-ANALYZER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-ANALYZER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:12:47 2024
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

(jnxExAnalyzer,) = mibBuilder.importSymbols(
    "JUNIPER-EX-SMI",
    "jnxExAnalyzer")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

jnxAnalyzerMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 1, 1)
)
jnxAnalyzerMIB.setRevisions(
        ("2008-08-01 00:00",
         "2009-04-22 00:00",
         "2010-07-30 00:00",
         "2014-07-17 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxAnalyzerMIBObjects_ObjectIdentity = ObjectIdentity
jnxAnalyzerMIBObjects = _JnxAnalyzerMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 1, 1, 1)
)
_JnxAnalyzerTable_Object = MibTable
jnxAnalyzerTable = _JnxAnalyzerTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    jnxAnalyzerTable.setStatus("current")
_JnxAnalyzerEntry_Object = MibTableRow
jnxAnalyzerEntry = _JnxAnalyzerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 1, 1, 1, 1, 1)
)
jnxAnalyzerEntry.setIndexNames(
    (0, "JUNIPER-ANALYZER-MIB", "jnxAnalyzerName"),
)
if mibBuilder.loadTexts:
    jnxAnalyzerEntry.setStatus("current")


class _JnxAnalyzerName_Type(DisplayString):
    """Custom type jnxAnalyzerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_JnxAnalyzerName_Type.__name__ = "DisplayString"
_JnxAnalyzerName_Object = MibTableColumn
jnxAnalyzerName = _JnxAnalyzerName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 1, 1, 1, 1, 1, 1),
    _JnxAnalyzerName_Type()
)
jnxAnalyzerName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxAnalyzerName.setStatus("current")
_JnxAnalyzerStatus_Type = TruthValue
_JnxAnalyzerStatus_Object = MibTableColumn
jnxAnalyzerStatus = _JnxAnalyzerStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 1, 1, 1, 1, 1, 2),
    _JnxAnalyzerStatus_Type()
)
jnxAnalyzerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAnalyzerStatus.setStatus("obsolete")


class _JnxMirroringRatio_Type(Unsigned32):
    """Custom type jnxMirroringRatio based on Unsigned32"""
    defaultValue = 1


_JnxMirroringRatio_Object = MibTableColumn
jnxMirroringRatio = _JnxMirroringRatio_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 1, 1, 1, 1, 1, 3),
    _JnxMirroringRatio_Type()
)
jnxMirroringRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMirroringRatio.setStatus("current")


class _JnxLossPriority_Type(Integer32):
    """Custom type jnxLossPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 0))
    )


_JnxLossPriority_Type.__name__ = "Integer32"
_JnxLossPriority_Object = MibTableColumn
jnxLossPriority = _JnxLossPriority_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 1, 1, 1, 1, 1, 4),
    _JnxLossPriority_Type()
)
jnxLossPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLossPriority.setStatus("current")
_JnxAnalyzerInputTable_Object = MibTable
jnxAnalyzerInputTable = _JnxAnalyzerInputTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    jnxAnalyzerInputTable.setStatus("obsolete")
_JnxAnalyzerInputEntry_Object = MibTableRow
jnxAnalyzerInputEntry = _JnxAnalyzerInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 1, 1, 1, 2, 1)
)
jnxAnalyzerInputEntry.setIndexNames(
    (0, "JUNIPER-ANALYZER-MIB", "jnxAnalyzerName"),
    (0, "JUNIPER-ANALYZER-MIB", "jnxAnalyzerInputValue"),
)
if mibBuilder.loadTexts:
    jnxAnalyzerInputEntry.setStatus("obsolete")


class _JnxAnalyzerInputValue_Type(DisplayString):
    """Custom type jnxAnalyzerInputValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_JnxAnalyzerInputValue_Type.__name__ = "DisplayString"
_JnxAnalyzerInputValue_Object = MibTableColumn
jnxAnalyzerInputValue = _JnxAnalyzerInputValue_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 1, 1, 1, 2, 1, 1),
    _JnxAnalyzerInputValue_Type()
)
jnxAnalyzerInputValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxAnalyzerInputValue.setStatus("obsolete")


class _JnxAnalyzerInputOption_Type(Integer32):
    """Custom type jnxAnalyzerInputOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("egress", 2),
          ("ingress", 1))
    )


_JnxAnalyzerInputOption_Type.__name__ = "Integer32"
_JnxAnalyzerInputOption_Object = MibTableColumn
jnxAnalyzerInputOption = _JnxAnalyzerInputOption_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 1, 1, 1, 2, 1, 2),
    _JnxAnalyzerInputOption_Type()
)
jnxAnalyzerInputOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAnalyzerInputOption.setStatus("obsolete")


class _JnxAnalyzerInputType_Type(Integer32):
    """Custom type jnxAnalyzerInputType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("interface", 1),
          ("vlanname", 2))
    )


_JnxAnalyzerInputType_Type.__name__ = "Integer32"
_JnxAnalyzerInputType_Object = MibTableColumn
jnxAnalyzerInputType = _JnxAnalyzerInputType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 1, 1, 1, 2, 1, 3),
    _JnxAnalyzerInputType_Type()
)
jnxAnalyzerInputType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAnalyzerInputType.setStatus("obsolete")
_JnxAnalyzerOutputTable_Object = MibTable
jnxAnalyzerOutputTable = _JnxAnalyzerOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    jnxAnalyzerOutputTable.setStatus("current")
_JnxAnalyzerOutputEntry_Object = MibTableRow
jnxAnalyzerOutputEntry = _JnxAnalyzerOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 1, 1, 1, 3, 1)
)
jnxAnalyzerOutputEntry.setIndexNames(
    (0, "JUNIPER-ANALYZER-MIB", "jnxAnalyzerName"),
    (0, "JUNIPER-ANALYZER-MIB", "jnxAnalyzerOutputValue"),
)
if mibBuilder.loadTexts:
    jnxAnalyzerOutputEntry.setStatus("current")


class _JnxAnalyzerOutputValue_Type(DisplayString):
    """Custom type jnxAnalyzerOutputValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_JnxAnalyzerOutputValue_Type.__name__ = "DisplayString"
_JnxAnalyzerOutputValue_Object = MibTableColumn
jnxAnalyzerOutputValue = _JnxAnalyzerOutputValue_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 1, 1, 1, 3, 1, 1),
    _JnxAnalyzerOutputValue_Type()
)
jnxAnalyzerOutputValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxAnalyzerOutputValue.setStatus("current")


class _JnxAnalyzerOutputType_Type(Integer32):
    """Custom type jnxAnalyzerOutputType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("interface", 1),
          ("vlanname", 2))
    )


_JnxAnalyzerOutputType_Type.__name__ = "Integer32"
_JnxAnalyzerOutputType_Object = MibTableColumn
jnxAnalyzerOutputType = _JnxAnalyzerOutputType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 1, 1, 1, 3, 1, 2),
    _JnxAnalyzerOutputType_Type()
)
jnxAnalyzerOutputType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAnalyzerOutputType.setStatus("current")
_JnxExAnalyzerInputTable_Object = MibTable
jnxExAnalyzerInputTable = _JnxExAnalyzerInputTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 1, 1, 1, 4)
)
if mibBuilder.loadTexts:
    jnxExAnalyzerInputTable.setStatus("current")
_JnxExAnalyzerInputEntry_Object = MibTableRow
jnxExAnalyzerInputEntry = _JnxExAnalyzerInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 1, 1, 1, 4, 1)
)
jnxExAnalyzerInputEntry.setIndexNames(
    (0, "JUNIPER-ANALYZER-MIB", "jnxAnalyzerName"),
    (0, "JUNIPER-ANALYZER-MIB", "jnxExAnalyzerInputOption"),
    (0, "JUNIPER-ANALYZER-MIB", "jnxExAnalyzerInputValue"),
)
if mibBuilder.loadTexts:
    jnxExAnalyzerInputEntry.setStatus("current")


class _JnxExAnalyzerInputOption_Type(Integer32):
    """Custom type jnxExAnalyzerInputOption based on Integer32"""
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
        *(("egress", 2),
          ("egress-vlan", 4),
          ("ingress", 1),
          ("vlan", 3))
    )


_JnxExAnalyzerInputOption_Type.__name__ = "Integer32"
_JnxExAnalyzerInputOption_Object = MibTableColumn
jnxExAnalyzerInputOption = _JnxExAnalyzerInputOption_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 1, 1, 1, 4, 1, 1),
    _JnxExAnalyzerInputOption_Type()
)
jnxExAnalyzerInputOption.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxExAnalyzerInputOption.setStatus("current")


class _JnxExAnalyzerInputValue_Type(DisplayString):
    """Custom type jnxExAnalyzerInputValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_JnxExAnalyzerInputValue_Type.__name__ = "DisplayString"
_JnxExAnalyzerInputValue_Object = MibTableColumn
jnxExAnalyzerInputValue = _JnxExAnalyzerInputValue_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 1, 1, 1, 4, 1, 2),
    _JnxExAnalyzerInputValue_Type()
)
jnxExAnalyzerInputValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxExAnalyzerInputValue.setStatus("current")


class _JnxExAnalyzerInputType_Type(Integer32):
    """Custom type jnxExAnalyzerInputType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("interface", 1),
          ("vlanname", 2))
    )


_JnxExAnalyzerInputType_Type.__name__ = "Integer32"
_JnxExAnalyzerInputType_Object = MibTableColumn
jnxExAnalyzerInputType = _JnxExAnalyzerInputType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 1, 1, 1, 4, 1, 3),
    _JnxExAnalyzerInputType_Type()
)
jnxExAnalyzerInputType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxExAnalyzerInputType.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-ANALYZER-MIB",
    **{"jnxAnalyzerMIB": jnxAnalyzerMIB,
       "jnxAnalyzerMIBObjects": jnxAnalyzerMIBObjects,
       "jnxAnalyzerTable": jnxAnalyzerTable,
       "jnxAnalyzerEntry": jnxAnalyzerEntry,
       "jnxAnalyzerName": jnxAnalyzerName,
       "jnxAnalyzerStatus": jnxAnalyzerStatus,
       "jnxMirroringRatio": jnxMirroringRatio,
       "jnxLossPriority": jnxLossPriority,
       "jnxAnalyzerInputTable": jnxAnalyzerInputTable,
       "jnxAnalyzerInputEntry": jnxAnalyzerInputEntry,
       "jnxAnalyzerInputValue": jnxAnalyzerInputValue,
       "jnxAnalyzerInputOption": jnxAnalyzerInputOption,
       "jnxAnalyzerInputType": jnxAnalyzerInputType,
       "jnxAnalyzerOutputTable": jnxAnalyzerOutputTable,
       "jnxAnalyzerOutputEntry": jnxAnalyzerOutputEntry,
       "jnxAnalyzerOutputValue": jnxAnalyzerOutputValue,
       "jnxAnalyzerOutputType": jnxAnalyzerOutputType,
       "jnxExAnalyzerInputTable": jnxExAnalyzerInputTable,
       "jnxExAnalyzerInputEntry": jnxExAnalyzerInputEntry,
       "jnxExAnalyzerInputOption": jnxExAnalyzerInputOption,
       "jnxExAnalyzerInputValue": jnxExAnalyzerInputValue,
       "jnxExAnalyzerInputType": jnxExAnalyzerInputType}
)
