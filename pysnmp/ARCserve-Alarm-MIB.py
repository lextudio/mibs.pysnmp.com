# SNMP MIB module (ARCserve-Alarm-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ARCserve-Alarm-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:40:13 2024
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
 NotificationType,
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
    "NotificationType",
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

_Cheyenne_ObjectIdentity = ObjectIdentity
cheyenne = _Cheyenne_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46)
)
_ArcServe_ObjectIdentity = ObjectIdentity
arcServe = _ArcServe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46, 877)
)
_ArcServeRev_ObjectIdentity = ObjectIdentity
arcServeRev = _ArcServeRev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46, 877, 1)
)


class _ArcServeevMajor_Type(Integer32):
    """Custom type arcServeevMajor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ArcServeevMajor_Type.__name__ = "Integer32"
_ArcServeevMajor_Object = MibScalar
arcServeevMajor = _ArcServeevMajor_Object(
    (1, 3, 6, 1, 4, 1, 46, 877, 1, 1),
    _ArcServeevMajor_Type()
)
arcServeevMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arcServeevMajor.setStatus("mandatory")


class _ArcServeRevMinor_Type(Integer32):
    """Custom type arcServeRevMinor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ArcServeRevMinor_Type.__name__ = "Integer32"
_ArcServeRevMinor_Object = MibScalar
arcServeRevMinor = _ArcServeRevMinor_Object(
    (1, 3, 6, 1, 4, 1, 46, 877, 1, 2),
    _ArcServeRevMinor_Type()
)
arcServeRevMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arcServeRevMinor.setStatus("mandatory")


class _ArcServeParmsTrapEnable_Type(Integer32):
    """Custom type arcServeParmsTrapEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ArcServeParmsTrapEnable_Type.__name__ = "Integer32"
_ArcServeParmsTrapEnable_Object = MibScalar
arcServeParmsTrapEnable = _ArcServeParmsTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 46, 877, 2),
    _ArcServeParmsTrapEnable_Type()
)
arcServeParmsTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arcServeParmsTrapEnable.setStatus("mandatory")


class _ArcServeParmsPollTime_Type(Integer32):
    """Custom type arcServeParmsPollTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 2592000),
    )


_ArcServeParmsPollTime_Type.__name__ = "Integer32"
_ArcServeParmsPollTime_Object = MibScalar
arcServeParmsPollTime = _ArcServeParmsPollTime_Object(
    (1, 3, 6, 1, 4, 1, 46, 877, 3),
    _ArcServeParmsPollTime_Type()
)
arcServeParmsPollTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arcServeParmsPollTime.setStatus("mandatory")
_ArcServeServerName_Type = OctetString
_ArcServeServerName_Object = MibScalar
arcServeServerName = _ArcServeServerName_Object(
    (1, 3, 6, 1, 4, 1, 46, 877, 4),
    _ArcServeServerName_Type()
)
arcServeServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arcServeServerName.setStatus("mandatory")
_ArcServetrapdesc_Type = OctetString
_ArcServetrapdesc_Object = MibScalar
arcServetrapdesc = _ArcServetrapdesc_Object(
    (1, 3, 6, 1, 4, 1, 46, 877, 5),
    _ArcServetrapdesc_Type()
)
arcServetrapdesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arcServetrapdesc.setStatus("optional")

# Managed Objects groups


# Notification objects

arcServetrapHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 46, 877, 0, 1)
)
arcServetrapHigh.setObjects(
      *(("ARCserve-Alarm-MIB", "arcServeServerName"),
        ("ARCserve-Alarm-MIB", "arcServetrapdesc"))
)
if mibBuilder.loadTexts:
    arcServetrapHigh.setStatus(
        ""
    )

arcServetrapMed = NotificationType(
    (1, 3, 6, 1, 4, 1, 46, 877, 0, 2)
)
arcServetrapMed.setObjects(
      *(("ARCserve-Alarm-MIB", "arcServeServerName"),
        ("ARCserve-Alarm-MIB", "arcServetrapdesc"))
)
if mibBuilder.loadTexts:
    arcServetrapMed.setStatus(
        ""
    )

arcServetrapLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 46, 877, 0, 3)
)
arcServetrapLow.setObjects(
      *(("ARCserve-Alarm-MIB", "arcServeServerName"),
        ("ARCserve-Alarm-MIB", "arcServetrapdesc"))
)
if mibBuilder.loadTexts:
    arcServetrapLow.setStatus(
        ""
    )

arcServetrap4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 46, 877, 0, 4)
)
arcServetrap4.setObjects(
      *(("ARCserve-Alarm-MIB", "arcServeServerName"),
        ("ARCserve-Alarm-MIB", "arcServetrapdesc"))
)
if mibBuilder.loadTexts:
    arcServetrap4.setStatus(
        ""
    )

arcServetrap5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 46, 877, 0, 5)
)
arcServetrap5.setObjects(
      *(("ARCserve-Alarm-MIB", "arcServeServerName"),
        ("ARCserve-Alarm-MIB", "arcServetrapdesc"))
)
if mibBuilder.loadTexts:
    arcServetrap5.setStatus(
        ""
    )

