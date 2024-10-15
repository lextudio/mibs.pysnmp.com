# SNMP MIB module (AISYSCFGFAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AISYSCFGFAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:35:24 2024
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

aiSysCfgFan = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 539, 32, 4)
)
aiSysCfgFan.setRevisions(
        ("2001-04-30 17:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Aii_ObjectIdentity = ObjectIdentity
aii = _Aii_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539)
)
_AiSysCfg_ObjectIdentity = ObjectIdentity
aiSysCfg = _AiSysCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 32)
)
_AiSCFanTrapInfo_ObjectIdentity = ObjectIdentity
aiSCFanTrapInfo = _AiSCFanTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 32, 4, 0)
)


class _AiSCFanAgregateStatus_Type(Integer32):
    """Custom type aiSCFanAgregateStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("okay", 1),
          ("trouble", 2))
    )


_AiSCFanAgregateStatus_Type.__name__ = "Integer32"
_AiSCFanAgregateStatus_Object = MibScalar
aiSCFanAgregateStatus = _AiSCFanAgregateStatus_Object(
    (1, 3, 6, 1, 4, 1, 539, 32, 4, 1),
    _AiSCFanAgregateStatus_Type()
)
aiSCFanAgregateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiSCFanAgregateStatus.setStatus("current")
_AiSCFanTable_Object = MibTable
aiSCFanTable = _AiSCFanTable_Object(
    (1, 3, 6, 1, 4, 1, 539, 32, 4, 2)
)
if mibBuilder.loadTexts:
    aiSCFanTable.setStatus("current")
_AiSCFanEntry_Object = MibTableRow
aiSCFanEntry = _AiSCFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 539, 32, 4, 2, 1)
)
aiSCFanEntry.setIndexNames(
    (0, "AISYSCFGFAN-MIB", "aiSCFanIndex"),
)
if mibBuilder.loadTexts:
    aiSCFanEntry.setStatus("current")


class _AiSCFanIndex_Type(Integer32):
    """Custom type aiSCFanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AiSCFanIndex_Type.__name__ = "Integer32"
_AiSCFanIndex_Object = MibTableColumn
aiSCFanIndex = _AiSCFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 539, 32, 4, 2, 1, 1),
    _AiSCFanIndex_Type()
)
aiSCFanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiSCFanIndex.setStatus("current")


class _AiSCFanDescription_Type(DisplayString):
    """Custom type aiSCFanDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AiSCFanDescription_Type.__name__ = "DisplayString"
_AiSCFanDescription_Object = MibTableColumn
aiSCFanDescription = _AiSCFanDescription_Object(
    (1, 3, 6, 1, 4, 1, 539, 32, 4, 2, 1, 2),
    _AiSCFanDescription_Type()
)
aiSCFanDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiSCFanDescription.setStatus("current")


class _AiSCFanStatus_Type(Integer32):
    """Custom type aiSCFanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fail", 2),
          ("okay", 1))
    )


_AiSCFanStatus_Type.__name__ = "Integer32"
_AiSCFanStatus_Object = MibTableColumn
aiSCFanStatus = _AiSCFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 539, 32, 4, 2, 1, 3),
    _AiSCFanStatus_Type()
)
aiSCFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiSCFanStatus.setStatus("current")

# Managed Objects groups


# Notification objects

aiSCFanTrapFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 539, 32, 4, 0, 1)
)
aiSCFanTrapFail.setObjects(
      *(("AISYSCFGFAN-MIB", "aiSCFanIndex"),
        ("AISYSCFGFAN-MIB", "aiSCFanStatus"))
)
if mibBuilder.loadTexts:
    aiSCFanTrapFail.setStatus(
        "current"
    )

aiSCFanTrapOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 539, 32, 4, 0, 2)
)
aiSCFanTrapOk.setObjects(
      *(("AISYSCFGFAN-MIB", "aiSCFanIndex"),
        ("AISYSCFGFAN-MIB", "aiSCFanStatus"))
)
if mibBuilder.loadTexts:
    aiSCFanTrapOk.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AISYSCFGFAN-MIB",
    **{"aii": aii,
       "aiSysCfg": aiSysCfg,
       "aiSysCfgFan": aiSysCfgFan,
       "aiSCFanTrapInfo": aiSCFanTrapInfo,
       "aiSCFanTrapFail": aiSCFanTrapFail,
       "aiSCFanTrapOk": aiSCFanTrapOk,
       "aiSCFanAgregateStatus": aiSCFanAgregateStatus,
       "aiSCFanTable": aiSCFanTable,
       "aiSCFanEntry": aiSCFanEntry,
       "aiSCFanIndex": aiSCFanIndex,
       "aiSCFanDescription": aiSCFanDescription,
       "aiSCFanStatus": aiSCFanStatus}
)
