# SNMP MIB module (HPNSATRAPCFG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPNSATRAPCFG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:02:28 2024
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
 enterprises,
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
    "enterprises",
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

_Hp_ObjectIdentity = ObjectIdentity
hp = _Hp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11)
)
_Nm_ObjectIdentity = ObjectIdentity
nm = _Nm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2)
)
_Hpnsa_ObjectIdentity = ObjectIdentity
hpnsa = _Hpnsa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23)
)
_HpnsaTrapCfg_ObjectIdentity = ObjectIdentity
hpnsaTrapCfg = _HpnsaTrapCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 13)
)
_HpnsaTrapCfgMibRev_ObjectIdentity = ObjectIdentity
hpnsaTrapCfgMibRev = _HpnsaTrapCfgMibRev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 13, 1)
)


class _HpnsaTrapCfgMibRevMajor_Type(Integer32):
    """Custom type hpnsaTrapCfgMibRevMajor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpnsaTrapCfgMibRevMajor_Type.__name__ = "Integer32"
_HpnsaTrapCfgMibRevMajor_Object = MibScalar
hpnsaTrapCfgMibRevMajor = _HpnsaTrapCfgMibRevMajor_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 13, 1, 1),
    _HpnsaTrapCfgMibRevMajor_Type()
)
hpnsaTrapCfgMibRevMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaTrapCfgMibRevMajor.setStatus("mandatory")


class _HpnsaTrapCfgMibRevMinor_Type(Integer32):
    """Custom type hpnsaTrapCfgMibRevMinor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnsaTrapCfgMibRevMinor_Type.__name__ = "Integer32"
_HpnsaTrapCfgMibRevMinor_Object = MibScalar
hpnsaTrapCfgMibRevMinor = _HpnsaTrapCfgMibRevMinor_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 13, 1, 2),
    _HpnsaTrapCfgMibRevMinor_Type()
)
hpnsaTrapCfgMibRevMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaTrapCfgMibRevMinor.setStatus("mandatory")
_HpnsaTrapCfgAgent_ObjectIdentity = ObjectIdentity
hpnsaTrapCfgAgent = _HpnsaTrapCfgAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 13, 2)
)
_HpnsaTrapCfgAgentTable_Object = MibTable
hpnsaTrapCfgAgentTable = _HpnsaTrapCfgAgentTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 13, 2, 1)
)
if mibBuilder.loadTexts:
    hpnsaTrapCfgAgentTable.setStatus("mandatory")
_HpnsaTrapCfgAgentEntry_Object = MibTableRow
hpnsaTrapCfgAgentEntry = _HpnsaTrapCfgAgentEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 13, 2, 1, 1)
)
hpnsaTrapCfgAgentEntry.setIndexNames(
    (0, "HPNSATRAPCFG-MIB", "hpnsaTrapCfgAgentIndex"),
)
if mibBuilder.loadTexts:
    hpnsaTrapCfgAgentEntry.setStatus("mandatory")


class _HpnsaTrapCfgAgentIndex_Type(Integer32):
    """Custom type hpnsaTrapCfgAgentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnsaTrapCfgAgentIndex_Type.__name__ = "Integer32"
_HpnsaTrapCfgAgentIndex_Object = MibTableColumn
hpnsaTrapCfgAgentIndex = _HpnsaTrapCfgAgentIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 13, 2, 1, 1, 1),
    _HpnsaTrapCfgAgentIndex_Type()
)
hpnsaTrapCfgAgentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaTrapCfgAgentIndex.setStatus("mandatory")


class _HpnsaTrapCfgAgentName_Type(DisplayString):
    """Custom type hpnsaTrapCfgAgentName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnsaTrapCfgAgentName_Type.__name__ = "DisplayString"
_HpnsaTrapCfgAgentName_Object = MibTableColumn
hpnsaTrapCfgAgentName = _HpnsaTrapCfgAgentName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 13, 2, 1, 1, 2),
    _HpnsaTrapCfgAgentName_Type()
)
hpnsaTrapCfgAgentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaTrapCfgAgentName.setStatus("mandatory")


