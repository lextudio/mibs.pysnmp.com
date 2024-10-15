# SNMP MIB module (ZHONE-PW-BUNDLE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZHONE-PW-BUNDLE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:20:41 2024
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

(DisplayString,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")

(zhoneModules,) = mibBuilder.importSymbols(
    "Zhone",
    "zhoneModules")


# MODULE-IDENTITY

zhonePwBundle = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 6, 115)
)
zhonePwBundle.setRevisions(
        ("2010-01-21 06:41",
         "2008-08-18 06:50")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZhonePwBundleTable_Object = MibTable
zhonePwBundleTable = _ZhonePwBundleTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 6, 115, 1)
)
if mibBuilder.loadTexts:
    zhonePwBundleTable.setStatus("current")
_ZhonePwBundleEntry_Object = MibTableRow
zhonePwBundleEntry = _ZhonePwBundleEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 6, 115, 1, 1)
)
zhonePwBundleEntry.setIndexNames(
    (0, "ZHONE-PW-BUNDLE-MIB", "zhonePwBundlePwIndex"),
)
if mibBuilder.loadTexts:
    zhonePwBundleEntry.setStatus("current")


class _ZhonePwBundlePwIndex_Type(Integer32):
    """Custom type zhonePwBundlePwIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ZhonePwBundlePwIndex_Type.__name__ = "Integer32"
_ZhonePwBundlePwIndex_Object = MibTableColumn
zhonePwBundlePwIndex = _ZhonePwBundlePwIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 6, 115, 1, 1, 1),
    _ZhonePwBundlePwIndex_Type()
)
zhonePwBundlePwIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhonePwBundlePwIndex.setStatus("current")
_ZhonePwBundleLocalIpAddr_Type = IpAddress
_ZhonePwBundleLocalIpAddr_Object = MibTableColumn
zhonePwBundleLocalIpAddr = _ZhonePwBundleLocalIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5504, 6, 115, 1, 1, 2),
    _ZhonePwBundleLocalIpAddr_Type()
)
zhonePwBundleLocalIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhonePwBundleLocalIpAddr.setStatus("current")


class _ZhonePwBundleDs0Bundle_Type(Bits):
    """Custom type zhonePwBundleDs0Bundle based on Bits"""
    namedValues = NamedValues(
        *(("ds0-0", 0),
          ("ds0-1", 1),
          ("ds0-10", 10),
          ("ds0-11", 11),
          ("ds0-12", 12),
          ("ds0-13", 13),
          ("ds0-14", 14),
          ("ds0-15", 15),
          ("ds0-16", 16),
          ("ds0-17", 17),
          ("ds0-18", 18),
          ("ds0-19", 19),
          ("ds0-2", 2),
          ("ds0-20", 20),
          ("ds0-21", 21),
          ("ds0-22", 22),
          ("ds0-23", 23),
          ("ds0-24", 24),
          ("ds0-25", 25),
          ("ds0-26", 26),
          ("ds0-27", 27),
          ("ds0-28", 28),
          ("ds0-29", 29),
          ("ds0-3", 3),
          ("ds0-30", 30),
          ("ds0-31", 31),
          ("ds0-4", 4),
          ("ds0-5", 5),
          ("ds0-6", 6),
          ("ds0-7", 7),
          ("ds0-8", 8),
          ("ds0-9", 9))
    )

_ZhonePwBundleDs0Bundle_Type.__name__ = "Bits"
_ZhonePwBundleDs0Bundle_Object = MibTableColumn
zhonePwBundleDs0Bundle = _ZhonePwBundleDs0Bundle_Object(
    (1, 3, 6, 1, 4, 1, 5504, 6, 115, 1, 1, 3),
    _ZhonePwBundleDs0Bundle_Type()
)
zhonePwBundleDs0Bundle.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhonePwBundleDs0Bundle.setStatus("current")
_ZhonePwBundleRowStatus_Type = RowStatus
_ZhonePwBundleRowStatus_Object = MibTableColumn
zhonePwBundleRowStatus = _ZhonePwBundleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 6, 115, 1, 1, 4),
    _ZhonePwBundleRowStatus_Type()
)
zhonePwBundleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhonePwBundleRowStatus.setStatus("current")


class _ZhonePwBundleTos_Type(Integer32):
    """Custom type zhonePwBundleTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ZhonePwBundleTos_Type.__name__ = "Integer32"
_ZhonePwBundleTos_Object = MibTableColumn
zhonePwBundleTos = _ZhonePwBundleTos_Object(
    (1, 3, 6, 1, 4, 1, 5504, 6, 115, 1, 1, 5),
    _ZhonePwBundleTos_Type()
)
zhonePwBundleTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhonePwBundleTos.setStatus("current")


class _ZhonePwBundleIsdnMode_Type(Integer32):
    """Custom type zhonePwBundleIsdnMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("lt", 2),
          ("nt1", 3))
    )


_ZhonePwBundleIsdnMode_Type.__name__ = "Integer32"
_ZhonePwBundleIsdnMode_Object = MibTableColumn
zhonePwBundleIsdnMode = _ZhonePwBundleIsdnMode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 6, 115, 1, 1, 6),
    _ZhonePwBundleIsdnMode_Type()
)
zhonePwBundleIsdnMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhonePwBundleIsdnMode.setStatus("current")

# Managed Objects groups

zhonePwBundleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 6, 115, 2)
)
zhonePwBundleGroup.setObjects(
      *(("ZHONE-PW-BUNDLE-MIB", "zhonePwBundleLocalIpAddr"),
        ("ZHONE-PW-BUNDLE-MIB", "zhonePwBundleDs0Bundle"),
        ("ZHONE-PW-BUNDLE-MIB", "zhonePwBundleRowStatus"),
        ("ZHONE-PW-BUNDLE-MIB", "zhonePwBundleTos"),
        ("ZHONE-PW-BUNDLE-MIB", "zhonePwBundleIsdnMode"))
)
if mibBuilder.loadTexts:
    zhonePwBundleGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZHONE-PW-BUNDLE-MIB",
    **{"zhonePwBundle": zhonePwBundle,
       "zhonePwBundleTable": zhonePwBundleTable,
       "zhonePwBundleEntry": zhonePwBundleEntry,
       "zhonePwBundlePwIndex": zhonePwBundlePwIndex,
       "zhonePwBundleLocalIpAddr": zhonePwBundleLocalIpAddr,
       "zhonePwBundleDs0Bundle": zhonePwBundleDs0Bundle,
       "zhonePwBundleRowStatus": zhonePwBundleRowStatus,
       "zhonePwBundleTos": zhonePwBundleTos,
       "zhonePwBundleIsdnMode": zhonePwBundleIsdnMode,
       "zhonePwBundleGroup": zhonePwBundleGroup}
)