arcServetrap6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 46, 877, 0, 7)
)
arcServetrap6.setObjects(
      *(("ARCserve-Alarm-MIB", "arcServeServerName"),
        ("ARCserve-Alarm-MIB", "arcServetrapdesc"))
)
if mibBuilder.loadTexts:
    arcServetrap6.setStatus(
        ""
    )

arcServetrap7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 46, 877, 0, 8)
)
arcServetrap7.setObjects(
      *(("ARCserve-Alarm-MIB", "arcServeServerName"),
        ("ARCserve-Alarm-MIB", "arcServetrapdesc"))
)
if mibBuilder.loadTexts:
    arcServetrap7.setStatus(
        ""
    )

arcServetrap8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 46, 877, 0, 9)
)
arcServetrap8.setObjects(
      *(("ARCserve-Alarm-MIB", "arcServeServerName"),
        ("ARCserve-Alarm-MIB", "arcServetrapdesc"))
)
if mibBuilder.loadTexts:
    arcServetrap8.setStatus(
        ""
    )

arcServetrap9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 46, 877, 0, 9)
)
arcServetrap9.setObjects(
      *(("ARCserve-Alarm-MIB", "arcServeServerName"),
        ("ARCserve-Alarm-MIB", "arcServetrapdesc"))
)
if mibBuilder.loadTexts:
    arcServetrap9.setStatus(
        ""
    )

arcServetrap10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 46, 877, 0, 10)
)
arcServetrap10.setObjects(
      *(("ARCserve-Alarm-MIB", "arcServeServerName"),
        ("ARCserve-Alarm-MIB", "arcServetrapdesc"))
)
if mibBuilder.loadTexts:
    arcServetrap10.setStatus(
        ""
    )

arcServetrap11 = NotificationType(
    (1, 3, 6, 1, 4, 1, 46, 877, 0, 11)
)
arcServetrap11.setObjects(
      *(("ARCserve-Alarm-MIB", "arcServeServerName"),
        ("ARCserve-Alarm-MIB", "arcServetrapdesc"))
)
if mibBuilder.loadTexts:
    arcServetrap11.setStatus(
        ""
    )

arcServetrap12 = NotificationType(
    (1, 3, 6, 1, 4, 1, 46, 877, 0, 12)
)
arcServetrap12.setObjects(
      *(("ARCserve-Alarm-MIB", "arcServeServerName"),
        ("ARCserve-Alarm-MIB", "arcServetrapdesc"))
)
if mibBuilder.loadTexts:
    arcServetrap12.setStatus(
        ""
    )

arcServetrap13 = NotificationType(
    (1, 3, 6, 1, 4, 1, 46, 877, 0, 13)
)
arcServetrap13.setObjects(
      *(("ARCserve-Alarm-MIB", "arcServeServerName"),
        ("ARCserve-Alarm-MIB", "arcServetrapdesc"))
)
if mibBuilder.loadTexts:
    arcServetrap13.setStatus(
        ""
    )

arcServetrap14 = NotificationType(
    (1, 3, 6, 1, 4, 1, 46, 877, 0, 14)
)
arcServetrap14.setObjects(
      *(("ARCserve-Alarm-MIB", "arcServeServerName"),
        ("ARCserve-Alarm-MIB", "arcServetrapdesc"))
)
if mibBuilder.loadTexts:
    arcServetrap14.setStatus(
        ""
    )

arcServetrap15 = NotificationType(
    (1, 3, 6, 1, 4, 1, 46, 877, 0, 15)
)
arcServetrap15.setObjects(
      *(("ARCserve-Alarm-MIB", "arcServeServerName"),
        ("ARCserve-Alarm-MIB", "arcServetrapdesc"))
)
if mibBuilder.loadTexts:
    arcServetrap15.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARCserve-Alarm-MIB",
    **{"cheyenne": cheyenne,
       "arcServe": arcServe,
       "arcServetrapHigh": arcServetrapHigh,
       "arcServetrapMed": arcServetrapMed,
       "arcServetrapLow": arcServetrapLow,
       "arcServetrap4": arcServetrap4,
       "arcServetrap5": arcServetrap5,
       "arcServetrap6": arcServetrap6,
       "arcServetrap7": arcServetrap7,
       "arcServetrap8": arcServetrap8,
       "arcServetrap9": arcServetrap9,
       "arcServetrap10": arcServetrap10,
       "arcServetrap11": arcServetrap11,
       "arcServetrap12": arcServetrap12,
       "arcServetrap13": arcServetrap13,
       "arcServetrap14": arcServetrap14,
       "arcServetrap15": arcServetrap15,
       "arcServeRev": arcServeRev,
       "arcServeevMajor": arcServeevMajor,
       "arcServeRevMinor": arcServeRevMinor,
       "arcServeParmsTrapEnable": arcServeParmsTrapEnable,
       "arcServeParmsPollTime": arcServeParmsPollTime,
       "arcServeServerName": arcServeServerName,
       "arcServetrapdesc": arcServetrapdesc}
)
