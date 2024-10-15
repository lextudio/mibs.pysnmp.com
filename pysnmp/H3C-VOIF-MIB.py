# SNMP MIB module (H3C-VOIF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/H3C-VOIF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:51:51 2024
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

(h3cVoice,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "h3cVoice")

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

h3cVoiceIf = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 2)
)
h3cVoiceIf.setRevisions(
        ("2005-03-15 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cVoIfObjects_ObjectIdentity = ObjectIdentity
h3cVoIfObjects = _H3cVoIfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 2, 1)
)
_H3cVoIfConfigTable_Object = MibTable
h3cVoIfConfigTable = _H3cVoIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 2, 1, 1)
)
if mibBuilder.loadTexts:
    h3cVoIfConfigTable.setStatus("current")
_H3cVoIfConfigEntry_Object = MibTableRow
h3cVoIfConfigEntry = _H3cVoIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 2, 1, 1, 1)
)
h3cVoIfConfigEntry.setIndexNames(
    (0, "H3C-VOIF-MIB", "h3cVoIfCfgPortNumber"),
    (0, "H3C-VOIF-MIB", "h3cVoIfCfgGroupNumber"),
)
if mibBuilder.loadTexts:
    h3cVoIfConfigEntry.setStatus("current")
_H3cVoIfCfgPortNumber_Type = Integer32
_H3cVoIfCfgPortNumber_Object = MibTableColumn
h3cVoIfCfgPortNumber = _H3cVoIfCfgPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 2, 1, 1, 1, 1),
    _H3cVoIfCfgPortNumber_Type()
)
h3cVoIfCfgPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cVoIfCfgPortNumber.setStatus("current")
_H3cVoIfCfgGroupNumber_Type = Integer32
_H3cVoIfCfgGroupNumber_Object = MibTableColumn
h3cVoIfCfgGroupNumber = _H3cVoIfCfgGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 2, 1, 1, 1, 2),
    _H3cVoIfCfgGroupNumber_Type()
)
h3cVoIfCfgGroupNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cVoIfCfgGroupNumber.setStatus("current")


class _H3cVoIfCfgCngOn_Type(Integer32):
    """Custom type h3cVoIfCfgCngOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_H3cVoIfCfgCngOn_Type.__name__ = "Integer32"
_H3cVoIfCfgCngOn_Object = MibTableColumn
h3cVoIfCfgCngOn = _H3cVoIfCfgCngOn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 2, 1, 1, 1, 3),
    _H3cVoIfCfgCngOn_Type()
)
h3cVoIfCfgCngOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoIfCfgCngOn.setStatus("current")
_H3cVoIfConfigInputGain_Type = Integer32
_H3cVoIfConfigInputGain_Object = MibTableColumn
h3cVoIfConfigInputGain = _H3cVoIfConfigInputGain_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 2, 1, 1, 1, 4),
    _H3cVoIfConfigInputGain_Type()
)
h3cVoIfConfigInputGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoIfConfigInputGain.setStatus("current")


class _H3cVoIfConfigOutputGain_Type(Integer32):
    """Custom type h3cVoIfConfigOutputGain based on Integer32"""
    defaultValue = 0


_H3cVoIfConfigOutputGain_Object = MibTableColumn
h3cVoIfConfigOutputGain = _H3cVoIfConfigOutputGain_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 2, 1, 1, 1, 5),
    _H3cVoIfConfigOutputGain_Type()
)
h3cVoIfConfigOutputGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoIfConfigOutputGain.setStatus("current")


class _H3cVoIfCfgEchoCancelSwitch_Type(Integer32):
    """Custom type h3cVoIfCfgEchoCancelSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_H3cVoIfCfgEchoCancelSwitch_Type.__name__ = "Integer32"
_H3cVoIfCfgEchoCancelSwitch_Object = MibTableColumn
h3cVoIfCfgEchoCancelSwitch = _H3cVoIfCfgEchoCancelSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 2, 1, 1, 1, 6),
    _H3cVoIfCfgEchoCancelSwitch_Type()
)
h3cVoIfCfgEchoCancelSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoIfCfgEchoCancelSwitch.setStatus("current")
_H3cVoIfCfgEchoCancellDelay_Type = Integer32
_H3cVoIfCfgEchoCancellDelay_Object = MibTableColumn
h3cVoIfCfgEchoCancellDelay = _H3cVoIfCfgEchoCancellDelay_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 2, 1, 1, 1, 7),
    _H3cVoIfCfgEchoCancellDelay_Type()
)
h3cVoIfCfgEchoCancellDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoIfCfgEchoCancellDelay.setStatus("current")