class _HpnsaTrapCfgAgentVersion_Type(DisplayString):
    """Custom type hpnsaTrapCfgAgentVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_HpnsaTrapCfgAgentVersion_Type.__name__ = "DisplayString"
_HpnsaTrapCfgAgentVersion_Object = MibTableColumn
hpnsaTrapCfgAgentVersion = _HpnsaTrapCfgAgentVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 13, 2, 1, 1, 3),
    _HpnsaTrapCfgAgentVersion_Type()
)
hpnsaTrapCfgAgentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaTrapCfgAgentVersion.setStatus("mandatory")


class _HpnsaTrapCfgAgentDate_Type(OctetString):
    """Custom type hpnsaTrapCfgAgentDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 7),
    )


_HpnsaTrapCfgAgentDate_Type.__name__ = "OctetString"
_HpnsaTrapCfgAgentDate_Object = MibTableColumn
hpnsaTrapCfgAgentDate = _HpnsaTrapCfgAgentDate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 13, 2, 1, 1, 4),
    _HpnsaTrapCfgAgentDate_Type()
)
hpnsaTrapCfgAgentDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaTrapCfgAgentDate.setStatus("mandatory")
_HpnsaTrapTargetCfg_ObjectIdentity = ObjectIdentity
hpnsaTrapTargetCfg = _HpnsaTrapTargetCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 13, 3)
)


class _HpnsaRemoveTrapTarget_Type(DisplayString):
    """Custom type hpnsaRemoveTrapTarget based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_HpnsaRemoveTrapTarget_Type.__name__ = "DisplayString"
_HpnsaRemoveTrapTarget_Object = MibScalar
hpnsaRemoveTrapTarget = _HpnsaRemoveTrapTarget_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 13, 3, 1),
    _HpnsaRemoveTrapTarget_Type()
)
hpnsaRemoveTrapTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnsaRemoveTrapTarget.setStatus("mandatory")


class _HpnsaAddTrapTarget_Type(DisplayString):
    """Custom type hpnsaAddTrapTarget based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_HpnsaAddTrapTarget_Type.__name__ = "DisplayString"
_HpnsaAddTrapTarget_Object = MibScalar
hpnsaAddTrapTarget = _HpnsaAddTrapTarget_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 13, 3, 2),
    _HpnsaAddTrapTarget_Type()
)
hpnsaAddTrapTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnsaAddTrapTarget.setStatus("mandatory")


class _HpnsaRestartSNMP_Type(Integer32):
    """Custom type hpnsaRestartSNMP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noActionNeeded", 1),
          ("restartSNMP", 2))
    )


_HpnsaRestartSNMP_Type.__name__ = "Integer32"
_HpnsaRestartSNMP_Object = MibScalar
hpnsaRestartSNMP = _HpnsaRestartSNMP_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 13, 3, 3),
    _HpnsaRestartSNMP_Type()
)
hpnsaRestartSNMP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaRestartSNMP.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPNSATRAPCFG-MIB",
    **{"hp": hp,
       "nm": nm,
       "hpnsa": hpnsa,
       "hpnsaTrapCfg": hpnsaTrapCfg,
       "hpnsaTrapCfgMibRev": hpnsaTrapCfgMibRev,
       "hpnsaTrapCfgMibRevMajor": hpnsaTrapCfgMibRevMajor,
       "hpnsaTrapCfgMibRevMinor": hpnsaTrapCfgMibRevMinor,
       "hpnsaTrapCfgAgent": hpnsaTrapCfgAgent,
       "hpnsaTrapCfgAgentTable": hpnsaTrapCfgAgentTable,
       "hpnsaTrapCfgAgentEntry": hpnsaTrapCfgAgentEntry,
       "hpnsaTrapCfgAgentIndex": hpnsaTrapCfgAgentIndex,
       "hpnsaTrapCfgAgentName": hpnsaTrapCfgAgentName,
       "hpnsaTrapCfgAgentVersion": hpnsaTrapCfgAgentVersion,
       "hpnsaTrapCfgAgentDate": hpnsaTrapCfgAgentDate,
       "hpnsaTrapTargetCfg": hpnsaTrapTargetCfg,
       "hpnsaRemoveTrapTarget": hpnsaRemoveTrapTarget,
       "hpnsaAddTrapTarget": hpnsaAddTrapTarget,
       "hpnsaRestartSNMP": hpnsaRestartSNMP}
)