class _H3cVoIfCfgPlarNumber_Type(OctetString):
    """Custom type h3cVoIfCfgPlarNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_H3cVoIfCfgPlarNumber_Type.__name__ = "OctetString"
_H3cVoIfCfgPlarNumber_Object = MibTableColumn
h3cVoIfCfgPlarNumber = _H3cVoIfCfgPlarNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 2, 1, 1, 1, 8),
    _H3cVoIfCfgPlarNumber_Type()
)
h3cVoIfCfgPlarNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoIfCfgPlarNumber.setStatus("current")
_H3cVoIfCfgDescription_Type = OctetString
_H3cVoIfCfgDescription_Object = MibTableColumn
h3cVoIfCfgDescription = _H3cVoIfCfgDescription_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 2, 1, 1, 1, 9),
    _H3cVoIfCfgDescription_Type()
)
h3cVoIfCfgDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoIfCfgDescription.setStatus("current")


class _H3cVoIfCfgStatus_Type(Integer32):
    """Custom type h3cVoIfCfgStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_H3cVoIfCfgStatus_Type.__name__ = "Integer32"
_H3cVoIfCfgStatus_Object = MibTableColumn
h3cVoIfCfgStatus = _H3cVoIfCfgStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 2, 1, 1, 1, 10),
    _H3cVoIfCfgStatus_Type()
)
h3cVoIfCfgStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoIfCfgStatus.setStatus("current")


class _H3cVoIfCfgCallingNumSubstRule_Type(Integer32):
    """Custom type h3cVoIfCfgCallingNumSubstRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_H3cVoIfCfgCallingNumSubstRule_Type.__name__ = "Integer32"
_H3cVoIfCfgCallingNumSubstRule_Object = MibTableColumn
h3cVoIfCfgCallingNumSubstRule = _H3cVoIfCfgCallingNumSubstRule_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 2, 1, 1, 1, 11),
    _H3cVoIfCfgCallingNumSubstRule_Type()
)
h3cVoIfCfgCallingNumSubstRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoIfCfgCallingNumSubstRule.setStatus("current")


class _H3cVoIfCfgCalledNumSubstRule_Type(Integer32):
    """Custom type h3cVoIfCfgCalledNumSubstRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_H3cVoIfCfgCalledNumSubstRule_Type.__name__ = "Integer32"
_H3cVoIfCfgCalledNumSubstRule_Object = MibTableColumn
h3cVoIfCfgCalledNumSubstRule = _H3cVoIfCfgCalledNumSubstRule_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 2, 1, 1, 1, 12),
    _H3cVoIfCfgCalledNumSubstRule_Type()
)
h3cVoIfCfgCalledNumSubstRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoIfCfgCalledNumSubstRule.setStatus("current")
_H3cVoIfCfgSubLine_Type = OctetString
_H3cVoIfCfgSubLine_Object = MibTableColumn
h3cVoIfCfgSubLine = _H3cVoIfCfgSubLine_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 2, 1, 1, 1, 13),
    _H3cVoIfCfgSubLine_Type()
)
h3cVoIfCfgSubLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoIfCfgSubLine.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-VOIF-MIB",
    **{"h3cVoiceIf": h3cVoiceIf,
       "h3cVoIfObjects": h3cVoIfObjects,
       "h3cVoIfConfigTable": h3cVoIfConfigTable,
       "h3cVoIfConfigEntry": h3cVoIfConfigEntry,
       "h3cVoIfCfgPortNumber": h3cVoIfCfgPortNumber,
       "h3cVoIfCfgGroupNumber": h3cVoIfCfgGroupNumber,
       "h3cVoIfCfgCngOn": h3cVoIfCfgCngOn,
       "h3cVoIfConfigInputGain": h3cVoIfConfigInputGain,
       "h3cVoIfConfigOutputGain": h3cVoIfConfigOutputGain,
       "h3cVoIfCfgEchoCancelSwitch": h3cVoIfCfgEchoCancelSwitch,
       "h3cVoIfCfgEchoCancellDelay": h3cVoIfCfgEchoCancellDelay,
       "h3cVoIfCfgPlarNumber": h3cVoIfCfgPlarNumber,
       "h3cVoIfCfgDescription": h3cVoIfCfgDescription,
       "h3cVoIfCfgStatus": h3cVoIfCfgStatus,
       "h3cVoIfCfgCallingNumSubstRule": h3cVoIfCfgCallingNumSubstRule,
       "h3cVoIfCfgCalledNumSubstRule": h3cVoIfCfgCalledNumSubstRule,
       "h3cVoIfCfgSubLine": h3cVoIfCfgSubLine}
)
